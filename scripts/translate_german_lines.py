#!/usr/bin/env python3
"""Fast line-level DE→EN pass; preserves structure and code fences."""
from __future__ import annotations

import argparse
import re
from pathlib import Path

import argostranslate.translate

ROOT = Path(__file__).resolve().parent.parent
DOMAINS = ROOT / "domains"

GERMAN_HINT = re.compile(
    r"[äöüÄÖÜß]|\b(und|der|die|das|für|fuer|nicht|mit|Zweck|Arbeitsablauf|"
    r"Grundbeispiele|Beispiel|Wann|Freigabe|Lieferobjekt|Eingabe|Umsätze|"
    r"Quelle|Kategorie|sowie|wurde|können|koennen)\b",
    re.I,
)


def translator():
    t = argostranslate.translate.get_translation_from_codes("de", "en")
    if t:
        return t
    raise SystemExit("Install de→en model via scripts/machine_translate_domains.py once")


def split_frontmatter(text: str):
    if not text.startswith("---"):
        return None, text
    end = text.find("\n---", 3)
    if end == -1:
        return None, text
    body_start = end + 4
    if body_start < len(text) and text[body_start] == "\n":
        body_start += 1
    return text[3:end], text[body_start:]


def translate_line(t, line: str) -> str:
    if not GERMAN_HINT.search(line):
        return line
    if line.strip().startswith("|") and "http" in line:
        cells = line.split("|")
        return "|".join(t.translate(c) if GERMAN_HINT.search(c) else c for c in cells)
    return t.translate(line)


def process(text: str, t) -> str:
    fm, body = split_frontmatter(text)
    in_code = False
    out_lines = []
    for line in body.splitlines(keepends=True):
        if line.strip().startswith("```"):
            in_code = not in_code
            out_lines.append(line)
            continue
        if in_code:
            out_lines.append(line)
            continue
        stripped = line.rstrip("\n")
        out_lines.append(translate_line(t, stripped) + ("\n" if line.endswith("\n") else ""))
    new_body = "".join(out_lines)
    if fm is None:
        return new_body
    new_fm_lines = [translate_line(t, ln) for ln in fm.splitlines()]
    return f"---\n" + "\n".join(new_fm_lines) + f"\n---\n{new_body}"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=DOMAINS)
    args = parser.parse_args()
    t = translator()
    n = 0
    for path in sorted(args.root.rglob("*.md")):
        text = path.read_text(encoding="utf-8")
        if not GERMAN_HINT.search(text):
            continue
        path.write_text(process(text, t), encoding="utf-8")
        n += 1
        try:
            shown = path.relative_to(ROOT)
        except ValueError:
            shown = path
        print(shown, flush=True)
    print(f"Done {n} files.")


if __name__ == "__main__":
    main()