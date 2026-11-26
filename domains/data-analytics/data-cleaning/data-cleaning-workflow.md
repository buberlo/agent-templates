---
id: data-cleaning-workflow
title: "Data Cleaning Workflow"
domain: data-analytics
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
  - name: motherduck MCP (Hermes-catalog)
    install: "https://github.com/NousResearch/hermes-agent/tree/main/optional-mcps/motherduck"
    version_notes: "Nous-approved optional-mcps-catalog entry (Listing 23 Nov 2026)."
  - name: MarkItDown
    install: "https://github.com/microsoft/markitdown"
    version_notes: "197975 GitHub Stars"
inputs:
  - "Raw data path, key columns"
  - "Quality rules (Unique, Range, Regex)"
  - "Dealing with outliers (flag|quarantine)"
outputs:
  - "cleaned.parquet or CSV"
  - "quality_report.md"
  - "transform.sql or Python-Skript"
risk_level: low
example_count: 2
version: "1.1.0"
updated: "2026-11-23"
---

## Purpose

**Deterministic cleanup** with auditable rulebook—original remains cleaned as a new file.

## When to use

- Before ETL/ML, after supplier export.
Duplicates and format garbage.

**When not**

- „KI-Raten“ without dokumentierte Regeln.

## Tool stack

| Tool | Role | Justification |
|------|-------|------------|
| DuckDB/SQL | Regeln | Reproduzierbar |
| motherduck | Remote | Optional |

## System prompt

```text
Role: data quality engineer (data-analytics/data-cleaning).
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
DROP only if user deletes quarantine permanently.
Log rows in out rows quarantined percent.
German column names ok quoted identifiers.
Validate cleaned rowcount + quarantine = source rowcount.
Referential checks fk orphan counts optional user.
After cleaning checksum sha256 cleaned file log.
```

## Workflow

1. Source profilieren.
2. Regeln in YAML festhalten.
3. Write SQL/Python transformation.
4. Dry-run auf Sample.
5. Vollrun cleaned + quarantine.
6. Check the rowcount balance sheet.
7. quality_report ausliefern.

## Definition of done / Definition of Done

[ ] Source unchanged
- [ ] Bilanz rowcount stimmt
- [ ] Regel-IDs in Quarantine
- [ ] cleaning_rules.yaml versioniert

## Security

- Quarantine kann PII enthalten—Schutz.

## Pitfalls

- Deduplication without a timeline yields the wrong record.
- Regex zu aggressiv.
- Locale Datum still wrong.
Quarantine not stored.
- Silent drop rows.

## Basic examples

### Example 1 (Example data (self-written))
- **Task:** Dedupe orders order_id keep latest
- **Input:** orders.csv
- **Prompt:**

```text
quality report + cleaned.parquet quarantine with rule_id.
```

- **Expected result:**

```text
counts balance | dedupe rule documented
```

### Example 2 (Example data (self-written))
- **Task:** email regex validate
- **Input:** contacts.csv
- **Prompt:**

```text
invalid emails to quarantine REGEX_EMAIL rule.
```

- **Expected result:**

```text
quarantine n rows REGEX_EMAIL | valid in cleaned
```