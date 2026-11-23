---
id: data-cleaning-workflow
title: "Data Cleaning & Qualitätsregeln"
domain: daten-analytics
category: data-cleaning
tags:
  - data-quality
  - cleaning
target_agents:
  - hermes
  - grokbot
  - generic-mcp-agents
  - generic
required_tools:
  - name: motherduck MCP (Hermes-Katalog)
    install: "https://github.com/NousResearch/hermes-agent/tree/main/optional-mcps/motherduck"
    version_notes: "Nous-approved optional-mcps-Katalogeintrag (Listing 23.11.2026)."
  - name: MarkItDown
    install: "https://github.com/microsoft/markitdown"
    version_notes: "197975 GitHub Stars"
inputs:
  - "Rohdaten-Pfad, Schlüsselspalten"
  - "Qualitätsregeln (Unique, Range, Regex)"
  - "Umgang mit Ausreißern (flag|quarantine)"
outputs:
  - "cleaned.parquet oder CSV"
  - "quality_report.md"
  - "transform.sql oder Python-Skript"
risk_level: low
example_count: 2
version: "1.1.0"
updated: "2026-11-23"
---

## Zweck

**Deterministische Bereinigung** mit auditablem Regelwerk—Original bleibt, bereinigt als neue Datei.

## Wann nutzen

- Vor ETL/ML, nach Lieferanten-Export.
- Duplikate und Format-Müll.

**Wann nicht**

- „KI-Raten“ ohne dokumentierte Regeln.

## Tool-Stack

| Tool | Rolle | Begründung |
|------|-------|------------|
| DuckDB/SQL | Regeln | Reproduzierbar |
| motherduck | Remote | Optional |

## System-Prompt / Instruktionen

```text
Role: data quality engineer (daten-analytics/data-cleaning).
Mission: Apply explicit cleaning rules; never overwrite source; quarantine bad rows.
Inputs: source path, primary keys[], rules list unique|not_null|regex|range|enum, outlier policy flag.
Profile before: rowcount, null%, distinct keys, duplicate key count.
Rules engine: SQL CASE or Python apply per rule; rule_id column on quarantine table.
Quarantine table: all rejected rows with rule_ids_failed array or multiple cols.
Cleaning: trim strings, unify date ISO8601, decimal comma only if locale DE user says normalize dot.
Dedupe: keep latest by timestamp col user defines or first occurrence document.
PII: hash columns in quarantine if exporting samples.
Output: data/cleaned.parquet, data/quarantine.parquet, quality_report.md counts per rule.
Version cleaning_rules_v1.yaml copied in report.
No destroy source file.
Motherduck execute same sql if remote authorized.
MarkItDown optional convert report for email.
FREIGABE DROP only if user deletes quarantine permanently.
Log rows in out rows quarantined percent.
German column names ok quoted identifiers.
Validate cleaned rowcount + quarantine = source rowcount.
Referential checks fk orphan counts optional user.
After cleaning checksum sha256 cleaned file log.
```

## Arbeitsablauf

1. Source profilieren.
2. Regeln in YAML festhalten.
3. SQL/Python-Transformation schreiben.
4. Dry-run auf Sample.
5. Vollrun cleaned + quarantine.
6. Rowcount-Bilanz prüfen.
7. quality_report ausliefern.

## Qualitätskriterien / Definition of Done

- [ ] Source unverändert
- [ ] Bilanz rowcount stimmt
- [ ] Regel-IDs in Quarantine
- [ ] cleaning_rules.yaml versioniert

## Sicherheit & Freigaben

- Quarantine kann PII enthalten—Schutz.

## Fallstricke

- Dedupe ohne Zeitachse falscher Datensatz.
- Regex zu aggressiv.
- Locale Datum still wrong.
- Quarantine nicht gespeichert.
- Silent drop rows.

## Grundbeispiele

### Beispiel 1 (Beispieldaten)

- **Aufgabe:** Dedupe orders order_id keep latest
- **Input:** orders.csv
- **Prompt:**

```text
quality report + cleaned.parquet quarantine with rule_id.
```

- **Erwartetes Ergebnis:**

```text
counts balance | dedupe rule documented
```

### Beispiel 2 (Beispieldaten)

- **Aufgabe:** email regex validate
- **Input:** contacts.csv
- **Prompt:**

```text
invalid emails to quarantine REGEX_EMAIL rule.
```

- **Erwartetes Ergebnis:**

```text
quarantine n rows REGEX_EMAIL | valid in cleaned
```