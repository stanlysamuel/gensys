// Runs benchmarks through the same runtime the site uses (Pyodide + the Z3 wheel + src/py/harness.py) under Node.
//   node scripts/smoke-test.mjs                    run the smoke suite below
//   node scripts/smoke-test.mjs <benchmark> <mode> run one benchmark (file stem) and print its output
import { readFile, readdir } from "node:fs/promises";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";
import { loadPyodide } from "pyodide";

const webDir = join(dirname(fileURLToPath(import.meta.url)), "..");
const repoDir = join(webDir, "..");
const runtime = JSON.parse(await readFile(join(webDir, "runtime.json"), "utf8"));
const { version } = JSON.parse(await readFile(join(webDir, "node_modules", "pyodide", "package.json"), "utf8"));
const wheel = join(webDir, "public", "pyodide", version, runtime.z3Wheel.file);

const SUITE = [
  // [benchmark, encoding, expected exit code, expected last verdict]
  ["1_cinderella-C2", "simple", 0, "REALIZABLE"],
  ["3_repair-lock", "product-buchi", 0, "REALIZABLE"],
  ["6_cinderella-environment-reach", "simple", 0, "REALIZABLE"],
  ["11_elevator3", "simple", 5, null],
  ["16_watertank-safety", "product-co-buchi", 0, "REALIZABLE"],
  ["18_sort3", "otf", 0, "REALIZABLE"],
  ["22_box-limited", "simple", 0, "UNREALIZABLE"],
];

let output = [];
const py = await loadPyodide({ stdout: (l) => output.push(l), stderr: (l) => output.push(l) });
await py.loadPackage(wheel, { messageCallback: () => {} });
py.FS.mkdirTree("/home/pyodide/gensys");
for (const file of await readdir(join(repoDir, "gensys"))) {
  if (file.endsWith(".py")) py.FS.writeFile(`/home/pyodide/gensys/${file}`, await readFile(join(repoDir, "gensys", file), "utf8"));
}
py.runPython(await readFile(join(webDir, "src", "py", "harness.py"), "utf8"));
const runSpec = py.globals.get("run_spec");

async function run(benchmark, mode) {
  output = [];
  py.FS.writeFile("/home/pyodide/spec.py", await readFile(join(repoDir, "benchmarks", `${benchmark}.py`), "utf8"));
  const start = performance.now();
  const exitCode = runSpec("/home/pyodide/spec.py", py.toPy([mode]));
  const verdict = output.map((l) => l.trim()).filter((l) => l === "REALIZABLE" || l === "UNREALIZABLE").pop() ?? null;
  return { exitCode, verdict, seconds: (performance.now() - start) / 1000, output };
}

if (process.argv.length === 4) {
  const r = await run(process.argv[2], process.argv[3]);
  console.log(r.output.join("\n"));
  console.log(`exit=${r.exitCode} verdict=${r.verdict} time=${r.seconds.toFixed(2)}s`);
  process.exit(0);
}

let failures = 0;
for (const [benchmark, mode, exitCode, verdict] of SUITE) {
  const r = await run(benchmark, mode);
  const ok = r.exitCode === exitCode && r.verdict === verdict;
  if (!ok) failures++;
  console.log(`${ok ? "ok  " : "FAIL"} ${benchmark} ${mode}: exit=${r.exitCode} verdict=${r.verdict} (${r.seconds.toFixed(2)}s)`);
  if (!ok) console.log(r.output.slice(-15).join("\n"));
}
console.log(failures ? `${failures} of ${SUITE.length} failed` : `all ${SUITE.length} passed`);
process.exit(failures ? 1 : 0);
