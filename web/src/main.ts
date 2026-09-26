import "./styles.css";
import { DEFAULT_GAME, OBJECTIVES, generate, validate, type GameSpec, type GameType, type Move, type Objective } from "./builder";
import { createEditor, replaceDoc } from "./editor";
import { MODES, examples, type Example, type Mode } from "./examples";
import type { FromWorker, RuntimePhase, ToWorker } from "./protocol";

const el = <T extends HTMLElement = HTMLElement>(id: string) => document.getElementById(id) as T;

const ui = {
  status: el("runtime-status"),
  exampleSelect: el<HTMLSelectElement>("example-select"),
  exampleInfo: el("example-info"),
  modeGroup: el("mode-group"),
  limitSelect: el<HTMLSelectElement>("limit-select"),
  runBtn: el<HTMLButtonElement>("run-btn"),
  stopBtn: el<HTMLButtonElement>("stop-btn"),
  result: el("result"),
  console: el("console"),
  fileInput: el<HTMLInputElement>("file-input"),
  builder: el<HTMLDialogElement>("builder-dialog"),
  builderForm: el<HTMLFormElement>("builder-form"),
  movesList: el("moves-list"),
  builderErrors: el("builder-errors"),
  help: el<HTMLDialogElement>("help-dialog"),
  toast: el("toast"),
};

// ---------------------------------------------------------------------------------------------
// Specification state: which example (if any) is loaded, and the encoding passed as sys.argv[1].
// ---------------------------------------------------------------------------------------------

type Source = { kind: "example"; example: Example } | { kind: "custom"; name: string };
let source: Source = { kind: "example", example: examples[0] };

const DRAFT_KEY = "gensys-playground:draft";

function currentMode(): Mode {
  return (ui.modeGroup.querySelector<HTMLInputElement>("input:checked")?.value as Mode) ?? "simple";
}

function setMode(mode: Mode) {
  const input = ui.modeGroup.querySelector<HTMLInputElement>(`input[value="${mode}"]`);
  if (input) input.checked = true;
}

function fileName(): string {
  if (source.kind === "example") return `${source.example.id}.py`;
  const base = source.name.trim().replace(/\.py$/i, "").replace(/[^\w.-]+/g, "-").replace(/^-+|-+$/g, "");
  return `${base || "spec"}.py`;
}

function isModified(): boolean {
  return source.kind === "example" && editor.state.doc.toString() !== source.example.code;
}

function renderSource() {
  ui.exampleSelect.value = source.kind === "example" ? source.example.id : "";
  ui.exampleInfo.replaceChildren();
  if (source.kind === "example") {
    const { description, spec } = source.example;
    ui.exampleInfo.append(description + (isModified() ? " (edited)" : ""));
    if (spec) {
      const specEl = document.createElement("span");
      specEl.className = "spec";
      specEl.textContent = spec;
      ui.exampleInfo.append(specEl);
    }
  } else {
    ui.exampleInfo.append(`Custom specification: ${fileName()}`);
  }
}

function populateExamples() {
  const custom = new Option("Custom specification", "");
  custom.disabled = true;
  ui.exampleSelect.append(custom);
  for (const ex of examples) ui.exampleSelect.append(new Option(`${ex.number}. ${ex.title}`, ex.id));
}

function loadExample(example: Example, mode: Mode = example.mode) {
  const hadEdits = editor.state.doc.length > 0 && (source.kind === "custom" || isModified());
  source = { kind: "example", example };
  replaceDoc(editor, example.code);
  setMode(mode);
  renderSource();
  saveDraft();
  if (hadEdits) toast(`Loaded "${example.title}". Undo in the editor brings your previous text back.`);
}

function loadCustom(name: string, code: string, mode: Mode = currentMode()) {
  source = { kind: "custom", name };
  replaceDoc(editor, code);
  setMode(mode);
  renderSource();
  saveDraft();
}

let draftTimer: number | undefined;
function saveDraft() {
  window.clearTimeout(draftTimer);
  draftTimer = window.setTimeout(writeDraft, 400);
}

