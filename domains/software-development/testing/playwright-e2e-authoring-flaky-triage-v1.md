---
id: playwright-e2e-authoring-flaky-triage-v1
title: "Playwright MCP E2E test authoring and flaky-test triage"
domain: software-development
category: testing
tags:
  - playwright
  - e2e
  - mcp
  - flaky-tests
target_agents:
  - cursor
  - claude-code
  - hermes
  - grokbot
  - generic-mcp-agents
required_tools:
  - name: Playwright MCP
    install: "https://github.com/microsoft/playwright-mcp"
    version_notes: "Official Microsoft server; see https://playwright.dev/mcp/introduction for client config."
  - name: GitHub Official MCP
    install: "https://github.com/github/github-mcp-server"
    version_notes: "Optional for linking failures to CI workflow runs and opening issues."
inputs:
  - "Target URL or route under test (staging or localhost)"
  - "User story or acceptance criteria for the flow"
  - "Optional CI log snippet naming a flaky spec file and line"
outputs:
  - "playwright spec draft with stable locators and test plan"
  - "Flaky-test triage memo with retry evidence and fix suggestions"
risk_level: medium
example_count: 2
version: "1.0.0"
updated: "2026-11-25"
---

## Purpose

Author new end-to-end UI tests and triage intermittent failures using Playwright MCP accessibility snapshots, then align outputs with the project's existing test layout. The agent runs browser interactions through MCP; it does not merge to main or trigger production deploys without human approval.

## When to use

- A product squad needs a first Playwright spec for a checkout or onboarding flow on a staging host.
- CI reports a flaky test and you want a structured hypothesis list before editing waits or selectors.
- You pair Playwright MCP with a coding agent that writes specs into the repo after review.

### When not to use

- Pure API contract testing with no browser surface (use the project unit or integration framework instead).
- Large-scale scraping or data extraction where Playwright MCP snapshot size would dominate context; see `web-playwright-research-scrape` patterns.
- Running tests against production customer accounts without a dedicated sandbox tenant.

## Tool stack

| Tool | Role | Rationale |
|------|------|-----------|
| Playwright MCP | Browser drive and a11y tree | Official Microsoft MCP for UI interaction and snapshots ([playwright.dev/mcp/introduction](https://playwright.dev/mcp/introduction)) |
| Local Playwright test runner | Verify specs | Human or agent runs `npx playwright test` after draft review |
| GitHub Official MCP | CI correlation | Optional: map flaky job to commit and workflow file |
| Project test framework | Structure | Match existing `tests/e2e` conventions |

## System prompt

```text
You are an E2E test engineer working through Playwright MCP for software-development/testing.
You explore the target URL with Playwright MCP tools, prefer role- and text-based locators from accessibility snapshots over brittle CSS hooks, and you document each locator choice in plain language.
When authoring a new spec you produce a single focused describe block per user story, use test.step for readability, and avoid hard-coded sleeps except when justified with a comment tying the wait to a known animation or network idle boundary.
You never store real customer credentials in the spec; use environment variables or a documented test account alias such as e2e-user@example.com.
For flaky triage you collect at least two failure modes from logs or MCP reruns, classify them as timing, selector drift, data pollution, or environment drift, and you propose the smallest fix first such as expect.poll or locator strictness.
You do not delete existing tests, disable CI required checks, or push commits unless the user types COMMIT APPROVED with a branch name.
You run Playwright MCP interactions sequentially when the client warns about parallel tool rate limits, and you cap snapshot size by scoping to the active modal or panel.
You output a short test plan table before the spec file contents so reviewers can reject scope creep early.
When CI artifacts are missing you state assumptions explicitly and list commands the human should run locally.
You cite Playwright MCP documentation for capability limits and you do not claim features that are not listed in the official introduction page.
```

## Workflow

1. Confirm base URL, auth method, and whether tests target Chromium only or the matrix in `playwright.config`.
2. Use Playwright MCP to walk the happy path once; save a locator map in the triage memo.
3. Draft the spec with `data-testid` only where accessibility roles are insufficient.
4. If flaky: rerun the failing step three times with unchanged selectors; log pass/fail pattern.
5. Propose fix (wait strategy, isolation fixture, or mock route) ranked by invasiveness.
6. Human runs `npx playwright test` locally or in CI; agent revises only after log feedback.
7. Optional: open a draft PR description listing new tags and required secrets for CI.

## Definition of done

- [ ] Spec uses stable locators justified against snapshot evidence
- [ ] No plaintext passwords or production URLs without explicit user consent
- [ ] Flaky memo lists category, evidence, and proposed fix before code edit
- [ ] Playwright MCP usage matches official server scope (no invented CLI flags)

## Security

- Keep OAuth and basic-auth secrets in CI secret stores, not in committed specs.
- Staging credentials must be rotated independently of production.
- Screenshots from MCP may include PII; redact before attaching to tickets.

## Pitfalls

- Oversized accessibility snapshots exhaust context; narrow to one frame at a time ([Playwright MCP introduction](https://playwright.dev/mcp/introduction)).
- `networkidle` waits are deprecated in many apps with websockets; prefer `expect(locator).toBeVisible()`.
- Parallel workers expose shared-account race conditions that look like flakes.
- Mixing Playwright MCP exploration with `@playwright/test` codegen output without reconciliation creates duplicate helpers.
- Running against prod without rate limits can trigger WAF blocks mistaken for test failures.

## Basic examples

### Example 1 (Example data (self-written))

- **Task:** Author a first test for guest checkout on `https://shop-staging.example.com`.
- **Input:** Acceptance criteria: add SKU `WIDGET-01`, view cart, reach login wall without paying.
- **Prompt:**

```text
Use Playwright MCP to walk guest checkout through the login wall on shop-staging.example.com.
Output test plan plus e2e/guest-checkout.spec.ts draft using @playwright/test.
No commits.
```

- **Expected result:**

The response includes a four-step test plan table, then a spec with `getByRole('button', { name: 'Add to cart' })` style locators, environment variable placeholder `STAGING_BASE_URL`, and a note that payment steps are out of scope. Each locator line references what was visible in the MCP snapshot narrative.

### Example 2 (Example data (self-written))

- **Task:** Triage flaky `tests/e2e/cart-quantity.spec.ts:44` timing out on CI twice per day.
- **Input:** Log shows `Timeout 15000ms exceeded` on `locator('[data-testid=cart-count]')`.
- **Prompt:**

```text
Flaky triage only: hypothesize root cause for cart-count timeout, suggest minimal fix.
Include rerun strategy with Playwright MCP on staging.
```

- **Expected result:**

A triage memo labels the failure as timing or selector drift, recommends `expect(cartCount).toHaveText('2')` with `expect.configure({ timeout: 10000 })`, suggests verifying whether cart count updates via websocket, and lists three ordered fixes without editing the repo until FIX APPROVED.