---
id: testing-workflow
title: "Testing"
domain: software-development
category: testing
tags:
  - testing
  - playwright
  - pytest
target_agents:
  - hermes
  - claude-code
  - cursor
  - generic-mcp-agents
required_tools:
  - name: playwright
    install: "npm init playwright@latest"
    version_notes: "CLI preferred for CI"
  - name: pytest
    install: "pip: pytest"
    version_notes: "Python stacks"
  - name: npm test
    install: "package.json scripts"
    version_notes: "vitest/jest"
inputs:
  - "Test scope (unit/e2e)"
  - "URLs or Modulpfade"
outputs:
  - "Green Tests or Failure Report"
  - "playwright.config / test files"
risk_level: low
example_count: 3
version: "1.0.0"
updated: "2026-11-23"
---

## Purpose

Write unit, integration and E2E tests and run them with **Playwright CLI** / Project Runner — reproducible, not just MCP snapshots.

## When to use

- Feature needs a regression test before merge.
- Flaky E2E stabilisieren.

**When not:** load test without dedicated tooling.

## Tool stack

| Tool | Role | Justification |
|------|-------|------------|
| playwright | E2E | `npx playwright test` |
| pytest | Backend | `pytest -q` |
| vitest/jest | Unit | `npm test` |

## System prompt

```text
Testing workflow (software-development/testing).

Prefer Playwright CLI over Playwright MCP for CI parity and lower token cost.
Unit first: pytest or npm test before adding E2E.
Playwright: npx playwright test --project=chromium; use data-testid selectors.
Generate tests: npx playwright codegen only locally with user consent for target URL.
Flake fixes: await expect with timeout, no bare sleep except documented.
Record trace on failure: --trace on-first-retry in config suggestion.
Never run tests against prod URLs unless user names allowlisted staging URL.
Snapshot updates: npx playwright test --update-snapshots only after visual approval.
Collect: failure screenshot path from test-results/.
Do not disable tests instead of fixing without noting tech debt.
Coverage optional; focus on behavior assertions.
Document commands run in thread.
```

## Workflow

1. Test-Runner ermitteln: `cat package.json` / `pyproject.toml`.
2. Unit: `pytest -q` or `npm test`.
3. Install Playwright: `npx playwright install chromium` if missing.
4. Write spec under `tests/e2e/`.
5. `npx playwright test tests/e2e/checkout.spec.ts`.
6. On failure: `npx playwright show-report`.
7. Add CI snippet for GitHub Actions.

## Definition of done

- [ ] Tests locally green
- [ ] No hardcoded prod URLs
- [ ] Flake-Retry-Policy in config

## Security

- No Credentials in committed test files.
- Playwright against internal apps only with VPN hint.

## Pitfalls

- Playwright MCP-only — expensive and unlike CI.
- codeging against Prod - data change.
- waitForTimeout statt expect — flaky.
- Parallel workers + shared DB — isolation fehlt.
- --update-snapshots unreviewed — visuelle Regression.

## Basic examples

### Example 1 (Example data (self-written))
- **Task:** Login E2E staging.
- **Input:** `https://staging.example.com`.
- **Prompt:**

```text
Add playwright spec for login; run headed once then headless; no MCP.
```

- **Expected result:**

```bash
npx playwright test tests/e2e/login.spec.ts --project=chromium
# 1 passed
```

### Example 2 (Example data (self-written))
- **Task:** pytest API smoke.
- **Input:** `tests/api/`.
- **Prompt:**

```text
pytest -q; add test for 401 on missing token.
```

- **Expected result:**

```bash
pytest -q tests/api/
# .... 12 passed
```

### Example 3 (Example data (self-written))
- **Task:** CLI vs MCP Tokenkosten.
- **Input:** reine Extraktion vs. App-E2E.
- **Prompt:**

```text
Recommend playwright CLI for CI e2e; MCP only for interactive debug session.
```

- **Expected result:**

```text
CI: npx playwright test
Debug: optional Playwright MCP with narrow snapshot scope
```