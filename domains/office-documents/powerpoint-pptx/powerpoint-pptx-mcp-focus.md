---
id: powerpoint-pptx-mcp-focus
title: "PowerPoint PPTX: Skill-Fokus"
domain: office-documents
category: powerpoint-pptx
tags:
  - pptx
  - skill
target_agents:
  - hermes
  - openclaw
  - generic-mcp-agents
required_tools:
  - name: Anthropic document skills (pptx)
    install: "https://github.com/anthropics/skills"
    version_notes: "Official"
  - name: Hermes microsoft-office
    install: "https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/productivity/productivity-microsoft-office"
    version_notes: "pptx scripts"
inputs:
  - "pptx-Task"
outputs:
  - "Tool-Routing"
  - "Verify-Checkliste"
risk_level: low
example_count: 2
version: "1.1.0"
updated: "2026-11-23"
---

## Purpose

**PPTX-Skills** gezielt laden—Anthropic vs. Hermes vs. OpenClaw—with Verify-Checkliste statt generischem Office-MCP-Buendel.

## When to use

- Agenten-Setup for Praesentations-Tasks.
- Audit existder .pptx before Event.
- Token-Budget for Document-Skills plan.

**When not to use**

- Vollstaendiges Deck from Briefing (→ powerpoint-pptx-workflow).

## Tool stack

| Tool | Role | Rationale |
|------|-------|------------|
| Anthropic pptx | Write/validate | Offiziell |
| Hermes microsoft-office | pptx read | Bundled |
| ClawHub pptx skills | OpenClaw | Optional |

## System prompt

```text
You configure minimal tools for pptx tasks.

Routing:
- Claude Code with document-skills → Anthropic pptx primary
- Hermes only environment → microsoft-office pptx CLIs
- openclaw user → verified ClawHub skill if named

Audit mode: slide count, title list, embedded media count, notes presence—read only.

Never enable xlsx/docx MCPs unless user adds tasks same session.

Verify checklist after any write:
1) skill validator
2) optional soffice pdf export
3) thumbnail spot check slide 1 and last

Approvals: overwrite template.pptx on share drive needs yes.

Output: enabled tools list, verify checklist markdown, link to workflow template for builds.

Do not promise pixel-perfect match to PowerPoint desktop.

Warn when animations requested—python-pptx limitations.

If encrypted pptx, stop until password from user secure channel.
List embedded fonts licensing risk when customer brand fonts used.
```

## Workflow

1. Umgebung erkennen (Claude/Hermes/OpenClaw).
2. only pptx-Tools enable.
3. audit or build-Handoff clarify.
4. Verify-Checkliste ausgeben.
5. at build → workflow-Template referenzieren.
6. Token-Hinweis at vielen MCPs.
7. Log the gewaehlten Skill-Version.

## Definition of done

- [ ] Maximal pptx-relevante Tools aktiv
- [ ] Verify-Checkliste geliefert
- [ ] Build an workflow verwiesen
- [ ] no Overwrite without approval
- [ ] Limitationen (Animation) genannt

## Security

- Decks with Insider-Info not in oeffentliche Skills loggen.
- approval before Share-Link.
- no API-Keys in Notizen.

## Pitfalls

- document-skills Plugin only docx geladen.
- ClawHub-Skill unverifiziert.
- PDF-QA viasprungen.
- Master-Slides kaputt after python-pptx.
- Grosse Medien without Kompression.

## Basic examples

### Example 1 (Example data (self-written))
- **Task:** Claude Code Setup.
- **Input:** User will edit investor.pptx.
- **Prompt:**

```text
Route tools for pptx audit + safe edits; minimal MCP; verify checklist.
```

- **Expected result:**

```text
Anthropic pptx + audit table; checklist 3 steps; no xlsx MCP.
```

### Example 2 (Example data (self-written))
- **Task:** Hermes-only Server.
- **Input:** Build new deck.
- **Prompt:**

```text
Hermes path only; hand off to powerpoint-pptx-workflow with CLI names.
```

- **Expected result:**

```text
Route: Hermes microsoft-office; workflow link; Claude skill not assumed.
```