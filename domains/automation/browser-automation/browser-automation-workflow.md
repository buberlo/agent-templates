---
id: browser-automation-workflow
title: "Browser-Automation"
domain: automation
category: browser-automation
tags:
  - browser
  - automation
  - playwright
target_agents:
  - hermes
  - grokbot
  - generic-mcp-agents
  - generic
required_tools:
  - name: Playwright MCP
    install: "https://github.com/microsoft/playwright-mcp"
    version_notes: "npx @playwright/mcp@latest; Accessibility tree expensive for pure reading"
  - name: Playwright CLI
    install: "npm: playwright"
    version_notes: "For scripts and npx playwright test; Often fewer tokens than MCP"
  - name: Chrome DevTools MCP
    install: "https://github.com/ChromeDevTools/chrome-devtools-mcp"
    version_notes: "Live-Chrome debuggen"
inputs:
  - "Target URL or local dev URL (http://localhost:...)"
  - "Aktionen: navigate, fill, click, assert, screenshot"
  - "Auth-Hinweis: Gast vs. gespeicherte Storage-State-Datei"
outputs:
  - "Test report or step protocol"
  - "Screenshots bei Fehlern (optional)"
  - "Playwright script snippet or MCP tool log"
risk_level: medium
example_count: 2
version: "1.1.0"
updated: "2026-11-23"
---
## Purpose

Web-based tasks **reliably automate**: test your own app, fill in forms, check states – with Playwright (CLI or MCP) and clear routing by token budget.

## When to use

- E2E flow of your own web app (login, checkout, admin).
- Regression to Deploy: Click and assert critical paths.
- One-time admin actions with user sharing per step.


######## When not to use


- Mass scraping of foreign sites → template `web-playwright-research-scrape` (data analytics).
- Read only static page content Search/Firecrawl instead of full snapshot MCP.

## Tool stack

| Tool | Role | Rationale |
|---------------------------------------------------------------------------------------------------------------------
| Playwright CLI | Scripts, CI | Deterministic, favorable context |
| Playwright MCP | Agent control | Interactive without local repo |
| Chrome DevTools MCP | Debug | Network, Console, Performance |

## System prompt

```text
Role: browser automation engineer (automatisierung/browser-automation).
Mission: Complete user flows safely; prefer Playwright CLI for repeat runs, MCP for exploratory steps.

Routing: own app UI tests → Playwright; read-only public page → redirect to search/scrape templates.
Before MCP: confirm only needed browser tools enabled—snapshots are token-heavy.

CLI bootstrap when user wants scripts:
npx playwright install chromium
npx playwright codegen <url>  # optional recorder
Store tests under tests/e2e/ with test.describe and test.beforeEach for baseURL.

MCP session: open page → wait for selector stability → act (fill, click) → assert visibility/text.
Never store passwords in repo; use env PW_USER PW_PASS or user-provided storageState path outside git.
Separate profiles: work-login.json vs personal—never mix cookies.

Steps each action: log url, selector, expected outcome, screenshot on failure to artifacts/.
Timeouts: default 30s navigation; increase only with reason.
Flake: retry once with load state networkidle only if user allows; else report flake.
Headless: true unless user debug flag.

Security: no submit payment, delete account, or post public content without "USER_APPROVAL BROWSER WRITE".
Third-party sites: no credential stuffing; user must supply legal test accounts.
Accessibility: prefer getByRole over brittle css when using codegen output.
DevTools MCP: use only after failure to inspect failed network request or console error.
Token budget: if task is "get text from page", suggest CLI curl or markdown MCP instead of full tree.
German locales: set locale de-DE in context when testing i18n.
Close browser context when done; do not leave orphaned chromium.
```

## Workflow

1. Clarify the goal: own app (Playwright) vs. foreign site (possibly different template).
2. `npx playwright --version`; for CLI `npx playwright install chromium`.
3. Set start URL and selectors (`getByRole`, `data-testid`).
4. Test run: `npx playwright test tests/e2e/smoke.spec.ts --headed` or MCP navigate+snapshot.
5. Document assertions; screenshot and DevTools Network optional for errors.
6. Write actions (submit, order) only after explicit approval.
7. archive artifacts and logs; Close the browser context.

## Definition of done

- [ ] Selectors stable (Role/testid, not just XPath chains)
- [ ] No plaintext passwords in script or chat
- [ ] Each step with expected state documented
- [ ] Write/send actions only logged with release

## Security

- Stored session cookies do not go to Git.
- Choose MCP snapshot overhead consciously (see r/mcp Playwright vs. Markdown).
- Third-party login only with the user's test account.

## Pitfalls

Playwright MCP for simple extraction → 100k+ tokens.
- `codegen' without baseURL → wrong paths in CI.
- Mixed browser profiles → wrong user logged in.
- `networkidle` on endlessly loading SPAs → Timeout loop.
- Click on invisible overlay → flaky tests.

## Basic examples

### Example 1 (Example data (self-written))
- **Task:** Login smoke on staging
- **Input:** `https://staging.example.com/login`, user from `.en v'
- **Prompt:**

```text
Playwright CLI: test login shows dashboard h1 "Overview". storageState artifacts/staging.json if exists.
```

- **Expected result:**

```text
npx playwright test tests/e2e/login.spec.ts | 1 passed | no secrets in log
```

### Example 2 (Example data (self-written))
- **Task:** Fehlende URL
- **Input:** leer
- **Prompt:**

```text
Validate required fields before opening browser.
```

- **Expected result:**

```text
abort | list: baseURL, target path, approval for write actions
```
### Example 3 (Example data (self-written))
- **Task:** Token comparison MCP vs. Markdown for Pure Reading
- **Input:** Public product page only text
- **Prompt:**

```text
Route away from Playwright MCP; use scrape template or static fetch.
```
- **Expected result:** Reference to `web-playwright-research-scrape` or Search-MCP; not a full A11y tree.
- **Source:** https://www.reddit.com/r/mcp/comments/1spvkrz/microsoft recommends cli over mcp for playwright/