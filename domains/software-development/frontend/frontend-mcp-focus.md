---
id: frontend-mcp-focus
title: "Frontend: MCP/Skill-Fokus"
domain: software-development
category: frontend
tags:
  - frontend
  - mcp
  - playwright
target_agents:
  - hermes
  - claude-code
  - cursor
  - generic-mcp-agents
required_tools:
  - name: Playwright MCP
    install: "UI debug"
    version_notes: "CLI verify required"
  - name: Chrome DevTools MCP
    install: "layout/perf"
    version_notes: "optional"
inputs:
  - "Local dev URL"
  - "Skill verify playwright CLI"
outputs:
  - "Component fix"
  - "MCP vs CLI matrix"
risk_level: low
example_count: 2
version: "1.0.0"
updated: "2026-11-23"
---

## Purpose

Frontend debugging: **Playwright MCP** for UI state, Skill ends with **`npx playwright test`** and `npm run build`.

## When to use

- Hydration/Layout-Bug schwer reproduzierbar.
Agent with MCP browser snapshot.

**When not:** Pure Typo — edit only.

## Tool stack

| Tool | Role | Justification |
|------|-------|------------|
| Playwright MCP | Observe | snapshots |
| playwright CLI | Verify | tests |
| DevTools MCP | Perf | optional |

## System prompt

```text
Frontend MCP/Skill focus (software-development/frontend).

Use MCP to observe failing UI state once; then fix code; verify with CLI playwright and build.
Limit MCP rounds to 3 per bug to control tokens.
DevTools MCP for layout shift or network waterfall only when perf issue stated.
Never consider task done without npm run build success.
MCP must target localhost dev URL user provides, not prod.
Export reproduction as playwright spec when bug recurring.
Disable MCP after spec written for remaining iterations.
Document MCP snapshot findings vs DOM after fix.
Prefer data-testid selectors in specs over CSS from MCP snapshot.
Run lint with same command as CI from package.json scripts field.
If hydration error, note server/client component boundary in summary.
Capture before/after screenshots only in local test-results, not chat attachments.
List React strict mode double-render issues when relevant to flaky MCP observations.
Coordinate with design tokens file when visual mismatch is reported.
```

## Workflow

1. `npm run dev` URL confirm.
2. MCP: reproduce bug snapshot.
3. Code fix im workspace.
4. `npm run build`.
5. `npx playwright test` relevant spec.
6. Optional DevTools MCP confirm LCP improved.
7. Matrix MCP rounds vs CLI runs.

## Definition of done

- [ ] build + playwright green
- [ ] MCP rounds dokumentiert
- [ ] localhost only

## Security

- MCP captures may show user data — redact.

## Pitfalls

- Endless MCP loop without fix.
- Fix gegen snapshot stale selector.
- DevTools on prod URL.
- MCP cost on static text extraction task.

## Basic examples

### Example 1 (Example data)

- **Task:** Modal not clickable.
- **Input:** localhost:5173.
- **Prompt:**

```text
MCP open modal once; fix z-index; playwright test.
```

- **Expected result:**

```bash
npx playwright test tests/modal.spec.ts
```

### Example 2 (Example data)

- **Task:** No MCP.
- **Input:** type error only.
- **Prompt:**

```text
tsc fix only; build verify.
```

- **Expected result:**

```bash
npm run build
# MCP not used
```