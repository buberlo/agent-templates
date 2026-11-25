---
id: figma-dev-mode-component-impl-v1
title: "Figma MCP Dev Mode design-to-component implementation"
domain: software-development
category: design-to-code
tags:
  - figma
  - design-system
  - react
  - mcp
target_agents:
  - cursor
  - claude-code
  - grokbot
  - generic-mcp-agents
required_tools:
  - name: Figma MCP server (remote)
    install: "https://developers.figma.com/docs/figma-mcp-server/"
    version_notes: "Remote endpoint https://mcp.figma.com/mcp per Figma developer docs."
  - name: Playwright MCP
    install: "https://github.com/microsoft/playwright-mcp"
    version_notes: "Optional visual smoke on Storybook or preview URL."
inputs:
  - "Figma file URL and target frame or component node name"
  - "Target codebase path (e.g. packages/ui)"
  - "Styling stack (Tailwind, CSS modules, etc.)"
outputs:
  - "Component implementation plan with token mapping"
  - "Draft component source files for human review"
risk_level: medium
example_count: 2
version: "1.0.0"
updated: "2026-11-25"
---

## Purpose

Implement a UI component from a selected Figma frame using the official Figma MCP server for variables, layout, and component metadata, then generate code aligned with the repository design system. Canvas write-back requires separate approval and is out of scope for this template.

## When to use

- Design hands off a Dev Mode inspected component for engineering implementation.
- You need variables and spacing tokens pulled into code without screenshot guesswork.
- Cursor or Claude Code with Figma MCP remote connector is already authenticated.

### When not to use

- Full page builds without a scoped frame selection (context explosion).
- Writing edits back to Figma production files without design approval.
- Designs under NDA files you cannot authenticate via MCP.

## Tool stack

| Tool | Role | Rationale |
|------|------|-----------|
| Figma MCP server | Design context | Official remote MCP ([developers.figma.com/docs/figma-mcp-server/](https://developers.figma.com/docs/figma-mcp-server/)) |
| Code Connect (optional) | Mapping | When configured, prefer mapped code components per Figma docs |
| Playwright MCP | Visual check | Snapshot Storybook route after implementation |

## System prompt

```text
You are a design-system engineer implementing a single Figma component into code for software-development/design-to-code.
You use Figma MCP to load only the user-named frame or component node, extracting variables, auto-layout direction, padding, and text styles without requesting the entire file tree.
You map Figma variables to existing theme tokens in the codebase when names align, and you propose new tokens only in a separate tokens appendix for design approval.
You generate accessible React or framework-native markup with semantic roles, focus styles, and keyboard behavior for interactive controls shown in the design.
You do not call Figma write-to-canvas tools unless FIGMA WRITE APPROVED is issued and you warn that remote write features may be rate-limited per Figma plans documentation.
You match repository patterns for exports, tests, and Storybook stories, and you avoid introducing new dependencies without DEPENDENCY APPROVED.
You produce a short implementation plan before code blocks so reviewers can reject scope early.
You run Playwright MCP against a local Storybook URL only when the user supplies localhost or staging preview hosts, never against unauthorized production sites.
You cite https://developers.figma.com/docs/figma-mcp-server/ for capabilities and do not claim desktop-only features when only remote MCP is configured.
You document any ambiguous design states such as hover versus pressed as open questions for design rather than guessing hex values.
```

## Workflow

1. User shares Figma URL and exact node name; confirm read access.
2. Pull component metadata and variables via Figma MCP.
3. Inventory existing code components that might wrap or extend the design.
4. Draft implementation plan and token mapping table.
5. Write component and story files locally; no commit without COMMIT APPROVED.
6. Optional Playwright MCP screenshot compare against design at 1x scale note only.
7. Hand off checklist for design QA in Figma compare mode.

## Definition of done

- [ ] Only scoped Figma nodes referenced
- [ ] Accessibility roles and labels present for interactive parts
- [ ] No Figma canvas writes or secret file keys in output
- [ ] Implementation plan precedes code

## Security

- Figma OAuth tokens remain in the MCP client; do not paste personal access tokens into templates.
- Remote MCP write features are beta; treat as high risk ([Figma MCP introduction](https://developers.figma.com/docs/figma-mcp-server/)).

## Pitfalls

- Loading entire design files exhausts context; select one frame.
- Variable renames in Figma desync token maps in code.
- Ignoring Code Connect mappings duplicates existing components.
- Pixel-perfect chasing ignores responsive breakpoints not shown in frame.
- Mixing Hermes catalog figma wrapper with remote MCP causes conflicting install instructions.

## Basic examples

### Example 1 (Example data (self-written))

- **Task:** Implement `Button/Primary` from file `https://www.figma.com/file/Example/Design-System`.
- **Input:** Target stack React + Tailwind in `packages/ui`.
- **Prompt:**

```text
Figma MCP: extract Primary button specs and draft packages/ui/ButtonPrimary.tsx plus story.
Plan first, no commit.
```

- **Expected result:**

Plan table mapping padding, radius, and color variables to Tailwind classes or CSS variables, component using `forwardRef`, story with default and disabled variants, open question if loading state not in frame.

### Example 2 (Example data (self-written))

- **Task:** Verify implemented card matches design on Storybook `http://localhost:6006/?path=/story/card`.
- **Input:** Playwright MCP allowed on localhost.
- **Prompt:**

```text
Playwright MCP snapshot Card story and list visual deltas vs Figma spacing notes only.
No Figma writes.
```

- **Expected result:**

Bullet list of spacing or typography deltas such as title 16px vs 18px, recommendation to adjust `gap-4` to `gap-5`, no screenshot attachments with real customer data.