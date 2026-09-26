// Messages exchanged between the UI thread and the Pyodide worker.

export type RuntimePhase = "python" | "z3" | "gensys" | "ready" | "failed";

export type ToWorker = { type: "run"; id: number; code: string; argv: string[] };

export type FromWorker =
  | { type: "status"; phase: RuntimePhase; detail?: string }
  | { type: "output"; id: number; stream: "stdout" | "stderr"; lines: string[] }
  | { type: "done"; id: number; exitCode: number; elapsedMs: number };
