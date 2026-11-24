---
id: hermes-workflow
title: "Hermes Agent (Nous Research)"
domain: agent-platforms
category: hermes
tags:
  - hermes
  - agent-platforms
  - agent-platform
target_agents:
  - hermes
  - generic-mcp-agents
required_tools:
  - name: Hermes Agent
    install: "https://github.com/NousResearch/hermes-agent"
    version_notes: "265550 GitHub Stars; Quickstart Desktop or CLI"
  - name: Nous-approved MCP-catalog
    install: "https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp"
    version_notes: "66 optional mcps; deactivated by default; Hermes MCP install"
inputs:
  - "Task briefing with desired result and risk level"
  - "Optional: Repo-Pfad, Ticket-IDs, URLs"
outputs:
  - "Nachvollziehbares result (Datei, Zusammenfassung or Ticket-Update)"
  - "Protocol of activated MCPs/Skills and Delegation Steps"
risk_level: low
example_count: 2
version: "1.0.0"
updated: "2026-11-23"
---

## Purpose

Use Hermes as a locally configurable agent platform: Skills control behavior, the Nous MCP catalogue provides data sources, optionally delegate coding loops to Claude Code or Codex without loading an uncontrolled tool zoo each time.

## When to use

- You need a **least privilege** start (few MCPs) and only want to expand if necessary (`hermes mcp install`, skills from catalogue).
- Aufgaben passen zu Slash-Commands or Skills wie `/github`, Research- or Dokumentations-Flows.

#### When not to use

- If you need ClawHub community skills without Nous review (OpenClaw is the registry focus). If the task needs a pure macOS-only-skill platform and you work on Linux — `platforms: [macos] is quietly skipped.

## Tool stack

| Tool | Role | Rationale |
|------|-------|-----------|
| Hermes Agent | Orchestrator | Skills, Memory, Cron, Tool Gateway, Delegation |
| Nous-approved MCP catalogue | Curated access | Only PR-merged `optional-mcps/`; Secrets about Install Card |
| Skills (~/.hermes/skills) | Ablauf & progressive disclosure | Getrennt von MCP-Verbindungen |
| Optional Delegation | Coding Runtime | Codex/Claude Code only for the implementation loop |

## System prompt

```text
You work on Hermes (Nous Research). Minimize active MCPs: only install what the task needs.
Skills liefern Prozedur, MCP liefert Daten/Aktionen — not verwechseln.
Before write, send, deploy or delete actions: obtain explicit user sharing.
Bei Dokument-Outputs: erzeugen → validate (falls Skill) → Render (PDF/PNG) → Datei erneut lesen.
Check skills with platforms filters; Under Linux, macOS-only skills are skipped.
Tokens nie in Chat, Skill-Files or MCP-Command-argv.
Log each tool call in a short line (tool, purpose, result status).
If coding is required: Delegation to Codex/Claude Code, complete review in the Hermes thread.
For sync conflicts: respect local deletions; Restore only with Hermes skills reset --restore.
Include/exclude for MCP and Skills nutzen, statt alles eingeschaltet zu lassen.
```

## Workflow

1. `hermes setup` or portal open; Check the actual state of the MCPs with `hermes mcp` (default: off).
2. Decompose task into briefing, risk and desired artifact.
3. Only install appropriate skills (hermes skills install) and add MCPs from the Nous catalogue.
4. Include/exclude so that prompt budget and permissions remain minimal.
5. Start the agent thread; Select slash command or skill trigger.
6. Check the result; for documents, follow the Verify render path of the skill document.
7. submit optional coding to delegation; Review changes in the Orchestrator.
8. File artifact and tool log for reproducibility.

## Definition of done

- [ ] Only MCPs/Skills required for the task were active (traceable listed)
- [ ] No write/send action without documented release
- [ ] Result corresponds to briefing; for Office/PDF: validator or visual render checked
- [ ] Platforms filter tested (no silently missing macOS skill on Linux)
- [ ] Delegation (if used) completed in the Hermes thread, not only in the sub-agent

## Security

- MCP entries preferably come from the Nous catalogue; Custom server only after review.
- Secrets about Hermes install cards/OAuth, never in prompts or argv.
- Write, send, pay, deploy and delete only after explicit approval.
- Document skills: after generating validate and visually render (verify step).

## Pitfalls

- **Platforms filter:** Skills with `platforms: [macos]` do not run on Linux without error message — The task is “broken”. Source: Community report in Hermes Category Research.
**Skill sync:** Sync does not blindly overwrite local deletions; Accidentally deleted skills need hermes skills reset --restore.
**MCP flood:** Too many concurrent MCPs inflate tool schemes and context (see also 67k token measurement on other clients).
- **Skill vs. MCP:** Just activating MCP is not enough if the process is in a skill manual.
- **Delegation without review:** Codex/Claude Code with writing right without feedback generates contradictory commits.

## Basic examples

### Example 1 (Example data (self-written))
- **Task:** GitHub Issue triage with minimal MCP set
- **Input:** Issue URL `https://github.com/org/repo/issues/42`, short briefing “labels and draft comments”
- **Prompt:**
```text
Installiere nur github-MCP aus dem Nous-catalog. Lies Issue #42, schlage Labels vor.
Do not post a comment without my release. Log every MCP call.
```
- **Expected result:**
```text
Issue title + body summary (3 sentences)
Label-Vorschlag: bug, needs-triage
Entwurf-Kommentar in Markdown (not gepostet)
Log: github.get_issue OK, github.list_labels OK
```

### Example 2 (Example data (self-written))
- **Task:** Use Hermes skill with macOS platform under Linux
- **Input:** Skill from browse list with `platforms: [macos]` for desktop automation
- **Prompt:**
```text
Execute the macos-only Skill for Calendar export.
```
- **Expected result:**
```text
Skill is not loaded (silently skipped).
Agent reports: no suitable skill for this platform — Alternative: choose manual export or Linux-compatible skill.
```