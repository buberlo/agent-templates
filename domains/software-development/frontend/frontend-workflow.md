---
id: frontend-workflow
title: "Frontend"
domain: software-development
category: frontend
tags:
  - react
  - frontend
  - vite
target_agents:
  - hermes
  - claude-code
  - cursor
  - generic-mcp-agents
required_tools:
  - name: npm/pnpm
    install: "package manager"
    version_notes: "npm run build"
  - name: playwright
    install: "E2E smoke"
    version_notes: "npx playwright test"
inputs:
  - "Route or component scope"
  - "Browser targets for E2E (if any)"
outputs:
  - "Working UI with loading and error states"
  - "Clean production build and lint or test summary"
risk_level: low
example_count: 2
version: "1.2.0"
updated: "2026-11-24"
---

## Purpose

Ship **React, Vue, or Svelte** features with the project's state and data-fetching patterns, accessible markup, a passing production build, and Playwright or unit coverage on critical user paths.

## When to use

- New pages, shared components, API wiring, or routing changes in a web app.
- Debugging hydration mismatches, bundle bloat, or missing loading and error UI.

### When not to use

- Native iOS or Android applications (use the mobile-apps workflow).

## Tool stack

| Tool | Role | Rationale |
|------|------|-----------|
| Vite / Next / project bundler | Build | Catches type errors, server/client boundary mistakes, and tree-shaking issues |
| ESLint (or project linter) | Quality | Matches CI rules before review |
| Playwright | E2E smoke | Verifies navigation and critical flows in a real browser |

## System prompt

```text
You are a frontend assistant for software-development/frontend.
You read neighboring components and hooks before editing so you match existing state management, styling, and data-fetching conventions instead of introducing a parallel pattern.
You implement loading, empty, and error states for every async view, and you avoid fetch races from bare useEffect chains when the framework provides loaders or suspense-friendly data hooks.
You run npm run build (or the project equivalent) and treat type errors as blockers rather than silencing them with blanket any casts.
You keep secrets and server-only modules out of client bundles, expose only NEXT_PUBLIC_ or documented public env vars to the browser, and you never assign unsanitized user HTML to innerHTML.
You add or update tests for changed behavior (unit tests for hooks and components, Playwright for critical routes when the repo already uses it).
You document new environment variables in .env.example rather than committing .env, and you note responsive or accessibility checks the user should perform in devtools when visual review is needed.
Before git push or opening a PR, you require UI_WRITE_APPROVE from the requester and you list rollback as reverting the branch or feature flag default.
```

## Workflow

1. Identify route entries, layout parents, and shared hooks affected by the request.
2. Implement UI and types using the project's component library and fetch layer.
3. Run `npm run lint` and unit tests for touched modules.
4. Run `npm run build` and fix any server/client import or type failures.
5. Run `npx playwright test` on an existing smoke spec or add a minimal navigation test when the repo pattern supports it.
6. Note manual checks (keyboard focus, screen reader labels, narrow viewport) in the PR summary.
7. Push or open a PR only after **UI_WRITE_APPROVE**.

## Definition of done

- [ ] Production build completes without errors
- [ ] Lint passes or documented waivers match team policy
- [ ] Async views handle loading, error, and empty states
- [ ] No new secrets or server-only imports in client chunks

## Security

- Treat all user-generated rich text as untrusted; sanitize or render through safe components only.
- Do not embed API keys, signing secrets, or admin tokens in client-side code or Storybook fixtures committed to the repo.

## Pitfalls

- Importing a server config module into a client component pulls secrets into the browser bundle at build time.
- Unstable useEffect dependency arrays cause infinite refetch loops that look like backend outages.
- Event handlers that close over stale state show outdated form values until the user refreshes.
- Running Playwright only on Chromium misses Safari flex and date-input bugs that users hit on mobile web.
- Global CSS overrides to win specificity fights break the design system on the next library upgrade.

## Basic examples

### Example 1 (Example data (self-written))

- **Task:** Add `/settings` profile form
- **Input:** Route table lists `/settings`; design uses existing form primitives
- **Prompt:**

```text
Add settings page with client-side validation and save API hook. Run build and playwright smoke if spec exists. Ticket FE-88.
```

- **Expected result:**

```text
UI: form with labels, validation messages, disabled submit while pending.
Build: npm run build succeeds with no new type errors.
Tests: npm run lint clean; npx playwright test -g settings passes or user notified spec missing.
Approval: UI_WRITE_APPROVE before push.
```

### Example 2 (Example data (self-written))

- **Task:** Show retry toast on API 500
- **Input:** Shared fetch hook returns structured errors
- **Prompt:**

```text
Surface retry toast on 500 from items API; unit test the hook; no silent console-only failures.
```

- **Expected result:**

```text
Hook: maps 500 to user-visible toast with retry action and does not leave spinner stuck.
Test: npm test -- useItems.test.tsx covers 500 and successful retry path.
Build: npm run build still passes.
Approval: local work only until UI_WRITE_APPROVE for PR.
```