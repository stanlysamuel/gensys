import { readFileSync } from "node:fs";
import { defineConfig } from "vite";

const readJson = (path: string) => JSON.parse(readFileSync(new URL(path, import.meta.url), "utf8"));
const runtime = readJson("./runtime.json");
const pyodide = readJson("./node_modules/pyodide/package.json");

export default defineConfig({
  define: {
    __PYODIDE_VERSION__: JSON.stringify(pyodide.version),
    __Z3_WHEEL__: JSON.stringify(runtime.z3Wheel.file),
  },
  // The app bundles the gensys package and benchmarks from the repository root.
  server: { fs: { allow: [".."] } },
  worker: { format: "es" },
  build: { target: "es2022", chunkSizeWarningLimit: 1000 },
});
