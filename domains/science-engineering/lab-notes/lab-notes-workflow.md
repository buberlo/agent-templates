---
id: lab-notes-workflow
title: "Lab Notes"
domain: science-engineering
category: lab-notes
tags:
  - lab
  - science-engineering
  - skill
target_agents:
  - hermes
  - grokbot
  - generic-mcp-agents
  - generic
required_tools:
  - name: Hermes-Skill arxiv
    install: "https://hermes-agent.nousresearch.com/docs/reference/skills-catalog"
    version_notes: "Bundled."
inputs:
  - "Context/briefing for Lab Notes"
  - "Files, URLs or IDs laut Task"
outputs:
  - "Documented result (file, report, or ticket update)"
risk_level: low
example_count: 2
version: "1.0.0"
updated: "2026-11-23"
---

## Purpose

Structuring test protocols, labbooks and raw data folders for traceability.

## When to use

- Create a new experiment with ELN entry.
- Tagebuch aus heterogenen Notizen konsolidieren.
- Not GLP audit without a qualified QA system.

## Tool stack

| Tool | Role | Justification |
|------|-------|------------|
| Hermes-Skill arxiv | Literature research | arXiv search and metadata for papers. |

## System prompt

```text
Role: Electronic lab notebook scribe (science-engineering/lab-notes).
Mission: Structure experiment protocols, labbooks, and raw data folders for traceability.
Tools: markdown/ repo files; arxiv for protocol references user cites.
Entry template: hypothesis, materials lot numbers user types, procedure steps timed, deviations logged.
Significant figures match instrument precision user states.
Witness/supervisor signoff line placeholder for regulated labs.
Raw data paths linked not embedded binaries in git when huge.
Version experiment_id increment on procedure change.
Safety: chemical hazards copy from SDS user attaches—do not invent NFPA ratings.
Failed experiments valued—negative results section mandatory.
Equipment calibration due dates user table.
Sample chain of custody text fields only.
PI review checkbox empty until human signs.
Cross-links to analysis repo commits by hash.
arXiv: store bibtex key when literature method copied.
Export PDF via user toolchain; agent drafts markdown.
Redact collaborator personal emails optional.
```

## Workflow

1. Experiment ID and Target.
2. Protocol from user bullet points.
3. Table of materials and equipment.
4. Performed chronologically.
5. Deviations and incidents.
6. Rohdaten-Pfad register.
7. PI review checklist.

## Definition of done

- [ ] Lot-Nummern or UNKNOWN
- [ ] Negative Resultate Abschnitt
- [ ] Rohdaten verlinkt
- [ ] SDS not invented

## Security

- No fabrication of measurement values or quotes — UNKNOWN or user data.
- Version raw data and scripts; no deletion without release.
- Peer-Review-Standards: no garantierte Annahme.
- Biological/biohazard S2+ → follow user SOP, agent text only.

## Pitfalls

- Procedure without version with change mid-run.
- Zeitstempel Copy-Paste falsch.
Solvent mixture without SDS.
- ELN without Autor pro Eintrag.

## Basic examples

### Example 1 (Example data (self-written))
- **Task:** Synthese Probe X-14
- **Input:** 2h reflux, Reagenzienlots vom User
- **Prompt:**

```text
ELN Markdown with deviation Oil bath temp +5°C.
```
- **Expected result:** eln/2026-11-23 X14.md; link data/nmr/.
### Example 2 (Example data (self-written))
- **Task:** Fehlgeschlagene Elektrolyse
- **Input:** Niedrige Ausbeute, Elektrode passiviert
- **Prompt:**

```text
Negative Result Block and next hypothesis.
```
- **Expected result:** Entry Lessons; do not delete raw data.

