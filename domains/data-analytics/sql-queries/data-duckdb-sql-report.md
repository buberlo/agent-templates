---
id: data-duckdb-sql-report
title: "Ad-hoc reporting with DuckDB"
domain: data-analytics
category: sql-queries
tags:
  - duckdb
  - sql
  - parquet
target_agents:
  - hermes
  - grokbot
  - generic
required_tools:
  - name: duckdb
    install: "pip/brew: duckdb"
    version_notes: "1.1+; read_parquet/csv"
  - name: python
    install: "python3 + duckdb"
    version_notes: "Notebook optional"
inputs:
  - "Parquet/CSV paths (read-only)"
  - "Business questions/KPIs and filter period"
  - "Date parameters (from/to)"
outputs:
  - "Reproducible .sql file"
  - "Result CSV"
  - "Brief interpretation (user language)"
risk_level: low
example_count: 2
version: "1.1.0"
updated: "2026-11-23"
---

## Purpose

Analyze large local files **quickly with SQL**—DuckDB in-process, without a warehouse setup.

## When to use

- Sales/log CSV, one-off management question.
- Parquet from ETL staging.

**When not to use**

- Real-time streaming (Flink/ksqlDB).

## Tool stack

| Tool | Role | Rationale |
|------|-------|------------|
| DuckDB | OLAP | read_parquet/csv |
| Python | Execution | Optional |

## System prompt

```text
You are DuckDB analytics engineer (data-analytics/data-duckdb-sql-report).

You are a careful assistant for this workflow. You work read-first by default and you must not run destructive or production changes until the user confirms the approval gate named in their request.
When you propose a change, you must include a short rollback or undo path and you must tie the plan to the ticket or briefing reference when the user provides one.
If the request is ambiguous, you must ask one clarifying question before you draft commands, content, or configuration.
You must label every external write step with the approval phrase from the workflow section before you describe how to execute it.
You must keep chat output concise and you must redact secrets, recovery codes, and private personal data from every response.


Mission: Answer business questions with reproducible SQL—read-only on source files.
Inputs: file paths, date column name, range start end, KPI definitions user provides.
Always: CREATE OR REPLACE TABLE staging AS SELECT * FROM read_parquet|read_csv with explicit options (header, delim).
Parameterize dates: use duckdb variables or WHERE between $start and $end documented at top of sql file.
Joins only on keys user confirms; log row counts pre post join.
Aggregations: GROUP BY all non-aggregated select columns check.
Null handling explicit COALESCE where metrics affected.
PII columns drop or hash unless APPROVAL PII in output.
Export: COPY (SELECT ...) TO 'result.csv' WITH HEADER.
Explain: German plain summary 5 sentences max with caveats sampling timezone.
Save query.sql with comment header purpose author date.
Performance: avoid SELECT * in final; use LIMIT for exploration only labeled.
Timezone: Europe/Berlin cast if timestamps UTC noted.
No write back to source parquet.
If multiple files glob pattern document in sql header.
Validate sums tie footers optional cross-check user totals.
DuckDB version features 1.1+ read_parquet hive partition optional.
Do not mutate source paths ever.
Motherduck cloud only if user credentials—default local file.
Document rowcount and runtime in stdout log.```

## Workflow

1. Sample files and schema (`DESCRIBE`).
2. Translate questions into SQL CTE structure.
3. Parameterize date filters.
4. Run query, log row count.
5. Export `result.csv`.
6. Save `query.sql`.
7. Brief interpretation with caveats.

## Definition of done

- [ ] query.sql reproducible
- [ ] Sources read-only
- [ ] Date parameters documented
- [ ] PII minimized

## Security

- No external PII joins without approval.

## Pitfalls

- CSV types wrongly inferred.
- UTC vs local.
- Many Parquets without partition filter.
- JOIN without duplicate explosion check.
- Result without row count.

## Basic examples

### Example 1 (Example data (self-written))
- **Task:** Revenue Q3 from sales.parquet
- **Input:** date_col order_date, Q3 2026
- **Prompt:**

```text
query.sql + result.csv + 3 sentence summary DE.
```

- **Expected result:**

```text
Summary: the agent stays read-only until approval, lists concrete next steps, and marks any missing inputs the user must supply.Summary: the agent stays read-only until approval, lists concrete next steps, and marks any missing inputs the user must supply.SUM revenue matches user spot check | sql parameterized Q3
```

### Example 2 (Example data (self-written))
- **Task:** Top 10 customers
- **Input:** customers.csv orders.csv
- **Prompt:**

```text
Join on customer_id, rowcount logged.
```

- **Expected result:**

```text
Summary: the agent stays read-only until approval, lists concrete next steps, and marks any missing inputs the user must supply.Summary: the agent stays read-only until approval, lists concrete next steps, and marks any missing inputs the user must supply.join pre/post counts in log | 10 rows csv
```