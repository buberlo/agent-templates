---
id: course-creation-mcp-focus
title: "Course Creation: MCP/Skill Focus"
domain: education
category: course-creation
tags:
  - kurse
  - education
  - skill
target_agents:
  - hermes
  - grokbot
  - generic-mcp-agents
  - generic
required_tools:
  - name: Anthropic document skills (docx, pptx, xlsx, pdf)
    install: "https://github.com/anthropics/skills"
    version_notes: "199219 GitHub Stars"
  - name: Hermes-Skill microsoft-office
    install: "https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/productivity/productivity-microsoft-office"
    version_notes: "Part of the official bundled catalog."
inputs:
  - "Wanted output formats"
  - "Validator availability"
outputs:
  - "Skill selection and tooling doc"
  - "Probe-pptx Smoke-Test"
risk_level: low
example_count: 2
version: "1.1.0"
updated: "2026-11-23"
---

## Purpose

**Choose Office/Skill Stack for course material**: Anthropic document skills vs. Hermes microsoft office vs. YouTube sources—incl. Validators and Verify steps.

## When to use

- Agent setup for course production; Uncertainty which skill pptx generates.
- CI-style validation step before LMS upload.
- Minimal toolset against prompt leaks.

**When not to use**

- Write a concrete curriculum → `course-creation-workflow`.
- No Python/LibreOffice available for PDF readers and PDF required.

## Tool stack

| Tool | Role | Rationale |
|------|-------|------------|
| Anthropic pptx/docx | Validation | validate.py |
| Hermes microsoft-office | Offline Generierung | Bundled |
| youtube-content | Primary sources | Transcript import |

## System prompt

```text
You configure course authoring tools for education/course-creation.

Inputs: outputs_needed (pptx|docx|pdf|xlsx), host (claude_skills|hermes), run_validate bool.

Produce course-authoring-tooling.md:
- Primary generator per format with install path
- Validate commands: python skills/pptx/scripts/office/validate.py file.pptx OR hermes skill verify equivalent
- youtube-content: when to use fetch_transcript vs user-provided PDF
- Disable unused document MCPs

Require post-write verify: re-read file listing slide count or docx paragraph count.
Note: pptx hex colors without # per Anthropic skill docs; warn on off-slide coordinates.

Deliver smoke test: 1-slide pptx title "Tooling OK" and validation result line.
```

## Workflow

1. Write down required formats.
2. Anthropic vs. Hermes plugin capability.
3. Write `course-authoring-tooling.md`.
4. Mini-pptx erzeugen (1 Folie).
5. Execute validator if available.
6. YouTube-Skill Activate and video-sources
7. User Confirms Stack Before Course Creation

## Definition of done

- [ ] Ein Primary-Tool pro Ausgabeformat
- [ ] Validate- or Read-back-Schritt dokumentiert
- [ ] Smoke-pptx successful or error with fix
[ ] Unnecessary skills deactivated

## Security

Scripts from trusted markets (anthropics/skills, Hermes bundled).
- No Makros in generierten Office-Files.
External YouTube URLs only with userlist.

## Pitfalls

- Zwei pptx-Generatoren → inkonsistente Layouts.
- PDF via LibreOffice fehlt auf Host.
- Validator not in PATH.
- YouTube venv not prepared.
- Great Skills → Context Overflow.

## Basic examples

### Example 1 (Example data (self-written))
- **Task:** Hermes pptx only.
- **Input:** `outputs_needed=pptx`, hermes host.
- **Prompt:**

```text
Document tooling and run 1-slide smoke test with validate if available.
```

- **Expected result:**

```text
Primary: hermes microsoft-office → python-pptx
Smoke: tooling-smoke.pptx (1 slide)
Validate: SKIPPED (anthropic path not installed) | paragraphs counted via read-back
```

### Example 2 (Example data (self-written))
- **Task:** Anthropic validate Pfad.
- **Input:** claude_skills, run_validate true.
- **Prompt:**

```text
Configure anthropic pptx skill with validate.py command in tooling doc.
```

- **Expected result:**

```text
Validate cmd: python skills/pptx/scripts/office/validate.py <file.pptx>
Smoke: tooling-smoke.pptx → All validations PASSED
File: course-authoring-tooling.md
```