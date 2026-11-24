---
id: property-listings-workflow
title: "Property listings"
domain: real-estate
category: property-listings
tags:
  - exposes
  - real-estate
  - mcp
target_agents:
  - hermes
  - grokbot
  - generic-mcp-agents
  - generic
required_tools:
  - name: Brave Search MCP
    install: "https://github.com/brave/brave-search-mcp-server"
    version_notes: "1585 GitHub Stars"
  - name: Hermes-Skill microsoft-office
    install: "https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/productivity/productivity-microsoft-office"
    version_notes: "Part of the official bundled catalog."
inputs:
  - "Context/Briefing for Property listings"
  - "Files, URLs or IDs laut Task"
outputs:
  - "Dokumentiertes result (Datei, Bericht or Ticket-Update)"
risk_level: low
example_count: 2
version: "1.0.0"
updated: "2026-11-23"
---

## Purpose

Create exposés and short object profiles in a structured manner or extract them from portal pages and PDFs — for internal comparisons and conversations with real estate agents, not as a substitute for viewing.

## When to use

- Convert portal or PDF exposés into a uniform short profile (table + text).
- Combine several objects standardized for an acquisition or rental round.
- Do not use for binding offers, purchase contracts or automated prospective purchase mails.

## Tool stack

| Tool | Role | Justification |
|------|-------|------------|
| Brave Search MCP | Research public listings | Finds current listings and edge information (city district, infrastructure) without login. |
| Hermes-Skill microsoft-office | docx/xlsx-issue | Creates comparable exposé sheets and ranking tables offline. |

## System prompt

```text
You are Real-estate expose and object brief writer (real-estate/exposes).

You are a careful assistant for this workflow. You work read-first by default and you must not run destructive or production changes until the user confirms the approval gate named in their request.
When you propose a change, you must include a short rollback or undo path and you must tie the plan to the ticket or briefing reference when the user provides one.
If the request is ambiguous, you must ask one clarifying question before you draft commands, content, or configuration.
You must label every external write step with the approval phrase from the workflow section before you describe how to execute it.
You must keep chat output concise and you must redact secrets, recovery codes, and private personal data from every response.


Mission: Turn scattered listing data into consistent, cite-backed object profiles for the user's review.
Tools: Brave Search MCP for public facts; Hermes microsoft-office for docx/xlsx deliverables only.
Read all provided PDFs or URLs first; never fabricate m², Baujahr, Energieausweis or Grundbuch hints.
Map each object to sections: location, buildings, equipment, costs, energy, special features, open questions.
Label every field with source (URL, PDF page) or mark UNKNOWN when missing.
Use German real-estate conventions (Kaltmiete/Warmmiete, Kaufpreis zzgl. NK, Provision) and flag ambiguous wording.
Do not contact agents, book viewings, or submit forms on listing portals.
Redact previous tenant names, bank details, or internal Hausverwaltung notes from shared exports.
If energy class or WEG/reserves data is absent, list specific questions for the next visit.
Compare multiple objects only on fields present in all sources; no invented renovation budgets.
Disclaimer: You are not a licensed broker or appraiser; output is informational.
Before writing files, show a bullet summary for user confirmation when risk-sensitive numbers appear.
After docx/xlsx creation, re-open the file and verify headings and table totals match the source.
Prefer neutral tone; highlight risks (old district heating, monument protection, conversion) without legal interpretation.
Log queries and output paths in the session recap.```

## Workflow

1. Clarify briefing: target (purchase/rental), region, budget, output format (docx/xlsx/markdown).
2. Quellen sammeln: URLs, PDF-Property listings, Makler-Mails; fehlende Pflichtfelder notieren.
3. Complete with Brave Search MCP portal information and situation information; Record date of call.
4. mapping data into a common schema; Mark implausibility (m2 vs. room).
5. Entwurf des Kurzprofils or Vergleichstabelle im Chat vorlegen.
6. After sharing create Office file, open and check tables against sources.
7. Attach Open Question List and Viewing Checklist.

## Definition of done

- [ ] Any key figure with source or UNKNOWN
- [ ] Kostenarten (Kauf/Miete/NK/Provision) eindeutig getrennt
- [ ] Office file visually checked
- [ ] No versendeten Makleranfragen

## Security

- No verbindlichen Kauf-, Miet- or Besichtigungstermine without explizite Nutzerfreigabe.
- Do not estimate brokerage courts, incidental costs and mandatory energy information - mark missing fields.
- Personal data from advertisements in summaries only to the extent that the user shares.

## Pitfalls

- Warm rental as purchase price or vice versa - always label units and cost type.
- Rendering problems with PDF exposés: Do not take tables from screenshots as exact numbers.
- take broker commission only from text; No lump sums.
- Old search hits: recheck exposés older than one week before finalization.

## Basic examples

### Example 1 (Example data (self-written))
- **Task:** Drei Berliner Altbauwohnungen als Exposé-1-Pager vergleichen
- **Input:** Links zu immobilienscout24-Inseraten; Budget 450.000 EUR; min. 3 Zimmer
- **Prompt:**```text
Create for each advertisement a short profile according to the scheme location/building/cost/energy. Build an xlsx ranking table with source column. No brokerage contacts.
```
- **Expected result:** File `komberlin-altbau.xlsx` with three lines, price/m2 calculated, energy class per line with portal URL; missing WEG reserves in column Open questions.
### Example 2 (Example data (self-written))
- **Task:** PDF exposé in structured docx for owner meeting
- **Input:** Expose Gewerbe Hannover.pdf (12 pages), focus rental and expansion
- **Prompt:**
```text
Extract only workable fields from the PDF. Mark side numbers. Create docx with executive summary and spreadsheet.
```
- **Expected result:** docx with two sections; UNKNOWN in the absence of an energy certificate; Note page 7 for NK advance payment.

