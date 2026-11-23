---
id: generic-mcp-agents-mcp-focus
title: "Generic MCP agents: MCP and skill focus"
domain: agent-platforms
category: generic-mcp-agents
tags:
  - generic
  - agent-platforms
  - catalog
target_agents:
  - hermes
  - grokbot
  - generic-mcp-agents
  - generic
required_tools:
  - name: punkpeye/awesome-mcp-servers
    install: "https://github.com/punkpeye/awesome-mcp-servers"
    version_notes: "Directory only"
  - name: modelcontextprotocol/servers
    install: "https://github.com/modelcontextprotocol/servers"
    version_notes: "Reference server for protocol tests"
inputs:
  - "Planned MCP list with transport"
  - "Skill markdown with tool assignment"
outputs:
  - "MCP minimization report"
  - "Skill-MCP mapping table"
risk_level: low
example_count: 3
version: "1.0.0"
updated: "2026-11-23"
---

## Purpose

**MCP/Skill Focus** for any agent platform: which server covers which data source, which skill step calls which tool, where Verify renders and shares sit — following schema overhead, Grok transport rules, Hermes Platform filters and ClawHub Verify.

## When to use

- You optimize an overloaded MCP stack (symptom: slow starts, bad responses).
- Team documents Skill↔MCP matrix for onboarding.

###### When not to use

- If there is no skill yet — write sequence first, then MCP. If you use Reference Server directly in production without hardening.

## Tool stack

| Tool | Role | Rationale |
|------|-------|-----------|
| awesome-mcp-servers | Shortlist | Entries | Source repos |
| modelcontextprotocol/servers | Learning | Protocol, not Prod |
| Skill-Dokument | Orchestrierung | Steps, verify, gates |
| Plattform-MCP-CLI | Umsetzung | claude mcp / hermes mcp / openclaw mcp / Cursor settings |
| Tool allowlists | Safety | Read default |

## System prompt

```text
MCP/Skill Focus for Generic Agents. Create table: SkillStep | MCP | Tool | Read/Write | Sharing.
Jede Datenquelle maximal ein MCP; Duplikate zusammenlegen.
Messe impliziten Overhead: wenige breite Server oft besser als viele spezialisierte.
Schema token problem: remove unused MCPs from large tasks (reference ~67k overhead).
Skills carry Verify for documents (validate, render, re-read) — MCP write replaces the not.
ClawHub: verify (~12 % Malware Feb 2026) wenn Registry-Skills OpenClaw/Gateway tangieren.
Grok: Custom MCP HTTPS or Box-Command; argv without Secrets.
Hermes: Check Skill platforms tag.
OpenClaw: Tool-Policy pro MCP-Tool.
Cursor/Claude: mcp.json without PAT; Injection auf MCP content.
Reference servers nur in Dev-Sandbox.
Completion: minimization report (before/after MCP count, estimated tool count).
Write tools: Needs approval on all platforms where available.
```

## Workflow

1. Inventory: estimate all MCPs, tool number.
2. Open or create a skill document (steps numbered).
3. Pro Skill-Schritt MCP-Tool zuordnen or „lokal“ markieren.
4. Remove duplicates and unused servers.
5. Check transport rules (Grok HTTPS/Box, no laptop localhost).
6. Check registry skills in chain for verify status.
7. Read-only Smoke pro verbleibendem MCP.
8. Matrix ins Repo committen; Secrets redacted.
9. Pilot-Task; Retrospektive im minimization report.

## Definition of done

-[ ] skill MCP matrix completely for the task
- [ ] MCP number reduced or justified
- [ ] Verify render in Skill for document steps
- [ ] Plattform-Transport-Regeln eingehalten
- [ ] No Secrets in Matrix/Config
- [ ] ClawHub/Registry in Kette verifiziert falls verwendet

## Security

- MCP-Content untrusted; Write-Gates im Skill verankert.
- Registry-verify bei ClawHub-Pfad.
- Reference server not unhardened in Prod.

## Pitfalls

- **67k Overhead:** Matrix does not help if 10 MCPs remain — shorten.
- **Two MCPs, one source:** Double schema, conflicting tools.
- **Skill without tool column:** Agent chooses wrong MCP tool.
- **Verify nur in MCP:** Office braucht Skill-Script + Render.
- **ClawHub ~12 %:** Skill aus Registry in Matrix without verify-Zeile.
- **Grok argv secrets:** In Matrix as Command-MCP noted with Key in Arg — prohibited.

## Basic examples

### Example 1 (Real-world example)

- **Task:** Overhead reduzieren
- **Input:** 8 MCPs, 120 tools estimated
- **Prompt:**
```text
Build matrix, consolidate on 3 MCPs, re-estimate tool count.
```
- **Expected result:**
```text
Vorher: 8 MCPs / ~120 tools
Nachher: 3 MCPs / ~45 tools
minimization report committed (secrets redacted)
```

### Example 2 (Example data)

- **Task:** Document-Schritt in Matrix
- **Input:** Skill step 5 „deliver pptx“
- **Prompt:**
```text
Show MCP only for export if necessary; validate+render in Skill step 6–7.
```
- **Expected result:**
```text
| 5 | (local skill) | write deck | write | user |
| 6 | (local skill) | validate.py | read | auto |
| 7 | (local skill) | render png | read | auto |
Kein MCP in steps 6–7
```

### Example 3 (Example data)

- **Task:** Grok Box-Command Zeile
- **Input:** Custom MCP via npx auf Bot-Box
- **Prompt:**```text
Matrix-Eintrag: Command MCP without API_KEY in argv, nur env auf Box.
```
- **Expected result:**
```text
Command: npx @acme/mcp-server
Env: ACME_KEY (Box secret store)
Shared-bot Sichtbarkeit vermerkt
Kein localhost User-Laptop
```