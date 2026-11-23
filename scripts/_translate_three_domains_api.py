#!/usr/bin/env python3
"""Translate German lines in migrated domain files via Google (rate-limited)."""
from __future__ import annotations

import gc
import re
import sys
import time
from pathlib import Path

from deep_translator import GoogleTranslator

ROOT = Path(__file__).resolve().parent.parent / "domains"
DIRS = ["communication", "content-marketing", "customer-service"]

GERMAN_LINE = re.compile(r"[äöüßÄÖÜ]", re.I)

CODE = re.compile(r"```[\s\S]*?```")
PH = "\uE000C{0}\uE001"


def protect_codeblock(text: str):
    blocks = []

    def repl(m):
        blocks.append(m.group())
        return PH.format(len(blocks) - 1)

    return CODE.sub(repl, text), blocks


def restore_codeblock(text: str, blocks: list[str]) -> str:
    for i, b in enumerate(blocks):
        text = text.replace(PH.format(i), b)
    return text


def split_frontmatter(text: str) -> tuple[str, str]:
    if not text.startswith("---"):
        return "", text
    m = re.match(r"^---\n.*?\n---\n", text, re.S)
    if not m:
        return "", text
    return m.group(), text[m.end() :]


def translate_chunk(text: str, translator: GoogleTranslator) -> str:
    if not GERMAN_LINE.search(text):
        return text
    time.sleep(3)
    return translator.translate(text)


def translate_file(text: str) -> str:
    translator = GoogleTranslator(source="de", target="en")
    fm, body = split_frontmatter(text)
    if fm and GERMAN_LINE.search(fm):
        protected, blocks = protect_codeblock(fm)
        fm = restore_codeblock(translate_chunk(protected, translator), blocks)
    protected, blocks = protect_codeblock(body)
    body = restore_codeblock(translate_chunk(protected, translator), blocks)
    return fm + body


def main() -> None:
    targets = sys.argv[1:] if len(sys.argv) > 1 else None
    n = 0
    for d in DIRS:
        for path in sorted((ROOT / d).rglob("*.md")):
            rel = str(path.relative_to(ROOT))
            if targets and rel not in targets and path.name not in targets:
                continue
            text = path.read_text(encoding="utf-8")
            path.write_text(translate_file(text), encoding="utf-8")
            n += 1
            print(rel, flush=True)
            gc.collect()
    print("done", n)


if __name__ == "__main__":
    main()