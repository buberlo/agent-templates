#!/usr/bin/env python3
"""Translate remaining German in three domain trees via MyMemory API."""
from __future__ import annotations

import json
import re
import time
import urllib.parse
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent / "domains"
DIRS = ["communication", "content-marketing", "customer-service"]
CODE = re.compile(r"```[\s\S]*?```")
GERMAN = re.compile(
    r"[äöüßÄÖÜ]|\b(und|für|nicht|oder|mit|bei|von|wird|sind|Templates|Entwurf|Nutzer|abgeleitet)\b",
    re.I,
)


def mymemory_translate(text: str, retries: int = 4) -> str:
    if len(text) > 480:
        mid = len(text) // 2
        return mymemory_translate(text[:mid]) + mymemory_translate(text[mid:])
    q = urllib.parse.quote(text)
    url = f"https://api.mymemory.translated.net/get?q={q}&langpair=de|en"
    for i in range(retries):
        try:
            with urllib.request.urlopen(url, timeout=60) as r:
                data = json.loads(r.read().decode())
            time.sleep(0.35)
            return data["responseData"]["translatedText"]
        except Exception:
            time.sleep(2 * (i + 1))
    return text


def protect_codeblock(text: str):
    blocks: list[str] = []

    def repl(m):
        blocks.append(m.group())
        return f"__CB{len(blocks) - 1}__"

    return CODE.sub(repl, text), blocks


def restore_codeblock(text: str, blocks: list[str]) -> str:
    for i, b in enumerate(blocks):
        text = text.replace(f"__CB{i}__", b)
    return text


def translate_file(text: str) -> str:
    in_code = False
    out: list[str] = []
    for line in text.splitlines(keepends=True):
        if line.strip().startswith("```"):
            in_code = not in_code
            out.append(line)
            continue
        if in_code or not GERMAN.search(line):
            out.append(line)
        else:
            out.append(mymemory_translate(line))
    return "".join(out)


def main() -> None:
    updated = 0
    for d in DIRS:
        for path in sorted((ROOT / d).rglob("*.md")):
            text = path.read_text(encoding="utf-8")
            new = translate_file(text)
            if new != text:
                path.write_text(new, encoding="utf-8")
                updated += 1
            print(str(path.relative_to(ROOT)), flush=True)
    print("updated", updated)


if __name__ == "__main__":
    main()