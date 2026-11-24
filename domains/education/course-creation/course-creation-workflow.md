---
id: course-creation-workflow
title: "Course creation"
domain: education
category: course-creation
tags:
  - courses
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
  - name: Hermes-Skill youtube-content
    install: "https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/media/media-youtube-content"
    version_notes: "Bundled catalog."
inputs:
  - "Topic, audience, duration"
  - "Learning objectives (measurable)"
  - "Sources and media"
outputs:
  - "Curriculum outline"
  - "Lessons (docx/md)"
  - "Slides (pptx)"
  - "Exercises with sample solutions (internal)"
risk_level: low
example_count: 3
version: "1.1.0"
updated: "2026-11-23"
---

## Purpose

**Curriculum from measurable learning objectives through lessons, exercises, and slides**—with mandatory citations and office skills for file-ready delivery.

## When to use

- New internal or customer course (workshop, e-learning module).
- Learning objectives and duration are known.
- docx/pptx skills or Hermes microsoft-office available.

**When not to use**

- University accreditation without subject-matter approval.
- Copyrighted third-party sources without a license.
- Exam content without item review by a subject expert.

## Tool stack

| Tool | Role | Rationale |
|------|-------|------------|
| Anthropic pptx/docx | Precise Office artifacts | Validators |
| Hermes microsoft-office | Offline python-docx/pptx | No Office install required |
| youtube-content | Source videos → outline | Transcript with source |

## System prompt

```text
You build courses for education/course-creation.

You are a careful assistant for this workflow. You work read-first by default and you must not run destructive or production changes until the user confirms the approval gate named in their request.
When you propose a change, you must include a short rollback or undo path and you must tie the plan to the ticket or briefing reference when the user provides one.
If the request is ambiguous, you must ask one clarifying question before you draft commands, content, or configuration.
You must label every external write step with the approval phrase from the workflow section before you describe how to execute it.
You must keep chat output concise and you must redact secrets, recovery codes, and private personal data from every response.


Inputs: topic, audience, duration_hours, modality (live|self_paced), language DE, source_urls[], bloom_level target.
Pipeline:
1) Write measurable learning objectives (3-6), each with verb from Bloom taxonomy.
2) Curriculum outline: modules, lesson titles, time boxes, prerequisites.
3) For each lesson: concept explanation, activity, formative check question, optional homework.
4) Exercises: include instructor_solution separate file, not in student pack if assessment.
5) Slides: one pptx deck per module, speaker notes, max 6 bullets per slide.
6) Cite all external facts with source_urls; mark UNSOURCED if missing.
7) Run office validate script on pptx when Anthropic skill available.
Do not plagiarize courseware sites verbatim.
Deliver: outline.md, lessons/*.md, slides/module-*.pptx paths, sources.bib.```

## Workflow

1. Align learning objectives with the user (SMART).
2. `outline.md` with modules and timings.
3. Lesson texts per module as Markdown.
4. Exercises + `instructor_solutions.md`.
5. Generate pptx per module; `validate.py` when available.
6. Complete `sources.bib`.
7. Package `output/course-<topic>/` for review.

## Definition of done

- [ ] Each learning objective mapped to a lesson/exercise
- [ ] pptx validated or manually reviewed
- [ ] Sources for external facts
- [ ] Assessments separate from participant materials

## Security

- No personal example data without consent.
- Early childhood education/medicine: human subject-matter expert required.
- LMS publish only after approval.

## Pitfalls

- Slides full of text instead of teaching.
- Exercises without solvability check.
- YouTube summary without timestamp verification.
- pptx validator skipped → broken layouts.
- Learning objectives not measurable.

## Basic examples

### Example 1 (Example data (self-written))
- **Task:** 2h workshop “API fundamentals”.
- **Input:** Beginner developers, DE.
- **Prompt:**

```text
Create outline + 3 lessons + 10-slide deck with speaker notes, cite REST docs only from provided URLs.
```

- **Expected result:**

```text
Summary: the agent stays read-only until approval, lists concrete next steps, and marks any missing inputs the user must supply.Summary: the agent stays read-only until approval, lists concrete next steps, and marks any missing inputs the user must supply.Objectives: 4 (e.g. "name REST verb", "read JSON error")
Files: outline.md, lessons/L1-L3.md, slides/module-1.pptx (10 slides)
sources.bib: 2 URLs
```

### Example 2 (Example data (self-written))
- **Task:** Missing audience.
- **Input:** Topic only "Kubernetes".
- **Prompt:**

```text
Build full course package.
```

- **Expected result:**

```text
Summary: the agent stays read-only until approval, lists concrete next steps, and marks any missing inputs the user must supply.Summary: the agent stays read-only until approval, lists concrete next steps, and marks any missing inputs the user must supply.Abort: audience and duration_hours required.
Follow-up: role (Dev/Ops)? duration? exam yes/no?
No pptx generated.
```

### Example 3 (Real-world example)

- **Task:** Short briefing deck; validate with Anthropic pptx skill.
- **Input:** Tutorial briefing as PowerPoint.
- **Prompt:**

```text
pptxgenjs 4.0.1, skills/pptx/scripts/office/validate.py, python-pptx for cross-check.
```

- **Expected result:**

```text
Summary: the agent stays read-only until approval, lists concrete next steps, and marks any missing inputs the user must supply.Summary: the agent stays read-only until approval, lists concrete next steps, and marks any missing inputs the user must supply.File briefing.pptx — Validator: All validations PASSED
3 slides 16x9, text + speaker notes
Source: https://aifrontierpost.com/articles/anthropic-official-agent-skills-tutorial/
```