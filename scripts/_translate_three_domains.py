#!/usr/bin/env python3
"""Restore from main, apply English headings/slugs, translate body lines with argos."""
from __future__ import annotations

import gc
import re
import subprocess
import sys
from pathlib import Path

import argostranslate.translate

ROOT = Path(__file__).resolve().parent.parent / "domains"
REPO = Path(__file__).resolve().parent.parent
DIRS = ["communication", "content-marketing", "customer-service"]


def git_main(path: str) -> str | None:
    r = subprocess.run(
        ["git", "-C", str(REPO), "show", f"main:domains/{path}"],
        capture_output=True,
        text=True,
    )
    return r.stdout if r.returncode == 0 else None


def rel_to_main(rel: str) -> str:
    p = rel
    for a, b in [
        ("communication/", "kommunikation/"),
        ("customer-service/", "kundenservice/"),
        ("calendar-scheduling", "kalender-scheduling"),
        ("phone-voice-agents", "telefon-voice-agents"),
        ("meeting-transcription", "meetings-transkription"),
        ("content-strategy", "content-strategie"),
        ("landing-pages", "landingpages"),
        ("social-media-strategy", "social-media-strategie"),
    ]:
        p = p.replace(a, b)
    return p


def apply_migrate(text: str) -> str:
    pairs = [
        ("## Zweck", "## Purpose"),
        ("## Wann nutzen", "## When to use"),
        ("## Tool-Stack", "## Tool stack"),
        ("## System-Prompt / Instruktionen", "## System prompt"),
        ("## Arbeitsablauf", "## Workflow"),
        ("## Qualitätskriterien / Definition of Done", "## Definition of done"),
        ("## Sicherheit & Freigaben", "## Security"),
        ("## Fallstricke", "## Pitfalls"),
        ("## Grundbeispiele", "## Basic examples"),
        ("**Domain-Slug:**", "**Domain slug:**"),
        ("**Kategorien:**", "**Categories:**"),
        ("**Stand:**", "**As of:**"),
        ("## Übersicht", "## Overview"),
        ("## Kategorien", "## Categories"),
        ("| Kategorie |", "| Category |"),
        ("- **Kategorie:**", "- **Category:**"),
        ("- **Aufgabe:**", "- **Task:**"),
        ("- **Erwartetes Ergebnis:**", "- **Expected result:**"),
        ("## Kurzbeschreibung", "## Summary"),
        ("## Empfohlener Tool-Stack", "## Recommended tool stack"),
        ("## MCP-Server und Skills", "## MCP servers and skills"),
        ("## Typische Workflows", "## Typical workflows"),
        ("## Quellen", "## Sources"),
        ("| Rolle |", "| Role |"),
        ("| Begründung |", "| Rationale |"),
        ("| Typ |", "| Type |"),
        ("| Einsatz |", "| Use |"),
        ("| Installation |", "| Install |"),
        ("| Popularitaet |", "| Popularity |"),
        ("| Quelle |", "| Source |"),
        ("| Unverified? |", "| Unverified |"),
        ("nein (so belegt)", "no (as cited)"),
        ("**Wann nicht**", "**When not to use**"),
        ("**Wann nicht:**", "**When not to use:**"),
        ("Kontext/Briefing für", "Context/briefing for"),
        ("Dateien, URLs oder IDs laut Aufgabe", "Files, URLs, or IDs per task"),
        (
            "Dokumentiertes Ergebnis (Datei, Bericht oder Ticket-Update)",
            "Documented result (file, report, or ticket update)",
        ),
    ]
    for a, b in pairs:
        text = text.replace(a, b)
    text = re.sub(r"### Beispiel (\d+) \(Beispieldaten\)", r"### Example \1 (Example data)", text)
    text = re.sub(r"### Beispiel (\d+) \(Praxisbeispiel\)", r"### Example \1 (Real-world example)", text)
    text = re.sub(r"### Beispiel (\d+)", r"### Example \1", text)
    repls = [
        ("domain: kommunikation", "domain: communication"),
        ("domain: kundenservice", "domain: customer-service"),
        ("  - kommunikation", "  - communication"),
        ("  - kundenservice", "  - customer-service"),
        ("`kommunikation`", "`communication`"),
        ("`kundenservice`", "`customer-service`"),
        ("category: kalender-scheduling", "category: calendar-scheduling"),
        ("category: telefon-voice-agents", "category: phone-voice-agents"),
        ("meetings-transkription", "meeting-transcription"),
        ("kalender-scheduling", "calendar-scheduling"),
        ("telefon-voice-agents", "phone-voice-agents"),
        ("kommunikation/", "communication/"),
        ("kundenservice/", "customer-service/"),
        ("content-strategie", "content-strategy"),
        ("social-media-strategie", "social-media-strategy"),
        ("landingpages", "landing-pages"),
        ("id: kalender-scheduling-workflow", "id: calendar-scheduling-workflow"),
        ("id: kalender-scheduling-mcp-focus", "id: calendar-scheduling-mcp-focus"),
        ("id: meetings-transkription-workflow", "id: meeting-transcription-workflow"),
        ("id: meetings-transkription-mcp-focus", "id: meeting-transcription-mcp-focus"),
        ("id: telefon-voice-agents-workflow", "id: phone-voice-agents-workflow"),
        ("id: content-strategie-workflow", "id: content-strategy-workflow"),
        ("id: landingpages-workflow", "id: landing-pages-workflow"),
        ('title: "Kalender und Scheduling: MCP/Skill-Fokus"', 'title: "Calendar and scheduling: MCP/skill focus"'),
        ('title: "Kalender und Scheduling"', 'title: "Calendar and scheduling"'),
        (
            'title: "Meetings und Transkription: MCP/Skill-Fokus"',
            'title: "Meetings and transcription: MCP/skill focus"',
        ),
        ('title: "Meetings und Transkription"', 'title: "Meetings and transcription"'),
        ('title: "Telefon und Voice-Agents"', 'title: "Phone and voice agents"'),
        (
            'title: "Chat und Messaging: MCP/Skill-Fokus"',
            'title: "Chat and messaging: MCP/skill focus"',
        ),
        ('title: "Chat und Messaging"', 'title: "Chat and messaging"'),
        ('title: "E-Mail: MCP/Skill-Fokus"', 'title: "Email: MCP/skill focus"'),
        ('title: "Helpdesk und Tickets"', 'title: "Helpdesk and tickets"'),
        ('title: "Qualität und CSAT"', 'title: "Quality and CSAT"'),
        ('title: "Wissensdatenbank Support"', 'title: "Knowledge base support"'),
        ('title: "Live-Chat und Bots"', 'title: "Live chat and bots"'),
        ('title: "Buffer Kampagnenplanung"', 'title: "Buffer campaign planning"'),
        ('title: "Posteingang triagieren (Gmail MCP)"', 'title: "Inbox triage (Gmail MCP)"'),
        ('title: "iMessage und SMS"', 'title: "iMessage and SMS"'),
        ("ClawHub-Zahlen: Leaderboard 23.11.2026.", "ClawHub figures: leaderboard 2026-11-23."),
        ("Bundled-Katalog.", "Bundled catalog."),
        (
            "Nous-approved optional-mcps-Katalogeintrag (Listing 23.11.2026).",
            "Nous-approved optional-mcps catalog entry (listing 2026-11-23).",
        ),
    ]
    for a, b in repls:
        text = text.replace(a, b)
    return text


