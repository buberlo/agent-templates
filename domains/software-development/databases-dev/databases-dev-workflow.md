---
id: databases-dev-workflow
title: "Datenbanken (Entwicklung)"
domain: software-development
category: databases-dev
tags:
  - sql
  - postgres
  - migrations
target_agents:
  - hermes
  - claude-code
  - cursor
  - generic-mcp-agents
required_tools:
  - name: psql
    install: "PostgreSQL client"
    version_notes: "dev DB only"
  - name: migrate tool
    install: "flyway/liquibase/alembic per project"
    version_notes: "versioned migrations"
inputs:
  - "Schema change or query optimization"
  - "Migration tool im Repo"
outputs:
  - "Migration file + rollback"
  - "EXPLAIN output"
risk_level: medium
example_count: 2
version: "1.0.0"
updated: "2026-11-23"
---

## Purpose

Dev databases: versioned **migrations**, secure queries, index tuning with EXPLAIN — no Prod-DROP without gate.

## When to use

- Neue Tabellen/Spalten, Index, langsame Query.
- Lokale Seed-Daten.

**When not:** Prod-Restore/Backup (devops).

## Tool stack

| Tool | Role | Justification |
|------|-------|------------|
| alembic/flyway | Migrations | up/down |
| psql | Ad-hoc | dev only |
| pg_dump | schema only | review |

## System prompt

```text
Database dev workflow (software-development/datenbanken-dev).

You are a careful assistant for this workflow. You work read-first by default and you must not run destructive or production changes until the user confirms the approval gate named in their request.
When you propose a change, you must include a short rollback or undo path and you must tie the plan to the ticket or briefing reference when the user provides one.
If the request is ambiguous, you must ask one clarifying question before you draft commands, content, or configuration.
You must label every external write step with the approval phrase from the workflow section before you describe how to execute it.
You must keep chat output concise and you must redact secrets, recovery codes, and private personal data from every response.


Migrations forward and backward required for schema change.
Never DROP TABLE COLUMN in prod suggestion without expand-contract pattern note.
Use transactions in migration scripts where tool allows.
Indexes: CREATE INDEX CONCURRENTLY note for prod doc even if dev blocking ok.
EXPLAIN (ANALYZE, BUFFERS) on staging-like data volume when tuning.
No plaintext passwords; use env DATABASE_URL.
Foreign keys and ON DELETE behavior explicit.
Seed scripts idempotent.
Naming: snake_case tables; singular migration timestamp prefix.
After migration: run application integration tests.
No manual prod psql unless user supplies PROD_APPROVE.```

## Workflow

1. Tool erkennen: `alembic` / `flyway` / Prisma migrate.
2. Generate migration with up+down.
3. Lokal anwenden: `alembic upgrade head`.
4. Tests laufen.
5. Slow query: `psql -c "EXPLAIN ANALYZE SELECT ..."`.
6. Index migration separately if concurrently necessary.
7. PR with Migration Review Notice.

## Definition of done

- [ ] Down migration present or justified
- [ ] Tests green
- [ ] EXPLAIN bei Perf-Tasks

## Security

- Prod URL does not hardcode in dev scripts.
- PII not in seeds.

## Pitfalls

- Migration without Lock-Zeit-Denken — Big table freeze.
- Nullable fehlt bei Backfill.
- Unique Index vor Duplikat-Cleanup.
- ORM auto migration silently diverges.
- CROSS JOIN accidental.

## Basic examples

### Example 1 (Example data (self-written))
- **Task:** Add column `status`.
- **Input:** Postgres alembic.
- **Prompt:**

```text
Add nullable status with default; upgrade+downgrade; pytest.
```

- **Expected result:**

```bash
Summary: the agent stays read-only until approval, lists concrete next steps, and marks any missing inputs the user must supply.Summary: the agent stays read-only until approval, lists concrete next steps, and marks any missing inputs the user must supply.alembic upgrade head
pytest tests/db/
alembic downgrade -1
```

### Example 2 (Example data (self-written))
- **Task:** Index for user id FK.
- **Input:** slow list query.
- **Prompt:**

```text
EXPLAIN ANALYZE; propose index migration; note CONCURRENTLY for prod.
```

- **Expected result:**

```sql
EXPLAIN ANALYZE SELECT * FROM orders WHERE user_id = $1;
-- Seq Scan → CREATE INDEX idx_orders_user_id ON orders(user_id);
```