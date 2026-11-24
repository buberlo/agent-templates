---
id: skills-authoring-workflow
title: "Skills authorisieren"
domain: ai-ops
category: skills-authoring
tags:
  - skills
  - ai-ops
  - authoring
target_agents:
  - hermes
  - grokbot
  - generic-mcp-agents
  - generic
required_tools:
  - name: SKILL.md convention
    install: "https://code.claude.com/docs/en/features-overview"
    version_notes: "Progressive disclosure"
  - name: Hermes / OpenClaw skills
    install: "skills install verify"
    version_notes: "Verify vor Prod"
inputs:
  - "Skill Purpose and Trigger Phrases"
  - "Linked MCPs (minimum)"
outputs:
  - "SKILL.md"
  - "Verify-Schritte"
risk_level: low
example_count: 2
version: "1.1.0"
updated: "2026-11-23"
---
## Purpose

**Skills as lean workflows**: SKILL.md with clear when/what, progressive disclosure, Verify before writing actions — do not duplicate MCP.

## When to use

- Team reuses the same agent flow.
OpenClaw/Hermes Skill catalogue.

## Tool stack

| Tool | Role | Rationale |
|--------------------------------------------------------------------------------------------------------------------------------
| SKILL.md | Instruction | No code compulsion |
| MCP | Tools | Separate |
| skills verify | Trust | OpenClaw |

## System prompt

```text
Role: skill author (ki-ops/skills-authoring).
Mission: Write SKILL.md that triggers on user intents lists required mcps and links template ids.

Skill frontmatter: name description when_to_use one paragraph triggers bullet phrases.
Body sections: Purpose When not Steps DoD Safety Examples keep under 150 lines initial.
Progressive: detail advanced steps collapsed heading optional readme sibling file.
MCP: reference by catalog name do not paste full tool json schemas into skill.
Verify step mandatory before write send pay delete re-read file or screenshot per org policy.
Version skill semver in filename or metadata changelog one line per release.
Testing: run three dry conversations trigger phrases must load skill without false positive other domains.
Install doc: openclaw skills install path hermes skills path cursor skills path if applicable.
Security: no api keys in skill; env var names only.
Relation: one skill one domain folder match domains/*/category pattern when business skill.
Anti duplicate: if identical to existing skill merge not fork.
Handoff prompt-engineering-workflow for system prompt inside skill long form.
Publish clawhub only if org allows supply chain verify owner reputation.
```## Workflow

1. Define trigger phrases and non-targets.
Create SKILL.md structure.
link MCP list minimally.
4. Install Verify step for writes.
5. Three trigger tests dialogically.
6. `skills verify` when OpenClaw.
7. Version and Changelog committen.

## Definition of done

Clear triggers without overmatch
- [ ] Verify before writing actions
No secrets in the skill.
- [ ] MCP list minimal

## Security

- Verify ClawHub skills before Prod.

## Pitfalls

- Skill replaces MCP-Doku → Tools are missing.
- Too wide trigger → wrong skill activation.
- Huge skill file → token load on every turn.

## Basic examples

### Example 1 (Example data (self-written))
- **Task:** n8n Draft Skill
- **Input:** trigger "n8n workflow"
* Prompt: *

```text
SKILL.md links n8n-make-zapier-workflow verify before activate.
```

- **Expected result:**

```text
skill file | 3 trigger tests pass | mcp n8n only
```

### Example 2 (Example data (self-written))
- **Task:** API key in skill
- **Input:** stripe_sk_live in example
- **Prompt:**

```text
Paste real key so agent works.
```

- **Expected result:**

```text
reject | STRIPE_API_KEY env name only
```

### Example 2 (Example data (self-written))
- **Task:** Second dry run
- **Input:** Example data only
- **Prompt:**
```text
Repeat workflow; no external writes.
```
- **Expected result:** Checklist only.
