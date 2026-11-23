---
id: bibliothek-zotero-workflow
domain: recherche-wissen
title: "Literaturverwaltung mit Zotero"
category: bibliothek-zotero
tags:
  - zotero
  - citations
  - bibtex
target_agents:
  - hermes
  - cursor
  - generic
required_tools:
  - name: Zotero CLI / Better BibTeX export
    install: "https://www.zotero.org/; BBT plugin optional"
    version_notes: "Nutzer-Desktop"
  - name: Brave Search MCP
    install: "https://github.com/brave/brave-search-mcp-server"
    version_notes: "Metadaten finden"
inputs:
  - "DOI/URL/Titel"
  - "Zotero-Collection"
outputs:
  - "Neue Einträge oder .bib"
  - "Import-Anleitung"
risk_level: low
version: "1.1.0"
updated: "2026-11-23"
example_count: 2
---

## Zweck

**Quellen in Zotero** erfassen—Metadaten recherchieren, BibTeX exportieren, Agent schreibt nicht direkt in Nutzer-DB ohne Tool.

## Wann nutzen

- Team nutzt Zotero als Single Source für Zitate.
- Agent liefert .bib + Import-Schritte oder Web-Translator-Hinweise.
- DOI-Listen aus Papers abarbeiten.

**Wann nicht**

- Vollautomatik ohne Zotero API/Connector beim Nutzer.
- Paywall-PDFs massenladen.
- Bibtex ohne Nutzer-Review bei Thesis.

## Tool-Stack

| Tool | Rolle | Begründung |
|------|-------|------------|
| Zotero | Bibliothek | Canonical |
| Better BibTeX | Export | Citation keys |
| Search MCP | Find metadata | DOI discovery |
| Crossref | Optional API | DOI lookup |

## System-Prompt / Instruktionen

```text
You help manage Zotero libraries—default deliver structured metadata and .bib files for user import unless Zotero MCP/API connected.

Inputs: list of dois urls or titles, target collection name, citation key pattern, output references.bib and import_steps.md.

For each item:
- Resolve DOI via crossref or search MCP; fields: title, authors, year, journal, doi, url.
- Generate citation key unique: AuthorYearTitleWord.
- Bibtex type article|inproceedings|misc per metadata.

If PDF attachment requested: only link open-access url; do not scrape paywalls.

Import steps for user:
1) Zotero File → Import references.bib
2) Verify collection
3) BBT refresh keys if used

Duplicate check: compare doi in existing bib user provides.

Approvals: modify live zotero sync library requires connected tool + user yes.

No fabricated dois.

Output: references.bib, import_steps.md, missing_metadata.csv.

When user has zotero-connector MCP, use only with their oauth—not desktop password.

Tag items with project tag user provides.

Note language field for DE sources.
Keep abstract optional not required for import.
```

## Arbeitsablauf

1. Eingabeliste normalisieren (DOI bevorzugt).
2. Metadaten pro Eintrag holen.
3. BibTeX schreiben.
4. Duplikate gegen Nutzer-.bib.
5. import_steps.md.
6. missing_metadata für FAILs.
7. Nutzer importiert lokal.

## Qualitätskriterien / Definition of Done

- [ ] Jeder Eintrag DOI oder MISSING note
- [ ] Keys eindeutig
- [ ] Import-Schritte klar
- [ ] Keine Paywall-PDFs gezogen
- [ ] Keine fake DOI

## Sicherheit & Freigaben

- Zotero Sync Token nicht im Chat.
- PDFs nur OA.
- Thesis-Daten lokal.

## Fallstricke

- Falsche BibTeX-Typen.
- Umlaute in keys.
- BBT ohne Refresh.
- Crossref Lag bei neuen DOIs.
- Duplicate keys on import.

## Grundbeispiele

### Beispiel 1 (Beispieldaten)

- **Aufgabe:** 5 DOIs nach BibTeX.
- **Input:** DOI-Liste Projekt X.
- **Prompt:**

```text
Resolve metadata; references.bib; import_steps for Zotero.
```

- **Erwartetes Ergebnis:**

```text
references.bib 5 entries; import_steps.md; missing empty.
```

### Beispiel 2 (Beispieldaten)

- **Aufgabe:** Titel ohne DOI.
- **Input:** Paper title only.
- **Prompt:**

```text
Search metadata; if no DOI mark in missing_metadata.csv.
```

- **Erwartetes Ergebnis:**

```text
Row in missing_metadata or resolved doi after search.
```