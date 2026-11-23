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
  - "Parquet/CSV Pfade"
  - "Fragen/KPIs"
  - "Filterzeitraum"
outputs:
  - "SQL-Datei"
  - "Ergebnis-CSV"
  - "Kurzinterpretation"
risk_level: low
version: "1.0.0"
updated: "2026-11-23"
example_count: 2
---

## Zweck

Große lokale Datensätze schnell per SQL analysieren ohne Warenehouse-Setup.

## Wann nutzen

- Log-Exports, Verkaufs-CSV, eine-offene-Frage.
- Nicht für Echtzeit-Streaming (dafür Flink/ksqlDB).

## Tool-Stack

| Tool | Rolle | Begründung |
|------|-------|------------|
| DuckDB | OLAP engine | In-process, schnell |
| pandas | optional | Ergebnis nachbearbeiten |
| evidence | optional | Docs aus SQL |

## System-Prompt / Instruktionen

```text
Analyze data with DuckDB SQL; read-only on sources.
Write reproducible .sql with parameterized date filters.
Output CSV and plain-language summary in German.
Never join in external PII without approval.
```

## Arbeitsablauf

1. Schema inspizieren `DESCRIBE SELECT *`.
2. SQL entwerfen; EXPLAIN prüfen.
3. Ergebnis exportieren.
4. Plausibilität (Summen, Nullen).
5. Query + Ergebnis versionieren.

## Qualitätskriterien / Definition of Done

- [ ] Query deterministisch
- [ ] Laufzeit dokumentiert
- [ ] Keine PII in Summary

## Sicherheit & Freigaben

- Daten lokal; keine Cloud-Uploads.
- Aggregation statt Rohdaten in Tickets.

## Grundbeispiele

### Beispiel 1 (Beispieldaten)

_Siehe vorheriger Abschnitt; bei Migration ergänzt._

### Beispiel 2 (Beispieldaten)

- **Aufgabe:** Validierung
- **Input:** n/a
- **Prompt:** `validate output`
- **Erwartetes Ergebnis:** OK

## Beispiele (Legacy)

**Eingabe:** `sales_2026.parquet`, Umsatz nach Region Q3
**Erwartetes Ergebnis:** `report_q3.csv`, 1-Seiten-Fazit
