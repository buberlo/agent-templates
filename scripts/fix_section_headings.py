#!/usr/bin/env python3
"""Normalize template section headings to validator-required English titles."""
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DOMAINS = ROOT / "domains"
SKIP = set()

REPLACEMENTS = [
    ("## System prompt / instructions", "## System prompt"),
    ("## System-Prompt / Instruktionen", "## System prompt"),
    ("## Quality criteria / Definition of Done", "## Definition of done"),
    ("## Quality Criteria / Definition of Done", "## Definition of done"),
    ("## Security & approvals", "## Security"),
    ("## Wann nicht nutzen", "### When not to use"),
    ("### Wann nicht nutzen", "### When not to use"),
    ("## When not to use", "### When not to use"),
    ("## Zweck", "## Purpose"),
    ("## Wann nutzen", "## When to use"),
    ("## Tool-Stack", "## Tool stack"),
    ("## Arbeitsablauf", "## Workflow"),
    ("## Fallstricke", "## Pitfalls"),
    ("## Grundbeispiele", "## Basic examples"),
    ("## Qualitätskriterien", "## Definition of done"),
    ("## Sicherheit & Freigaben", "## Security"),
    ("## Sicherheit", "## Security"),
    ("### Beispiel ", "### Example "),
    ("(Beispieldaten)", "(Example data)"),
    ("(Praxisbeispiel)", "(Real-world example)"),
]


def main() -> None:
    n = 0
    for path in DOMAINS.rglob("*.md"):
        text = path.read_text(encoding="utf-8")
        orig = text
        for a, b in REPLACEMENTS:
            text = text.replace(a, b)
        if text != orig:
            path.write_text(text, encoding="utf-8")
            n += 1
    print(f"Updated {n} template files.")


if __name__ == "__main__":
    main()