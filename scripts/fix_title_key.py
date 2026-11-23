#!/usr/bin/env python3
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
for path in ROOT.glob("domains/*/*/*.md"):
    text = path.read_text(encoding="utf-8")
    if "Title:" in text.split("---", 2)[1] if text.startswith("---") else "":
        text = text.replace("\nTitle:", "\ntitle:")
        path.write_text(text, encoding="utf-8")
        print(path)