#!/usr/bin/env python3
"""Translate remaining German in three domains (batched per file)."""
from __future__ import annotations

import re
import sys
import time
from pathlib import Path

from deep_translator import GoogleTranslator

ROOT = Path(__file__).resolve().parent.parent / "domains"
TARGETS = [ROOT / "data-analytics", ROOT / "devops-cloud", ROOT / "education"]
T = GoogleTranslator(source="de", target="en")
CHUNK = 4500

GERMAN = re.compile(r"[äöüßÄÖÜ]|\b(und|für|mit|nicht|oder|wenn|wird|sind|auf|aus|bei|Zuerst|Keine|Kein|Siehe|Domän|Nutzer|Repo|Freigabe)\b")


def protect(text: str) -> tuple[str, list[str]]:
    store: list[str] = []

    def put(m: re.Match[str]) -> str:
        store.append(m.group(0))
        return f"\x00P{len(store)-1}\x00"

    for pat in (r"https?://[^\s\)>\"']+", r"```[\s\S]*?```", r"`[^`\n]+`", r"\x00P\d+\x00"):
        text = re.sub(pat, put, text)
    return text, store


def unprotect(text: str, store: list[str]) -> str:
    for i, s in enumerate(store):
        text = text.replace(f"\x00P{i}\x00", s)
    return text


def tr(text: str) -> str:
    text = text.strip()
    if not text or not GERMAN.search(text):
        return text
    protected, store = protect(text)
    if not GERMAN.search(re.sub(r"\x00P\d+\x00", "", protected)):
        return unprotect(protected, store)
    out = []
    for i in range(0, len(protected), CHUNK):
        piece = protected[i : i + CHUNK]
        for _ in range(4):
            try:
                out.append(T.translate(piece))
                break
            except Exception as e:
                time.sleep(2.0)
        else:
            out.append(piece)
        time.sleep(0.25)
    return unprotect("".join(out), store)


def translate_fm_value(val: str) -> str:
    if "://" in val or val.startswith("http"):
        return val
    return tr(val)


def process(path: Path) -> None:
    raw = path.read_text(encoding="utf-8")
    if not GERMAN.search(raw):
        return
    if raw.startswith("---"):
        end = raw.find("\n---\n", 3)
        if end == -1:
            body = raw
            fm = ""
        else:
            fm = raw[: end + 5]
            body = raw[end + 5 :]
    else:
        fm, body = "", raw

    new_fm_lines = []
    for line in fm.splitlines():
        if line.startswith("title:") and '"' in line:
            m = re.match(r'(title:\s*")(.*)(")\s*$', line)
            if m:
                line = f'{m.group(1)}{translate_fm_value(m.group(2))}{m.group(3)}'
        elif re.match(r"\s+version_notes:", line):
            key, _, rest = line.partition(":")
            line = f"{key}:{tr(rest.strip())}" if GERMAN.search(rest) else line
        elif line.strip().startswith("- ") and GERMAN.search(line) and "http" not in line:
            line = tr(line)
        new_fm_lines.append(line)

    if GERMAN.search(body):
        body = tr(body)
    text = "\n".join(new_fm_lines) + body
    if not text.endswith("\n"):
        text += "\n"
    path.write_text(text, encoding="utf-8")


def main() -> None:
    files: list[Path] = []
    for root in TARGETS:
        files.extend(sorted(root.rglob("*.md")))
    for i, p in enumerate(files):
        process(p)
        print(f"{i+1}/{len(files)} {p.name}", flush=True)
    print(len(files))


if __name__ == "__main__":
    main()