GERMAN_LINE = re.compile(
    r"[äöüßÄÖÜ]|"
    r"\b(und|für|nicht|oder|mit|bei|nach|von|wird|sind|Templates|Kategorie|Entwurf|Nutzer|"
    r"Dokumentation|Anforderung|Zeit|Teilnehmer|Einladung|Nutzer|Schrift|Posteingang)\b",
    re.I,
)


def split_frontmatter(text: str) -> tuple[str, str]:
    if not text.startswith("---"):
        return "", text
    m = re.match(r"^---\n.*?\n---\n", text, re.S)
    if not m:
        return "", text
    return m.group(), text[m.end() :]


def tr_line(line: str) -> str:
    if not GERMAN_LINE.search(line):
        return line
    return argostranslate.translate.translate(line, "de", "en")


def translate_frontmatter(fm: str) -> str:
    out = []
    for line in fm.splitlines(keepends=True):
        if line.startswith("title:") or (
            line.strip().startswith("- ") and GERMAN_LINE.search(line)
        ):
            out.append(tr_line(line))
        else:
            out.append(line)
    return "".join(out)


def translate_body(body: str) -> str:
    lines: list[str] = []
    in_code = False
    for line in body.splitlines(keepends=True):
        if line.strip().startswith("```"):
            in_code = not in_code
            lines.append(line)
            continue
        if in_code:
            lines.append(line)
        else:
            lines.append(tr_line(line))
    return "".join(lines)


def translate_file(text: str) -> str:
    fm, body = split_frontmatter(text)
    if fm:
        fm = translate_frontmatter(fm)
        body = translate_body(body)
        return fm + body
    return translate_body(text)


def main() -> None:
    only = sys.argv[1:] if len(sys.argv) > 1 else None
    count = 0
    for d in DIRS:
        for path in sorted((ROOT / d).rglob("*.md")):
            rel = str(path.relative_to(ROOT))
            if only and rel not in only and path.name not in only:
                continue
            raw = git_main(rel_to_main(rel))
            if not raw:
                print("skip", rel, file=sys.stderr)
                continue
            path.write_text(translate_file(apply_migrate(raw)), encoding="utf-8")
            count += 1
            print(rel, flush=True)
            gc.collect()
    print("translated", count)


if __name__ == "__main__":
    main()