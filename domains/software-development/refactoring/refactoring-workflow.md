---
id: refactoring-workflow
title: "Refactoring"
domain: software-development
category: refactoring
tags:
  - refactoring
  - quality
target_agents:
  - hermes
  - claude-code
  - cursor
  - generic-mcp-agents
required_tools:
  - name: git
    install: "small commits"
    version_notes: "safety"
  - name: test runner
    install: "project default"
    version_notes: "safety net"
inputs:
  - "Refactor scope (module/file)"
  - "Non-goals"
outputs:
  - "Behavior-preserving diff"
  - "Metrics before/after optional"
risk_level: low
example_count: 2
version: "1.0.0"
updated: "2026-11-23"
---

## Purpose

Structural improvements **without behavioral change** — green before/after tests, small commits, measurable complexity reduction.

## When to use

- Legacy-Modul entflechten, Duplikate entfernen.
- Naming and extract method before feature.

**When not:** Refactor + Feature mix in a PR without separation.

## Tool stack

| Tool | Role | Justification |
|------|-------|------------|
| tests | Safety | must stay green |
| git | Steps | commit per step |
| coverage | optional | should not drop |

## System prompt

```text
Refactoring workflow (software-development/refactoring).

Run full test suite baseline before changes; same command after each logical step.
One refactoring technique per commit when possible: rename, extract, move.
No behavior change; if bug found, separate bugfix PR.
Avoid refactor while tests red; fix tests first or scope down.
Public API surface: deprecate don't break without version plan.
Remove dead code only with coverage or usage proof.
Measure: cyclomatic complexity or file LOC before/after optional.
No drive-by formatting entire repo.
Document intent in PR: why easier to change.
If tests missing, add characterization tests before refactor.
Stop if scope expands; propose follow-up issue.
```

## Workflow

1. Baseline tests: `npm test` / `pytest`.
2. Scope-Files listen; non-goals fixieren.
3. Characterization test if gap.
4. Refactor Schritt 1; tests.
5. Schritt 2; tests.
6. Optional metrics.
7. PR nur Refactor-Label.

## Definition of done

- [ ] Tests before/after green
- [ ] No feature behavior changed
- [ ] Diff lesbar segmentiert

## Security

- Security-sensitive Module: extra review.

## Pitfalls

- Refactor without Tests — Regression.
- Riesiger Rename PR unreviewable.
- Semantics changed at "cleanup".
- Performance-Regression durch Extra-Indirection.
- Package public exports broken.

## Basic examples

### Example 1 (Example data)

- **Task:** Extract payment validator.
- **Input:** checkout.ts 800 LOC.
- **Prompt:**

```text
Extract validatePayment; tests green each step; no behavior change.
```

- **Expected result:**

```bash
npm test
git log --oneline -3
# extract validator, adjust imports, tests pass each
```

### Example 2 (Example data)

- **Task:** Rename confusing vars module-wide.
- **Input:** analytics module.
- **Prompt:**

```text
Rename only in analytics/; single commit; full test suite.
```

- **Expected result:**

```bash
pytest
# diff only rename, grep no oldSymbol left
```