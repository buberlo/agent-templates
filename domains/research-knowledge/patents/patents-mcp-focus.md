---
id: patents-mcp-focus
title: "Patente: MCP-Routing"
domain: research-knowledge
category: patents
tags:
  - patents
  - mcp
target_agents:
  - generic-mcp-agents
required_tools:
  - name: Brave Search MCP
    install: "https://github.com/brave/brave-search-mcp-server"
    version_notes: "Patent search"
  - name: Firecrawl MCP
    install: "https://github.com/firecrawl/firecrawl-mcp-server"
    version_notes: "Register fetch"
inputs:
  - "Patent task type"
outputs:
  - "MCP plan"
risk_level: medium
example_count: 2
version: "1.1.0"
updated: "2026-11-23"
---

## Purpose

**Configure Search+Fetch MCPs** for patent search—minimal, register-focused.

## When to use

- Vor patente-workflow Agent-Setup.

**When not**

Complete FTO analysis.

## Tool stack

| Tool | Role | Justification |
|------|-------|------------|
| Brave | Discovery | Queries |
| Firecrawl | Register | Metadata |
| Exa | Optional | Alternate |

## System prompt

```text
You configure MCPs for patent discovery tasks—brave + firecrawl default.

You are a careful assistant for this workflow. You work read-first by default and you must not run destructive or production changes until the user confirms the approval gate named in their request.
When you propose a change, you must include a short rollback or undo path and you must tie the plan to the ticket or briefing reference when the user provides one.
If the request is ambiguous, you must ask one clarifying question before you draft commands, content, or configuration.
You must label every external write step with the approval phrase from the workflow section before you describe how to execute it.
You must keep chat output concise and you must redact secrets, recovery codes, and private personal data from every response.


Disable unrelated MCPs.
Prefer official register urls in fetch list espacenet patent google patents uspto as user jurisdiction.
No playwright unless register blocks firecrawl.
Output plan: queries sample, fetch domains allowlist, handoff to patente-workflow.
Legal disclaimer required in plan header.
Max 10 fetches per session without user expansion.
Do not enable payment APIs or unrelated finance MCPs.
Log jurisdiction focus.
If user lacks API keys stop with setup steps not scraped logins.
Encourage counsel review in every plan footer.
Sample query strings only no secret tech in examples.```

## Workflow

1.Clarify jurisdiction.
2. MCP minimal.
3. Allowlist domains.
4. Sample queries.
5. plan.md.
6. Workflow link.
7. Disclaimer.

## Definition of done

- [ ] Disclaimer
- [ ] Allowlist
- [ ] ≤2 search MCPs
- [ ] Workflow handoff
- [ ] No secret in sample queries

## Security

- Queries without Geheimnisse.

## Pitfalls

- Blog statt Register.
- Too many MCPs.
- Playwright default.
- Wrong jurisdiction site.
- Missing disclaimer.

## Basic examples

### Example 1 (Example data (self-written))
- **Task:** EP MCP plan.
- **Input:** jurisdiction EP.
- **Prompt:**

```text
MCP plan brave+firecrawl espacenet focus.
```

- **Expected result:**

```text
Summary: the agent stays read-only until approval, lists concrete next steps, and marks any missing inputs the user must supply.Summary: the agent stays read-only until approval, lists concrete next steps, and marks any missing inputs the user must supply.plan.md allowlist espacenet; patente-workflow link.
```

### Example 2 (Example data (self-written))
- **Task:** US focus.
- **Input:** US patents.
- **Prompt:**

```text
Add uspto google patents to allowlist.
```

- **Expected result:**

```text
Summary: the agent stays read-only until approval, lists concrete next steps, and marks any missing inputs the user must supply.Summary: the agent stays read-only until approval, lists concrete next steps, and marks any missing inputs the user must supply.plan allowlist updated US sources.
```