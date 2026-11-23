#!/usr/bin/env python3
"""Apply Phase-3 hand-authored bodies to workflow templates (eight domains)."""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent))
from phase3_eight_domains_data import TEMPLATES  # noqa: E402


def split_frontmatter(text: str) -> tuple[str | None, str]:
    if not text.startswith("---"):
        return None, text
    end = text.find("\n---", 3)
    if end == -1:
        return None, text
    body_start = end + 4
    if body_start < len(text) and text[body_start] == "\n":
        body_start += 1
    return text[3:end].strip() + "\n", text[body_start:]


def main() -> int:
    written = 0
    for rel, body in TEMPLATES.items():
        path = ROOT / rel
        if not path.exists():
            raise SystemExit(f"missing template path: {rel}")
        text = path.read_text(encoding="utf-8")
        fm, _old = split_frontmatter(text)
        if fm is None:
            raise SystemExit(f"no frontmatter: {rel}")
        path.write_text(f"---\n{fm}---\n\n{body.lstrip()}\n", encoding="utf-8")
        written += 1
    print(f"Updated {written} templates")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())