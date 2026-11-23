#!/usr/bin/env python3
"""One-off: translate data-analytics, devops-cloud, education markdown to English."""
from __future__ import annotations

import re
import time
from pathlib import Path

from deep_translator import GoogleTranslator

ROOT = Path(__file__).resolve().parent.parent / "domains"
TARGETS = [ROOT / "data-analytics", ROOT / "devops-cloud", ROOT / "education"]

TRANSLATOR = GoogleTranslator(source="de", target="en")

# Longest-first plain replacements (URLs and numbers preserved).
PLAIN: list[tuple[str, str]] = [
    ("Templates und Kategorie-Metadaten für **Daten und Analytics** — abgeleitet aus der Recherche vom 2026-11-23.",
     "Templates and category metadata for **Data and Analytics** — derived from research dated 2026-11-23."),
    ("Templates und Kategorie-Metadaten für **DevOps und Cloud** — abgeleitet aus der Recherche vom 2026-11-23.",
     "Templates and category metadata for **DevOps and Cloud** — derived from research dated 2026-11-23."),
    ("Templates und Kategorie-Metadaten für **Bildung** — abgeleitet aus der Recherche vom 2026-11-23.",
     "Templates and category metadata for **Education** — derived from research dated 2026-11-23."),
    ("# Daten und Analytics", "# Data and Analytics"),
    ("# DevOps und Cloud", "# DevOps and Cloud"),
    ("# Bildung", "# Education"),
    ("| BI und Dashboards |", "| BI and Dashboards |"),
    ("| Datenvisualisierung |", "| Data visualization |"),
    ("| Tabellenanalyse |", "| Spreadsheet analysis |"),
    ("| SQL-Abfragen |", "| SQL queries |"),
    ("| Docker und Container |", "| Docker and containers |"),
    ("| Monitoring und Observability |", "| Monitoring and observability |"),
    ("| Cloud-Kosten |", "| Cloud costs |"),
    ("| Kurse erstellen |", "| Course creation |"),
    ("| Nachhilfe und Tutoring |", "| Tutoring |"),
    ("| Studium und Forschung |", "| Study and research |"),
    ("# BI und Dashboards", "# BI and Dashboards"),
    ("# SQL-Abfragen", "# SQL queries"),
    ("# Datenvisualisierung", "# Data visualization"),
    ("# Tabellenanalyse", "# Spreadsheet analysis"),
    ("# Cloud-Kosten", "# Cloud costs"),
    ("# Kurse erstellen", "# Course creation"),
    ("# Lernkarten", "# Flashcards"),
    ("# Nachhilfe und Tutoring", "# Tutoring"),
    ("# Sprachen", "# Languages"),
    ("# Studium und Forschung", "# Study and research"),
    ("# Docker und Container", "# Docker and containers"),
    ("# Monitoring und Observability", "# Monitoring and observability"),
    ("**Wann nicht**", "**When not to use**"),
    ("| Rolle |", "| Role |"),
    ("| Begründung |", "| Rationale |"),
    ("| Typ |", "| Type |"),
    ("| Siehe required_tools | Kern | Domänenspezifisch |", "| See required_tools | Core | Domain-specific |"),
    ("nein (so belegt)", "no (as documented)"),
    ("Hermes-Katalog", "Hermes catalog"),
    (
        "Nous-approved optional-mcps-Katalogeintrag (Listing 23.11.2026).",
        "Nous-approved optional-mcps catalog entry (listing 2026-11-23).",
    ),
    ("CLI / Bibliothek", "CLI / library"),
    (
        "Dateien und Office-Dokumente nach Markdown wandeln – wird in Skills und MCP-Wrappern genutzt.",
        "Convert files and Office documents to Markdown—used in skills and MCP wrappers.",
    ),
    ("Python-Paket / Repo.", "Python package / repo."),
    ("Analytisches SQL.", "Analytical SQL."),
    ("Analytisches SQL / DuckDB-Cloud.", "Analytical SQL / DuckDB Cloud."),
    ("SQL gegen Supabase, Read-only bevorzugen.", "SQL against Supabase; prefer read-only."),
    ("MCP/Skill-Fokus", "MCP/Skill focus"),
    ("Ergänzung wenn MCP read-only reicht", "Supplement when MCP read-only is enough"),
    (
        "- Auftrag, erlaubte Tools und Definition of Done festlegen.\n"
        "- Zuerst lesen/recherchieren, dann Entwurf, dann Freigabe fuer wirkende Schritte.\n"
        "- Output gegenlesen (Datei, URL, Ticket) und Quelle angeben.",
        "- Confirm the task, allowed tools, and definition of done.\n"
        "- Read/research first, then draft, then approval for consequential steps.\n"
        "- Review output (file, URL, ticket) and cite sources.",
    ),
    (
        "- Skills sind Workflows/Anweisungen (progressive disclosure), MCP sind Verbindungen und Tools. "
        "Beides kombinieren, nicht verwechseln. Quellen: https://code.claude.com/docs/en/features-overview , "
        "https://github.com/ComposioHQ/awesome-claude-skills",
        "- Skills are workflows/instructions (progressive disclosure); MCP servers are connections and tools. "
        "Combine both; do not conflate them. Sources: https://code.claude.com/docs/en/features-overview , "
        "https://github.com/ComposioHQ/awesome-claude-skills",
    ),
    (
        "- Nur die MCPs/Skills aktivieren, die die Aufgabe braucht. Hermes filtert per include/exclude; "
        "OpenClaw hat Tool-Policy und Prompt-Budgets. Quellen: https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp , "
        "https://docs.openclaw.ai/skills/",
        "- Enable only the MCPs/skills the task needs. Hermes filters via include/exclude; "
        "OpenClaw has tool policy and prompt budgets. Sources: https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp , "
        "https://docs.openclaw.ai/skills/",
    ),
    (
        "- Keine Tokens oder Passwörter in Chat, Skill-Dateien oder Command-Argumente von Custom-MCPs schreiben. "
        "Grok-Bot-Wiki: OAuth-Tokens bleiben auf dem Connector-Backend; Command-Server dürfen keine Credentials in argv enthalten. "
        "Quelle: https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp",
        "- Do not put tokens or passwords in chat, skill files, or custom MCP command arguments. "
        "Grok Bot wiki: OAuth tokens stay on the connector backend; command servers must not pass credentials in argv. "
        "Source: https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp",
    ),
    (
        "- Schreiben, Senden, Bezahlen, Deployen und Löschen nur nach expliziter Freigabe; gute Document-Skills "
        "verlangen einen Verify-Schritt (Datei erneut lesen, PDF/PNG rendern).",
        "- Write, send, pay, deploy, and delete only after explicit approval; good document skills require a "
        "verify step (re-read the file, render PDF/PNG).",
    ),
    ("MCP-Server und Skills", "MCP servers and skills"),
    ("| Einsatz |", "| Use |"),
    ("| Installation |", "| Install |"),
    ("| Popularitaet |", "| Popularity |"),
    ("| Quelle |", "| Source |"),
    ("| Unverified? |", "| Unverified |"),
    ("Freigabe", "approval"),
    ("fuer ", "for "),
    ("noetig", "needed"),
    ("pruefen", "check"),
    ("ueber ", "over "),
    ("z. B.", "e.g."),
]

