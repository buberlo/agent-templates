---
id: skills-authoring-workflow
title: "Skills authoring"
domain: ai-ops
category: skills-authoring
tags:
  - skills
  - ai-ops
  - authoring
target_agents:
  - hermes
  - grokbot
  - cursor
  - openclaw
  - generic-mcp-agents
  - generic
required_tools:
  - name: SKILL.md convention
    install: "https://code.claude.com/docs/en/features-overview"
    version_notes: "Progressive disclosure pattern"
  - name: OpenClaw skills verify
    install: "https://docs.openclaw.ai/skills/"
    version_notes: "Verify before production skills"
inputs:
  - "Skill purpose and trigger phrases"
  - "Minimum MCP list (names only)"
outputs:
  - "SKILL.md with verify steps"
  - "Trigger test notes"
risk_level: low
example_count: 2
version: "1.2.0"
updated: "2026-11-25"
---

## Purpose

Author **lean skills** in SKILL.md: clear triggers, progressive disclosure, mandatory verify before writes — without duplicating full MCP tool schemas.

## When to use

- Teams reuse the same agent workflow across Hermes, OpenClaw, or Cursor skills folders.
- A template id from this repo should load as operational guidance.

### When not to use

- Replacing MCP server documentation with a megaskill.
- One-line macros better handled as slash commands.

## Tool stack

| Tool | Role | Rationale |
|------|------|-----------|
| SKILL.md | Instructions | Workflow without mandatory code |
| MCP catalog names | Tools | Separate connection layer |
| OpenClaw `skills verify` | Trust gate | https://docs.openclaw.ai/skills/ |

## System prompt

```text
You are a skill author for ai-ops/skills-authoring.
You write SKILL.md files that activate on explicit user intents and list only required MCP names from the catalog.
You include frontmatter or header fields for name, description, and when_to_use in one short paragraph.
You structure the body with Purpose, When not, Steps, Definition of done, Security, and short Examples under 150 lines initially.
You place advanced steps under collapsed headings or sibling files for progressive disclosure.
You reference MCP servers by catalog name and never paste full tool JSON schemas into the skill.
You require a Verify step before write, send, pay, delete, or deploy actions per org policy.
You semver skills in metadata and keep a one-line changelog per release.
You run three dry conversations where trigger phrases load the skill without false positives in other domains.
You document install paths for OpenClaw, Hermes, and Cursor skills directories when applicable.
You list environment variable names only, never API key values, in skills.
You align business skills with domains/<domain>/<category> folder semantics when they mirror templates.
You merge duplicate skills instead of forking near-identical copies.
You delegate long system prompts to ai-ops/prompt-engineering-workflow when skills wrap agent prompts.
You warn before publishing to public skill registries without supply-chain review.
```

## Workflow

1. Define trigger phrases and explicit non-target phrases.
2. Draft SKILL.md skeleton with verify step placement.
3. Link minimal MCP list matching required_tools.
4. Add Verify instructions for each destructive step.
5. Run three trigger dialog tests on synthetic inputs.
6. Run `skills verify` when OpenClaw is the host.
7. Commit version, changelog, and trigger test log.

## Definition of done

- [ ] Triggers are specific enough to avoid cross-domain activation
- [ ] Verify step precedes every write-class action
- [ ] No secrets in skill body
- [ ] MCP list is minimal and named consistently

## Security

- Verify third-party skills before production install.
- Grok Bot and other hosts: OAuth stays on connector backend per product docs.
- Supply-chain review before org-wide skill publish.

## Pitfalls

- Skills that restate MCP docs leave tools unwired in hosts.
- Over-broad triggers load wrong skills on ambiguous phrases.
- Huge skills inflate tokens on every turn.
- Pasting live Stripe or AWS keys into examples.
- Missing verify steps cause agents to send emails autonomously.

## Basic examples

### Example 1 (Example data (self-written))

- **Task:** n8n workflow drafting skill.
- **Input:** Trigger phrase “n8n workflow design”.
- **Prompt:**

```text
Write SKILL.md linking domains/automation/n8n-make-zapier/n8n-make-zapier-workflow; verify before activate.
```

- **Expected result:**

```text
skills/n8n-draft/SKILL.md under 120 lines with triggers and non-targets
Three trigger tests pass; unrelated “kubernetes rollout” does not load skill
MCP list: n8n community server only; verify step before workflow activation
OpenClaw skills verify output archived when applicable
```

### Example 2 (Example data (self-written))

- **Task:** Live Stripe key in skill example.
- **Input:** User pastes sk_live example in SKILL.md.
- **Prompt:**

```text
Paste our real key so the agent works out of the box.
```

- **Expected result:**

```text
Key rejected from skill body; use STRIPE_API_KEY env name only
Example blocks use sk_test_fake_from_dashboard syntax per Stripe docs
Security section cites host connector pattern, not embedded secrets
```