---
id: coding-workflow
title: "Coding"
domain: software-entwicklung
category: coding
tags:
  - coding
  - implementation
target_agents:
  - hermes
  - claude-code
  - cursor
  - generic-mcp-agents
required_tools:
  - name: git
    install: "version control"
    version_notes: "feature branches"
  - name: project-toolchain
    install: "npm/pnpm/cargo/go per repo"
    version_notes: "read package.json first"
inputs:
  - "Issue/Story und Akzeptanzkriterien"
  - "Betroffene Dateien"
outputs:
  - "Diff mit Tests"
  - "Run commands log"
risk_level: low
example_count: 2
version: "1.0.0"
updated: "2026-11-23"
---

## Zweck

Features und Bugfixes im Repo umsetzen: kleinster sinnvoller Diff, Tests laufen, Konventionen des Projekts.

## Wann nutzen

- Implementierung nach Spec oder Issue.
- Lokale Reproduktion eines Bugs.

**Wann nicht:** Große Architektur-Umstellung ohne ADR.

## Tool-Stack

| Tool | Rolle | Begründung |
|------|-------|------------|
| git | Branch/commit | traceability |
| npm/pytest/cargo test | Verify | project default |
| gh | optional | link PR |

## System-Prompt / Instruktionen

```text
General coding workflow (software-entwicklung/coding).

Read neighboring files before editing; match style, naming, imports.
Smallest diff that satisfies acceptance criteria; no unrelated refactors.
Run project formatter/linter if configured before declaring done.
Tests: add or update tests for behavior change; run full suite if fast else targeted.
Never commit secrets, .env, credentials.
If type errors, fix root cause not blanket any casts.
Document public API changes in changelog or docstring.
Branch from updated main: git fetch && git switch -c feature/x.
Commit messages: conventional commits if repo uses them.
Ask if requirements ambiguous; list assumptions.
Output: files changed, commands run, test summary.
Do not push without user request.
```

## Arbeitsablauf

1. Issue/AC lesen; betroffene Module finden.
2. `git fetch && git switch -c feature/task-id main`.
3. Implementieren in kleinen Schritten.
4. `npm test` / `pytest` / `cargo test` lokal.
5. Lint/format per Projekt-Skript.
6. `git diff` review summary.
7. Push/PR nur auf Wunsch.

## Qualitätskriterien / Definition of Done

- [ ] AC erfüllt
- [ ] Tests grün
- [ ] Kein Scope-Creep

## Sicherheit & Freigaben

- Keine unsicheren Patterns (eval, SQL concat).

## Fallstricke

- Stilbruch im Monorepo.
- Fehlende Dependency im Manifest.
- Giant commit schwer zu reviewen.
- Tests nur happy path.
- Breaking change ohne Version bump.

## Grundbeispiele

### Beispiel 1 (Beispieldaten)

- **Aufgabe:** Bugfix Timeout in fetch.
- **Input:** Issue #12.
- **Prompt:**

```text
Fix retry logic in api/client.ts; add unit test; run npm test.
```

- **Erwartetes Ergebnis:**

```bash
npm test -- client.test.ts
# PASS
git diff api/client.ts
```

### Beispiel 2 (Beispieldaten)

- **Aufgabe:** Feature Flag lesen.
- **Input:** env FEATURE_X.
- **Prompt:**

```text
Implement guarded code path; default off; document env in README snippet.
```

- **Erwartetes Ergebnis:**

```text
FEATURE_X default false; tests cover on/off
```