#!/usr/bin/env python3
"""Line-by-line offline translation (low memory)."""
import re
import sys
from pathlib import Path

import argostranslate.translate

ROOT = Path(__file__).resolve().parent.parent / "domains"
GERMAN = re.compile(r"[äöüßÄÖÜ]|\b(und|für|mit|nicht|wenn|wird|sind|Ziel|Nutzer|Freigabe|Wann nicht)\b", re.I)
de = next(l for l in argostranslate.translate.get_installed_languages() if l.code == "de")
en = next(l for l in argostranslate.translate.get_installed_languages() if l.code == "en")
TR = de.get_translation(en)


def tr_line(line: str) -> str:
    if not GERMAN.search(line) or "http://" in line or "https://" in line:
        return line
    return TR.translate(line)


def process(path: Path) -> bool:
    raw = path.read_text(encoding="utf-8")
    in_fm = in_code = False
    fm_done = False
    out = []
    for line in raw.splitlines(keepends=True):
        if line.strip() == "---":
            if not fm_done:
                in_fm = not in_fm
                if not in_fm:
                    fm_done = True
            out.append(line)
            continue
        if line.strip().startswith("```"):
            in_code = not in_code
            out.append(line)
            continue
        if in_code or (in_fm and not line.startswith("title:") and not line.startswith("  - ")):
            out.append(line)
            continue
        out.append(tr_line(line.rstrip("\n")) + ("\n" if line.endswith("\n") else ""))
    text = "".join(out)
    if text != raw:
        path.write_text(text, encoding="utf-8")
        return True
    return False


def main() -> None:
    targets = [ROOT / d for d in ("data-analytics", "devops-cloud", "education")]
    files = []
    for t in targets:
        files += sorted(t.rglob("*.md"))
    if "--remaining" in sys.argv:
        files = [p for p in files if GERMAN.search(p.read_text(encoding="utf-8"))]
    changed = 0
    for i, p in enumerate(files, 1):
        did = process(p)
        if did:
            changed += 1
        print(f"{i}/{len(files)} {'*' if did else ''}{p.relative_to(ROOT.parent)}", flush=True)
    print("changed", changed, "total", len(files))


if __name__ == "__main__":
    main()