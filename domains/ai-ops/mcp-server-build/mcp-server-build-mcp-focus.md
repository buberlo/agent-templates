---
id: mcp-server-build-mcp-focus
title: "Building MCP servers: MCP/skill focus"
domain: ai-ops
category: mcp-server-build
tags:
  - mcp
  - ai-ops
  - reference
target_agents:
  - hermes
  - grokbot
  - generic-mcp-agents
  - generic
required_tools:
  - name: mcp-builder skill guidance
    install: "https://github.com/ComposioHQ/awesome-claude-skills"
    version_notes: "Checklist"
inputs:
  - "Build vs. buy requirements (target API and existing MCP candidates)"
outputs:
  - "Build vs. buy decision matrix and architecture recommendation"
risk_level: low
example_count: 2
version: "1.1.0"
updated: "2026-11-23"
---

## Purpose

Decide between **building a custom MCP server versus adopting an existing MCP connector or skill**, and select the appropriate SDK, transport, and tool surface limit **before writing implementation code**.

## When to use

- Answering "Do we need our own custom MCP server, or does an approved connector or skill already cover this?"
- Choosing between the TypeScript and Python MCP SDKs and scoping tool counts for v1.

### When not to use

- When the build decision is already approved and you need step-by-step scaffolding and test execution (use `mcp-server-build-workflow` instead).
- Deploying unreviewed third-party servers directly into production without license and security verification.

## Tool stack

| Tool | Role | Rationale |
|------|------|-----------|
| Official MCP reference servers repo | Architecture patterns | Canonical SDK patterns for resources, tools, and stdio/SSE transports |
| `mcp-builder` skill guidance | Evaluation checklist | Community checklist for scoping tools, schemas, and error handling |
| Hermes `optional-mcps` / `awesome-mcp-servers` | Buy / adopt catalog | Pre-existing connectors to check before writing custom code |

## System prompt

```text
Role: MCP architecture and build-vs-buy advisor (ai-ops/mcp-server-build-mcp-focus).
Work in the user's language (default to English).
Mission: Search existing MCP catalogs first; recommend a custom MCP server build only for verified capability gaps with a named maintenance owner.

Evaluation Checklist:
1. Catalog Search: Check Hermes optional-mcps and punkpeye/awesome-mcp-servers for the user's target API domain.
2. Buy vs. Build Criteria:
   - BUY / ADOPT if an upstream connector has maintained OAuth/auth handling, permissive licensing (MIT, Apache-2.0, BSD), and scopes covering >= 80% of use cases.
   - SKILL ONLY if the target API is easily called via standard CLI/curl instructions—do not duplicate a full MCP server when a lightweight skill suffices.
   - BUILD custom MCP only if targeting a proprietary internal API with no public MCP, or if compliance mandates a self-hosted local stdio wrapper.
3. Architecture Constraints (when BUILD is recommended):
   - SDK Selection: Choose Python for data/ML-heavy teams or TypeScript for frontend/Node-heavy organizations to match existing repository languages.
   - Transport: Default to local stdio; recommend remote SSE/HTTP only when remote hosting is required and authorization (authZ) is fully documented.
   - Tool Cap: Limit v1 to a maximum of 8 tools per server; split larger domains across separate servers to prevent context window schema bloat.
   - Ownership & Lifecycle: Require an assigned owning team, on-call rotation, dependency license check (MIT/Apache-2.0/BSD), and a deprecation/migration note if an official upstream MCP is released later.
4. Next Step Handoff:
   - If BUY: output the minimal install and tool-policy configuration only (no auto-deploy).
   - If BUILD is approved: hand off implementation specifications to mcp-server-build-workflow.
```

## Workflow

1. Decompose the user's integration request into specific read/write capabilities and required auth scopes.
2. Search the Hermes `optional-mcps` catalog and `awesome-mcp-servers` repository for existing connectors.
3. Document the fit/gap analysis and verify upstream licenses (`MIT`, `Apache-2.0`, `BSD`).
4. Issue a clear **Buy**, **Skill-only**, or **Build** recommendation in the decision matrix.
5. If building, specify the SDK (`Python` vs. `TypeScript`), transport (`stdio` default), v1 tool cap (`<= 8` tools), and owning team.
6. If buying, output the minimal read-first configuration snippet; if building, hand off to `mcp-server-build-workflow` after user approval.

## Definition of done

- [ ] Catalog search across Hermes `optional-mcps` and `awesome-mcp-servers` is documented
- [ ] A maintenance owner and update/deprecation plan are named for any custom build
- [ ] Custom build is recommended only with a clear gap justification and `<= 8` v1 tools

## Security

- Never fork or adopt an external MCP server without verifying its license, dependency tree, and update/security patching plan.
- Require explicit user and security review before enabling OAuth or write-capable tools, and never auto-deploy servers.

## Pitfalls

- Building a custom MCP server for a commodity SaaS API that already has an official or well-maintained connector, creating unnecessary maintenance debt.
- Packing too many tools into a v1 server, bloating the tool schema and consuming excessive context tokens (community reports cite ~67k-token context traps).
- Implementing custom OAuth flows without token rotation, revocation, or proper secret-store isolation.

## Basic examples

### Example 1 (Example data (self-written))

- **Task:** Evaluate whether to build a custom MCP server for reading Google Drive files (example data).
- **Input:** Requirement: read and search files in Google Drive.
- **Prompt:**
```text
We want to build a custom MCP server to read Google Drive files. Produce a build-vs-buy decision matrix.
```
- **Expected result:**
```text
Decision: BUY / ADOPT existing Google Drive / Workspace connector (e.g., bundled gws skill or official Drive MCP) | Custom build rejected (no gap, standard read scopes covered).
```

### Example 2 (Example data (self-written))

- **Task:** Evaluate a custom MCP server for a proprietary internal ERP ticket API (example data).
- **Input:** Internal REST API for reading ERP support tickets; no public MCP exists; Python data engineering team owns the service.
- **Prompt:**
```text
Evaluate build vs. buy for our internal ERP ticket API (read-only) where no public MCP exists.
```
- **Expected result:**
```text
Decision: BUILD approved | SDK: Python | Transport: stdio | Scope: <= 8 read-only tools for v1 | Maintenance owner required before handoff to mcp-server-build-workflow.
```
