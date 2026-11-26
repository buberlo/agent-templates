---
id: grokbot-workflow
title: "Grok Bot"
domain: agent-platforms
category: grokbot
tags:
  - grokbot
  - agent-platforms
  - product-connector
target_agents:
  - grokbot
  - generic-mcp-agents
required_tools:
  - name: Grok Bot Plugins / Custom MCP
    install: "https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp"
    version_notes: "Connect Apps, Custom MCP HTTPS/Command; Wiki 0.75.x–0.77.x"
  - name: Grok Bot 101
    install: "https://x.ai/bot/guides/grok-bot-101"
    version_notes: "Same plugin MCP model as Cursor"
inputs:
  - "Task description and desired tools"
  - "For Custom MCP: public HTTPS URL or command on the bot box"
outputs:
  - "Result in the bot thread with documented tool policies"
  - "List of blocked and allowed tools"
risk_level: low
example_count: 2
version: "1.0.0"
updated: "2026-11-23"
---

## Purpose

Running Grok Bot with **Connect Apps** (curated plugins) or **Custom MCP**: OAuth remains on the connector backend, the bot does not see raw tokens. Custom server only as public HTTPS or as command-process on the bot-computer, not as localhost on the user's laptop.

## When to use

Tasks require connected SaaS services via Connect Apps with fixed tool policies (Always allow / Needs approval / Blocked).
- You run MCP logic on the **bot box** (npx/uvx) and accept that shared bot teams can read Command and Args.

#### When not to use

- If you only have an MCP on `127.0.0.1` on the developer computer (without public HTTPS or Box Command). If you want to activate more than ~200 skills (Skill-Ceiling since Wiki 0.71.2). When secrets need to be safe in headers — Wiki does not mention a reliable secret header path for Custom MCP.

## Tool stack

| Tool | Role | Rationale |
|------|-------|-----------|
| Connect Apps | catalog-Plugins |OAuth auf Backend, Bot without Token|
| Custom MCP (HTTPS) | Remote Server | Streamable HTTP/SSE, publicly available |
| Custom MCP (Command) | Box-Runtime |npx/uvx auf Bot-Maschine; argv without Secrets|
| @-Attach | Context | Skills/Plugins on Task |
| Tool Policies | Risikosteuerung | Granular pro Tool (ab 0.70.2/1.2.3) |

## System prompt

```text
Du arbeitest als Grok Bot with Plugins and MCP. Nutze Connect Apps for Standard-Integrationen.
Custom MCP only: public HTTPS or Command on the bot box — never laptop localhost, never VPN-only without reachability.
No tokens, API keys or passwords in chat, skill texts or command arguments.
OAuth resides on the connector backend; never request raw credentials from the user.
Before destructive tools (write, send, delete, pay): Policy “Needs approval” or explicit release.
Block individual tools when the task needs them — less schema noise.
Observe skill ceiling of 200: only @-attach relevant skills.
If the connector is missing: work on the box (CLI/Files), do not start, a private MCP is connected.
Shared Bot: alle Command-Zeilen als for Team-Leser sichtbar behandeln.
After Document Creation: Verify (read/render) as usual in Document Skills.
```

## Workflow

Open Connect Apps; Select plugin and comply with the auth deadline.
Formulate the task; Apply appropriate skills with @ (stay under 200 skill ceiling).
3. Missing integration: plan a custom MCP — HTTPS endpoint or box command, never a local laptop host.
4. Tool-Policies setzen: kritische Tools auf Needs approval or Blocked.
5. Bot-Task starten; Ausgaben protokollieren.
6. Before Send/Write: Wait for approval or use policy dialogue.
7. For Command-MCP: check argv for secrets (environment variables on Box, not Args).
8. Briefly document results and policy list for audit.

## Definition of done

- [ ] No custom MCP on unreachable localhost/VPN-only without documented box alternative
- [ ] Tool policies match the risk (writes not “Always allow” without reason)
- [ ] No Credentials in argv, Chat or Skill-Files
- [ ] Only attached skills/tools that the task needs
- [ ] Document artifacts verified (read/render)

## Security

- Connect Apps: Tokens only on connector backend; bot requests no secrets in plain text.
- Command-Server auf Shared Bots: Team kann Befehlszeile lesen — no Keys in Args.
- Write, send, pay, deploy and delete only after approval or policy.

## Pitfalls

**localhost MCP:** User laptop MCP is invisible to the bot — instead HTTPS or Box Command.
- **argv-Secrets:** Wiki bans credentials in command arguments; Use Env on the box.
- **Skill-Ceiling 200:** Too many active skills lead to confusion or abort — targeted @-attach.
**Shared bot visibility:** Internal URLs or tokens in command lines are readable by members.
- **Marketing threads:** Apply viral “N GitHub MCP” lists on X unchecked — trust only Wiki/Connect apps.
- **No secret header:** According to the wiki, custom MCP has no secure header secret mechanism — adapt design accordingly.

## Basic examples

### Example 1 (Example data (self-written))
- **Task:** Linear tickets read via Connect App
**Input:** Connect app “Linear” connected; Task “Listen to Open Bugs of the Week”
- **Prompt:**
```text
@linear Use only reading tools. No status changes. Output as a markdown table (ID, title, status).
```
- **Expected result:**
```text
| ID | Titel | Status |
| LIN-101 | Login timeout | In Progress |
| LIN-104 | Footer link 404 | Todo |
(5 lines, no PATCH/POST executed)
```

### Example 2 (Example data (self-written))
- **Task:** Wrong custom MCP (localhost on developer machine)
- **Input:** User suggests `http://127.0.0.1:3847/mcp` on MacBook
- **Prompt:**```text
Connect my local MCP at localhost:3847.
```
- **Expected result:**
```text
Abort with reason: Bot reaches laptop-localhost not.
Suggestion: Start MCP on bot box as npx command OR public HTTPS with Auth on the server.
No attempt to pass token in argv.
```