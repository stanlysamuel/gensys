// The ASE 2023 benchmark suite, bundled straight from ../../benchmarks so the playground never drifts from it.
const sources = import.meta.glob<string>("../../benchmarks/*.py", { query: "?raw", import: "default", eager: true });

export interface Example {
  id: string; // file stem, e.g. "1_cinderella-C2"
  number: number;
  title: string;
  spec: string; // the "Spec:" line of the header comment
  description: string; // the rest of the header comment
  mode: Mode; // encoding to preselect
  code: string;
}

export type Mode = "simple" | "product-buchi" | "product-co-buchi" | "otf";

export const MODES: { value: Mode; label: string }[] = [
  { value: "simple", label: "Simple" },
  { value: "product-buchi", label: "Product Büchi" },
  { value: "product-co-buchi", label: "Product co-Büchi" },
  { value: "otf", label: "On-the-fly" },
];

// Display names, and the encoding to preselect where the simple one does not apply (the script exits with code 5).
const META: Record<string, { title: string; mode?: Mode }> = {
  "cinderella-C2": { title: "Cinderella–Stepmother (C = 2)" },
  "cinderella-C3": { title: "Cinderella–Stepmother (C = 3)" },
  "repair-lock": { title: "Repair lock" },
  "repair-critical-safety": { title: "Repair critical (safety)" },
  "synth-synchronization": { title: "Synthesize synchronization" },
  "cinderella-environment-reach": { title: "Cinderella–Stepmother (reachability)" },
  "cinderella-buchi": { title: "Cinderella–Stepmother (Büchi)" },
  "cinderella-genltl": { title: "Cinderella–Stepmother (general LTL)", mode: "otf" },
  "cinderella-scalability-test": { title: "Cinderella–Stepmother (scalability)" },
  "repair-critical-genltl": { title: "Repair critical (general LTL)", mode: "product-buchi" },
  elevator3: { title: "Elevator, 3 floors", mode: "product-buchi" },
  elevator4: { title: "Elevator, 4 floors", mode: "product-buchi" },
  elevator5: { title: "Elevator, 5 floors", mode: "product-buchi" },
  elevator8: { title: "Elevator, 8 floors", mode: "product-buchi" },
  elevator10: { title: "Elevator, 10 floors", mode: "product-buchi" },
  "watertank-safety": { title: "Water tanks (safety)" },
  "watertank-liveness": { title: "Water tank (liveness)", mode: "product-buchi" },
  sort3: { title: "Sort 3 variables" },
  sort4: { title: "Sort 4 variables" },
  sort5: { title: "Sort 5 variables" },
  box: { title: "Box" },
  "box-limited": { title: "Box (limited)" },
  diagonal: { title: "Diagonal" },
  evasion: { title: "Evasion" },
  follow: { title: "Follow" },
  "solitary-box": { title: "Solitary box" },
  square: { title: "Square" },
};

// Collects the comments that follow the imports, up to the "# 0. Define game type" step or the first code line.
function headerComment(code: string): string[] {
  const lines: string[] = [];
  for (const raw of code.split("\n")) {
    const line = raw.trim();
    if (line === "" || (lines.length === 0 && (line.startsWith("from ") || line.startsWith("import ")))) continue;
    if (!line.startsWith("#") || /^#\s*0\./.test(line)) break;
    lines.push(line.replace(/^#\s?/, ""));
  }
  return lines;
}

export const examples: Example[] = Object.entries(sources)
  .map(([path, code]) => {
    const id = path.split("/").pop()!.replace(/\.py$/, "");
    const [num, slug] = id.split(/_(.*)/s);
    const comment = headerComment(code);
    const specIndex = comment.findIndex((l) => /^spec(ification)?\s*:/i.test(l));
    const spec = specIndex >= 0 ? comment[specIndex].replace(/^spec(ification)?\s*:\s*/i, "") : "";
    const description = comment.filter((_, i) => i !== specIndex).join(" ");
    return { id, number: Number(num), title: META[slug]?.title ?? slug, spec, description, mode: META[slug]?.mode ?? "simple", code };
  })
  .sort((a, b) => a.number - b.number);
