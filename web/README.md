# GenSys-LTL Playground

A web frontend for GenSys-LTL. Users write a logical LTL game (or pick one of the 27 ASE 2023 benchmarks), choose an encoding, and run synthesis. Everything runs in the browser: the page loads Python ([Pyodide](https://pyodide.org)) and the [Z3](https://github.com/Z3Prover/z3) solver as WebAssembly, and runs the `gensys` package from this repository. There is no backend, so the site is a set of static files that Cloudflare can host.

## Features

- **Examples:** the benchmark suite in `../benchmarks`, bundled at build time, with its descriptions and specifications.
- **Editor:** a Python editor (CodeMirror) for writing or changing specifications. <kbd>Ctrl</kbd>/<kbd>⌘</kbd>+<kbd>Enter</kbd> runs.
- **Encodings:** Simple, Product Büchi, Product co-Büchi and On-the-fly. The choice is passed to the script as `sys.argv[1]`, exactly as `python3 benchmark.py <mode>` does.
- **Game builder:** a form for simple games (G, F, GF or FG objectives over `Int`, `Real` or `Bool` variables) that generates a GenSys-LTL script.
- **Results:** a Realizable/Unrealizable verdict, iteration count, run time, and the streamed solver output (which you can copy or save). The benchmarks' exit codes 5 (encoding not applicable) and 6 (encoding not provided) are reported as such.
- **Stop and time limits:** a run executes in a Web Worker, so the page stays responsive. Stop ends the worker and starts a new one.
- **Sharing:** Share copies a link that encodes the specification in the URL fragment, so it never reaches a server. Drafts are kept in the browser's local storage.

## Layout

```
web/
├── index.html              page markup and dialogs
├── src/
│   ├── main.ts             UI: examples, runs, output, builder, sharing
│   ├── worker.ts           Web Worker that boots Pyodide, installs Z3 and gensys, runs scripts
│   ├── py/harness.py       runs a script as __main__ with sys.argv and returns its exit code
│   ├── builder.ts          form → GenSys-LTL script generator
│   ├── examples.ts         benchmark metadata (bundled from ../benchmarks)
│   ├── editor.ts           CodeMirror setup
│   └── styles.css
├── scripts/
│   ├── prepare-runtime.mjs copies Pyodide into public/pyodide/<version>/ and downloads the Z3 wheel (SHA-256 checked)
│   └── smoke-test.mjs      runs benchmarks on the same runtime under Node
├── public/_headers         security and caching headers for Cloudflare
├── runtime.json            the pinned Z3 WebAssembly wheel
└── wrangler.jsonc          Cloudflare Workers static-assets configuration
```

The `gensys/*.py` sources and the benchmarks are imported from the repository root at build time, so the site always runs the checked-in engine.

## Develop

Requires Node.js 22.12 or later.

```sh
cd web
npm install
npm run dev      # http://localhost:5173
npm test         # runs a smoke suite of benchmarks through Pyodide + Z3 under Node
npm run build    # type-checks and writes the static site to dist/
```

`node scripts/smoke-test.mjs <benchmark> <mode>` runs a single benchmark on the browser runtime, for example `node scripts/smoke-test.mjs 11_elevator3 product-buchi`.

## Deploy to Cloudflare

The build output is about 20 MB of static files. The largest, `pyodide.asm.wasm`, is under 10 MB, well within Cloudflare's 25 MiB limit per file.

**Workers with static assets (recommended).** From `web/`:

```sh
npx wrangler login
npm run deploy   # builds, then uploads dist/ as the Worker "gensys-ltl-playground"
```

To deploy on every push instead, connect the repository in the Cloudflare dashboard (*Workers & Pages → Create → Import a repository*) with these settings:

| Setting | Value |
|---|---|
| Root directory | `web` |
| Build command | `npm run build` |
| Deploy command | `npx wrangler deploy` |

**Cloudflare Pages** also works: set the root directory to `web`, the build command to `npm run build`, and the output directory to `dist`.

Both platforms apply `public/_headers`. It sets a Content-Security-Policy (`script-src 'self' 'wasm-unsafe-eval'`, with nothing loaded from other origins) and long-lived caching for the hashed bundles and the versioned runtime directory.

## Runtime notes

- **Checked against the native tool.** The browser runs Python 3.14 (Pyodide 314.0.7) with Z3 5.1.0, the Z3 release that ships a Pyodide wheel. The native setup in the main README uses Z3 4.12.1. All 108 benchmark/encoding pairs (27 benchmarks × 4 encodings) were run both ways: natively on Python 3.11 with Z3 4.12.1 and a 60 s limit, and on this runtime under Node with a 120 s limit. Every pair that finished both ways (92 of them) gave the same exit code, verdicts and iteration counts. Two of those needed longer than 120 s in WebAssembly and were re-run to completion. The other 16 pairs timed out both ways and were not compared.
- **Python 3.13+.** From Python 3.13, `exec()` can no longer create local variables that `locals()` reads back (PEP 667). The fixpoint procedures in `gensys/fixpoints.py` declared their Z3 variables that way, so they now create them directly with `declare_state_variables`. The result is the same, including the `new123` renaming of state variables that clash with a procedure's own names. On Python 3.11 with Z3 4.12.1, all 108 benchmark/encoding pairs produce identical output before and after this change (for runs that time out, identical up to the cutoff).
- **Upgrading Pyodide.** The Z3 wheel's ABI tag (`pyemscripten_2026_0`) must match Pyodide's `abi_version`. `prepare-runtime` refuses to build when they differ. To upgrade, change the `pyodide` version in `package.json` and the wheel in `runtime.json` together.
- **Performance.** Z3 is single-threaded in WebAssembly, so the `ParOr` tactic in `gensys/fixpoints.py` tries its two strategies one after the other instead of racing them. Most benchmarks run within 1–3× of their native time. Some are much slower: the Cinderella–Stepmother product encodings take 10× or longer (C = 3 with Product Büchi takes about 10 minutes, against 4 s natively). Use the time limit or Stop for heavy runs.
- **Automata.** As with the native tool, product and on-the-fly games take hand-written automata. Spot is not available in the browser.