GERMAN_HINT = re.compile(
    r"(ä|ö|ü|ß|Ä|Ö|Ü|\bund\b|\bfür\b|\bmit\b|\bnicht\b|\boder\b|\bwenn\b|\bder\b|\bdie\b|\bdas\b|\bist\b|\bsind\b|\bauf\b|\baus\b|\bbei\b|\bZuerst\b|\bKein\b|\bKeine\b)",
    re.I,
)


def protect_segments(text: str) -> tuple[str, list[str]]:
    store: list[str] = []

    def stash(match: re.Match[str]) -> str:
        store.append(match.group(0))
        return f"\x00SEG{len(store) - 1}\x00"

    text = re.sub(r"https?://[^\s\)>\"']+", stash, text)
    text = re.sub(r"`[^`]+`", stash, text)
    text = re.sub(r"```[\s\S]*?```", stash, text)
    return text, store


def restore_segments(text: str, store: list[str]) -> str:
    for i, seg in enumerate(store):
        text = text.replace(f"\x00SEG{i}\x00", seg)
    return text


def translate_chunk(text: str) -> str:
    text = text.strip()
    if not text or not GERMAN_HINT.search(text):
        return text
    for _ in range(3):
        try:
            return TRANSLATOR.translate(text)
        except Exception:
            time.sleep(1.5)
    return text


def translate_line(line: str) -> str:
    if line.startswith("---") or line.startswith("id:") or line.startswith("domain:") or line.startswith("category:"):
        return line
    if line.startswith("  - http") or "://github.com" in line and line.strip().startswith("-"):
        return line
    if not GERMAN_HINT.search(line):
        return line
    protected, store = protect_segments(line)
    if not GERMAN_HINT.search(protected.replace("\x00", "")):
        return restore_segments(protected, store)
    translated = translate_chunk(protected)
    return restore_segments(translated, store)


def process_file(path: Path) -> None:
    text = path.read_text(encoding="utf-8")
    for old, new in sorted(PLAIN, key=lambda x: -len(x[0])):
        text = text.replace(old, new)
    lines = text.splitlines()
    out: list[str] = []
    in_frontmatter = False
    fm_done = False
    for line in lines:
        if line.strip() == "---":
            if not fm_done:
                in_frontmatter = not in_frontmatter
                if not in_frontmatter:
                    fm_done = True
            out.append(line)
            continue
        if in_frontmatter:
            if line.startswith("title:") and '"' in line:
                inner = re.search(r'title:\s*"(.*)"\s*$', line)
                if inner and GERMAN_HINT.search(inner.group(1)):
                    t = translate_chunk(inner.group(1))
                    line = f'title: "{t}"'
            elif line.strip().startswith("- ") and GERMAN_HINT.search(line):
                line = translate_line(line)
            elif re.match(r"\s+install:", line) and GERMAN_HINT.search(line):
                # keep URL in install; translate trailing notes only if no URL-only
                pass
            elif re.match(r"\s+version_notes:", line) and GERMAN_HINT.search(line):
                m = re.match(r"(\s+version_notes:\s*)(.*)$", line)
                if m:
                    line = m.group(1) + translate_chunk(m.group(2).strip('"'))
        else:
            if GERMAN_HINT.search(line):
                line = translate_line(line)
        out.append(line)
    path.write_text("\n".join(out) + ("\n" if text.endswith("\n") else ""), encoding="utf-8")


def mechanical_only(paths: list[Path]) -> None:
    for path in paths:
        text = path.read_text(encoding="utf-8")
        for old, new in sorted(PLAIN, key=lambda x: -len(x[0])):
            text = text.replace(old, new)
        path.write_text(text, encoding="utf-8")


def main() -> None:
    import sys

    files: list[Path] = []
    for root in TARGETS:
        files.extend(sorted(root.rglob("*.md")))
    if "--mechanical-only" in sys.argv:
        mechanical_only(files)
        print(f"Mechanical pass on {len(files)} files.")
        return
    for i, path in enumerate(files):
        process_file(path)
        print(f"{i + 1}/{len(files)} {path.relative_to(ROOT.parent)}", flush=True)
        time.sleep(0.15)
    print(f"Translated {len(files)} files.")


if __name__ == "__main__":
    main()