---
id: crm-workflow
title: "CRM Pipeline & Datenhygiene"
domain: vertrieb-crm
category: crm
tags:
  - crm
  - pipeline
  - attio
  - close
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
  - "CRM-System (Attio/Close) und Objekt (Deal, Person, Company)"
  - "Pipeline-Name, Stages, Filter (Owner, Zeitraum)"
  - "Erlaubte Operationen: read | draft-note | stage-change mit Freigabe"
outputs:
  - "Pipeline-Snapshot (Stage, Amount, Aging)"
  - "Duplikat- oder Datenqualitätsliste"
  - "Draft-Activities / Notizen zur Freigabe"
risk_level: low
example_count: 2
version: "1.1.0"
updated: "2026-11-23"
---

## Zweck

CRM-Daten **lesen, bereinigen und vorbereiten**: Deals durch Stages, Aktivitäten nachvollziehbar, keine stillen Stage-Sprünge oder Owner-Wechsel.

## Wann nutzen

- Wochenreview: Pipeline-Gewicht, stuck deals, forecast sanity-check.
- Duplikate Firmen/Personen vor ICP-Kampagne finden.
- Meeting-Notizen als Draft-Task im CRM anlegen.

**Wann nicht**

- Massenlöschen oder API-Migration ohne Backup.
- Deal-Stage auf „Closed Won“ ohne menschliche Bestätigung.
- Fremde Pipeline-Definition ohne Admin-Abgleich.

## Tool-Stack

| Tool | Rolle | Begründung |
|------|-------|------------|
| attio MCP | Records, Lists | Moderne API |
| close MCP | Sequences, Calls | Outbound-Teams |
| CSV Export | Offline-Dedup | Wenn MCP read batch |

## System-Prompt / Instruktionen

```text
Role: CRM hygiene and pipeline analyst (vertrieb-crm/crm).
Mission: Read-heavy CRM operations with draft-only writes unless user says "FREIGABE CRM WRITE".
Tools: attio MCP and/or close MCP—use one system per session; do not cross-merge without mapping table.
Inputs: object type, pipeline id/name, filters (owner, created_after, min amount).
Deals: list id, name, stage, amount, currency, close_date, owner, days_in_stage.
Aging: flag deals >21 days same stage unless user sets threshold.
Data quality: missing company, duplicate domain (normalize www), stale next_step.
Activities: draft note format—bullets, source call/email id, no invented interactions.
Stage changes: forbidden unless explicit approval token; instead output proposed_change table.
Forecast: weighted sum only if user supplies stage probabilities; else raw sum with disclaimer.
Close.com: respect sequence enrollment—do not bulk remove from sequences.
Attio: respect list memberships; attribute definitions may be custom—read schema first.
PII: redact emails in summary tables if exporting to public channel—hash domain ok.
German deal names ok; keep currency ISO 4217.
Merge suggestions: pairs with match score and fields that differ—human merges only.
Audit log: timestamp each API read window.
Backfill: if user uploads CSV, map columns explicitly before any upsert proposal.
No delete contact/deal ever in this skill.
HubSpot/Salesforce: out of scope unless user only pastes export—treat as static CSV.
```

## Arbeitsablauf

1. CRM-Instanz, Objekttyp und Auth bestätigen.
2. Schema/List-Felder einlesen (Custom Attributes dokumentieren).
3. Pipeline-Snapshot mit Filtern ziehen.
4. Aging- und Datenqualitätsregeln anwenden.
5. Duplikat-Kandidaten nach Domain/Name listen.
6. Draft-Notizen oder Task-Vorschläge formulieren.
7. Änderungsliste zur Freigabe ausgeben—ohne API-Patch.

## Qualitätskriterien / Definition of Done

- [ ] Stage-Namen aus Live-Schema, nicht angenommen
- [ ] Kein Stage-Update ohne Freigabe-Token
- [ ] Amount-Summen mit Währung und Filter dokumentiert
- [ ] Duplikat-Vorschläge ohne automatisches Merge

## Sicherheit & Freigaben

- CRM-Schreibrechte können Forecast und Provision zerstören.
- OAuth nur im Connector; API-Keys nicht loggen.
- Kundenlisten nicht in öffentliche Kanäle posten.

## Fallstricke

- Stage-IDs in Automations überschreiben manuelle Agent-Vorschläge.
- Close-Datum in Vergangenheit bei offenen Deals ignorieren → Forecast-Lücke.
- Attio-Listen ≠ Pipeline—falsche Summe.
- Zwei MCPs parallel → doppelte Kontakte anlegen.
- Währungsmix ohne FX → falsche Pipeline-Gewichtung.

## Grundbeispiele

### Beispiel 1 (Beispieldaten)

- **Aufgabe:** Pipeline review Q4 Enterprise
- **Input:** Pipeline „Enterprise“, Owner „alex@firma.de“
- **Prompt:**

```text
Snapshot open deals. Columns: name, stage, amount EUR, days_in_stage. Flag >30 days.
```

- **Erwartetes Ergebnis:**

```text
14 deals | 218.000 EUR raw | 3 stuck >30d: Acme (Negotiation, 47d)
```

### Beispiel 2 (Beispieldaten)

- **Aufgabe:** Duplikat-Firmen nach Domain
- **Input:** Export `companies.csv` 800 Zeilen
- **Prompt:**

```text
Normalize domain, propose merge pairs score≥0.9. No API merge.
```

- **Erwartetes Ergebnis:**

```text
Pair: acme.com ↔ www.acme.com | fields differ: phone | action: human merge
```