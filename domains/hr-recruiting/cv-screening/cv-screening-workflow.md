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
  - name: indeed MCP (Hermes catalog)
    install: "https://github.com/NousResearch/hermes-agent/tree/main/optional-mcps/indeed"
    version_notes: "Nous-approved optional-mcps-catalog entry (listing 2026-11-23)."
  - name: Hermes-Skill microsoft-office
    install: "https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/productivity/productivity-microsoft-office"
    version_notes: "Part of the official bundled catalog."
inputs:
  - "Requirements profile/scorecard (must/nice, weighting optional)"
  - "CV file(s) or text (one ID per candidate)"
  - "Permitted criteria (no prohibited characteristics under the General Act on Equal Treatment (AGG))"
  - "Target: Shortlist size or go/no-go thresholds"
outputs:
  - "screening_matrix.csv: candidate_id, scores, rationale"
  - "shortlist.md with ranking and interview recommendation"
  - "reject_summary.md (aggregated, without sensitive individual wording)"
risk_level: low
example_count: 2
version: "1.1.0"
updated: "2026-11-23"
---

## Purpose

Evaluate incoming CVs **in a structured and transparent manner** against a job specification – fairly, with documentation, and without AI bias as a hidden hard filter.

## When to use

- Make it possible to compare several CVs for the same role.
- First screening before human interview (human-in-the-loop).
- The hiring manager's scorecard is available.

**When not to use**

- Send automatic rejections without HR approval.
- Evaluation based on gender, age, origin, photo aesthetics.
- Individual CVs are rated without criteria, based on "gut feeling".

## Tool stack

| Tool | Role | Rationale |
|------|-------|------------|
| Hermes skill Microsoft Office | CV from docx/pdf text | Structured import |
| indeed MCP | Markt-Benchmark | Titel/Level grob einordnen (optional) |

## System prompt

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

## Workflow

1. Have the user confirm the scorecard and hard filters.
2. CVs einlesen; Kandidaten-IDs vergeben.
3. Rate each dimension with a quote or "not mentioned".
4. Must-Have-Gate anwenden; Scores aggregieren.
5. Create a shortlist based on the target size or threshold.
6. Write brief rationales and interview notes.
7. Export CSV/Markdown; no external dispatch actions.

## Definition of done

- [ ] Each score line with evidence or "not mentioned"
- [ ] No criteria outside the scorecard
- [ ] Shortlist size or reason for discontinuation documented
- [ ] No personal data copied beyond the export

## Security

- Treat CV content confidentially; only on behalf of the user.
- Rejections or ATS updates only after HR approval.
- AGG-konforme, sachliche Formulierungen in reject_summary.

## Pitfalls

- PDF OCR gaps → incorrectly "Skill missing".
- Gewichtung vergessen → falsche Rangfolge.
- Indeed benchmark as a replacement for the internal scorecard.
- A candidate appears twice under slightly different names.
- Check "Senior" in the title without years/complexity.

## Basic examples

### Example 1 (Example data)

- **Task:** 8 CVs, 4 Must-Haves, Top 3 Shortlist
- **Input:** Scorecard xlsx, CVs as docx
- **Prompt:**

```text
Weighted rubric. NO for any missing must-have. CSV + shortlist.md
```

- **Expected result:**

```text
8 rows | 3 shortlisted | 2 NO must-have | all rows have evidence snippets
```

### Example 2 (Example data)

- **Task:** Scorecard fehlt
- **Input:** PDF CV only
- **Prompt:**

```text
Abort without criteria.
```

- **Expected result:**

```text
No scores | request requirements profile | no shortlist
```
