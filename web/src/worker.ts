/// <reference lib="webworker" />
// Web Worker that hosts Pyodide, Z3 and the GenSys-LTL package. Synthesis runs block this thread,
// never the UI; the UI stops a run by terminating the worker.
import type { PyodideAPI } from "pyodide";
import type { FromWorker, ToWorker } from "./protocol";
import harness from "./py/harness.py?raw";

declare const self: DedicatedWorkerGlobalScope;

// The gensys package is bundled straight from the repository, so the site always runs the checked-in engine.
const gensysSources = import.meta.glob<string>("../../gensys/*.py", { query: "?raw", import: "default", eager: true });

const runtimeBase = new URL(`${import.meta.env.BASE_URL}pyodide/${__PYODIDE_VERSION__}/`, self.location.origin).href;
const SPEC_PATH = "/home/pyodide/spec.py";

function post(msg: FromWorker) {
  self.postMessage(msg);
}

// Python calls the stdout/stderr handlers synchronously while it runs, and timers cannot fire until it
// returns, so output is flushed from inside the handler once enough time has passed.
let currentRun = 0;
const pending: { stdout: string[]; stderr: string[] } = { stdout: [], stderr: [] };
let lastFlush = 0;

function flush() {
  for (const stream of ["stdout", "stderr"] as const) {
    if (pending[stream].length > 0) {
      post({ type: "output", id: currentRun, stream, lines: pending[stream] });
      pending[stream] = [];
    }
  }
  lastFlush = performance.now();
}

function write(stream: "stdout" | "stderr", line: string) {
  pending[stream].push(line);
  if (stream === "stderr" || performance.now() - lastFlush > 60) flush();
}

async function boot(): Promise<PyodideAPI> {
  post({ type: "status", phase: "python" });
  const { loadPyodide } = (await import(/* @vite-ignore */ `${runtimeBase}pyodide.mjs`)) as typeof import("pyodide");
  const py = await loadPyodide({ indexURL: runtimeBase });
  py.setStdout({ batched: (line) => write("stdout", line) });
  py.setStderr({ batched: (line) => write("stderr", line) });

  post({ type: "status", phase: "z3" });
  await py.loadPackage(`${runtimeBase}${__Z3_WHEEL__}`, { messageCallback: () => {} });

  post({ type: "status", phase: "gensys" });
  py.FS.mkdirTree("/home/pyodide/gensys");
  for (const [path, source] of Object.entries(gensysSources)) {
    py.FS.writeFile(`/home/pyodide/gensys/${path.split("/").pop()}`, source);
  }
  py.runPython(harness);
  py.runPython("import gensys.fixpoints");

  const version = py.runPython("import sys, z3; f'Python {sys.version.split()[0]} · Z3 {z3.get_version_string()}'");
  post({ type: "status", phase: "ready", detail: String(version) });
  return py;
}

const ready = boot().catch((err: unknown) => {
  post({ type: "status", phase: "failed", detail: String(err) });
  throw err;
});

self.onmessage = async (event: MessageEvent<ToWorker>) => {
  const msg = event.data;
  if (msg.type !== "run") return;
  const py = await ready;
  currentRun = msg.id;
  py.FS.writeFile(SPEC_PATH, msg.code);
  const runSpec = py.globals.get("run_spec");
  const argv = py.toPy(msg.argv);
  const start = performance.now();
  let exitCode = 1;
  try {
    exitCode = Number(runSpec(SPEC_PATH, argv));
  } catch (err) {
    // run_spec catches every Python exception, so reaching this means Pyodide itself failed.
    write("stderr", String(err));
    exitCode = -1;
  } finally {
    try {
      argv.destroy();
      runSpec.destroy();
    } catch {
      // After a fatal error every Pyodide call throws; the UI restarts the worker.
    }
  }
  const elapsedMs = performance.now() - start;
  flush();
  post({ type: "done", id: msg.id, exitCode, elapsedMs });
};
