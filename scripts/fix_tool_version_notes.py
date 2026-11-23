#!/usr/bin/env python3
"""Indent top-level version_notes lines inside required_tools blocks."""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DOMAINS = ROOT / "domains"


def fix_frontmatter(fm: str) -> str:
    lines = fm.splitlines()
    out = []
    in_tools = False
    for line in lines:
        if line.startswith("required_tools:"):
            in_tools = True
            out.append(line)
            continue
        if in_tools:
            if line.startswith("inputs:") or line.startswith("outputs:") or re.match(
                r"^(risk_level|example_count|version|updated|title|domain|category|id):", line
            ):
                in_tools = False
            elif re.match(r"^version_notes:", line):
                out.append("    " + line)
                continue
        out.append(line)
    return "\n".join(out)


def main() -> None:
    n = 0
    for path in DOMAINS.rglob("*.md"):
        if path.name in ("_category.md", "_domain.md"):
            continue
        text = path.read_text(encoding="utf-8")
        if not text.startswith("---"):
            continue
        end = text.find("\n---", 3)
        if end == -1:
            continue
        fm = text[3:end]
        body = text[end + 4 :]
        if body.startswith("\n"):
            body = body[1:]
        new_fm = fix_frontmatter(fm)
        if new_fm != fm:
            path.write_text(f"---\n{new_fm}\n---\n{body}", encoding="utf-8")
            n += 1
    print(f"Fixed {n} files.")


if __name__ == "__main__":
    main()