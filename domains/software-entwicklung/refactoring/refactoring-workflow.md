---
id: refactoring-workflow
title: "Refactoring"
domain: software-entwicklung
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

## Zweck

Strukturverbesserungen **ohne Verhaltensänderung** — Tests grün vor/nach, kleine Commits, messbare Komplexitätsreduktion.

## Wann nutzen

- Legacy-Modul entflechten, Duplikate entfernen.
- Benennung und Extract Method vor Feature.

**Wann nicht:** Refactor + Feature-Mix in einem PR ohne Trennung.

## Tool-Stack

| Tool | Rolle | Begründung |
|------|-------|------------|
| tests | Safety | must stay green |
| git | Steps | commit per step |
| coverage | optional | should not drop |

## System-Prompt / Instruktionen

```text
Refactoring workflow (software-entwicklung/refactoring).

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

## Arbeitsablauf

1. Baseline tests: `npm test` / `pytest`.
2. Scope-Dateien listen; non-goals fixieren.
3. Characterization test wenn Lücke.
4. Refactor Schritt 1; tests.
5. Schritt 2; tests.
6. Optional metrics.
7. PR nur Refactor-Label.

## Qualitätskriterien / Definition of Done

- [ ] Tests vor/nach grün
- [ ] Kein Feature-Verhalten geändert
- [ ] Diff lesbar segmentiert

## Sicherheit & Freigaben

- Security-sensitive Module: extra review.

## Fallstricke

- Refactor ohne Tests — Regression.
- Riesiger Rename PR unreviewable.
- Semantik geändert bei „cleanup“.
- Performance-Regression durch Extra-Indirection.
- Package public exports broken.

## Grundbeispiele

### Beispiel 1 (Beispieldaten)

- **Aufgabe:** Extract payment validator.
- **Input:** checkout.ts 800 LOC.
- **Prompt:**

```text
Extract validatePayment; tests green each step; no behavior change.
```

- **Erwartetes Ergebnis:**

```bash
npm test
git log --oneline -3
# extract validator, adjust imports, tests pass each
```

### Beispiel 2 (Beispieldaten)

- **Aufgabe:** Rename confusing vars module-wide.
- **Input:** analytics module.
- **Prompt:**

```text
Rename only in analytics/; single commit; full test suite.
```

- **Erwartetes Ergebnis:**

```bash
pytest
# diff only rename, grep no oldSymbol left
```