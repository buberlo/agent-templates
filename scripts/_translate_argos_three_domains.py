#!/usr/bin/env python3
"""Offline DE->EN translation for three domains (preserves ``` blocks)."""
from __future__ import annotations

import re
from pathlib import Path

import argostranslate.translate

ROOT = Path(__file__).resolve().parent.parent / "domains"
TARGETS = [ROOT / "data-analytics", ROOT / "devops-cloud", ROOT / "education"]
GERMAN = re.compile(r"[äöüßÄÖÜ]|\b(und|für|mit|nicht|oder|wenn|wird|sind|Ziel|Nutzer|Freigabe|Domäne|Begründung)\b", re.I)

langs = argostranslate.translate.get_installed_languages()
de = next(l for l in langs if l.code == "de")
en = next(l for l in langs if l.code == "en")
TR = de.get_translation(en)


def protect_urls(text: str) -> tuple[str, list[str]]:
    store: list[str] = []

    def put(m: re.Match[str]) -> str:
        store.append(m.group(0))
        return f"\x00U{len(store)-1}\x00"

    return re.sub(r"https?://[^\s\)>\"']+", put, text), store


def unprotect(text: str, store: list[str]) -> str:
    for i, s in enumerate(store):
        text = text.replace(f"\x00U{i}\x00", s)
    return text


def tr_block(text: str) -> str:
    if not text.strip() or not GERMAN.search(text):
        return text
    sections = re.split(r"(\n\n+)", text)
    out: list[str] = []
    for sec in sections:
        if not GERMAN.search(sec) or sec.strip() == "":
            out.append(sec)
            continue
        protected, store = protect_urls(sec)
        out.append(unprotect(TR.translate(protected), store))
    return "".join(out)


def process_text(text: str) -> str:
    if not GERMAN.search(text):
        return text
    parts = re.split(r"(```[\s\S]*?```)", text)
    out = []
    for part in parts:
        out.append(part if part.startswith("```") else tr_block(part))
    return "".join(out)


def process(path: Path, force: bool) -> None:
    raw = path.read_text(encoding="utf-8")
    if not force and not GERMAN.search(raw):
        return
    if raw.startswith("---"):
        end = raw.find("\n---\n", 3)
        if end < 0:
            return
        fm, body = raw[3:end], raw[end + 5 :]
        fm = process_text(fm)
        body = process_text(body)
        raw = "---\n" + fm + "\n---\n" + body
    else:
        raw = process_text(raw)
    # post-fix tokens / paths that argos mistranslates
    for a, b in (
        ("data-analytics", "data-analytics"),
        ("MotherDuck", "MotherDuck"),
        ("APPROVAL", "APPROVAL"),
    ):
        pass
    fixes = {
        "data data-analytics": "data-analytics",
        "Mother duck": "MotherDuck",
        "mother duck": "MotherDuck",
        "Git Hub": "GitHub",
        "Play wright": "Playwright",
        "Freigabe": "APPROVAL",
        "freigabe": "approval",
    }
    for a, b in fixes.items():
        raw = raw.replace(a, b)
    if not raw.endswith("\n"):
        raw += "\n"
    path.write_text(raw, encoding="utf-8")


def main() -> None:
    import sys

    only_german = "--remaining" in sys.argv
    files: list[Path] = []
    for root in TARGETS:
        files.extend(sorted(root.rglob("*.md")))
    if only_german:
        files = [p for p in files if GERMAN.search(p.read_text(encoding="utf-8"))]
    for i, p in enumerate(files, 1):
        process(p, force=not only_german)
        print(f"{i}/{len(files)} {p.relative_to(ROOT.parent)}", flush=True)
    print(len(files))


if __name__ == "__main__":
    main()