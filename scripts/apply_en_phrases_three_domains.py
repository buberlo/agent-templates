#!/usr/bin/env python3
"""Apply hand-authored English phrase replacements (three domains)."""
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent / "domains"
TARGETS = [ROOT / d for d in ("data-analytics", "devops-cloud", "education")]

PHRASES: list[tuple[str, str]] = [
    ("**Wann nicht:**", "**When not to use:**"),
    ("Große lokale Dateien **schnell per SQL** analysieren—DuckDB in-process, ohne Warehouse-Setup.",
     "Analyze large local files **quickly with SQL**—DuckDB in-process, without a warehouse setup."),
    ('title: "Ad-hoc Reporting mit DuckDB"', 'title: "Ad-hoc reporting with DuckDB"'),
    ('title: "Explorative Analyse mit pandas"', 'title: "Exploratory analysis with pandas"'),
    ('title: "ML-Training (tabellarisch)"', 'title: "ML training (tabular)"'),
    ('"Parquet/CSV Pfade (read-only)"', '"Parquet/CSV paths (read-only)"'),
    ('"Business-Fragen/KPIs und Filterzeitraum"', '"Business questions/KPIs and filter period"'),
    ('"Parameter für Datum (von/bis)"', '"Date parameters (from/to)"'),
    ('"Reproduzierbare .sql Datei"', '"Reproducible .sql file"'),
    ('"Ergebnis-CSV"', '"Result CSV"'),
    ('"Kurzinterpretation DE"', '"Brief interpretation (user language)"'),
    ('"Tabellendatei (CSV, Parquet, XLSX read-only)"', '"Table file (CSV, Parquet, XLSX read-only)"'),
    ('"Hypothesen und Zielspalten"', '"Hypotheses and target columns"'),
    ('"Profil-HTML (ydata-profiling o.ä.)"', '"Profile HTML (ydata-profiling or similar)"'),
    ('"Chart PNG + Datenqualitätsliste"', '"Chart PNG + data quality list"'),
    ("| Python | Ausführung | Optional |", "| Python | Execution | Optional |"),
    ("- Verkaufs-/Log-CSV, einmalige Management-Frage.", "- Sales/log CSV, one-off management question."),
    ("- Parquet aus ETL-Staging.", "- Parquet from ETL staging."),
    ("- Echtzeit-Streaming (Flink/ksqlDB).", "- Real-time streaming (Flink/ksqlDB)."),
    ("- Produktions-ML-Pipeline (→ ml-training).", "- Production ML pipeline (→ ml-training)."),
    ("- Neuer Datensatz, unklare Qualität.", "- New dataset, unclear quality."),
    ("- Hypothesen schnell prüfen.", "- Test hypotheses quickly."),
    ("**EDA vor Modell/Dashboard**: dtypes, Missing, Duplikate, Verteilungen, Korrelationen—Ausreißer nur mit approval droppen.",
     "**EDA before model/dashboard**: dtypes, missing values, duplicates, distributions, correlations—drop outliers only with approval."),
    ("1. Datei laden und Schema prüfen.", "1. Load file and inspect schema."),
    ("2. Missing/Duplikat-Audit.", "2. Missing/duplicate audit."),
    ("3. Univariate Verteilungen.", "3. Univariate distributions."),
    ("4. Bivariate Plots Ziel vs Features.", "4. Bivariate plots target vs features."),
    ("5. Outlier-Flags (IQR).", "5. Outlier flags (IQR)."),
    ("6. Profiling-HTML erzeugen.", "6. Generate profiling HTML."),
    ("7. Qualitätsliste und Notebook speichern.", "7. Save quality list and notebook."),
    ("- [ ] data_quality.md mit konkreten Issues", "- [ ] data_quality.md with concrete issues"),
    ("- [ ] Charts beschriftet DE", "- [ ] Charts labeled per user locale"),
    ("- [ ] Kein DROP ohne approval", "- [ ] No DROP without approval"),
    ("- [ ] Notebook von oben lauffähig", "- [ ] Notebook runnable top to bottom"),
    ("- Keine PII in Charts unaggregiert.", "- No unaggregated PII in charts."),
    ("- read_csv alles str.", "- read_csv everything as str."),
    ("- corr auf kategorisch encodiert falsch.", "- corr on wrongly encoded categoricals."),
    ("- Profiling 5M Zeilen OOM.", "- Profiling 5M rows OOM."),
    ("- Zeitspalte nicht geparst.", "- Time column not parsed."),
    ("- Ausreißer still entfernt.", "- Outliers silently removed."),
    ("1. Dateien und Schema samplen (`DESCRIBE`).", "1. Sample files and schema (`DESCRIBE`)."),
    ("2. Fragen in SQL-CTE-Struktur übersetzen.", "2. Translate questions into SQL CTE structure."),
    ("3. Datumfilter parametrisieren.", "3. Parameterize date filters."),
    ("4. Query ausführen, Rowcount loggen.", "4. Run query, log row count."),
    ("5. `result.csv` exportieren.", "5. Export `result.csv`."),
    ("6. `query.sql` speichern.", "6. Save `query.sql`."),
    ("7. DE-Kurzinterpretation mit Caveats.", "7. Brief interpretation with caveats."),
    ("- [ ] query.sql reproduzierbar", "- [ ] query.sql reproducible"),
    ("- [ ] Quellen read-only", "- [ ] Sources read-only"),
    ("- [ ] Datumsparameter dokumentiert", "- [ ] Date parameters documented"),
    ("- [ ] PII minimiert", "- [ ] PII minimized"),
    ("- Keine externen PII-Joins ohne approval.", "- No external PII joins without approval."),
    ("- CSV-Typen falsch inferiert.", "- CSV types wrongly inferred."),
    ("- UTC vs lokal.", "- UTC vs local."),
    ("- Viele Parquets ohne Partition-Filter.", "- Many Parquets without partition filter."),
    ("- JOIN ohne Duplikat-Explosion-Check.", "- JOIN without duplicate explosion check."),
    ("- Ergebnis ohne rowcount.", "- Result without row count."),
    ('- **Task:** Umsatz Q3 aus sales.parquet', '- **Task:** Revenue Q3 from sales.parquet'),
    ('- **Task:** Top 10 Kunden', '- **Task:** Top 10 customers'),
    ("CI/CD-Aufgaben über **GitHub MCP** und **gh** orchestrieren: Failed Runs lesen, Logs analysieren, Fixes als PR — Writes nur nach approval.",
     "Orchestrate CI/CD via **GitHub MCP** and **gh**: read failed runs, analyze logs, fixes as PR—writes only after approval."),
    ('"Repo und fehlgeschlagene Workflow-Run-ID"', '"Repo and failed workflow run ID"'),
    ('"Skill-Schritte für Lint/Test/Deploy"', '"Skill steps for lint/test/deploy"'),
    ('"Skill↔MCP-Matrix für CI"', '"Skill↔MCP matrix for CI"'),
    ('"Root-Cause-Notiz mit Log-Auszug"', '"Root-cause note with log excerpt"'),
    ("- Agent soll Actions-Logs und PR-Kontext ohne manuelles UI.", "- Agent should read Actions logs and PR context without manual UI."),
    ("- Team dokumentiert, welcher Skill-Schritt welches MCP-Tool nutzt.", "- Team documents which skill step uses which MCP tool."),
    ("**Wann nicht:** Wenn nur lokaler `act`-Test nötig ist ohne Remote — dann `coding-github-actions-ci-pipeline`.",
     "**When not to use:** When only local `act` test without remote—use `coding-github-actions-ci-pipeline`."),
    ("| GitHub Official MCP | Runs, PRs | Strukturierte API |", "| GitHub Official MCP | Runs, PRs | Structured API |"),
    ("| gh CLI | Logs/Fallback | `gh run view --log-failed` |", "| gh CLI | Logs/fallback | `gh run view --log-failed` |"),
    ("| Skill-CI | Ablauf | Repro, Fix, Verify |", "| Skill-CI | Flow | Repro, fix, verify |"),
    ("1. Skill-Matrix: Schritt → MCP-Tool / gh-Kommando.", "1. Skill matrix: step → MCP tool / gh command."),
    ("2. MCP: Workflow-Liste und letzte Runs auf `main` und PR-Branch.", "2. MCP: workflow list and latest runs on `main` and PR branch."),
    ("3. Fehl-Run-ID notieren; parallel `gh run view <id> --json conclusion,jobs`.", "3. Note failed run ID; in parallel `gh run view <id> --json conclusion,jobs`."),
    ("4. Log-Auszug (Fehlerblock) ins Ticket; Secrets redigieren.", "4. Log excerpt (error block) into ticket; redact secrets."),
    ("5. Lokalen Repro-Befehl aus Workflow extrahieren.", "5. Extract local repro command from workflow."),
    ("6. Fix-Entwurf als Diff; MCP/Skill Write nur nach approval.", "6. Fix draft as diff; MCP/skill write only after approval."),
    ("7. Nach Push: Run beobachten; Matrix aktualisieren.", "7. After push: watch run; update matrix."),
    ("- [ ] Failed Run mit Job+Step identifiziert", "- [ ] Failed run with job+step identified"),
    ("- [ ] Skill↔MCP-Matrix für den Task vollständig", "- [ ] Skill↔MCP matrix complete for task"),
    ("- [ ] Keine Secrets in Chat oder PR-Beschreibung", "- [ ] No secrets in chat or PR description"),
    ("- Pipeline-Secrets nie in den Chat spiegeln.", "- Never mirror pipeline secrets into chat."),
    ("- Write-Tools (PR merge, workflow_dispatch) nur mit approval.", "- Write tools (PR merge, workflow_dispatch) only with approval."),
    ("- Fine-grained PAT auf nötige Repos beschränken.", "- Limit fine-grained PAT to needed repos."),
    ("- MCP-Log-Größe truncated — gh CLI als Fallback.", "- MCP log size truncated—gh CLI as fallback."),
    ("- Zwei GitHub-MCPs parallel — doppelte Tool-Schemas, langsamer Agent.", "- Two GitHub MCPs in parallel—duplicate tool schemas, slower agent."),
    ("- `workflow_dispatch` aus Agent ohne Policy — versehentlicher Prod-Deploy.", "- `workflow_dispatch` from agent without policy—accidental prod deploy."),
    ("- Fork-PR-Kontext: MCP sieht andere Permissions als Maintainer-Branch.", "- Fork PR context: MCP sees different permissions than maintainer branch."),
    ("(data-analytics/daten-python-pandas-eda)", "(data-analytics/data-python-pandas-eda)"),
    ("category: spreadsheets-analyse", "category: spreadsheets-analysis"),
]

def main() -> None:
    n = 0
    for root in TARGETS:
        for p in root.rglob("*.md"):
            t = p.read_text(encoding="utf-8")
            orig = t
            for a, b in sorted(PHRASES, key=lambda x: -len(x[0])):
                t = t.replace(a, b)
            if t != orig:
                p.write_text(t, encoding="utf-8")
                n += 1
    print(f"updated {n} files, {len(PHRASES)} phrases")


if __name__ == "__main__":
    main()