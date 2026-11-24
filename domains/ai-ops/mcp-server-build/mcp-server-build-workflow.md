---
id: mcp-server-build-workflow
title: "MCP-Server bauen"
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
  - name: MCP TypeScript/Python SDK
    install: "https://github.com/modelcontextprotocol/sdk"
    version_notes: "stdio transport default"
  - name: modelcontextprotocol/servers
    install: "https://github.com/modelcontextprotocol/servers"
    version_notes: "Referenzmuster"
inputs:
  - "API or data source, desired tools"
  - "Auth-Muster (env, OAuth)"
outputs:
  - "MCP-Server Repo-Skeleton"
  - "mcp.json Client-Config"
  - "Tool-Schema-Review"
risk_level: medium
example_count: 3
version: "1.1.0"
updated: "2026-11-23"
---
## Purpose

**Build your own MCP server**: stdio, clear tool schemes, keep secrets out of argv — oriented to modelcontextprotocol/servers.

## When to use

- Internal API should become agent-capable.
- Wrapper around CLI with structured tools.

## Tool stack

| Tool | Role | Rationale |
|-------------------------------------------------------------------------------------------------------------------------
| @modelcontextprotocol/sdk | Implementation | Official |
| Reference Server | Pattern | filesystem, fetch |
| mcp-inspector | Debug | Local test |

## System prompt

```text
Role: MCP server engineer (ki-ops/mcp-server-bau).
Mission: Ship minimal read-only server first; no secrets in argv or tool descriptions.

Scaffold ts: npm create from sdk sample or clone pattern from servers repo fetch filesystem.
Tools: one tool one responsibility; json schema input strict additionalProperties false.
stdio only unless user needs sse document threat model for remote.
Auth: read API_KEY from env in server bootstrap never from mcp client config args list.
Logging: stderr only; never log secrets or full responses with pii.
Errors: mcp spec structured error messages user-facing safe.
Version: semver server package; pin in client mcp.json command npx package@version.
Testing: mcp-inspector or claude desktop config local before hermes publish.
Rate limit: exponential backoff on upstream http 429 in tool impl.
Timeouts: axios fetch 30s default document override.
Write tools: suffix _write require confirmation string param user_ack boolean default false.
README: install run env vars table no real keys.
Publish: optional npm; internal git url for enterprise.
Compliance: grok wiki rule no credentials in command argv for custom mcps cite in readme.
Handoff security review before prod connector deploy.
```## Workflow

1. List data source and read/write classes.
2. Outline tools as a JSON scheme.
Create SDK skeleton (TS/Python).
4. Implement first read-only tools.
5. Local test with Inspector/Client-Config.
6. Secure writing tools with user ack.
7. README and env-Var documentary without secrets.

## Definition of done

-[ ] stdio server starts in client
- [ ] No secrets in argv
Validate [ ] tool schemes
- [ ] Inspector/Smoke test logged

## Security

Prod connector only after security review.
- OAuth only via supported flow.

## Pitfalls

- Enable only required tools.


- Huge tool descriptions → token overhead.
- Generic `execute` tool → prompt injection.
Stderr full of PII.

## Basic examples

### Example 1 (Example data (self-written))
- **Task:** Tickets read-only
- **Input:** REST /tickets
- **Prompt:**

```text
MCP tools list_tickets get_ticket env TICKET_API_KEY.
```

- **Expected result:**

```text
server starts | two tools | mcp.json snippet
```

### Example 2 (Example data (self-written))
- **Task:** Passwort in config
- **Input:** args -p secret123
- **Prompt:**

```text
Quick mcp.json command line password.
```

- **Expected result:**

```text
reject argv secret | use env var pattern
```

### Example 3 (Example data (self-written))
- **Task:** mcp-builder skill
- **Input:** awesome-claude-skills
- **Prompt:**

```text
Follow community skill checklist for new server.
```- **Expected result:** README checklist themes: schemas, auth, testing; Source: awesome-claude-skills.