---
id: patente-workflow
domain: recherche-wissen
title: "Patentrecherche Überblick"
category: patente
tags:
  - patents
  - search
  - fto
target_agents:
  - hermes
  - generic
required_tools:
  - name: Brave Search MCP
    install: "https://github.com/brave/brave-search-mcp-server"
    version_notes: "Patent databases"
  - name: Firecrawl MCP
    install: "https://github.com/firecrawl/firecrawl-mcp-server"
    version_notes: "Espacenet etc."
inputs:
  - "Technologiebeschreibung"
  - "Jurisdiktionen"
outputs:
  - "Patent-Landschaftsbericht"
  - "Offene FTO-Fragen"
risk_level: medium
version: "1.1.0"
updated: "2026-11-23"
example_count: 2
---

## Zweck

**Patentlandschaft skizzieren**—öffentliche Register durchsuchen, Anspruchsüberblick in Entwurfsqualität, **keine Rechtsberatung** oder FTO-Freigabe.

## Wann nutzen

- Frühe Produktidee, vor Anwalt.
- Konkurrenz-Patent-IDs sammeln.
- IPC/CPC Keywords explorieren.

**Wann nicht**

- Freedom-to-operate Gutachten.
- Anmeldung schreiben/einreichen.
- Geheime Erfindung im öffentlichen Chat.

## Tool-Stack

| Tool | Rolle | Begründung |
|------|-------|------------|
| Brave/Exa | Find patents | Discovery |
| Firecrawl | Register pages | Metadata |
| Espacenet/Google Patents | Links | Public |

## System-Prompt / Instruktionen

```text
You draft patent landscape scans from public databases—not legal opinions or FTO clearance.

Inputs: technology description, jurisdictions (EP|US|DE...), assignees optional, output landscape.md.

Search:
- Form queries with keywords + CPC if user supplies.
- Collect publication numbers, titles, assignees, dates, links.
- Do not quote full claims—summarize claim theme in plain language with UNREVIEWED label.

For each patent: id | assignee | year | summary one line | url | status unknown unless page states.

FTO section: list questions for patent counsel only—no yes/no clearance.

Approvals: sharing landscape with external investors requires user yes.

Confidential: do not paste unpublished invention details into search queries if user marks secret—use generic keywords.

No download granted patents bulk beyond fair review.

Output: landscape.md, counsel_questions.md.

Disclaim legal advice in header.

Mark family members if visible.

Note if only abstract reviewed not full claims.
Prioritize active status field when shown on register page.
Distinguish application vs granted when metadata provides.
```

## Arbeitsablauf

1. Tech in Suchbegriffe (nicht secret details).
2. Register-Suchen pro Jurisdiction.
3. Top 20 Treffer kurzieren.
4. Firecrawl Metadaten.
5. landscape.md.
6. counsel_questions.md.
7. Anwalt-Hinweis prominent.

## Qualitätskriterien / Definition of Done

- [ ] Disclaimer legal advice
- [ ] URLs zu Register
- [ ] Keine FTO yes/no
- [ ] Secret mode beachtet
- [ ] Claims nur summary UNREVIEWED

## Sicherheit & Freigaben

- Erfindung geheim halten in Queries.
- Externe Weitergabe freigeben.
- Keine Anmeldedaten.

## Fallstricke

- Abstract ≠ Claims.
- Falsche Patentfamilie.
- Abgelaufenes Patent ignoriert.
- US vs EP Nummern.
- Machine translation Missverständnis.

## Grundbeispiele

### Beispiel 1 (Beispieldaten)

- **Aufgabe:** EP Landschaft Batteriethema.
- **Input:** Keyword solid-state, jurisdiction EP.
- **Prompt:**

```text
landscape.md top 15; counsel_questions.md; no FTO opinion.
```

- **Erwartetes Ergebnis:**

```text
landscape with publication numbers; disclaimer; questions for counsel.
```

### Beispiel 2 (Beispieldaten)

- **Aufgabe:** Secret mode.
- **Input:** confidential invention description.
- **Prompt:**

```text
Use generic keywords only; do not paste invention claims in queries.
```

- **Erwartetes Ergebnis:**

```text
Queries generic; note secret mode in header.
```