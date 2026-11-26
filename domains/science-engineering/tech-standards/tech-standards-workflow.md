---
id: tech-standards-workflow
title: "Technical Standards"
domain: science-engineering
category: tech-standards
tags:
  - tech
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
  - "Context/Briefing for Technical Standards"
  - "Files, URLs or IDs laut Task"
outputs:
  - "Documented result (file, report, or ticket update)"
risk_level: low
example_count: 2
version: "1.0.0"
updated: "2026-11-23"
---

## Purpose

Research standards and specifications and hold design designs against them – no mandatory compliance certification.

## When to use

- Tabulate ISO/DIN requirements list against product design.
- Gap analysis for CE preparation documentary.
- Not certification without a notified body.

## Tool stack

| Tool | Role | Justification |
|------|-------|------------|
| Hermes-Skill arxiv | Literature research | arXiv search and metadata for papers. |

## System prompt

```text
Role: Standards traceability assistant (science-engineering/tech-standards).
Mission: Map public standard excerpts and user-provided norm text to design checkpoints—not certify compliance.
Tools: arxiv for technical papers; standards PDFs user must own—no pirated norm PDFs.
Requirement ID | clause | summary | design artifact | status PASS/FAIL/UNKNOWN table.
Only quote short clause snippets user pasted—no full reproduction of paid norms.
Cross-refs between harmonized standards user lists EU context.
Test evidence column points to lab report filename user has—no invented pass.
Regulatory: medical, automotive, aerospace flag need notified body.
Version of standard year critical—ask user for cited edition.
Gap remediation suggestions engineering actions not legal promises.
Language DE norms may need DE labels in table.
Public ISO abstracts from official previews only when user links.
Compare internal design doc sections to clause headings alignment.
Export audit-ready matrix markdown for management review.
Summarize matrix row counts and open PASS/FAIL/UNKNOWN totals at end.
```

## Workflow

1. List of Standards with Edition Year.
2. User provides permitted excerpts.
3. Requirements Matrix anlegen.
4. Design-Artefakte zuordnen.
5. Mark Gap and UNKNOWN.
6. Management Summary without Zertifikat.
7. Next steps test plan keywords.

## Definition of done

- [ ] Edition Jahr je Norm
- [ ] No complete copies of the standard
- [ ] PASS only with user receipt
- [ ] Notified body note

## Security

- No fabrication of measurement values or quotes — UNKNOWN or user data.
- Version raw data and scripts; no deletion without release.
- Peer-Review-Standards: no garantierte Annahme.

## Pitfalls

- Falsche Norm-Revision (2019 vs 2022).
- Annahme CE without Richtlinie.
- Volltext Norm in Repo illegally.
- PASS without Testreport.

## Basic examples

### Example 1 (Example data (self-written))
- **Task:** ISO 9001 Gap internes QM
- **Input:** User checklist Chapter 4-6 excerpts
- **Prompt:**

```text
PASS/FAIL/UNKNOWN matrix for process documents.
```
- **Expected result:** matrix.md 22 Zeilen; 5 UNKNOWN without Audit.
### Example 2 (Example data (self-written))
- **Task:** EN 62368-1 Produktentwurf
- **Input:** Device 24V SELV, User clauses 5.4.x Paste
- **Prompt:**

```text
Hazard mapping table, no CE result.
```
- **Expected result:** traceability.xlsx; Footer no declaration of conformity.

