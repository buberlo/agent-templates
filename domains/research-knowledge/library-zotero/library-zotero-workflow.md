---
id: library-zotero-workflow
title: "Literature Management with Zotero"
domain: research-knowledge
category: library-zotero
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
    version_notes: "User-Desktop"
  - name: Brave Search MCP
    install: "https://github.com/brave/brave-search-mcp-server"
    version_notes: "Metadaten finden"
inputs:
  - "DOI/URL/Titel"
  - "Zotero-Collection"
outputs:
  - "New entries or .bib"
  - "Import-Anleitung"
risk_level: low
example_count: 2
version: "1.1.0"
updated: "2026-11-23"
---

## Purpose

**Capture sources in Zotero**—Research metadata, export BibTeX, Agent does not write directly into user DB without a tool.

## When to use

Team uses Zotero as a single source for quotes.
- Agent liefert .bib + Import-Schritte or Web-Translator-Hinweise.
- DOI-Listen aus Papers abarbeiten.

**When not**

- Vollautomatik without Zotero API/Connector beim User.
- Paywall-PDFs massenladen.
- Bibtex without User-Review bei Thesis.

## Tool stack

| Tool | Role | Justification |
|------|-------|------------|
| Zotero | Bibliothek | Canonical |
| Better BibTeX | Export | Citation keys |
| Search MCP | Find metadata | DOI discovery |
| Crossref | Optional API | DOI lookup |

## System prompt

```text
You help manage Zotero libraries—default deliver structured metadata and .bib files for user import unless Zotero MCP/API connected.

You are a careful assistant for this workflow. You work read-first by default and you must not run destructive or production changes until the user confirms the approval gate named in their request.
When you propose a change, you must include a short rollback or undo path and you must tie the plan to the ticket or briefing reference when the user provides one.
If the request is ambiguous, you must ask one clarifying question before you draft commands, content, or configuration.
You must label every external write step with the approval phrase from the workflow section before you describe how to execute it.
You must keep chat output concise and you must redact secrets, recovery codes, and private personal data from every response.


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
Keep abstract optional not required for import.```

## Workflow

1. Eingabeliste normalisieren (DOI bevorzugt).
2. Metadaten pro Eintrag holen.
3. BibTeX schreiben.
4. Duplikate gegen User-.bib.
5. import_steps.md.
Missing metadata for FAILs.
7. User importiert lokal.

## Definition of done

- [ ] Jeder Eintrag DOI or MISSING note
- [ ] Keys eindeutig
- [ ] Import-Schritte klar
- [ ] No Paywall-PDFs gezogen
- [ ] No fake DOI

## Security

- Zotero Sync Token not in chat.
- PDFs nur OA.
- Thesis-Daten lokal.

## Pitfalls

- Falsche BibTeX-Typen.
- Umlaute in keys.
- BBT without Refresh.
- Crossref Lag bei neuen DOIs.
- Duplicate keys on import.

## Basic examples

### Example 1 (Example data (self-written))
- **Task:** 5 DOIs nach BibTeX.
- **Input:** DOI-Liste Projekt X.
- **Prompt:**

```text
Resolve metadata; references.bib; import_steps for Zotero.
```

- **Expected result:**

```text
Summary: the agent stays read-only until approval, lists concrete next steps, and marks any missing inputs the user must supply.Summary: the agent stays read-only until approval, lists concrete next steps, and marks any missing inputs the user must supply.references.bib 5 entries; import_steps.md; missing empty.
```

### Example 2 (Example data (self-written))
- **Task:** Titel without DOI.
- **Input:** Paper title only.
- **Prompt:**

```text
Search metadata; if no DOI mark in missing_metadata.csv.
```

- **Expected result:**

```text
Summary: the agent stays read-only until approval, lists concrete next steps, and marks any missing inputs the user must supply.Summary: the agent stays read-only until approval, lists concrete next steps, and marks any missing inputs the user must supply.Row in missing_metadata or resolved doi after search.
```