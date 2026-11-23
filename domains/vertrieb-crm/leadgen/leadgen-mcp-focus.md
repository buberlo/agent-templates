---
id: leadgen-mcp-focus
title: "Leadgen: Recherche-MCP vs. CRM-Import"
domain: vertrieb-crm
category: leadgen
tags:
  - leadgen
  - exa
  - mcp
target_agents:
  - hermes
  - grokbot
  - generic-mcp-agents
  - generic
required_tools:
  - name: Exa MCP
    install: "https://github.com/exa-labs/exa-mcp-server"
    version_notes: "5264 GitHub Stars"
  - name: Brave Search MCP
    install: "https://github.com/brave/brave-search-mcp-server"
    version_notes: "1585 GitHub Stars"
  - name: attio MCP (Hermes-Katalog)
    install: "https://github.com/NousResearch/hermes-agent/tree/main/optional-mcps/attio"
    version_notes: "Nous-approved optional-mcps-Katalogeintrag (Listing 23.11.2026)."
  - name: close MCP (Hermes-Katalog)
    install: "https://github.com/NousResearch/hermes-agent/tree/main/optional-mcps/close"
    version_notes: "Nous-approved optional-mcps-Katalogeintrag (Listing 23.11.2026)."
inputs:
  - "Recherche-Tiefe vs. CRM-Import in einer Session"
  - "API-Budget und erlaubte MCPs"
outputs:
  - "Routing-Entscheid recherchieren → CSV → CRM"
  - "Nutzungsprotokoll pro MCP"
risk_level: low
example_count: 2
version: "1.1.0"
updated: "2026-11-23"
---

## Zweck

Leadgen-Sessions **entkoppeln**: erst Exa/Brave für Discovery, dann optional ein CRM-MCP für Draft-Import—nicht gleichzeitig alle vier MCPs voll laden.

## Wann nutzen

- Token-Budget knapp, aber Liste + CRM nötig.
- Unklar, ob Exa alleine reicht vs. Brave-Verifikation.

**Wann nicht**

- Reine akademische Websuche → `recherche-wissen/web-exa`, nicht dieses Fokus-Template.

## Tool-Stack

| Tool | Rolle | Begründung |
|------|-------|------------|
| Exa MCP | Discovery | Breite semantische Treffer |
| Brave Search | Verify | Zweitquelle |
| attio / close | Import Draft | Nur Phase 2 |

## System-Prompt / Instruktionen

```text
You stage leadgen tooling (vertrieb-crm/leadgen-mcp-focus).

Phase A – Research only: Exa MCP on; Brave for spot-check top N; attio/close OFF.
Deliver: CSV path and row count; cite queries used.

Phase B – CRM (optional): disable Exa if user confirms research complete; enable single CRM MCP (attio OR close, never both).
Deliver: import mapping YAML and dry-run row preview (5 rows)—no insert until FREIGABE CRM IMPORT.

Do not use web-exa recherche template ids in this flow—Exa here is account discovery only.

If Brave and Exa disagree on company existence, downgrade fit_score and keep both URLs.

Rate limits: log HTTP 429; switch to smaller batch, do not add third search MCP.

Hermes include filter: recommend attio off during Phase A to save tokens.

User asks "just CSV": Phase B skipped entirely.

User asks "push to CRM": require CSV checksum match before Phase B.

Document phase transitions with timestamps.

German queries ok for DACH ICP; store query language in log.

Close import: warn about duplicate lead rules in workspace.

Attio lists: fetch list schema before mapping columns.

Never run Close sequences from this focus template.
```

## Arbeitsablauf

1. Ziel: nur CSV oder CSV+CRM klären.
2. Phase A: Exa/Brave aktivieren, CRM-MCPs aus Policy.
3. Liste exportieren und Checksumme notieren.
4. Nutzer-Review-Gate.
5. Phase B optional: ein CRM, Mapping + Dry-Run.
6. Freigabe für Insert abwarten.
7. Abschlussbericht Phasen und MCP-Nutzung.

## Qualitätskriterien / Definition of Done

- [ ] Klare Phasentrennung im Log
- [ ] Maximal ein CRM in Phase B
- [ ] Dry-Run vor Insert
- [ ] Kein web-exa-Recherche-Scope vermischt

## Sicherheit & Freigaben

- CRM-Bulk-Insert kann Duplikate massenhaft erzeugen.
- API-Keys nicht in Queries loggen.

## Fallstricke

- attio während Exa-Suche aktiv → Kontext-Overflow.
- Brave für jede Zeile statt Stichprobe → Budget leer.
- Phase B ohne CSV-Review.
- Close+Attio parallel importieren.
- Exa-Ergebnis als CRM-Company ohne Domain-Normalisierung.

## Grundbeispiele

### Beispiel 1 (Beispieldaten)

- **Aufgabe:** Nur CSV, 20 Accounts
- **Input:** ICP SaaS DACH
- **Prompt:**

```text
Phase A only. attio excluded. Deliver leads_dach_saas.csv.
```

- **Erwartetes Ergebnis:**

```text
Phase A complete | MCPs: exa, brave | CSV 20 rows | Phase B skipped
```

### Beispiel 2 (Beispieldaten)

- **Aufgabe:** CSV dann Attio Dry-Run
- **Input:** `leads_dach_saas.csv` sha256 bekannt
- **Prompt:**

```text
Phase B attio mapping, 5-row preview, no insert.
```

- **Erwartetes Ergebnis:**

```text
mapping.yaml | preview ids match csv | awaiting FREIGABE
```