function writeDraft() {
  window.clearTimeout(draftTimer);
  try {
    const draft =
      source.kind === "example" && !isModified()
        ? { example: source.example.id, mode: currentMode() }
        : { code: editor.state.doc.toString(), name: source.kind === "custom" ? source.name : undefined,
            example: source.kind === "example" ? source.example.id : undefined, mode: currentMode() };
    localStorage.setItem(DRAFT_KEY, JSON.stringify(draft));
  } catch {
    // Storage can be unavailable (private windows, blocked site data); drafts are a convenience only.
  }
}

function restoreDraft(): boolean {
  try {
    const draft = JSON.parse(localStorage.getItem(DRAFT_KEY) ?? "null");
    if (!draft) return false;
    const example = examples.find((e) => e.id === draft.example);
    const mode = MODES.some((m) => m.value === draft.mode) ? (draft.mode as Mode) : undefined;
    if (typeof draft.code === "string") {
      if (example) {
        source = { kind: "example", example };
        replaceDoc(editor, draft.code);
        setMode(mode ?? example.mode);
        renderSource();
      } else {
        loadCustom(typeof draft.name === "string" ? draft.name : "spec.py", draft.code, mode);
      }
      return true;
    }
    if (example) {
      loadExample(example, mode);
      return true;
    }
  } catch {
    // Ignore unreadable drafts.
  }
  return false;
}

// ---------------------------------------------------------------------------------------------
// Share links: #example=<id>&mode=<mode>, or #code=<deflated base64url>&name=<name>&mode=<mode>.
// ---------------------------------------------------------------------------------------------

