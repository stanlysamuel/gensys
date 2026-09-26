// Copies the Pyodide runtime out of node_modules and downloads the Z3 WebAssembly wheel into
// public/pyodide/<pyodide-version>/, so the site serves everything itself (no CDN at runtime).
import { createHash } from "node:crypto";
import { copyFile, mkdir, readFile, rm, writeFile } from "node:fs/promises";
import { existsSync, readdirSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";

const webDir = join(dirname(fileURLToPath(import.meta.url)), "..");
const pyodideDir = join(webDir, "node_modules", "pyodide");
const runtime = JSON.parse(await readFile(join(webDir, "runtime.json"), "utf8"));
const { version } = JSON.parse(await readFile(join(pyodideDir, "package.json"), "utf8"));
const lock = JSON.parse(await readFile(join(pyodideDir, "pyodide-lock.json"), "utf8"));

if (lock.info.abi_version !== runtime.z3Wheel.abi) {
  throw new Error(
    `Pyodide ${version} has ABI ${lock.info.abi_version}, but the Z3 wheel in runtime.json targets ` +
      `${runtime.z3Wheel.abi}. Pin a Pyodide release with a matching ABI or update runtime.json.`,
  );
}

const publicRoot = join(webDir, "public", "pyodide");
const outDir = join(publicRoot, version);
await mkdir(outDir, { recursive: true });

// Remove runtimes left behind by earlier Pyodide versions.
for (const entry of readdirSync(publicRoot)) {
  if (entry !== version) await rm(join(publicRoot, entry), { recursive: true, force: true });
}

for (const file of ["pyodide.mjs", "pyodide.asm.mjs", "pyodide.asm.wasm", "python_stdlib.zip", "pyodide-lock.json"]) {
  await copyFile(join(pyodideDir, file), join(outDir, file));
}

const sha256 = (buf) => createHash("sha256").update(buf).digest("hex");
const wheelPath = join(outDir, runtime.z3Wheel.file);
if (!existsSync(wheelPath) || sha256(await readFile(wheelPath)) !== runtime.z3Wheel.sha256) {
  console.log(`Downloading ${runtime.z3Wheel.file} ...`);
  const res = await fetch(runtime.z3Wheel.url);
  if (!res.ok) throw new Error(`Failed to download the Z3 wheel: HTTP ${res.status}`);
  const buf = Buffer.from(await res.arrayBuffer());
  if (sha256(buf) !== runtime.z3Wheel.sha256) throw new Error("Z3 wheel checksum mismatch");
  await writeFile(wheelPath, buf);
}

console.log(`Runtime ready: Pyodide ${version} (Python ${lock.info.python}) + ${runtime.z3Wheel.file}`);
