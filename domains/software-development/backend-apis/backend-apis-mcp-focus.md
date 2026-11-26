---
id: backend-apis-mcp-focus
title: "Backend and APIs: MCP/Skill Focus"
domain: software-development
category: backend-apis
tags:
  - api
  - mcp
  - postgres
target_agents:
  - hermes
  - claude-code
  - cursor
  - generic-mcp-agents
required_tools:
  - name: postgres-mcp
    install: "Read-only DB MCP if listed"
    version_notes: "SELECT only default"
  - name: GitHub Official MCP
    install: "PR + OpenAPI in repo"
    version_notes: "Code search"
  - name: curl
    install: "verify HTTP"
    version_notes: "Skill verify step"
inputs:
  - "OpenAPI path in repo"
  - "DB read scope"
outputs:
  - "MCP matrix for API task"
  - "Verified curl transcript"
risk_level: medium
example_count: 2
version: "1.0.0"
updated: "2026-11-23"
---

## Purpose

API development with **GitHub MCP** (Spec in repo) and optional **Postgres MCP** read-only — HTTP Verify always curl/test in the skill.

## When to use

- Agent soll Schema + Code + DB-Sample kombinieren.
- Skill trennt DB-MCP read von HTTP verify.

**When not:** If no DB — only baking-apis-workflow.

## Tool stack

| Tool | Role | Justification |
|------|-------|------------|
| GitHub MCP | Spec search | openapi.yaml |
| Postgres MCP | Schema read | no writes |
| curl | Verify | real HTTP |

## System prompt

```text
Backend APIs MCP/Skill focus (software-development/backend-apis).

Skill: read spec (GitHub MCP) -> read schema (Postgres MCP SELECT only) -> implement locally -> verify curl/pytest.
Postgres MCP: never INSERT/UPDATE/DELETE without explicit approval and migration path.
GitHub MCP writes (PR) gated; draft diff only until approval.
One database MCP; no duplicate SQL tools.
OpenAPI from repo is source; MCP search for handlers matching path.
If MCP DB unavailable, fall back to described schema in migration files.
Verify step mandatory with curl exit 0 on happy path.
Redact connection strings from chat.
Matrix documents which MCP supplied each fact.
Disable DB MCP in prod connection strings unless user supplies staging DSN name.
```

## Workflow

1. GitHub MCP: find openapi.yaml and route handlers.
2. Postgres MCP: describe table columns (read).
3. Implement change in workspace.
4. pytest integration.
5. curl verify Skill step.
6. PR via gh after approval.
7. Matrix archived in PR comment draft.

## Definition of done

- [ ] HTTP verification documented
- [ ] DB MCP read-only eingehalten
- [ ] Spec and code synchronous

## Security

Prod-DB prohibited by MCP without release.
- Tokens in curl via env vars only.

## Pitfalls

Check MCP DB for incorrect DB — DSN.
- GitHub MCP write PR without Tests.
- Schema cache stale.
- Zwei SQL MCPs konkurrieren.

## Basic examples

### Example 1 (Example data (self-written))
- **Task:** Order endpoint + schema check.
- **Input:** table `orders`.
- **Prompt:**

```text
GitHub read openapi; postgres describe orders; implement; curl verify.
```

- **Expected result:**

```bash
curl -sf http://localhost:8080/v1/orders/1 -H "Authorization: Bearer test"
```

### Example 2 (Example data (self-written))
- **Task:** Block prod DSN.
- **Input:** user pastes prod url.
- **Prompt:**

```text
Refuse postgres MCP prod; use migrations sql read only.
```

- **Expected result:**

```text
MCP DB step skipped; schema from db/migrations/0003_orders.sql
```