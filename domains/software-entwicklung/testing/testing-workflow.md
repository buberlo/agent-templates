---
id: testing-workflow
title: "Testing"
domain: software-entwicklung
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
    version_notes: "CLI bevorzugt für CI"
  - name: pytest
    install: "pip: pytest"
    version_notes: "Python stacks"
  - name: npm test
    install: "package.json scripts"
    version_notes: "vitest/jest"
inputs:
  - "Test scope (unit/e2e)"
  - "URLs oder Modulpfade"
outputs:
  - "Grüne Tests oder Failure-Report"
  - "playwright.config / test files"
risk_level: low
example_count: 3
version: "1.0.0"
updated: "2026-11-23"
---

## Zweck

Unit-, Integrations- und E2E-Tests schreiben und mit **Playwright CLI** / Projekt-Runner ausführen — reproduzierbar, nicht nur MCP-Snapshots.

## Wann nutzen

- Feature braucht Regression-Test vor Merge.
- Flaky E2E stabilisieren.

**Wann nicht:** Lasttest ohne dediziertes Tooling.

## Tool-Stack

| Tool | Rolle | Begründung |
|------|-------|------------|
| playwright | E2E | `npx playwright test` |
| pytest | Backend | `pytest -q` |
| vitest/jest | Unit | `npm test` |

## System-Prompt / Instruktionen

```text
Testing workflow (software-entwicklung/testing).

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

## Arbeitsablauf

1. Test-Runner ermitteln: `cat package.json` / `pyproject.toml`.
2. Unit: `pytest -q` oder `npm test`.
3. Playwright install: `npx playwright install chromium` wenn fehlt.
4. Spec schreiben unter `tests/e2e/`.
5. `npx playwright test tests/e2e/checkout.spec.ts`.
6. Bei Fail: `npx playwright show-report`.
7. CI-Snippet für GitHub Actions ergänzen.

## Qualitätskriterien / Definition of Done

- [ ] Tests lokal grün
- [ ] Keine hardcoded prod URLs
- [ ] Flake-Retry-Policy in config

## Sicherheit & Freigaben

- Keine Credentials in committed test files.
- Playwright gegen interne Apps nur mit VPN-Hinweis.

## Fallstricke

- Playwright MCP-only — teuer und anders als CI.
- codegen gegen Prod — Datenänderung.
- waitForTimeout statt expect — flaky.
- Parallel workers + shared DB — isolation fehlt.
- --update-snapshots unreviewed — visuelle Regression.

## Grundbeispiele

### Beispiel 1 (Beispieldaten)

- **Aufgabe:** Login E2E staging.
- **Input:** `https://staging.example.com`.
- **Prompt:**

```text
Add playwright spec for login; run headed once then headless; no MCP.
```

- **Erwartetes Ergebnis:**

```bash
npx playwright test tests/e2e/login.spec.ts --project=chromium
# 1 passed
```

### Beispiel 2 (Beispieldaten)

- **Aufgabe:** pytest API smoke.
- **Input:** `tests/api/`.
- **Prompt:**

```text
pytest -q; add test for 401 on missing token.
```

- **Erwartetes Ergebnis:**

```bash
pytest -q tests/api/
# .... 12 passed
```

### Beispiel 3 (Praxisbeispiel)

- **Aufgabe:** CLI vs MCP Tokenkosten.
- **Input:** reine Extraktion vs. App-E2E.
- **Prompt:**

```text
Recommend playwright CLI for CI e2e; MCP only for interactive debug session.
```

- **Erwartetes Ergebnis:**

```text
CI: npx playwright test
Debug: optional Playwright MCP with narrow snapshot scope
```