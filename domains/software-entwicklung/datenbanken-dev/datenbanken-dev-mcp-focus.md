---
id: datenbanken-dev-mcp-focus
title: "Datenbanken (Entwicklung): MCP/Skill-Fokus"
domain: software-entwicklung
category: datenbanken-dev
tags:
  - sql
  - mcp
  - postgres
target_agents:
  - hermes
  - claude-code
  - cursor
  - generic-mcp-agents
required_tools:
  - name: postgres-mcp
    install: "community postgres MCP"
    version_notes: "SELECT default"
  - name: psql
    install: "verify step"
    version_notes: "same DSN as MCP staging"
inputs:
  - "Staging DSN name"
  - "Migration path"
outputs:
  - "Migration draft"
  - "MCP query audit"
risk_level: medium
example_count: 2
version: "1.0.0"
updated: "2026-11-23"
---

## Zweck

**Postgres MCP** nur für Schema-Reads und EXPLAIN auf **Staging**; Writes ausschließlich über Migration-Files im Repo.

## Wann nutzen

- Agent exploriert Schema per MCP, committet alembic/flyway.

**Wann nicht:** Wenn MCP nicht read-only konfiguriert.

## Tool-Stack

| Tool | Rolle | Begründung |
|------|-------|------------|
| Postgres MCP | Describe/explain | read |
| alembic | Writes | VCS |
| Skill | Gate | no MCP DDL |

## System-Prompt / Instruktionen

```text
Database dev MCP/Skill focus (software-entwicklung/datenbanken-dev).

MCP allowed: SELECT, EXPLAIN, \d equivalents; forbidden: DROP, TRUNCATE, UPDATE without migration file.
Skill verify: migration file exists + alembic upgrade on docker compose db.
DSN must match staging name user provides; reject prod hostnames pattern *prod*.
Log every MCP SQL in audit; parameters redacted.
One postgres MCP; disable duplicates.
If MCP returns sample rows, redact PII in summary.
Translate MCP findings into versioned migration, never live MCP DDL for schema change.
Connection pool limits: avoid MCP full table scan on large tables without LIMIT sample.
Fallback: read migrations folder if MCP auth fails.
```

## Arbeitsablauf

1. Confirm staging DSN.
2. MCP: table describe.
3. MCP: EXPLAIN slow query.
4. Write migration SQL file.
5. `alembic upgrade head` local.
6. pytest.
7. MCP audit attach to PR draft.

## Qualitätskriterien / Definition of Done

- [ ] Kein MCP DDL applied
- [ ] Migration in git
- [ ] Staging-only DSN

## Sicherheit & Freigaben

- Prod MCP blocked.
- Row samples redacted.

## Fallstricke

- MCP write tool mislabeled read.
- Staging = prod copy PII.
- MCP LIMIT vergessen — timeout.
- Migration nicht aus MCP abgeleitet.

## Grundbeispiele

### Beispiel 1 (Beispieldaten)

- **Aufgabe:** Index aus EXPLAIN MCP.
- **Input:** staging `app_staging`.
- **Prompt:**

```text
MCP EXPLAIN orders query; write migration index; no MCP CREATE INDEX.
```

- **Erwartetes Ergebnis:**

```text
migrations/20261123_idx_orders_user.py
alembic upgrade head OK
```

### Beispiel 2 (Beispieldaten)

- **Aufgabe:** Reject prod.
- **Input:** DSN host db.prod.internal.
- **Prompt:**

```text
Abort MCP; read schema from migrations only.
```

- **Erwartetes Ergebnis:**

```text
MCP not connected; schema from alembic versions
```