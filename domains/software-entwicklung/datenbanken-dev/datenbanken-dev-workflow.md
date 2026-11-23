---
id: datenbanken-dev-workflow
title: "Datenbanken (Entwicklung)"
domain: software-entwicklung
category: datenbanken-dev
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
  - "Schema-Änderung oder Query-Optimierung"
  - "Migration tool im Repo"
outputs:
  - "Migration file + rollback"
  - "EXPLAIN output"
risk_level: medium
example_count: 2
version: "1.0.0"
updated: "2026-11-23"
---

## Zweck

Dev-Datenbanken: versionierte **Migrationen**, sichere Queries, Index-Tuning mit EXPLAIN — kein Prod-DROP ohne Gate.

## Wann nutzen

- Neue Tabellen/Spalten, Index, langsame Query.
- Lokale Seed-Daten.

**Wann nicht:** Prod-Restore/Backup (devops).

## Tool-Stack

| Tool | Rolle | Begründung |
|------|-------|------------|
| alembic/flyway | Migrations | up/down |
| psql | Ad-hoc | dev only |
| pg_dump | schema only | review |

## System-Prompt / Instruktionen

```text
Database dev workflow (software-entwicklung/datenbanken-dev).

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
No manual prod psql unless user supplies PROD_APPROVE.
```

## Arbeitsablauf

1. Tool erkennen: `alembic` / `flyway` / Prisma migrate.
2. Migration generieren mit up+down.
3. Lokal anwenden: `alembic upgrade head`.
4. Tests laufen.
5. Slow query: `psql -c "EXPLAIN ANALYZE SELECT ..."`.
6. Index-Migration separat wenn concurrent nötig.
7. PR mit Migrations-Review-Hinweis.

## Qualitätskriterien / Definition of Done

- [ ] Down-Migration vorhanden oder begründet
- [ ] Tests grün
- [ ] EXPLAIN bei Perf-Tasks

## Sicherheit & Freigaben

- Prod-URL nicht in Dev-Skripten hardcoden.
- PII nicht in Seeds.

## Fallstricke

- Migration ohne Lock-Zeit-Denken — Big table freeze.
- Nullable fehlt bei Backfill.
- Unique Index vor Duplikat-Cleanup.
- ORM auto migration silently diverges.
- CROSS JOIN accidental.

## Grundbeispiele

### Beispiel 1 (Beispieldaten)

- **Aufgabe:** Spalte `status` hinzufügen.
- **Input:** Postgres alembic.
- **Prompt:**

```text
Add nullable status with default; upgrade+downgrade; pytest.
```

- **Erwartetes Ergebnis:**

```bash
alembic upgrade head
pytest tests/db/
alembic downgrade -1
```

### Beispiel 2 (Beispieldaten)

- **Aufgabe:** Index für user_id FK.
- **Input:** slow list query.
- **Prompt:**

```text
EXPLAIN ANALYZE; propose index migration; note CONCURRENTLY for prod.
```

- **Erwartetes Ergebnis:**

```sql
EXPLAIN ANALYZE SELECT * FROM orders WHERE user_id = $1;
-- Seq Scan → CREATE INDEX idx_orders_user_id ON orders(user_id);
```