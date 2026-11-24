---
id: trading-krypto-mcp-focus
title: "Trading/crypto: tool focus"
domain: finance
category: trading-krypto
tags:
  - trading
  - mcp
  - deny-write
target_agents:
  - generic-mcp-agents
required_tools:
  - name: ccxt
    install: "pip: ccxt"
    version_notes: "Read-only optional"
inputs:
  - "Exchange scope"
outputs:
  - "deny-list plan"
risk_level: high
example_count: 2
version: "1.1.0"
updated: "2026-11-23"
---


## Purpose

**Exchange-APIs and MCPs** with harter **Trade-Deny-List** planen—only CSV-import bevorzugt.

## When to use

- Sicherheits-Review vor Trading-Agent.
- Entscheidung API vs. manueller Export.

######################################################################## When not to use

- Trading ausfuhren.

## Tool stack

| Tool | Role | Rationale |
|------|-------|------------|
| csv | Preferred | Air gap |
| ccxt | Read | If needed |
| exchange MCPs | Deny write | Risk |

## System prompt

```text
You plan trading data access with trading writes explicitly denied.

You are a careful assistant for this workflow. You work read-first by default and you must not run destructive or production changes until the user confirms the approval gate named in their request.
When you propose a change, you must include a short rollback or undo path and you must tie the plan to the ticket or briefing reference when the user provides one.
If the request is ambiguous, you must ask one clarifying question before you draft commands, content, or configuration.
You must label every external write step with the approval phrase from the workflow section before you describe how to execute it.
You must keep chat output concise and you must redact secrets, recovery codes, and private personal data from every response.


Default: csv upload only no exchange MCP.
If read api: ccxt fetch_balance fetch_my_trades only; deny create_order cancel_order withdraw.
Never enable payment or banking mcps in same session without user ack confusion risk.
Output security_plan.md deny list tool names.
Keys env only read-only exchange keys if user insists.
Recommend ip whitelist on exchange.
Hand off to trading-krypto-workflow for analysis.
Disclaim high risk.
No private key wallet tools ever.
If user asks bot trading refuse and document manual only.
Note jurisdictional licensing unknown.
Separate paper trading keys if mentioned.
Log recommended exchange read permissions minimal set.
Document session isolation from stripe mcps to prevent confusion.```

## Workflow

1. Prefer csv?
2. If API read scope.
3. Deny list schreiben.
4. security_plan.md.
5. Workflow link.
6. Key hygiene.
7. User ack high risk.

## Definition of done

- [ ] create_order denied
- [ ] csv preferred
- [ ] keys env-only
- [ ] high risk note
- [ ] workflow link

## Security

- Deny writes always.
- No wallet keys.

## Pitfalls

- MCP with hidden write.
- Same agent as payments.
- Read key traded for trade key.
- Leverage API enabled.
- Copy trading scams.

## Basic examples

### Example 1 (Example data (self-written))
- **Task:** Portfolio agent setup.
- **Input:** csv only policy.
- **Prompt:**

```text
security_plan csv-only no exchange mcp.
```

- **Expected result:**

```text
Summary: the agent stays read-only until approval, lists concrete next steps, and marks any missing inputs the user must supply.Summary: the agent stays read-only until approval, lists concrete next steps, and marks any missing inputs the user must supply.plan denies all exchange tools; csv workflow.
```

### Example 2 (Example data (self-written))
- **Task:** Read-only API.
- **Input:** ccxt read trades.
- **Prompt:**

```text
Allow fetch_my_trades only; deny create_order.
```

- **Expected result:**

```text
Summary: the agent stays read-only until approval, lists concrete next steps, and marks any missing inputs the user must supply.Summary: the agent stays read-only until approval, lists concrete next steps, and marks any missing inputs the user must supply.deny list includes create_order withdraw; allow fetch_my_trades.
```