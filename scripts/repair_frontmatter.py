#!/usr/bin/env python3
"""Sync domain/category/id and fix list indentation only (safe)."""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DOMAINS = ROOT / "domains"
SKIP = {"_category.md", "_domain.md", "TEMPLATE.md"}


def repair_lists(fm: str) -> str:
    lines = fm.splitlines()
    out = []
    in_list = False
    for line in lines:
        if re.match(r"^(tags|target_agents|inputs|outputs|required_tools):", line):
            in_list = line.startswith(("tags", "target_agents", "inputs", "outputs"))
            out.append(line)
            continue
        if in_list and line.startswith("- ") and not line.startswith("  "):
            out.append("  " + line)
            continue
        if re.match(r"^(risk_level|example_count|version|updated|domain|category|id|title):", line):
            in_list = False
        if line.startswith("  - name:"):
            in_list = False
        out.append(line)
    return "\n".join(out)


def process(path: Path) -> bool:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---"):
        return False
    end = text.find("\n---", 3)
    if end == -1:
        return False
    body_start = end + 4
    if body_start < len(text) and text[body_start] == "\n":
        body_start += 1
    fm = "\n".join(ln for ln in text[3:end].splitlines() if ln.strip())
    body = text[body_start:]
    dom = path.parts[path.parts.index("domains") + 1]
    cat = path.parts[path.parts.index("domains") + 2]
    stem = path.stem
    fm = re.sub(r"^domain:\s*\S+", f"domain: {dom}", fm, flags=re.M)
    fm = re.sub(r"^category:\s*\S+", f"category: {cat}", fm, flags=re.M)
    fm = re.sub(r"^id:\s*\S+", f"id: {stem}", fm, flags=re.M)
    fm = repair_lists(fm)
    new_text = f"---\n{fm}\n---\n{body}"
    if new_text != text:
        path.write_text(new_text, encoding="utf-8")
        return True
    return False


def main() -> None:
    n = sum(1 for p in DOMAINS.glob("*/*/*.md") if p.name not in SKIP and not p.name.startswith("_") and process(p))
    print(f"Repaired {n} templates.")


if __name__ == "__main__":
    main()