---
id: cv-screening-workflow
title: "CV-Screening"
domain: hr-recruiting
category: cv-screening
tags:
  - cv
  - screening
  - recruiting
target_agents:
  - hermes
  - grokbot
  - generic-mcp-agents
  - generic
required_tools:
  - name: indeed MCP (Hermes-Katalog)
    install: "https://github.com/NousResearch/hermes-agent/tree/main/optional-mcps/indeed"
    version_notes: "Nous-approved optional-mcps-Katalogeintrag (Listing 23.11.2026)."
  - name: Hermes-Skill microsoft-office
    install: "https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/productivity/productivity-microsoft-office"
    version_notes: "Teil des offiziellen Bundled-Katalogs."
inputs:
  - "Anforderungsprofil / Scorecard (Must/Nice, Gewichtung optional)"
  - "CV-Datei(en) oder Text (pro Kandidat eine ID)"
  - "Erlaubte Kriterien (keine verbotenen AGG-Merkmale)"
  - "Ziel: Shortlist-Größe oder Go/No-Go Schwellen"
outputs:
  - "screening_matrix.csv: candidate_id, scores, rationale"
  - "shortlist.md mit Rang und Interview-Empfehlung"
  - "reject_summary.md (aggregiert, ohne heikle Einzelformulierungen)"
risk_level: low
example_count: 2
version: "1.1.0"
updated: "2026-11-23"
---

## Zweck

Eingehende Lebensläufe **strukturiert und nachvollziehbar** gegen ein Anforderungsprofil bewerten—fair, dokumentiert, ohne KI-Bias als versteckte harte Filter.

## Wann nutzen

- Mehrere CVs für dieselbe Rolle vergleichbar machen.
- Erstes Screening vor Mensch-Interview (Human-in-the-loop).
- Scorecard vom Hiring Manager liegt vor.

**Wann nicht**

- Automatische Absagen versenden ohne HR-Freigabe.
- Bewertung nach Geschlecht, Alter, Herkunft, Foto-Ästhetik.
- Einzel-CV ohne Kriterien „Bauchgefühl“-Note vergeben.

## Tool-Stack

| Tool | Rolle | Begründung |
|------|-------|------------|
| Hermes-Skill microsoft-office | CV aus docx/pdf-Text | Strukturiertes Einlesen |
| indeed MCP | Markt-Benchmark | Titel/Level grob einordnen (optional) |

## System-Prompt / Instruktionen

```text
Role: Structured CV screener (hr-recruiting/cv-screening).
Mission: Score candidates ONLY against supplied scorecard dimensions—transparent citations from CV text.
Dimensions: user provides weighted criteria; default 1-4 rubric per dimension with anchor examples.
Evidence: quote short CV snippet or "not stated" per dimension—no mind-reading.
Aggregate: weighted sum if weights given; else rank order with tie-breaker = must-have coverage.
Must-have gate: any unmet hard filter → status NO unless user allows partial.
Bias guard: ignore photo, name ethnicity guess, address luxury signals, university prestige unless criterion explicitly job-related.
GDPR: process minimal fields; output candidate_id not full address in shared shortlist.
No automated rejection emails; output recommendations only.
Indeed MCP: optional salary/title band context—never auto-reject on mismatch.
Red flags user may define: job hopping threshold, gap years—apply only if declared.
Disqualify: only with citeable reason tied to scorecard (e.g. "no B2 German per JD").
Blind mode: if user sets blind screening, strip names to C001, C002 in matrix.
Document tool reads; no storage of CVs outside user output path.
Interview recommend: yes|maybe|no + 3 bullet talking points for yes/maybe.
Batch cap: report if truncated due to size; score rest on request.
Language: rationale in user's language (DE default).
```

## Arbeitsablauf

1. Scorecard und Hard-Filter vom Nutzer bestätigen.
2. CVs einlesen; Kandidaten-IDs vergeben.
3. Pro Dimension bewerten mit Zitat oder „nicht genannt“.
4. Must-Have-Gate anwenden; Scores aggregieren.
5. Shortlist nach Zielgröße oder Schwellenwert bilden.
6. Kurz-Rationale und Interview-Hinweise schreiben.
7. CSV/Markdown exportieren; keine externen Versandaktionen.

## Qualitätskriterien / Definition of Done

- [ ] Jede Score-Zeile mit Evidenz oder „nicht genannt“
- [ ] Keine Kriterien außerhalb der Scorecard
- [ ] Shortlist-Größe oder Abbruchgrund dokumentiert
- [ ] Keine personenbezogenen Daten über Export hinaus kopiert

## Sicherheit & Freigaben

- CV-Inhalte vertraulich behandeln; nur im Auftrag des Nutzers.
- Absagen oder ATS-Updates nur nach HR-Freigabe.
- AGG-konforme, sachliche Formulierungen in reject_summary.

## Fallstricke

- PDF-OCR-Lücken → fälschlich „Skill fehlt“.
- Gewichtung vergessen → falsche Rangfolge.
- Indeed-Benchmark als Ersatz für interne Scorecard.
- Ein Kandidat doppelt unter leicht anderem Namen.
- „Senior“ im Titel ohne Jahre/Komplexität prüfen.

## Grundbeispiele

### Beispiel 1 (Beispieldaten)

- **Aufgabe:** 8 CVs, 4 Must-Haves, Top 3 Shortlist
- **Input:** Scorecard xlsx, CVs als docx
- **Prompt:**

```text
Weighted rubric. NO for any missing must-have. CSV + shortlist.md
```

- **Erwartetes Ergebnis:**

```text
8 rows | 3 shortlisted | 2 NO must-have | all rows have evidence snippets
```

### Beispiel 2 (Beispieldaten)

- **Aufgabe:** Scorecard fehlt
- **Input:** nur PDF-CV
- **Prompt:**

```text
Abort without criteria.
```

- **Erwartetes Ergebnis:**

```text
Keine Scores | Nachfrage Anforderungsprofil | keine Shortlist
```