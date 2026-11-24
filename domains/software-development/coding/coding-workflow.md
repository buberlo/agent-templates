---
id: coding-workflow
title: "Coding"
domain: software-development
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
  - "Issue/Story and acceptance criteria"
  - "Affected files"
outputs:
  - "Diff with tests"
  - "Run commands log"
risk_level: low
example_count: 2
version: "1.0.0"
updated: "2026-11-23"
---
## Purpose

Implement features and bug fixes in the repo: smallest meaningful diff, run tests, conventions of the project.

## When to use

- Implementation nach Spec or Issue.
- Lokale Reproduktion eines Bugs.

**When not:** Large architectural conversion without ADR.

## Tool stack

| Tool | Role | Justification |
|------|-------|------------|
| git | Branch/commit | traceability |
| npm/pytest/cargo test | Verify | project default |
| gh | optional | link PR |

## System prompt

```text
General coding workflow (software-development/coding).

You are a careful assistant for this workflow. You work read-first by default and you must not run destructive or production changes until the user confirms the approval gate named in their request.
When you propose a change, you must include a short rollback or undo path and you must tie the plan to the ticket or briefing reference when the user provides one.
If the request is ambiguous, you must ask one clarifying question before you draft commands, content, or configuration.
You must label every external write step with the approval phrase from the workflow section before you describe how to execute it.
You must keep chat output concise and you must redact secrets, recovery codes, and private personal data from every response.


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
Do not push without user request.```

## Workflow

1. Issue/AC lesen; betroffene Module finden.
2. `git fetch && git switch -c feature/task-id main`.
3. Implementieren in kleinen Schritten.
4. `npm test` / `pytest` / `cargo test` lokal.
5. Lint/format per Projekt-Skript.
6. `git diff` review summary.
7. Push/PR only on request.

## Definition of done

- [ ] AC fulfilled
- [ ] Tests green
- [ ] Kein Scope-Creep

## Security

- No unsicheren Patterns (eval, SQL concat).

## Pitfalls

- Stilbruch im Monorepo.
- Fehlende Dependency im Manifest.
- Giant commit schwer zu reviewen.
- Tests nur happy path.
- Breaking change without Version bump.

## Basic examples

### Example 1 (Example data (self-written))
- **Task:** Bugfix Timeout in fetch.
- **Input:** Issue #12.
- **Prompt:**

```text
Fix retry logic in api/client.ts; add unit test; run npm test.
```

- **Expected result:**

```bash
Summary: the agent stays read-only until approval, lists concrete next steps, and marks any missing inputs the user must supply.Summary: the agent stays read-only until approval, lists concrete next steps, and marks any missing inputs the user must supply.npm test -- client.test.ts
# PASS
git diff api/client.ts
```

### Example 2 (Example data (self-written))
- **Task:** Feature Flag lesen.
- **Input:** env FEATURE_X.
- **Prompt:**

```text
Implement guarded code path; default off; document env in README snippet.
```

- **Expected result:**

```text
Summary: the agent stays read-only until approval, lists concrete next steps, and marks any missing inputs the user must supply.Summary: the agent stays read-only until approval, lists concrete next steps, and marks any missing inputs the user must supply.FEATURE_X default false; tests cover on/off
```