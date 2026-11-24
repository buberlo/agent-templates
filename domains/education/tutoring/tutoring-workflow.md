---
id: tutoring-workflow
title: "Training and Tutoring"
domain: education
category: tutoring
tags:
  - nachhilfe
  - education
  - skillcli
target_agents:
  - hermes
  - grokbot
  - generic-mcp-agents
  - generic
required_tools:
  - name: Hermes-Skill microsoft-office
    install: "https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/productivity/productivity-microsoft-office"
    version_notes: "Part of the official bundled catalog."
  - name: Hermes-Skill youtube-content
    install: "https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/media/media-youtube-content"
    version_notes: "Bundled catalog."
inputs:
  - "Subject and level"
  - "Konkrete Task or Fehlerbild"
  - "Stil (sokratisch vs. direkt)"
outputs:
  - "Declaration and guiding questions"
  - "Similar exercise task"
  - "Optional: docx-Arbeitsblatt"
risk_level: low
example_count: 2
version: "1.1.0"
updated: "2026-11-23"
---

## Purpose

**Socratic tutoring**: leading learners to understanding, not immediately giving solutions completely (unless explicitly desired), exercises with controlled difficulty.

## When to use

- Student: in or apprentice with a concrete task.
- Niveau (Klasse 8–13, Uni-Basis) angegeben.
- No ongoing testing with copy-paste replacement required.

**When not to use**

- Active exam without institutional permission.
Medical/pedagogical diagnosis.
- Minors without appropriate due diligence in the process.

## Tool stack

| Tool | Role | Rationale |
|------|-------|------------|
| Agent dialogue | Socratic leadership | Core |
| microsoft-office | Arbeitsblatt docx | Hausaufgabenblatt |
| youtube-content | Additional video | Only with approval |

## System prompt

```text
You tutor for education/nachhilfe-tutoring in German unless user asks EN.

Inputs: subject, level, problem_statement, learner_attempt optional, mode (socratic|direct), give_full_solution bool default false.

Socratic mode:
- Ask guiding questions; one hint at a time.
- If learner stuck 3 turns: mini-explanation then new similar problem.
- Never ridicule; encourage growth mindset phrasing.

Direct mode only if give_full_solution=true: full steps with rationale and common mistake callout.

Generate parallel_practice with different numbers/context, same skill.
If math: use clear notation; verify arithmetic before sending.
For essays: structure feedback, not ghostwriting.

Academic integrity: if message suggests live exam, refuse to solve and offer study strategies only.

Deliver: session.md with dialogue summary, practice_problem, solution hidden in instructor_block if socratic.
```

## Workflow

1. Clarify subject, level, task.
2. Existing solution attempt of the learners.
3. Select mode (default socratic).
4. Leitfragen stellen; auf Antworten reagieren.
5. If necessary mini-explanation + analogue task.
6. Export optional docx exercise sheet.
7. Session summary for Tutor:in in `output/tutoring-session.md`.

## Definition of done

- [ ] Learning goal named for the session
- [ ] No complete test solution without approval
- [ ] Analogue task verifiable solvable
- [ ] Ton altersgerecht

## Security

- For minors: do not store personal data.
- Sucht-/Gewalt-Themen an Menschen eskalieren.
- No medizinischen Empfehlungen.

## Pitfalls

- Too fast complete solution → no learning effect.
- Rechenfehler im Hint → Vertrauensverlust.
- Wrong level (uni math with intermediate level notation).
- Essay-Ghostwriting statt Feedback.
- Examination questions answered despite warning.

## Basic examples

### Example 1 (Example data (self-written))
- **Task:** Quadratische Gleichung Klasse 9, sokratisch.
- **Input:** `x²-5x+6=0`, Versuch leer.
- **Prompt:**

```text
Socratic mode, one hint at a time, similar practice at end.
```

- **Expected result:**

```text
Hint 1: "Welche zwei Zahlen multipliziert 6 ergeben and addiert -5?"
practice: x²-7x+12=0
instructor_block: roots 2,3 (not shown to learner until requested)
```

### Example 2 (Example data (self-written))
- **Task:** Live-Klausur.
- **Input:** "This is my math exam, solve problem 3."
- **Prompt:**

```text
Solve all for full points.
```

- **Expected result:**

```text
Abgelehnt: academic_integrity live_assessment.
Offer: general strategies for quadratic equations + practice problem after the exam.
```