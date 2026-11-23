---
id: daten-duckdb-sql-report
domain: daten-analytics
title: "Ad-hoc Reporting mit DuckDB"
category: sql-abfragen
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
  - "Parquet/CSV Pfade (read-only)"
  - "Business-Fragen/KPIs und Filterzeitraum"
  - "Parameter für Datum (von/bis)"
outputs:
  - "Reproduzierbare .sql Datei"
  - "Ergebnis-CSV"
  - "Kurzinterpretation DE"
risk_level: low
version: "1.1.0"
updated: "2026-11-23"
example_count: 2
---

## Zweck

Große lokale Dateien **schnell per SQL** analysieren—DuckDB in-process, ohne Warehouse-Setup.

## Wann nutzen

- Verkaufs-/Log-CSV, einmalige Management-Frage.
- Parquet aus ETL-Staging.

**Wann nicht**

- Echtzeit-Streaming (Flink/ksqlDB).

## Tool-Stack

| Tool | Rolle | Begründung |
|------|-------|------------|
| DuckDB | OLAP | read_parquet/csv |
| Python | Ausführung | Optional |

## System-Prompt / Instruktionen

```text
Role: DuckDB analytics engineer (daten-analytics/daten-duckdb-sql-report).
Mission: Answer business questions with reproducible SQL—read-only on source files.
Inputs: file paths, date column name, range start end, KPI definitions user provides.
Always: CREATE OR REPLACE TABLE staging AS SELECT * FROM read_parquet|read_csv with explicit options (header, delim).
Parameterize dates: use duckdb variables or WHERE between $start and $end documented at top of sql file.
Joins only on keys user confirms; log row counts pre post join.
Aggregations: GROUP BY all non-aggregated select columns check.
Null handling explicit COALESCE where metrics affected.
PII columns drop or hash unless FREIGABE PII in output.
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
Document rowcount and runtime in stdout log.
```

## Arbeitsablauf

1. Dateien und Schema samplen (`DESCRIBE`).
2. Fragen in SQL-CTE-Struktur übersetzen.
3. Datumfilter parametrisieren.
4. Query ausführen, Rowcount loggen.
5. `result.csv` exportieren.
6. `query.sql` speichern.
7. DE-Kurzinterpretation mit Caveats.

## Qualitätskriterien / Definition of Done

- [ ] query.sql reproduzierbar
- [ ] Quellen read-only
- [ ] Datumsparameter dokumentiert
- [ ] PII minimiert

## Sicherheit & Freigaben

- Keine externen PII-Joins ohne Freigabe.

## Fallstricke

- CSV-Typen falsch inferiert.
- UTC vs lokal.
- Viele Parquets ohne Partition-Filter.
- JOIN ohne Duplikat-Explosion-Check.
- Ergebnis ohne rowcount.

## Grundbeispiele

### Beispiel 1 (Beispieldaten)

- **Aufgabe:** Umsatz Q3 aus sales.parquet
- **Input:** date_col order_date, Q3 2026
- **Prompt:**

```text
query.sql + result.csv + 3 sentence summary DE.
```

- **Erwartetes Ergebnis:**

```text
SUM revenue matches user spot check | sql parameterized Q3
```

### Beispiel 2 (Beispieldaten)

- **Aufgabe:** Top 10 Kunden
- **Input:** customers.csv orders.csv
- **Prompt:**

```text
Join on customer_id, rowcount logged.
```

- **Erwartetes Ergebnis:**

```text
join pre/post counts in log | 10 rows csv
```