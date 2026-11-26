---
id: etl-pipelines-workflow
title: "ETL-Pipelines & Orchestrierung"
domain: data-analytics
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
  - name: motherduck MCP (Hermes-catalog)
    install: "https://github.com/NousResearch/hermes-agent/tree/main/optional-mcps/motherduck"
    version_notes: "Nous-approved optional-mcps-catalog entry (Listing 23 Nov 2026)."
inputs:
  - "Sources (API, S3, SFTP), destination (warehouse/lake)"
  - "Frequenz, SLAs, Idempotenz"
  - "Fehler-Alert-Kanal"
outputs:
  - "Pipeline-Diagramm (Mermaid/ASCII)"
  - "n8n workflow JSON draft"
  - "DDL/Staging-SQL"
risk_level: medium
example_count: 2
version: "1.1.0"
updated: "2026-11-23"
---
## Purpose

Design ETL: Extract Transform Load with Idempotency, Retry, Staging—n8n-Workflow or SQL orchestration, Prod activation with share only.

## When to use

- Nightly Syncs CRM→DuckDB.
- API→Parquet Lake.

**When not* *

- Sub-Sekunden-Streaming without passende Tech.

## Tool stack

| Tool | Role | Justification |
|------|-------|------------|
| n8n | Orchestrator | Visuell |
| motherduck | Target | SQL load |

## System prompt

```text
Role: ETL pipeline designer (data-analytics/etl-pipelines).
Design idempotent pipelines with staging bronze silver optional—no prod cron enable without USER_APPROVAL ETL PROD.
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
USER_APPROVAL required activate schedule.
Partial failure: restart from watermark not full reload unless documented.
Compliance PII columns encrypt at rest note user infra.
Output: etl_design.md, workflow.json draft, staging_ddl.sql.
Test: dry run sample 100 rows procedure.
```

## Workflow

1.Clarify sources, goal, schedule.
2. Define watermark and keys.
3. Write staging DDL.
4. n8n-Flow skizzieren (Extract→Transform→Load).
5. Idempotenz-Testplan.
6. Fehler/Alert-Pfad.
7. Draft-Artefakte without Prod-Schedule.

## Definition of done

- [ ] Upsert/merge documented
- [ ] No Secrets in workflow.json
- [ ] Watermark-Strategie klar
Prod-Cron not active without release

## Security

- medium risk Prod-Writes.
- API-Keys in n8n Credentials.

## Pitfalls

- Full reload nightly teuer.
- Watermark Uhr vs Event-Time.
- n8n without Retry DLQ.
- Schema break silent null.
- PII in bronze unencrypted.

## Basic examples

### Example 1 (Example data (self-written))
- **Task:** CRM nightly sync
- **Input:** API updated_at watermark
- **Prompt:**

```text
etl_design.md mermaid upsert on id.
```

- **Expected result:**

```text
diagram extract transform load | watermark updated_at
```

### Example 2 (Example data (self-written))
- **Task:** n8n draft
- **Input:** 3 nodes extract transform load
- **Prompt:**

```text
workflow.json no secrets credential refs only.
```

- **Expected result:**

```text
json valid | no api_key strings
```