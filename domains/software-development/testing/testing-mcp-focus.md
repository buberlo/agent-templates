---
id: testing-mcp-focus
title: "Testing: MCP/Skill-Fokus"
domain: software-development
category: testing
tags:
  - testing
  - mcp
  - playwright
target_agents:
  - hermes
  - claude-code
  - cursor
  - generic-mcp-agents
required_tools:
  - name: Playwright MCP
    install: "https://github.com/microsoft/playwright-mcp"
    version_notes: "Debug; CLI for CI"
  - name: Chrome DevTools MCP
    install: "https://github.com/ChromeDevTools/chrome-devtools-mcp"
    version_notes: "Performance traces"
  - name: playwright CLI
    install: "npx playwright"
    version_notes: "Verify step in skill"
inputs:
  - "App URL (staging)"
  - "Skill TDD steps"
outputs:
  - "Skill↔MCP matrix"
  - "Exported playwright spec"
risk_level: low
example_count: 3
version: "1.0.0"
updated: "2026-11-23"
---

## Purpose

**Playwright MCP** for interactive debugging; Skill requires **CLI-Verify** (‘npx playwright test’) before Merge — MCP is not the only test source.

## When to use

- UI-Flow explorieren, danach Spec generieren.
- Performance spike with Chrome DevTools MCP.

**When not:** Pure API tests — pytest only.

## Tool stack

| Tool | Role | Justification |
|------|-------|------------|
| Playwright MCP | Explore | Snapshots teuer |
| playwright CLI | Verify | CI parity |
| TDD Skill | Reihenfolge | red-green-refactor |

## System prompt

```text
Testing MCP/Skill focus (software-development/testing).

Skill phases: explore (MCP optional) -> write spec file -> verify (CLI mandatory) -> commit.
Limit Playwright MCP turns; prefer codegen export to tests/e2e/*.spec.ts then CLI.
Chrome DevTools MCP only for perf/network diagnosis step, not default every test.
MCP snapshot token cost: warn when task is extract-only HTML.
Hermes TDD skill: failing test commit before implementation.
Never mark DoD complete without npx playwright test exit 0 locally or CI link.
Matrix: Step Explore | MCP browser; Step Verify | CLI only.
Disable Playwright MCP during CI agent job if duplicate.
Do not store credentials in MCP session prompts.
```

## Workflow

1. Skill-Matrix Explore vs Verify definieren.
2. Optional MCP: navigate staging login (read-only data).
3. Spec aus MCP/codegen in Repo schreiben.
4. `npx playwright test` — Skill Verify.
5. Bei Fail: trace `npx playwright show-trace`.
6. Unit-Tests parallel `npm test`.
7. PR with test plan.

## Definition of done

CLI playwright green
- [ ] MCP nur wo dokumentiert
- [ ] No Secrets in Specs

## Security

- Staging-URLs only default.
- MCP screenshots can post PII — not publicly.

## Pitfalls

- Nur MCP — no CI-Reproduzierbarkeit.
- Riesige A11y-Snapshots — Kontext voll.
- DevTools MCP auf Prod.
- Spec aus veralteter UI.

## Basic examples

### Example 1 (Example data)

- **Task:** Matrix Checkout-Flow.
- **Input:** staging shop.
- **Prompt:**

```text
MCP explore cart; write spec; npx playwright test verify.
```

- **Expected result:**

```text
tests/e2e/cart.spec.ts added
npx playwright test → 3 passed
```

### Example 2 (Example data)

- **Task:** MCP vermeiden bei API-only.
- **Input:** REST service.
- **Prompt:**

```text
pytest only skill; no Playwright MCP enabled.
```

- **Expected result:**

```bash
pytest -q
# MCP count 0
```

### Example 3 (Real-world example)

- **Task:** Performance regression.
- **Input:** langsame Dashboard-Ladezeit.
- **Prompt:**

```text
Chrome DevTools MCP trace one navigation; suggest test via CLI measureNavigationTiming.
```

- **Expected result:**

```text
LCP 4.2s flagged; add playwright performance assertion in spec
```