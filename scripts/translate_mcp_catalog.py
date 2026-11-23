#!/usr/bin/env python3
"""Translate mcp/catalog.json fields to English and English domain/category paths."""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CATALOG = ROOT / "mcp" / "catalog.json"

DOMAIN_MAP = {
    "automatisierung": "automation",
    "bildung": "education",
    "daten-analytics": "data-analytics",
    "finanzen": "finance",
    "gesundheit-fitness": "health-fitness",
    "immobilien": "real-estate",
    "it-betrieb-support": "it-operations-support",
    "ki-ops": "ai-ops",
    "kommunikation": "communication",
    "kundenservice": "customer-service",
    "medien": "media",
    "office-dokumente": "office-documents",
    "persoenlich-lifestyle": "personal-lifestyle",
    "projektmanagement": "project-management",
    "recherche-wissen": "research-knowledge",
    "recht-verwaltung": "legal-admin",
    "reisen-events": "travel-events",
    "software-entwicklung": "software-development",
    "vertrieb-crm": "sales-crm",
    "wissenschaft-engineering": "science-engineering",
}

CATEGORY_MAP = {
    "angebote-proposals": "offers-proposals",
    "audio-bearbeitung": "audio-editing",
    "behoerden-formulare": "government-forms",
    "bewerbungen": "job-applications",
    "bild-fotografie": "photo-imaging",
    "bild-generierung": "image-generation",
    "buchhaltung": "accounting",
    "compliance-nis2-dsgvo": "compliance-nis2-gdpr",
    "content-strategie": "content-strategy",
    "daten-experimente": "data-experiments",
    "datenbanken-dev": "databases-dev",
    "datenschutz": "privacy-compliance",
    "dreid-druck": "3d-printing",
    "dreid-modellierung": "3d-modeling",
    "einkauf": "shopping",
    "elektronik-diagnose": "electronics-diagnostics",
    "ernaehrung": "nutrition",
    "essen-rezepte": "food-recipes",
    "event-planung": "event-planning",
    "exposes": "property-listings",
    "fluege-hotels": "flights-hotels",
    "forensik": "forensics",
    "gesundheitsdaten-organisation": "health-data-organization",
    "cloud-kosten": "cloud-costs",
    "haushalt": "household",
    "identitaet-sso": "identity-sso",
    "immobilien-suche": "property-search",
    "kurse-erstellen": "course-creation",
    "lernkarten": "flashcards",
    "lokale-modelle-ollama": "local-models-ollama",
    "mcp-server-bau": "mcp-server-build",
    "meetings-transkription": "meeting-transcription",
    "planung": "planning",
    "plattform-deploy": "platform-deploy",
    "preis-monitoring": "price-monitoring",
    "produkte-vergleich": "product-comparison",
    "rechnungen": "invoicing",
    "reiseplanung": "trip-planning",
    "spielbibliotheken": "game-libraries",
    "spreadsheets-analyse": "spreadsheets-analysis",
    "sprachen": "languages",
    "sql-abfragen": "sql-queries",
    "steuern": "taxes",
    "stellenausschreibungen": "job-postings",
    "studium-forschung": "study-research",
    "termine-persoenlich": "personal-appointments",
    "untertitel-uebersetzung": "subtitles-translation",
    "vertraege": "contracts",
    "verwaltung-weg": "hoa-management",
    "video-bearbeitung": "video-editing",
    "landingpages": "landing-pages",
    "kalender-scheduling": "calendar-scheduling",
    "telefon-voice-agents": "phone-voice-agents",
    "datenbanken-dev": "databases-dev",
    "web-recherche": "web-research",
    "wikis-dokumentation": "wikis-documentation",
    "bibliothek-zotero": "library-zotero",
    "akademisch": "academic",
    "patente": "patents",
}

TYPE_MAP = {
    "Companion-App": "Companion app",
    "Bruecke": "Bridge",
    "Plattform-Feature": "Platform feature",
    "Skill": "Skill",
    "MCP": "MCP",
}

RISK_MAP = {
    "Nur aktivieren wenn Kategorie es braucht; Tokens nicht in argv.": (
        "Enable only when the category needs it; do not pass tokens in argv."
    ),
}


def remap_category_path(path: str) -> str:
    if "/" not in path:
        return path
    domain, category = path.split("/", 1)
    domain = DOMAIN_MAP.get(domain, domain)
    category = CATEGORY_MAP.get(category, category)
    return f"{domain}/{category}"


def main() -> None:
    data = json.loads(CATALOG.read_text(encoding="utf-8"))
    latest = data.get("generated_at", "2026-11-23")
    if re.fullmatch(r"\d{4}-\d{2}-\d{2}", str(latest)):
        data["generated_at"] = f"{latest}T00:00:00Z"
    for server in data.get("servers", []):
        server["categories"] = [remap_category_path(c) for c in server.get("categories", [])]
        if server.get("type") in TYPE_MAP:
            server["type"] = TYPE_MAP[server["type"]]
        rn = server.get("risk_notes", "")
        for old, new in RISK_MAP.items():
            if old in rn:
                server["risk_notes"] = new
        if re.search(r"[äöüß]|\b(nur|wenn|Kategorie)\b", rn, re.I):
            server["risk_notes"] = RISK_MAP.get(
                "Nur aktivieren wenn Kategorie es braucht; Tokens nicht in argv.",
                "Enable only when needed; keep secrets out of argv.",
            )
    CATALOG.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"Updated {CATALOG}")


if __name__ == "__main__":
    main()