#!/usr/bin/env python3
"""Translate one markdown file under domains/ (Argos, single process)."""
from __future__ import annotations

import sys
from pathlib import Path

# script dir on path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from _translate_three_domains import apply_migrate, git_main, rel_to_main, translate_file

ROOT = Path(__file__).resolve().parent.parent / "domains"


def main() -> None:
    if len(sys.argv) != 2:
        raise SystemExit("usage: translate_one_file.py <path-under-domains>")
    rel = sys.argv[1].replace("domains/", "")
    path = ROOT / rel
    if not path.is_file():
        raw = git_main(rel_to_main(rel))
        if not raw:
            raise SystemExit(f"no source: {rel}")
        text = apply_migrate(raw)
    else:
        text = path.read_text(encoding="utf-8")
    path.write_text(translate_file(text), encoding="utf-8")
    print("ok", rel)


if __name__ == "__main__":
    main()