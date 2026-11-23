#!/usr/bin/env python3
from pathlib import Path
import re
from translate_german_lines import GERMAN_HINT, translate_line, translator

SUBS = [
    (r"\bKeine\b", "No"),
    (r"\bkeine\b", "no"),
    (r"\bnicht\b", "not"),
    (r"\bNutzer\b", "User"),
    (r"\bbeachten\b", "observe"),
    (r"\bohne\b", "without"),
    (r"\bmit\b", "with"),
    (r"\bund\b", "and"),
    (r"\bfür\b", "for"),
    (r"\bfuer\b", "for"),
    (r"\boder\b", "or"),
    (r"\bAufgabe\b", "Task"),
    (r"\bDateien\b", "Files"),
    (r"\bKatalog\b", "catalog"),
    (r"\bKatalogeintrag\b", "catalog entry"),
    (r"\bErwartetes\b", "Expected"),
    (r"\bErgebnis\b", "result"),
    (r"\bUrheberrecht\b", "copyright"),
    (r"\bVerteilung\b", "distribution"),
    (r"\bcracken\b", "crack"),
    (r"\berfundenen\b", "invented"),
]

def main() -> None:
    t = translator()
    n = 0
    for path in Path("domains").rglob("*.md"):
        text = path.read_text(encoding="utf-8")
        orig = text
        for pat, rep in SUBS:
            text = re.sub(pat, rep, text)
        if GERMAN_HINT.search(text):
            lines = []
            for line in text.splitlines(keepends=True):
                core = line.rstrip("\n")
                if GERMAN_HINT.search(core) and not core.strip().startswith("```"):
                    core = translate_line(t, core)
                lines.append(core + ("\n" if line.endswith("\n") else ""))
            text = "".join(lines)
        if text != orig:
            path.write_text(text, encoding="utf-8")
            n += 1
    print(f"Updated {n} files.")


if __name__ == "__main__":
    main()