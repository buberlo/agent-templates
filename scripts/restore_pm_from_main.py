#!/usr/bin/env python3
"""Restore project-management workflows from main (German paths) and remap slugs."""
from __future__ import annotations

import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DOMAINS = ROOT / "domains"

MAP = [
    ("projektmanagement/agile-kanban/agile-kanban-workflow.md", "project-management/agile-kanban/agile-kanban-workflow.md"),
    ("projektmanagement/jira-linear/jira-linear-workflow.md", "project-management/jira-linear/jira-linear-workflow.md"),
    ("projektmanagement/planung/planung-workflow.md", "project-management/planning/planning-workflow.md"),
    ("projektmanagement/reporting/reporting-workflow.md", "project-management/reporting/reporting-workflow.md"),
    ("projektmanagement/tasks/tasks-workflow.md", "project-management/tasks/tasks-workflow.md"),
]

REPL = [
    ("domain: projektmanagement", "domain: project-management"),
    ("category: planung", "category: planning"),
    ('(projektmanagement/', '(project-management/'),
]


def main() -> None:
    for src, dest in MAP:
        raw = subprocess.check_output(
            ["git", "show", f"main:domains/{src}"], cwd=ROOT, text=True, errors="replace"
        )
        for a, b in REPL:
            raw = raw.replace(a, b)
        out = DOMAINS / dest
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(raw, encoding="utf-8")
        print(f"Wrote {dest}")


if __name__ == "__main__":
    main()