#!/usr/bin/env python3
"""Mechanical English normalization: headings, tags, filenames, ids."""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DOMAINS = ROOT / "domains"

TAG_MAP = {
    "ki-ops": "ai-ops",
    "automatisierung": "automation",
    "finanzen": "finance",
    "medien": "media",
    "bildung": "education",
    "daten-analytics": "data-analytics",
    "gesundheit-fitness": "health-fitness",
    "immobilien": "real-estate",
    "kommunikation": "communication",
    "kundenservice": "customer-service",
    "office-dokumente": "office-documents",
    "projektmanagement": "project-management",
    "recherche-wissen": "research-knowledge",
    "recht-verwaltung": "legal-admin",
    "reisen-events": "travel-events",
    "software-entwicklung": "software-development",
    "vertrieb-crm": "sales-crm",
    "wissenschaft-engineering": "science-engineering",
    "it-betrieb-support": "it-operations-support",
    "persoenlich-lifestyle": "personal-lifestyle",
    "reiseplanung": "trip-planning",
    "reisen-events": "travel-events",
}

HEADING_MAP = [
    ("## System prompt / instructions", "## System prompt"),
    ("## Quality criteria / Definition of Done", "## Definition of done"),
    ("## Security & approvals", "## Security"),
    ("### Wann nicht nutzen", "### When not to use"),
    ("## Wann nicht nutzen", "## When not to use"),
]

CATEGORY_HEADING_MAP = [
    ("## Kurzbeschreibung", "## Summary"),
    ("## Empfohlener Tool-Stack", "## Recommended tool stack"),
    ("## MCP-Server und Skills", "## MCP servers and skills"),
    ("## Typische Workflows", "## Typical workflows"),
    ("## Quellen", "## Sources"),
    ("- **Kategorie:**", "- **Category:**"),
    ("| Einsatz |", "| Use |"),
    ("| Installation |", "| Install |"),
    ("| Popularitaet |", "| Popularity |"),
    ("| Quelle |", "| Source |"),
    ("| Unverified? |", "| Unverified |"),
    ("| Begründung |", "| Rationale |"),
    ("| Rolle |", "| Role |"),
]

FILE_RENAMES = {
    "lokale-modelle-ollama-workflow.md": "local-models-ollama-workflow.md",
    "mcp-server-bau-workflow.md": "mcp-server-build-workflow.md",
    "mcp-server-bau-mcp-focus.md": "mcp-server-build-mcp-focus.md",
    "kurse-erstellen-workflow.md": "course-creation-workflow.md",
    "kurse-erstellen-mcp-focus.md": "course-creation-mcp-focus.md",
    "lernkarten-workflow.md": "flashcards-workflow.md",
    "sprachen-workflow.md": "languages-workflow.md",
    "studium-forschung-workflow.md": "study-research-workflow.md",
    "reiseplanung-workflow.md": "trip-planning-workflow.md",
    "event-planung-workflow.md": "event-planning-workflow.md",
    "fluege-hotels-workflow.md": "flights-hotels-workflow.md",
    "immobilien-suche-workflow.md": "property-search-workflow.md",
    "verwaltung-weg-workflow.md": "hoa-management-workflow.md",
    "exposes-workflow.md": "property-listings-workflow.md",
    "planung-workflow.md": "planning-workflow.md",
    "rechnungen-workflow.md": "invoicing-workflow.md",
    "steuern-workflow.md": "taxes-workflow.md",
    "daten-experimente-workflow.md": "data-experiments-workflow.md",
    "einkauf-workflow.md": "shopping-workflow.md",
    "haushalt-workflow.md": "household-workflow.md",
    "essen-rezepte-workflow.md": "food-recipes-workflow.md",
    "netzwerk-workflow.md": "network-workflow.md",
    "identitaet-sso-workflow.md": "identity-sso-workflow.md",
    "plattform-deploy-workflow.md": "platform-deploy-workflow.md",
    "plattform-deploy-mcp-focus.md": "platform-deploy-mcp-focus.md",
    "cloud-kosten-workflow.md": "cloud-costs-workflow.md",
    "forensik-workflow.md": "forensics-workflow.md",
    "compliance-nis2-dsgvo-mcp-focus.md": "compliance-nis2-gdpr-mcp-focus.md",
    "behoerden-formulare-workflow.md": "government-forms-workflow.md",
    "datenschutz-workflow.md": "privacy-compliance-workflow.md",
    "vertraege-workflow.md": "contracts-workflow.md",
    "ernaehrung-workflow.md": "nutrition-workflow.md",
    "gesundheitsdaten-organisation-workflow.md": "health-data-organization-workflow.md",
    "meetings-transkription-workflow.md": "meeting-transcription-workflow.md",
    "meetings-transkription-mcp-focus.md": "meeting-transcription-mcp-focus.md",
    "telefon-voice-agents-workflow.md": "phone-voice-agents-workflow.md",
    "bild-generierung-mcp-focus.md": "image-generation-mcp-focus.md",
    "bild-comfyui-sdxl-workflow.md": "image-comfyui-sdxl-workflow.md",
    "dreid-modellierung-workflow.md": "3d-modeling-workflow.md",
    "dreid-druck-workflow.md": "3d-printing-workflow.md",
    "e-signatur-workflow.md": "e-signature-workflow.md",
    "diagramme-whiteboard-workflow.md": "diagrams-whiteboard-workflow.md",
    "formulare-workflow.md": "forms-workflow.md",
    "musik-workflow.md": "music-workflow.md",
    "nachhilfe-tutoring-workflow.md": "tutoring-workflow.md",
    "elektronik-diagnose-workflow.md": "electronics-diagnostics-workflow.md",
    "dokumente-libreoffice-mail-merge.md": "documents-libreoffice-mail-merge.md",
    "dokumente-pandoc-markdown-pdf.md": "documents-pandoc-markdown-pdf.md",
    "untertitel-uebersetzung-mcp-focus.md": "subtitles-translation-mcp-focus.md",
    "video-bearbeitung-mcp-focus.md": "video-editing-mcp-focus.md",
    "bild-imagemagick-batch-resize.md": "image-imagemagick-batch-resize.md",
    "finanzen-camt053-reconcile.md": "finance-camt053-reconcile.md",
    "finanzen-datev-export-csv.md": "finance-datev-export-csv.md",
    "daten-python-pandas-eda.md": "data-python-pandas-eda.md",
    "daten-duckdb-sql-report.md": "data-duckdb-sql-report.md",
    "produkte-vergleich-workflow.md": "product-comparison-workflow.md",
    "termine-persoenlich-workflow.md": "personal-appointments-workflow.md",
    "spielbibliotheken-workflow.md": "game-libraries-workflow.md",
    "content-strategie-workflow.md": "content-strategy-workflow.md",
    "landingpages-workflow.md": "landing-pages-workflow.md",
    "preis-monitoring-workflow.md": "price-monitoring-workflow.md",
    "angebote-proposals-workflow.md": "offers-proposals-workflow.md",
    "akademisch-workflow.md": "academic-workflow.md",
    "patente-workflow.md": "patents-workflow.md",
    "patente-mcp-focus.md": "patents-mcp-focus.md",
    "web-recherche-mcp-focus.md": "web-research-mcp-focus.md",
    "web-exa-perplexity-briefing.md": "web-exa-perplexity-briefing.md",
    "bibliothek-zotero-mcp-focus.md": "library-zotero-mcp-focus.md",
    "bibliothek-zotero-workflow.md": "library-zotero-workflow.md",
    "wikis-dokumentation-mcp-focus.md": "wikis-documentation-mcp-focus.md",
    "wikis-dokumentation-workflow.md": "wikis-documentation-workflow.md",
    "datenbanken-dev-mcp-focus.md": "databases-dev-mcp-focus.md",
    "datenbanken-dev-workflow.md": "databases-dev-workflow.md",
    "kalender-scheduling-workflow.md": "calendar-scheduling-workflow.md",
    "kalender-scheduling-mcp-focus.md": "calendar-scheduling-mcp-focus.md",
    "stellenausschreibungen-workflow.md": "job-postings-workflow.md",
    "bewerbungen-workflow.md": "job-applications-workflow.md",
}

