import { basicSetup } from "codemirror";
import { indentWithTab } from "@codemirror/commands";
import { python } from "@codemirror/lang-python";
import { HighlightStyle, indentUnit, syntaxHighlighting } from "@codemirror/language";
import { Compartment, EditorState, Prec } from "@codemirror/state";
import { EditorView, keymap } from "@codemirror/view";
import { tags as t } from "@lezer/highlight";

// Colors come from CSS variables, so the editor follows the page's light and dark palettes.
const theme = EditorView.theme({
  "&": { backgroundColor: "var(--surface)", color: "var(--text)", height: "100%" },
  ".cm-scroller": { fontFamily: "var(--mono)", lineHeight: "1.55" },
  ".cm-content": { caretColor: "var(--accent)" },
  ".cm-cursor, .cm-dropCursor": { borderLeftColor: "var(--accent)" },
  ".cm-gutters": { backgroundColor: "var(--surface)", color: "var(--muted)", border: "none" },
  ".cm-activeLine": { backgroundColor: "color-mix(in srgb, var(--accent) 6%, transparent)" },
  ".cm-activeLineGutter": { backgroundColor: "transparent", color: "var(--text)" },
  "&.cm-focused > .cm-scroller > .cm-selectionLayer .cm-selectionBackground, .cm-selectionBackground, .cm-content ::selection":
    { backgroundColor: "color-mix(in srgb, var(--accent) 24%, transparent)" },
  ".cm-selectionMatch": { backgroundColor: "color-mix(in srgb, var(--accent) 12%, transparent)" },
  "&.cm-focused .cm-matchingBracket": { backgroundColor: "color-mix(in srgb, var(--accent) 20%, transparent)" },
  ".cm-foldPlaceholder": { backgroundColor: "var(--surface-2)", border: "1px solid var(--border)", color: "var(--muted)" },
  ".cm-tooltip": { backgroundColor: "var(--surface)", border: "1px solid var(--border)", color: "var(--text)" },
  ".cm-panels": { backgroundColor: "var(--surface-2)", color: "var(--text)" },
  "&.cm-focused": { outline: "none" },
});

const highlight = HighlightStyle.define([
  { tag: [t.keyword, t.controlKeyword, t.definitionKeyword, t.moduleKeyword, t.operatorKeyword], color: "var(--syn-keyword)" },
  { tag: [t.function(t.definition(t.variableName)), t.definition(t.className)], color: "var(--syn-def)", fontWeight: "600" },
  { tag: t.function(t.variableName), color: "var(--syn-builtin)" },
  { tag: [t.string, t.special(t.string)], color: "var(--syn-string)" },
  { tag: [t.number, t.bool, t.null], color: "var(--syn-number)" },
  { tag: t.comment, color: "var(--syn-comment)", fontStyle: "italic" },
  { tag: [t.operator, t.compareOperator, t.arithmeticOperator, t.logicOperator], color: "var(--syn-operator)" },
]);

const darkMode = window.matchMedia("(prefers-color-scheme: dark)");

export function createEditor(parent: HTMLElement, onRun: () => void, onChange: () => void): EditorView {
  const darkness = new Compartment();
  const view = new EditorView({
    parent,
    state: EditorState.create({
      extensions: [
        Prec.highest(keymap.of([{ key: "Mod-Enter", run: () => (onRun(), true) }])),
        basicSetup,
        keymap.of([indentWithTab]),
        indentUnit.of("    "),
        python(),
        theme,
        darkness.of(EditorView.darkTheme.of(darkMode.matches)),
        syntaxHighlighting(highlight),
        EditorView.updateListener.of((u) => u.docChanged && onChange()),
      ],
    }),
  });
  darkMode.addEventListener("change", (e) => view.dispatch({ effects: darkness.reconfigure(EditorView.darkTheme.of(e.matches)) }));
  return view;
}

// Replaces the whole document as one undoable change, so Ctrl+Z brings the previous text back.
export function replaceDoc(view: EditorView, text: string) {
  view.dispatch({ changes: { from: 0, to: view.state.doc.length, insert: text }, selection: { anchor: 0 }, scrollIntoView: true });
}
