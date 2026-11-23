#!/usr/bin/env python3
"""Offline DE→EN translation for domains/**/*.md via Argos Translate."""
from __future__ import annotations

import re
import sys
from pathlib import Path

import argostranslate.package
import argostranslate.translate

ROOT = Path(__file__).resolve().parent.parent
DOMAINS = ROOT / "domains"
CHUNK = 4500

GERMAN_HINT = re.compile(
    r"[äöüÄÖÜß]|\b(und|der|die|das|für|fuer|nicht|mit|Zweck|Arbeitsablauf|"
    r"Grundbeispiele|Beispiel|Wann|Freigabe|Lieferobjekt|Eingabe|Umsätze|"
    r"Quelle|Kategorie|sowie|oder|beim|keine)\b",
    re.I,
)


def get_translator():
    t = argostranslate.translate.get_translation_from_codes("de", "en")
    if t is not None:
        return t
    argostranslate.package.update_package_index()
    pkgs = argostranslate.package.get_available_packages()
    pair = next((p for p in pkgs if p.from_code == "de" and p.to_code == "en"), None)
    if not pair:
        raise SystemExit("No de→en Argos package available")
    path = pair.download()
    argostranslate.package.install_from_path(path)
    return argostranslate.translate.get_translation_from_codes("de", "en")


def translate_text(translator, text: str) -> str:
    if not text.strip() or not GERMAN_HINT.search(text):
        return text
    if len(text) <= CHUNK:
        return translator.translate(text)
    parts = []
    buf = ""
    for block in re.split(r"(\n\n)", text):
        candidate = buf + block
        if len(candidate) > CHUNK and buf:
            parts.append(translate_text(translator, buf))
            buf = block
        else:
            buf = candidate
    if buf:
        parts.append(translate_text(translator, buf))
    return "".join(parts)


def split_frontmatter(text: str):
    if not text.startswith("---"):
        return None, text
    end = text.find("\n---", 3)
    if end == -1:
        return None, text
    body_start = end + 4
    if body_start < len(text) and text[body_start] == "\n":
        body_start += 1
    return text[3:end], text[body_start:]


def translate_quoted_strings(translator, fm: str) -> str:
    out = []
    for line in fm.splitlines():
        if not GERMAN_HINT.search(line):
            out.append(line)
            continue
        m = re.match(r'^(\s*-\s+)"(.+)"\s*$', line)
        if m:
            out.append(f'{m.group(1)}"{translate_text(translator, m.group(2))}"')
            continue
        m = re.match(r'^(title:\s+)"(.+)"\s*$', line)
        if m:
            out.append(f'{m.group(1)}"{translate_text(translator, m.group(2))}"')
            continue
        m = re.match(r'^(\s+version_notes:\s+)"(.+)"\s*$', line)
        if m:
            out.append(f'{m.group(1)}"{translate_text(translator, m.group(2))}"')
            continue
        m = re.match(r'^(\s+install:\s+)"(.+)"\s*$', line)
        if m:
            out.append(f'{m.group(1)}"{translate_text(translator, m.group(2))}"')
            continue
        out.append(line)
    return "\n".join(out)


def process_file(translator, path: Path) -> bool:
    raw = path.read_text(encoding="utf-8")
    if not GERMAN_HINT.search(raw):
        return False
    fm, body = split_frontmatter(raw)
    parts = re.split(r"(```[\s\S]*?```)", body)
    new_parts = []
    for part in parts:
        if part.startswith("```"):
            new_parts.append(part)
        else:
            new_parts.append(translate_text(translator, part))
    new_body = "".join(new_parts)
    if fm:
        fm = translate_quoted_strings(translator, fm)
        out = f"---\n{fm}\n---\n{new_body}"
    else:
        out = new_body
    path.write_text(out, encoding="utf-8")
    return True


def main() -> None:
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=DOMAINS, help="Domain subtree to process")
    args = parser.parse_args()
    translator = get_translator()
    files = sorted(args.root.rglob("*.md"))
    done = 0
    for i, path in enumerate(files, 1):
        try:
            if process_file(translator, path):
                done += 1
                try:
                    shown = path.relative_to(ROOT)
                except ValueError:
                    shown = path
                print(f"[{i}/{len(files)}] {shown}", flush=True)
        except KeyboardInterrupt:
            sys.exit(1)
        except Exception as exc:
            print(f"ERR {path}: {exc}", file=sys.stderr, flush=True)
    print(f"Translated {done} files.")


if __name__ == "__main__":
    main()