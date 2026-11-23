#!/usr/bin/env python3
from pathlib import Path
from translate_german_lines import GERMAN_HINT, process, translator

ROOT = Path(__file__).resolve().parent.parent

def main() -> None:
    t = translator()
    n = 0
    for path in sorted((ROOT / "domains").rglob("_category.md")):
        text = path.read_text(encoding="utf-8").replace("**Stand:**", "**As of:**")
        if not GERMAN_HINT.search(text):
            continue
        path.write_text(process(text, t), encoding="utf-8")
        n += 1
        print(path.relative_to(ROOT))
    print(f"Updated {n} category files.")

if __name__ == "__main__":
    main()