CAT_DIR_RENAMES = {
    "netzwerk": "network",
    "bibliothek-zotero": "library-zotero",
    "wikis-dokumentation": "wikis-documentation",
    "akademisch": "academic",
    "patente": "patents",
    "web-recherche": "web-research",
    "kalender-scheduling": "calendar-scheduling",
    "telefon-voice-agents": "phone-voice-agents",
    "datenbanken-dev": "databases-dev",
    "social-media-strategie": "social-media-strategy",
    "nachhilfe-tutoring": "tutoring",
    "e-signatur": "e-signature",
    "diagramme-whiteboard": "diagrams-whiteboard",
    "formulare": "forms",
    "musik": "music",
    "video-produktion-pipeline": "video-production-pipeline",
    "elektronik-diagnose": "electronics-diagnostics",
}

ID_RENAMES = {k.replace(".md", ""): v.replace(".md", "") for k, v in FILE_RENAMES.items()}


def normalize_file(path: Path) -> None:
    text = path.read_text(encoding="utf-8")
    for old, new in HEADING_MAP:
        text = text.replace(old, new)
    if path.name in ("_category.md", "_domain.md"):
        for old, new in CATEGORY_HEADING_MAP:
            text = text.replace(old, new)
    for old_tag, new_tag in TAG_MAP.items():
        text = re.sub(rf"^(\s+-\s+){re.escape(old_tag)}\s*$", rf"\1{new_tag}", text, flags=re.M)
        text = re.sub(rf'^(\s+-\s+)"{re.escape(old_tag)}"\s*$', rf'\1"{new_tag}"', text, flags=re.M)
    if path.name not in ("_category.md", "_domain.md"):
        stem = path.stem
        if stem in ID_RENAMES:
            text = re.sub(rf"^id:\s*{re.escape(stem)}\s*$", f"id: {ID_RENAMES[stem]}", text, flags=re.M)
    path.write_text(text, encoding="utf-8")


def rename_files() -> None:
    for path in list(DOMAINS.rglob("*.md")):
        if path.name in FILE_RENAMES:
            dest = path.with_name(FILE_RENAMES[path.name])
            if dest.exists():
                continue
            path.rename(dest)


def rename_category_dirs() -> None:
    for dom_dir in DOMAINS.iterdir():
        if not dom_dir.is_dir():
            continue
        for cat_dir in list(dom_dir.iterdir()):
            if not cat_dir.is_dir():
                continue
            new_name = CAT_DIR_RENAMES.get(cat_dir.name)
            if not new_name:
                continue
            old_name = cat_dir.name
            dest = dom_dir / new_name
            if dest.exists():
                raise SystemExit(f"collision {dest}")
            for path in cat_dir.rglob("*.md"):
                text = path.read_text(encoding="utf-8")
                text = re.sub(
                    rf"^category:\s*{re.escape(old_name)}\s*$",
                    f"category: {new_name}",
                    text,
                    flags=re.M,
                )
                path.write_text(text, encoding="utf-8")
            cat_dir.rename(dest)


def main() -> None:
    for path in DOMAINS.rglob("*.md"):
        normalize_file(path)
    rename_files()
    rename_category_dirs()
    print("Normalized headings, tags, filenames, and category folders.")


if __name__ == "__main__":
    main()