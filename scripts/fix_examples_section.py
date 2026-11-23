#!/usr/bin/env python3
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

for path in ROOT.glob("domains/*/*/*.md"):
    if path.name.startswith("_"):
        continue
    text = path.read_text(encoding="utf-8")
    if "### Example" not in text:
        continue
    if "## Basic examples" in text:
        continue
    text = re.sub(r"(^### Example \d+)", r"## Basic examples\n\n\1", text, count=1, flags=re.M)
    path.write_text(text, encoding="utf-8")
print("done")