#!/usr/bin/env python3
"""Translate German text outside fenced code blocks."""
from __future__ import annotations

import re
import time
from pathlib import Path

from deep_translator import GoogleTranslator

ROOT = Path(__file__).resolve().parent.parent / "domains"
TARGETS = [ROOT / "data-analytics", ROOT / "devops-cloud", ROOT / "education"]
T = GoogleTranslator(source="de", target="en")
GERMAN = re.compile(r"[äöüßÄÖÜ]|\b(und|für|mit|nicht|oder|wenn|wird|sind|Ziel|Nutzer|Nutzen|Freigabe|Domäne|Kategorie|Siehe|Quelle|Begründung|Rolle)\b")


def translate_text_block(block: str) -> str:
    if not block or not GERMAN.search(block):
        return block
    store: list[str] = []

    def put(m: re.Match[str]) -> str:
        store.append(m.group(0))
        return f"\x00S{len(store)-1}\x00"

    protected = re.sub(r"https?://[^\s\)>\"']+", put, block)
    for _ in range(4):
        try:
            translated = T.translate(protected)
            break
        except Exception:
            time.sleep(1.5)
    else:
        translated = protected
    for i, s in enumerate(store):
        translated = translated.replace(f"\x00S{i}\x00", s)
    time.sleep(0.2)
    return translated


def translate_frontmatter(fm: str) -> str:
    out_lines = []
    for line in fm.splitlines():
        if line.startswith("title:") and '"' in line:
            m = re.match(r'(title:\s*")(.*)(")\s*$', line)
            if m and GERMAN.search(m.group(2)):
                val = T.translate(m.group(2))
                line = f'{m.group(1)}{val}{m.group(3)}'
                time.sleep(0.2)
        elif line.startswith("  - ") and GERMAN.search(line) and "http" not in line:
            line = T.translate(line)
            time.sleep(0.2)
        elif re.match(r"\s+version_notes:", line) and GERMAN.search(line):
            prefix, _, rest = line.partition(":")
            line = prefix + ":" + T.translate(rest.strip())
            time.sleep(0.2)
        out_lines.append(line)
    return "\n".join(out_lines)


def process(path: Path) -> None:
    raw = path.read_text(encoding="utf-8")
    if not GERMAN.search(raw):
        return
    if raw.startswith("---"):
        end = raw.find("\n---\n", 3)
        if end < 0:
            return
        fm = raw[3:end]
        body = raw[end + 5 :]
        fm = translate_frontmatter(fm)
        parts = re.split(r"(```[\s\S]*?```)", body)
        new_parts = []
        for part in parts:
            if part.startswith("```"):
                new_parts.append(part)
            else:
                new_parts.append(translate_text_block(part))
        raw = "---\n" + fm + "\n---\n" + "".join(new_parts)
    else:
        parts = re.split(r"(```[\s\S]*?```)", raw)
        raw = "".join(translate_text_block(p) if not p.startswith("```") else p for p in parts)
    if not raw.endswith("\n"):
        raw += "\n"
    path.write_text(raw, encoding="utf-8")


def main() -> None:
    files: list[Path] = []
    for root in TARGETS:
        files.extend(sorted(root.rglob("*.md")))
    for i, p in enumerate(files, 1):
        process(p)
        print(f"{i}/{len(files)} {p}", flush=True)
    print(len(files))


if __name__ == "__main__":
    main()