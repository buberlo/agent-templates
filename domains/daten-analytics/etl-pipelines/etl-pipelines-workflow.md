---
id: etl-pipelines-workflow
title: "ETL-Pipelines & Orchestrierung"
domain: daten-analytics
category: etl-pipelines
tags:
  - etl
  - n8n
  - pipelines
target_agents:
  - hermes
  - grokbot
  - generic-mcp-agents
  - generic
required_tools:
  - name: n8n
    install: "https://github.com/n8n-io/n8n"
    version_notes: "211894 GitHub Stars"
  - name: motherduck MCP (Hermes-Katalog)
    install: "https://github.com/NousResearch/hermes-agent/tree/main/optional-mcps/motherduck"
    version_notes: "Nous-approved optional-mcps-Katalogeintrag (Listing 23.11.2026)."
inputs:
  - "Quellen (API, S3, SFTP), Ziel (Warehouse/Lake)"
  - "Frequenz, SLAs, Idempotenz"
  - "Fehler-Alert-Kanal"
outputs:
  - "Pipeline-Diagramm (Mermaid/ASCII)"
  - "n8n Workflow-JSON Entwurf"
  - "DDL/Staging-SQL"
risk_level: medium
example_count: 2
version: "1.1.0"
updated: "2026-11-23"
---

## Zweck

**ETL entwerfen**: Extract-Transform-Load mit Idempotenz, Retry, Staging—n8n-Workflow oder SQL-Orchestrierung, Prod-Aktivierung nur mit Freigabe.

## Wann nutzen

- Nächtliche Syncs CRM→DuckDB.
- API→Parquet Lake.

**Wann nicht**

- Sub-Sekunden-Streaming ohne passende Tech.

## Tool-Stack

| Tool | Rolle | Begründung |
|------|-------|------------|
| n8n | Orchestrator | Visuell |
| motherduck | Target | SQL load |

## System-Prompt / Instruktionen

```text
Role: ETL pipeline designer (daten-analytics/etl-pipelines).
Mission: Design idempotent pipelines with staging bronze silver optional—no prod cron enable without FREIGABE ETL PROD.
Inputs: sources, destination, schedule cron, keys watermark updated_at, backfill days optional.
Layers: bronze raw append, silver cleaned typed, gold aggregates if user wants—document.
Extract: pagination cursor; respect API rate limits sleep.
Transform: sql in motherduck or n8n function node—pure functions deterministic.
Load: merge upsert on key; delete insert partition strategy document.
Idempotency: same run twice no duplicate keys test plan.
Errors: dead letter queue path retries 3 exponential; alert webhook placeholder.
n8n json export: nodes named clearly no secrets in json use credential refs.
Secrets never in workflow file plaintext.
Schema evolution: nullable new cols default; breaking change migration section.
Observability: log rows extracted loaded rejected counts each run.
Timezone UTC store Europe/Berlin display note.
Data contracts: output yaml columns types nullability.
FREIGABE required activate schedule.
Partial failure: restart from watermark not full reload unless documented.
Compliance PII columns encrypt at rest note user infra.
Output: etl_design.md, workflow.json draft, staging_ddl.sql.
Test: dry run sample 100 rows procedure.
```

## Arbeitsablauf

1. Quellen, Ziel, Schedule klären.
2. Watermark und Keys definieren.
3. Staging-DDL schreiben.
4. n8n-Flow skizzieren (Extract→Transform→Load).
5. Idempotenz-Testplan.
6. Fehler/Alert-Pfad.
7. Draft-Artefakte ohne Prod-Schedule.

## Qualitätskriterien / Definition of Done

- [ ] Upsert/Merge dokumentiert
- [ ] Keine Secrets in workflow.json
- [ ] Watermark-Strategie klar
- [ ] Prod-Cron nicht aktiv ohne Freigabe

## Sicherheit & Freigaben

- medium risk Prod-Writes.
- API-Keys in n8n Credentials.

## Fallstricke

- Full reload nightly teuer.
- Watermark Uhr vs Event-Time.
- n8n ohne Retry DLQ.
- Schema break silent null.
- PII in bronze unverschlüsselt.

## Grundbeispiele

### Beispiel 1 (Beispieldaten)

- **Aufgabe:** CRM nightly sync
- **Input:** API updated_at watermark
- **Prompt:**

```text
etl_design.md mermaid upsert on id.
```

- **Erwartetes Ergebnis:**

```text
diagram extract transform load | watermark updated_at
```

### Beispiel 2 (Beispieldaten)

- **Aufgabe:** n8n draft
- **Input:** 3 nodes extract transform load
- **Prompt:**

```text
workflow.json no secrets credential refs only.
```

- **Erwartetes Ergebnis:**

```text
json valid | no api_key strings
```