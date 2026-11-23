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
  - "Route/Component scope"
  - "Browser targets"
outputs:
  - "Working UI + tests"
  - "Build without Fehler"
risk_level: low
example_count: 2
version: "1.0.0"
updated: "2026-11-23"
---

## Purpose

Frontend features in React/Vue/Svelte: State, Routing, a11y, **Build and Playwright smoke**.

## When to use

- Neue Seiten, Komponenten, API-Anbindung.
- Bundle- or Hydration-Bugs.

**When not:** Native Mobile (mobile apps).

## Tool stack

| Tool | Role | Justification |
|------|-------|------------|
| vite/next | bundler | project default |
| eslint | lint | npm run lint |
| playwright | E2E | critical paths |

## System prompt

```text
Frontend workflow (software-development/frontend).

Follow existing state management pattern; do not introduce new global store without ask.
Data fetching: use project standard (react-query, trpc, fetch hooks).
Handle loading, error, empty states in UI.
Avoid useEffect fetch race; prefer declared data loaders if framework supports.
npm run build must pass before done; fix type errors properly.
Code split large routes; avoid importing server code client-side.
a11y: button type, label for, alt text.
Playwright: smoke login/dashboard path if exists.
Env vars: NEXT_PUBLIC_ only for public values.
No innerHTML without sanitization.
CSS modules/tailwind per repo convention.
Document any new env in .env.example not .env.
```

## Workflow

1. Route/component files identifizieren.
2. Implement + types.
3. `npm run lint && npm run test`.
4. `npm run build`.
5. `npx playwright test tests/smoke.spec.ts` wenn vorhanden.
6. Manual check responsive in devtools notes.
7. PR summary with build time.

## Definition of done

- [ ] Build green
- [ ] lint clean or justified
- [ ] Loading/error states

## Security

- XSS: no unescaped user HTML.

## Pitfalls

- Client bundle includes server secrets.
- useEffect dependency loops.
- Stale closure in handlers.
- Playwright only chromium while Safari bug.
- CSS specificity wars.

## Basic examples

### Example 1 (Example data)

- **Task:** Settings page.
- **Input:** route /settings.
- **Prompt:**

```text
Add form with validation; build; playwright smoke navigation.
```

- **Expected result:**

```bash
npm run build
npx playwright test -g settings
```

### Example 2 (Example data)

- **Task:** API error toast.
- **Input:** 500 from API.
- **Prompt:**

```text
Show retry toast; unit test hook; no silent fail.
```

- **Expected result:**

```bash
npm test -- useApi.test.tsx
```