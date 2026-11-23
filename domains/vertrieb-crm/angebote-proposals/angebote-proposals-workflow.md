---
id: angebote-proposals-workflow
title: "Angebote & Sales Proposals"
domain: vertrieb-crm
category: angebote-proposals
tags:
  - proposal
  - quoting
  - b2b
target_agents:
  - hermes
  - grokbot
  - generic-mcp-agents
  - generic
required_tools:
  - name: attio MCP (Hermes-Katalog)
    install: "https://github.com/NousResearch/hermes-agent/tree/main/optional-mcps/attio"
    version_notes: "Nous-approved optional-mcps-Katalogeintrag (Listing 23.11.2026)."
  - name: close MCP (Hermes-Katalog)
    install: "https://github.com/NousResearch/hermes-agent/tree/main/optional-mcps/close"
    version_notes: "Nous-approved optional-mcps-Katalogeintrag (Listing 23.11.2026)."
inputs:
  - "Deal-Kontext aus CRM, Discovery-Notizen"
  - "Preisliste, SKU/Modul-Matrix, Rabattregeln"
  - "Template (DOCX/PDF) oder Markdown-Skeleton"
outputs:
  - "Proposal-Entwurf (DE/EN) mit Scope, SLA, Preis"
  - "Annex: Annahmen und Ausschlüsse"
  - "CRM-Deal-Feld-Vorschlag (Draft)"
risk_level: medium
example_count: 2
version: "1.1.0"
updated: "2026-11-23"
---

## Zweck

**Verkaufsangebote** aus CRM-Fakten: Scope, Milestones, Preise und Rechtsdisclaimer—PDF/DOCX-Erzeugung nur nach Freigabe, keine signierten Verträge ohne Jurist.

## Wann nutzen

- Nach Discovery Call: formales Angebot innerhalb 48h.
- Renewal mit Preisanpassung und neuen Modulen.
- Rahmenvertrag-Anhang für Enterprise.

**Wann nicht**

- Verbindliche Rechtsberatung oder Steuerquote.
- Rabatt außerhalb genehmigter Matrix ohne Sales-Lead-OK.

## Tool-Stack

| Tool | Rolle | Begründung |
|------|-------|------------|
| attio / close MCP | Deal-Wahrheit | Read + draft fields |
| office word-docx Skill | Export | Optional |
| Nutzer-Preisliste | Kalkulation | Source of truth |

## System-Prompt / Instruktionen

```text
Role: B2B proposal writer (vertrieb-crm/angebote-proposals).
Mission: Draft commercial proposals grounded in CRM notes and approved price list—no unauthorized discounts.
Inputs: deal id, customer legal name, currency, term months, modules requested, competitor mentioned optional.
Sections DE default: Executive Summary, Ausgangslage, Lösung/Scope, Deliverables, Timeline, Investition, Annahmen, Ausschlüsse, Nächste Schritte, Gültigkeit (date).
Pricing: line items qty × unit from price list version user states; show subtotal, VAT note "exkl./inkl. USt. nach Kundentyp", total.
Discount: only if user supplies approved % or code; show list vs net.
CRM: read activities for facts—cite internally [CRM activity date], strip in customer-facing doc unless user wants.
Risks: no SLA uptime numbers not in master SLA doc user attaches.
Legal footer: "Unverbindlich bis Gegenzeichnung" unless user says binding framework exists.
English variant: mirror structure if recipient EN.
Redlines: if user pastes previous proposal, show diff summary not auto-send.
Outputs: proposal_draft.md, pricing_table.csv, crm_field_suggestions.md.
No e-signature API, no DocuSign send.
Close/Attio: suggest amount and close_date update as draft values.
Multi-year: annual uplift only if price list says so.
Payment terms: Net 30 default unless CRM says otherwise.
Implementation: person-days only from rate card.
Do not invent case studies—use only user-provided references.
Version: proposal v1.0 in filename with date.
```

## Arbeitsablauf

1. Deal lesen, fehlende Pflichtfelder nachfragen.
2. Preislisten-Version und Rabattregeln fixieren.
3. Scope aus Discovery in Deliverables übersetzen.
4. Timeline und Meilensteine skizzieren.
5. Preistabelle und Total bilden.
6. Annahmen/Ausschlüsse und Gültigkeit setzen.
7. CRM-Update-Vorschlag und Draft-Dokument ausgeben.

## Qualitätskriterien / Definition of Done

- [ ] Preise traceable zur Preisliste-Version
- [ ] Keine erfundenen Referenzkunden
- [ ] Gültigkeitsdatum gesetzt
- [ ] Kein Versand/Signatur ohne Freigabe

## Sicherheit & Freigaben

- `risk_level: medium`—falsche Preise binden rechtlich.
- Vertrauliche CRM-Notizen nicht im Kunden-PDF.

## Fallstricke

- Rabatt ohne Genehmigung.
- SLA aus Marketing-Website kopiert.
- Währung gemischt EUR/USD.
- Scope Creep ohne Change-Order-Hinweis.
- CRM-Betrag vor PDF-Abnahme gesetzt.

## Grundbeispiele

### Beispiel 1 (Beispieldaten)

- **Aufgabe:** Angebot 12 Monate SaaS Pro
- **Input:** attio deal, Preisliste v2026-09
- **Prompt:**

```text
DE proposal, 50 seats Pro, net excl VAT, valid 30 days.
```

- **Erwartetes Ergebnis:**

```text
proposal_draft.md with line 50× seat price | total matches list math
```

### Beispiel 2 (Beispieldaten)

- **Aufgabe:** Renewal +10% uplift
- **Input:** prior contract value, uplift rule in price list
- **Prompt:**

```text
Show year1 vs year2 table, assumptions section.
```

- **Erwartetes Ergebnis:**

```text
Uplift applied only to platform fee row | assumption: same seat count
```