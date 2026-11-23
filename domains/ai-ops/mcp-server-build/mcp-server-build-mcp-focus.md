---
id: mcp-server-build-mcp-focus
title: "MCP-Server bauen: MCP/Skill-Fokus"
domain: ai-ops
category: mcp-server-build
tags:
  - mcp
  - ai-ops
  - referenz
target_agents:
  - hermes
  - grokbot
  - generic-mcp-agents
  - generic
required_tools:
  - name: mcp-builder skill guidance
    install: "https://github.com/ComposioHQ/awesome-claude-skills"
    version_notes: "Checkliste"
inputs:
  - "Build vs. Buy (existierender MCP)"
outputs:
  - "Entscheidungsmatrix"
risk_level: low
example_count: 2
version: "1.1.0"
updated: "2026-11-23"
---
## Purpose

**Build vs. existing MCP** and focus SDK/reference server — before writing code.

## When to use

Do we need our own MCP?
Select TS vs. Python SDK.

## Tool stack

| Tool | Role | Rationale |
|-------------------------------------------------------------------------------------------------------------------
| servers repo | reference | pattern |
| mcp-builder skill | Process | Community |
| Hermes optional mcps | Buy | If fits |

## System prompt

```text
Role: MCP build advisor (ki-ops/mcp-server-bau-mcp-focus).
Mission: Search catalog first; custom server only for gap with maintenance owner.

Checklist search hermes optional mcps awesome mcp servers punkpeye repo query user api domain.
Buy if oauth maintained upstream and scopes fit 80 percent use cases.
Build if internal api no public mcp or compliance requires self host stdio on laptop.
SDK choice python for data teams ts for frontend heavy org match existing repo langs.
Transport stdio default; sse only if remote hosted with authZ documented.
Maintenance assign owner team on-call rotation before merge custom server.
Size cap: max 8 tools v1 else split servers by domain reduce schema bloat.
Skill vs server: skill is instructions only if api already has curl—do not duplicate mcp unnecessarily.
Handoff implementation to mcp-server-bau-workflow when build approved.
License verify dependencies with apache2 bsd.
Deprecation plan if upstream releases official mcp later migration note.
```

## Workflow

Decompose requirement into tools.
2. Catalogue search (Hermes, awesome-mcp).
3. Gap / Fit document.
4. Build/Buy recommendation with owner.
5. SDK choice and transport.
6. Build → mcp-server-bau-workflow.
7. Buy → Install-Config only.

## Definition of done

- [ ] Catalog search documented
-[ ] Owner named for maintenance
- [ ] Build only with justification

## Security

No fork without an update plan.

## Pitfalls

- Enable only required tools; every tool adds schema and auth surface.
- Custom MCP for existing connectors adds maintenance without new capability.
- Too many tools in v1 inflates context (community reports cite ~67k token traps).
- In-house OAuth flows without rotation or revoke are often underestimated in security review.

## Basic examples

Example 1 (Example data)

- **Task:** Google Drive
- **Input:** read files
- **Prompt:**

```text
Build mcp for drive.
```

- **Expected result:**

```text
buy existing connector | no custom build
```

### Example 2 (Example data)

- **Task:** Internal ERP
- **Input:** read tickets only
- **Prompt:**

```text
No public mcp.
```

- **Expected result:**

```text
build approved | handoff mcp-server-bau-workflow | owner required
```

### Example 2 (Example data)

- **Task:** Second dry run
- **Input:** Example data only
- **Prompt:**
```text
Repeat workflow; no external writes.
```
- **Expected result:** Checklist only.