async function compress(text: string): Promise<string> {
  const stream = new Blob([text]).stream().pipeThrough(new CompressionStream("deflate-raw"));
  const bytes = new Uint8Array(await new Response(stream).arrayBuffer());
  let binary = "";
  for (const b of bytes) binary += String.fromCharCode(b);
  return btoa(binary).replace(/\+/g, "-").replace(/\//g, "_").replace(/=+$/, "");
}

async function decompress(encoded: string): Promise<string> {
  const binary = atob(encoded.replace(/-/g, "+").replace(/_/g, "/"));
  const bytes = Uint8Array.from(binary, (c) => c.charCodeAt(0));
  const stream = new Blob([bytes]).stream().pipeThrough(new DecompressionStream("deflate-raw"));
  return new Response(stream).text();
}

async function shareLink(): Promise<string> {
  const params = new URLSearchParams();
  if (source.kind === "example" && !isModified()) {
    params.set("example", source.example.id);
  } else {
    params.set("code", await compress(editor.state.doc.toString()));
    params.set("name", fileName());
  }
  params.set("mode", currentMode());
  return `${location.origin}${location.pathname}#${params}`;
}

async function restoreFromHash(): Promise<boolean> {
  const params = new URLSearchParams(location.hash.slice(1));
  const modeParam = params.get("mode");
  const mode = MODES.some((m) => m.value === modeParam) ? (modeParam as Mode) : undefined;
  const example = examples.find((e) => e.id === params.get("example"));
  if (example) {
    loadExample(example, mode);
    return true;
  }
  const code = params.get("code");
  if (code) {
    try {
      loadCustom(params.get("name") ?? "shared.py", await decompress(code), mode);
      return true;
    } catch {
      toast("This share link is damaged, so an example was loaded instead.");
    }
  }
  return false;
}

// ---------------------------------------------------------------------------------------------
// Runtime: the Pyodide worker. Stopping a run terminates the worker and starts a fresh one.
// ---------------------------------------------------------------------------------------------

let worker: Worker;
let runtimeReady = false;
let runtimeVersion = "";

const PHASE_LABELS: Record<RuntimePhase | "running", string> = {
  python: "Starting Python…",
  z3: "Loading Z3…",
  gensys: "Loading GenSys-LTL…",
  ready: "Ready",
  running: "Solving…",
  failed: "Runtime failed to load",
};

function setStatus(phase: RuntimePhase | "running") {
  ui.status.dataset.phase = phase;
  ui.status.querySelector(".label")!.textContent = PHASE_LABELS[phase];
  const detail = phase === "ready" || phase === "running" ? runtimeVersion : "";
  ui.status.querySelector(".detail")!.textContent = detail ? ` · ${detail}` : "";
  ui.status.title = detail;
}

let bootWatchdog: number | undefined;

function startWorker() {
  runtimeReady = false;
  ui.runBtn.disabled = true;
  setStatus("python");
  // Pyodide waits forever, rather than failing, when the browser refuses to compile WebAssembly.
  window.clearTimeout(bootWatchdog);
  bootWatchdog = window.setTimeout(() => {
    if (!runtimeReady && ui.status.dataset.phase !== "failed") {
      appendLines(["The Python runtime is still loading after a minute. On a slow connection, keep waiting;",
        "otherwise this browser may be blocking WebAssembly (for example, iOS Lockdown Mode or a strict security policy)."], "meta");
    }
  }, 60_000);
  worker = new Worker(new URL("./worker.ts", import.meta.url), { type: "module" });
  worker.onmessage = (e: MessageEvent<FromWorker>) => onWorkerMessage(e.data);
  worker.onerror = (e) => {
    appendLines([`Runtime error: ${e.message}`], "err");
    if (run) {
      const r = run;
      endRun();
      crashed(r, performance.now() - r.started);
    } else {
      setStatus("failed");
    }
  };
}

function onWorkerMessage(msg: FromWorker) {
  switch (msg.type) {
    case "status":
      if (msg.phase === "ready") {
        runtimeReady = true;
        window.clearTimeout(bootWatchdog);
        runtimeVersion = msg.detail ?? "";
        ui.runBtn.disabled = false;
        setStatus("ready");
      } else if (msg.phase === "failed") {
        setStatus("failed");
        appendLines([`The Python runtime failed to load: ${msg.detail ?? "unknown error"}`], "err");
      } else {
        setStatus(msg.phase);
      }
      break;
    case "output":
      if (run && msg.id === run.id) {
        for (const line of msg.lines) run.observe(line);
        appendLines(msg.lines, msg.stream === "stderr" ? "err" : undefined);
      }
      break;
    case "done":
      if (run && msg.id === run.id) finishRun(msg.exitCode, msg.elapsedMs);
      break;
  }
}

// ---------------------------------------------------------------------------------------------
// Runs
// ---------------------------------------------------------------------------------------------

class Run {
  verdict: "REALIZABLE" | "UNREALIZABLE" | null = null;
  verdicts = 0;
  iterations: string | null = null;
  readonly started = performance.now();
  constructor(
    readonly id: number,
    readonly mode: Mode,
    readonly file: string,
  ) {}

  observe(line: string) {
    const text = line.trim();
    if (text === "REALIZABLE" || text === "UNREALIZABLE") {
      this.verdict = text;
      this.verdicts++;
    }
    const iterations = /^Number of iterations:\s*(\d+)/.exec(text);
    if (iterations) this.iterations = iterations[1];
  }
}

let run: Run | null = null;
let runCounter = 0;
let tickTimer: number | undefined;
let limitTimer: number | undefined;

function modeLabel(mode: Mode) {
  return MODES.find((m) => m.value === mode)?.label ?? mode;
}

function formatSeconds(ms: number) {
  const s = ms / 1000;
  if (s < 60) return `${s.toFixed(s < 10 ? 2 : 1)} s`;
  const total = Math.round(s);
  return `${Math.floor(total / 60)} min ${total % 60} s`;
}

function startRun() {
  if (run) return;
  if (!runtimeReady) {
    toast("The Python runtime is still loading. Synthesize will be enabled when it is ready.");
    return;
  }
  const code = editor.state.doc.toString();
  run = new Run(++runCounter, currentMode(), fileName());
  clearConsole();
  appendLines([`$ python3 ${run.file} ${run.mode}`], "meta");
  ui.runBtn.hidden = true;
  ui.stopBtn.hidden = false;
  setStatus("running");
  const limit = Number(ui.limitSelect.value);
  showResult("running", "Solving…", `${modeLabel(run.mode)} encoding · 0.00 s`);
  tickTimer = window.setInterval(() => {
    if (run) setResultDetail(`${modeLabel(run.mode)} encoding · ${formatSeconds(performance.now() - run.started)}`);
  }, 100);
  const limitLabel = ui.limitSelect.selectedOptions[0]?.text ?? `${limit} s`;
  if (limit > 0) limitTimer = window.setTimeout(() => stopRun(`the ${limitLabel} time limit was reached`), limit * 1000);
  const msg: ToWorker = { type: "run", id: run.id, code, argv: [run.mode] };
  worker.postMessage(msg);
}

function endRun() {
  window.clearInterval(tickTimer);
  window.clearTimeout(limitTimer);
  ui.runBtn.hidden = false;
  ui.stopBtn.hidden = true;
  run = null;
}

function stats(r: Run, elapsedMs: number): [string, string][] {
  const rows: [string, string][] = [
    ["Encoding", modeLabel(r.mode)],
    ["Time", formatSeconds(elapsedMs)],
  ];
  if (r.iterations) rows.push(["Iterations", r.iterations]);
  if (r.verdicts > 1) rows.push(["Verdicts", `${r.verdicts} (last shown)`]);
  return rows;
}

function finishRun(exitCode: number, elapsedMs: number) {
  const r = run!;
  endRun();
  setStatus("ready");
  if (exitCode === 0 && r.verdict === "REALIZABLE") {
    showResult("realizable", "Realizable", "The controller has a strategy that satisfies the specification.", stats(r, elapsedMs));
  } else if (exitCode === 0 && r.verdict === "UNREALIZABLE") {
    showResult("unrealizable", "Unrealizable", "No controller strategy satisfies the specification from the initial states.", stats(r, elapsedMs));
  } else if (exitCode === 0) {
    showResult("finished", "Finished", "The script ran to completion without reporting a verdict.", stats(r, elapsedMs));
  } else if (exitCode === 5) {
    showResult("skipped", "Encoding not applicable", `This specification has no ${modeLabel(r.mode)} encoding. Try another encoding.`, stats(r, elapsedMs));
  } else if (exitCode === CRASHED) {
    crashed(r, elapsedMs);
  } else if (exitCode === 6) {
    showResult("skipped", "Encoding not provided", `The ${modeLabel(r.mode)} encoding is known not to scale for this benchmark, so it was not written.`, stats(r, elapsedMs));
  } else {
    showResult("error", exitCode === 1 ? "Python error" : `Exited with code ${exitCode}`, "See the output below for details.", stats(r, elapsedMs));
  }
}

// Exit code the worker reports when Pyodide itself fails (for example, WebAssembly running out of memory).
const CRASHED = -1;

function crashed(r: Run, elapsedMs: number) {
  worker.terminate();
  showResult("error", "Runtime crashed", "The Python runtime stopped unexpectedly, often because it ran out of memory. It has been restarted.", stats(r, elapsedMs));
  startWorker();
}

function stopRun(reason = "you stopped it") {
  if (!run) return;
  const r = run;
  const elapsed = performance.now() - r.started;
  endRun();
  worker.terminate();
  appendLines([`■ Stopped after ${formatSeconds(elapsed)}: ${reason}.`], "meta");
  const partial = r.verdict ? ` The last verdict printed before stopping was ${r.verdict}.` : "";
  showResult("stopped", "Stopped", `The run ended because ${reason}.${partial}`, stats(r, elapsed));
  startWorker();
}

function showResult(state: string, title: string, detail: string, rows: [string, string][] = []) {
  ui.result.dataset.state = state;
  ui.result.querySelector(".result-title")!.textContent = title;
  setResultDetail(detail);
  const dl = ui.result.querySelector(".result-stats")!;
  dl.replaceChildren(
    ...rows.map(([k, v]) => {
      const div = document.createElement("div");
      const dt = document.createElement("dt");
      const dd = document.createElement("dd");
      dt.textContent = k;
      dd.textContent = v;
      div.append(dt, dd);
      return div;
    }),
  );
}

function setResultDetail(text: string) {
  ui.result.querySelector(".result-detail")!.textContent = text;
}

// ---------------------------------------------------------------------------------------------
// Output console. The full log is kept for copying and saving; the page shows the most recent lines.
// ---------------------------------------------------------------------------------------------

const MAX_VISIBLE_LINES = 3000;
const MAX_LOG_LINES = 500_000;
let log: string[] = [];
let queued: { text: string; cls?: string }[] = [];
let hiddenLines = 0;
let flushScheduled = false;

function appendLines(lines: string[], cls?: string) {
  for (const text of lines) {
    if (log.length < MAX_LOG_LINES) log.push(text);
    queued.push({ text, cls });
  }
  if (!flushScheduled) {
    flushScheduled = true;
    requestAnimationFrame(flushConsole);
  }
}

function flushConsole() {
  flushScheduled = false;
  const pane = ui.console;
  const atBottom = pane.scrollHeight - pane.scrollTop - pane.clientHeight < 40;
  const frag = document.createDocumentFragment();
  for (const { text, cls } of queued.slice(-MAX_VISIBLE_LINES)) {
    const span = document.createElement("span");
    const verdict = text.trim();
    span.className = cls ?? (verdict === "REALIZABLE" ? "verdict-ok" : verdict === "UNREALIZABLE" ? "verdict-bad" : "");
    span.textContent = text + "\n";
    frag.append(span);
  }
  hiddenLines += Math.max(0, queued.length - MAX_VISIBLE_LINES);
  queued = [];
  pane.append(frag);
  const lineNodes = pane.querySelectorAll(":scope > span:not(.truncated)");
  const excess = lineNodes.length - MAX_VISIBLE_LINES;
  for (let i = 0; i < excess; i++) lineNodes[i].remove();
  hiddenLines += Math.max(0, excess);
  if (hiddenLines > 0) {
    let note = pane.querySelector<HTMLElement>(".truncated");
    if (!note) {
      note = document.createElement("span");
      note.className = "truncated meta";
      pane.prepend(note);
    }
    note.textContent = `… ${hiddenLines.toLocaleString()} earlier lines hidden. Use "Save log" for the full output.\n`;
  }
  if (atBottom) pane.scrollTop = pane.scrollHeight;
}

function clearConsole() {
  log = [];
  queued = [];
  hiddenLines = 0;
  ui.console.replaceChildren();
}

// ---------------------------------------------------------------------------------------------
// Game builder dialog
// ---------------------------------------------------------------------------------------------

let lastGame: GameSpec = structuredClone(DEFAULT_GAME);

function addMoveRow(move: Move) {
  const row = document.createElement("div");
  row.className = "move-row";
  const name = document.createElement("input");
  name.type = "text";
  name.value = move.name;
  name.placeholder = "name";
  name.spellcheck = false;
  name.setAttribute("aria-label", "Move name");
  name.className = "move-name";
  const constraints = document.createElement("textarea");
  constraints.rows = Math.max(1, move.constraints.split("\n").length);
  constraints.value = move.constraints;
  constraints.placeholder = "x_ == x + 1";
  constraints.spellcheck = false;
  constraints.setAttribute("aria-label", "Move constraints");
  constraints.className = "move-constraints";
  const remove = document.createElement("button");
  remove.type = "button";
  remove.className = "btn icon ghost";
  remove.textContent = "✕";
  remove.setAttribute("aria-label", "Remove move");
  remove.addEventListener("click", () => row.remove());
  row.append(name, constraints, remove);
  ui.movesList.append(row);
}

function fillBuilder(spec: GameSpec) {
  const f = ui.builderForm.elements;
  (f.namedItem("title") as HTMLInputElement).value = spec.title;
  (f.namedItem("variables") as HTMLInputElement).value = spec.variables;
  (f.namedItem("type") as HTMLSelectElement).value = spec.type;
  (f.namedItem("goal") as HTMLTextAreaElement).value = spec.goal;
  (f.namedItem("environment") as HTMLTextAreaElement).value = spec.environment;
  (f.namedItem("init") as HTMLTextAreaElement).value = spec.init;
  ui.builderForm.querySelector<HTMLInputElement>(`input[name="objective"][value="${spec.objective}"]`)!.checked = true;
  ui.movesList.replaceChildren();
  spec.moves.forEach(addMoveRow);
  updateObjectiveHint();
  ui.builderErrors.replaceChildren();
}

function readBuilder(): GameSpec {
  const data = new FormData(ui.builderForm);
  return {
    title: String(data.get("title") ?? ""),
    variables: String(data.get("variables") ?? ""),
    type: String(data.get("type")) as GameType,
    objective: String(data.get("objective")) as Objective,
    goal: String(data.get("goal") ?? ""),
    environment: String(data.get("environment") ?? ""),
    init: String(data.get("init") ?? ""),
    moves: [...ui.movesList.querySelectorAll(".move-row")].map((row) => ({
      name: row.querySelector<HTMLInputElement>(".move-name")!.value,
      constraints: row.querySelector<HTMLTextAreaElement>(".move-constraints")!.value,
    })),
  };
}

function updateObjectiveHint() {
  const objective = new FormData(ui.builderForm).get("objective") as Objective | null;
  el("objective-hint").textContent = objective ? `φ in ${OBJECTIVES[objective].ltl}(φ)` : "";
}

// ---------------------------------------------------------------------------------------------
// Misc helpers
// ---------------------------------------------------------------------------------------------

let toastTimer: number | undefined;
function toast(message: string) {
  ui.toast.textContent = message;
  ui.toast.hidden = false;
  window.clearTimeout(toastTimer);
  toastTimer = window.setTimeout(() => (ui.toast.hidden = true), 3200);
}

function download(name: string, text: string) {
  const url = URL.createObjectURL(new Blob([text], { type: "text/plain" }));
  const a = document.createElement("a");
  a.href = url;
  a.download = name;
  a.click();
  setTimeout(() => URL.revokeObjectURL(url), 1000);
}

async function copyText(text: string, done: string) {
  try {
    await navigator.clipboard.writeText(text);
    toast(done);
  } catch {
    toast("Copying is blocked in this browser context.");
  }
}

// ---------------------------------------------------------------------------------------------
// Wiring
// ---------------------------------------------------------------------------------------------

const editor = createEditor(el("editor"), startRun, () => {
  renderSource();
  saveDraft();
});

populateExamples();
startWorker();
if (!(await restoreFromHash()) && !restoreDraft()) loadExample(examples[0]);
history.replaceState(null, "", location.pathname + location.search);

if (/Mac|iPhone|iPad/.test(navigator.platform)) document.querySelector(".shortcut")!.textContent = "⌘ ↵";

ui.exampleSelect.addEventListener("change", () => {
  const example = examples.find((e) => e.id === ui.exampleSelect.value);
  if (example) loadExample(example);
});
ui.modeGroup.addEventListener("change", saveDraft);
window.addEventListener("pagehide", writeDraft);
document.addEventListener("visibilitychange", () => document.visibilityState === "hidden" && writeDraft());
ui.runBtn.addEventListener("click", startRun);
ui.stopBtn.addEventListener("click", () => stopRun());
document.addEventListener("keydown", (e) => {
  if ((e.ctrlKey || e.metaKey) && e.key === "Enter" && !document.querySelector("dialog[open]")) {
    e.preventDefault();
    startRun();
  }
});

el("upload-btn").addEventListener("click", () => ui.fileInput.click());
ui.fileInput.addEventListener("change", async () => {
  const file = ui.fileInput.files?.[0];
  if (file) loadCustom(file.name, await file.text());
  ui.fileInput.value = "";
});
el("download-btn").addEventListener("click", () => download(fileName(), editor.state.doc.toString()));
el("share-btn").addEventListener("click", async () => copyText(await shareLink(), "Share link copied to the clipboard."));

el("copy-log-btn").addEventListener("click", () => copyText(log.join("\n"), "Output copied to the clipboard."));
el("download-log-btn").addEventListener("click", () => download(fileName().replace(/\.py$/, ".log"), log.join("\n") + "\n"));
el("clear-log-btn").addEventListener("click", clearConsole);

el("help-btn").addEventListener("click", () => ui.help.showModal());

el("new-game-btn").addEventListener("click", () => {
  fillBuilder(lastGame);
  ui.builder.showModal();
});
el("add-move-btn").addEventListener("click", () => {
  addMoveRow({ name: `move${ui.movesList.children.length + 1}`, constraints: "" });
  ui.movesList.querySelector<HTMLInputElement>(".move-row:last-child .move-name")?.focus();
});
ui.builderForm.addEventListener("change", (e) => {
  if ((e.target as HTMLInputElement).name === "objective") updateObjectiveHint();
});
ui.builderForm.addEventListener("submit", (e) => {
  if ((e.submitter as HTMLButtonElement | null)?.value !== "create") return;
  const spec = readBuilder();
  const errors = validate(spec);
  if (errors.length > 0) {
    e.preventDefault();
    const list = document.createElement("ul");
    for (const err of errors) list.append(Object.assign(document.createElement("li"), { textContent: err }));
    ui.builderErrors.replaceChildren(list);
    return;
  }
  lastGame = spec;
  loadCustom(`${spec.title || "custom-game"}.py`, generate(spec), "simple");
  toast("Game created. Press Synthesize to solve it.");
});
