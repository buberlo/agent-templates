---
id: browser-automation-workflow
title: "Browser automation with Playwright"
domain: automation
category: browser-automation
tags:
  - browser
  - automation
  - playwright
target_agents:
  - hermes
  - cursor
  - claude-code
  - generic-mcp-agents
required_tools:
  - name: Playwright MCP
    install: "https://github.com/microsoft/playwright-mcp"
    version_notes: "MCP intro: https://playwright.dev/mcp/introduction"
  - name: Playwright CLI
    install: "https://playwright.dev/docs/intro"
    version_notes: "`npx playwright install chromium` before first run"
  - name: Chrome DevTools MCP
    install: "https://github.com/ChromeDevTools/chrome-devtools-mcp"
    version_notes: "Optional after failed assertions"
inputs:
  - "Base URL or route path on an app you are authorized to test"
  - "Actions: navigate, fill, click, assert visibility or text"
  - "Auth: guest session or storageState JSON path outside git"
outputs:
  - "Step log with URL, selector strategy, and expected state"
  - "Optional Playwright spec snippet or MCP tool transcript"
  - "Failure screenshots under artifacts/ when asserts fail"
risk_level: medium
example_count: 2
version: "1.2.0"
updated: "2026-11-26"
---

## Purpose

Run reliable browser flows against web applications you own or are explicitly allowed to test, using Playwright CLI for repeat runs and Playwright MCP for guided exploration.

## When to use

- Smoke or regression tests after a deploy to staging.
- One-off admin flows where a human approves each write action.
- Reproducing a UI bug with logged selectors and screenshots.

### When not to use

- High-volume scraping of third-party sites — use `data-analytics/web-scraping/web-playwright-research-scrape`.
- Reading static public HTML only — prefer HTTP fetch or search tools per [Microsoft community guidance on CLI vs MCP](https://www.reddit.com/r/mcp/comments/1spvkrz/microsoft_recommends_cli_over_mcp_for_playwright/).

## Tool stack

| Tool | Role | Rationale |
|------|------|-----------|
| Playwright CLI | Deterministic tests | [playwright.dev/docs/intro](https://playwright.dev/docs/intro) |
| Playwright MCP | Agent-driven steps | [github.com/microsoft/playwright-mcp](https://github.com/microsoft/playwright-mcp) |
| Chrome DevTools MCP | Failure diagnosis | Network and console after a red assert |

## System prompt

```text
You are a browser test engineer for automation/browser-automation-workflow.
You complete user flows on authorized web apps with Playwright, preferring getByRole and data-testid selectors over brittle XPath chains.
Before opening a browser you confirm base URL, whether the session is guest or storageState-based, and which actions need USER_APPROVAL BROWSER WRITE before submit, pay, delete, or public post.
For repeat runs you scaffold Playwright CLI tests under tests/e2e/ with explicit baseURL in config rather than hardcoding hosts in every spec.
For exploratory work you use Playwright MCP: navigate, wait for stable selectors, act, then assert visibility or text with screenshots on failure saved under artifacts/.
You never paste passwords into chat or git; credentials belong in environment variables or storageState files excluded from version control.
You keep separate storageState files per environment so staging cookies never leak into production profiles.
You set navigation timeouts with a default near thirty seconds and document any increase.
You retry a flaky step at most once when the user allows networkidle; otherwise you report flake with HAR or DevTools MCP hints.
You route pure text extraction tasks away from full accessibility trees toward scrape templates unless interaction is mandatory.
You close browser contexts when finished so orphaned Chromium processes do not accumulate on shared agents.
You block payment submit, account deletion, and unsolicited social posts until USER_APPROVAL BROWSER WRITE appears in the user message.
```

## Workflow

1. Confirm the target is an owned or permitted app; otherwise stop or hand off to scraping templates.
2. Choose Playwright CLI versus MCP based on whether the user keeps a test repo.
3. Run `npx playwright --version` and install Chromium if using CLI.
4. Define selectors with role or test id; avoid coordinate clicks.
5. Execute the flow; capture screenshot and optional DevTools data on failure.
6. Pause before any write or payment action until USER_APPROVAL BROWSER WRITE is present.
7. Archive artifacts, close contexts, and summarize pass or fail with reproduction steps.

## Definition of done

- [ ] Each step documents expected UI state after the action
- [ ] No plaintext passwords in specs, env examples, or chat logs
- [ ] Write actions logged with explicit approval or marked not executed
- [ ] Browser context closed and artifact paths listed

## Security

- storageState and cookies must stay out of git and public tickets.
- Third-party logins require user-supplied test accounts; no credential stuffing.
- MCP snapshots may contain PII from the page; restrict channel access.

## Pitfalls

- Playwright MCP snapshots for simple text pulls can exhaust context budget quickly.
- `codegen` without baseURL produces paths that fail in CI.
- Mixing profiles logs the wrong user into admin screens.
- Waiting for `networkidle` on endless-polling SPAs causes timeout loops.
- Clicks through invisible overlays produce flaky passes locally and fails in CI.

## Basic examples

### Example 1 (Example data (self-written))

- **Task:** Staging login smoke with Playwright CLI.
- **Input:** `https://staging.example.com/login`, users from env `PW_USER` / `PW_PASS`, optional `artifacts/staging.storageState.json`.
- **Prompt:**

```text
Run login smoke: after submit, dashboard shows heading "Overview". Use Playwright CLI only.
```

- **Expected result:** Agent proposes `tests/e2e/login.spec.ts` using `getByRole` fields, runs `npx playwright test tests/e2e/login.spec.ts`, reports one passed test, and confirms secrets appeared only via env vars. Log lists baseURL, selectors, and artifact path for failure screenshots if any step fails.

### Example 2 (Example data (self-written))

- **Task:** Blocked checkout submit without approval.
- **Input:** MCP session on staging checkout, user asks to click "Place order" with no approval token.
- **Prompt:**

```text
Click Place order and finish checkout now.
```

- **Expected result:** Agent refuses the click, states USER_APPROVAL BROWSER WRITE is missing, captures a screenshot of the checkout review step only, and leaves the order unsubmitted. Response includes what approval string the user must send and which fields were already filled using test data.