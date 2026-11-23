#!/usr/bin/env python3
"""Recover frontmatter when risk_level was swallowed into outputs list."""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DOMAINS = ROOT / "domains"
SKIP = {"_category.md", "_domain.md"}


def recover(path: Path) -> bool:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---"):
        return False
    end = text.find("\n---", 3)
    if end == -1:
        return False
    body = text[end + 4 :]
    if body.startswith("\n"):
        body = body[1:]
    fm = text[3:end]
    if 'risk_level' not in fm and 'example_count' in fm:
        return False
    if '- "risk_level:' not in fm and '\n  - "risk_level:' not in fm and 'outputs:\n  - "risk_level' not in fm:
        if 'risk_level:' in fm and not fm.count('risk_level:') > 1:
            return False

    dom = path.parts[path.parts.index("domains") + 1]
    cat = path.parts[path.parts.index("domains") + 2]
    stem = path.stem

    title_m = re.search(r'^title:\s*"(.*)"', fm, re.M)
    title = title_m.group(1) if title_m else stem.replace("-", " ").title()

    inputs = re.findall(r'inputs:\s*\n((?:\s+-\s+.*\n)+)', fm)
    outputs = re.findall(r'outputs:\s*\n((?:\s+-\s+.*\n)+)', fm)
    tools_block = ""
    tm = re.search(r'(required_tools:\s*\n(?:\s+-\s+.*\n(?:\s+[^\n]+\n)*)+)', fm)
    if tm:
        tools_block = tm.group(1).rstrip()

    tags_block = ""
    tagm = re.search(r'(tags:\s*\n(?:\s+-\s+.*\n)+)', fm)
    if tagm:
        tags_block = tagm.group(1).rstrip()

    agents_block = ""
    agm = re.search(r'(target_agents:\s*\n(?:\s+-\s+.*\n)+)', fm)
    if agm:
        agents_block = agm.group(1).rstrip()

    def clean_items(block: str) -> list[str]:
        items = []
        for line in block.splitlines():
            m = re.match(r'\s*-\s*"?-?\s*"?(.+?)"?\s*$', line)
            if not m:
                continue
            val = m.group(1).strip().strip('"')
            if val.startswith("risk_level") or val.startswith("example_count") or val.startswith("version:") or val.startswith("updated:"):
                break
            items.append(val)
        return items

    input_items = clean_items(inputs[0]) if inputs else ["Task briefing"]
    output_items = clean_items(outputs[0]) if outputs else ["Documented deliverable"]

    risk = re.search(r'risk_level:\s*(\w+)', fm)
    ec = re.search(r'example_count:\s*(\d+)', fm)
    ver = re.search(r'version:\s*"([^"]+)"', fm)
    upd = re.search(r'updated:\s*"([^"]+)"', fm)

    lines = [
        f"id: {stem}",
        f'title: "{title}"',
        f"domain: {dom}",
        f"category: {cat}",
    ]
    if tags_block:
        lines.append(tags_block)
    else:
        lines += [f"tags:", f"  - {cat}"]
    if agents_block:
        lines.append(agents_block)
    else:
        lines += ["target_agents:", "  - generic-mcp-agents"]
    if tools_block:
        lines.append(tools_block)
    else:
        lines += ["required_tools:", "  - name: primary-tool", '    install: "see category"', '    version_notes: "as of 2026-11-23"']
    lines.append("inputs:")
    for item in input_items:
        lines.append(f'  - "{item}"')
    lines.append("outputs:")
    for item in output_items:
        lines.append(f'  - "{item}"')
    lines += [
        f"risk_level: {risk.group(1) if risk else 'low'}",
        f"example_count: {ec.group(1) if ec else '2'}",
        f'version: "{ver.group(1) if ver else "1.0.0"}"',
        f'updated: "{upd.group(1) if upd else "2026-11-23"}"',
    ]
    new_fm = "\n".join(lines)
    path.write_text(f"---\n{new_fm}\n---\n{body}", encoding="utf-8")
    return True


def main() -> None:
    n = 0
    for path in sorted(DOMAINS.glob("*/*/*.md")):
        if path.name in SKIP or path.name.startswith("_"):
            continue
        if recover(path):
            n += 1
    print(f"Recovered {n} files.")


if __name__ == "__main__":
    main()