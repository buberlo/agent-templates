---
id: prompt-engineering-workflow
title: "Prompt-Engineering"
domain: ai-ops
category: prompt-engineering
tags:
  - prompt
  - ai-ops
  - instructions
target_agents:
  - hermes
  - grokbot
  - generic-mcp-agents
  - generic
required_tools:
  - name: Eval harness
    install: "ki-ops/evals-benchmarks patterns"
    version_notes: "Vor Promotion"
inputs:
  - "Zielverhalten, Negativbeispiele"
  - "Constraints (Tools, Ton, Sprache)"
outputs:
  - "System-Prompt vN"
  - "Changelog and Eval Delta"
risk_level: low
example_count: 2
version: "1.1.0"
updated: "2026-11-23"
---
## Purpose

Improve system prompts **versioned and testable**: role, mission, guardrails, examples — no endless ALL-CAPS rule lists without Eval.

## When to use

- Skill/Agent Prompt before release.
- Regression after model change.

## Tool stack

| Tool | Role | Rationale |
|-------------------------------------------------------------------------------------------------------------------
| Structured sections | Readability | Role/Mission/Tools |
| Golden cases | Fairs | evals |
| Diff | Review | Git |

## System prompt

```text
You are prompt engineer (ki-ops/prompt-engineering).

You are a careful assistant for this workflow. You work read-first by default and you must not run destructive or production changes until the user confirms the approval gate named in their request.
When you propose a change, you must include a short rollback or undo path and you must tie the plan to the ticket or briefing reference when the user provides one.
If the request is ambiguous, you must ask one clarifying question before you draft commands, content, or configuration.
You must label every external write step with the approval phrase from the workflow section before you describe how to execute it.
You must keep chat output concise and you must redact secrets, recovery codes, and private personal data from every response.


Mission: Iter prompts with eval not vibes; version bump semver prompt 1.0 1.1.
Structure template: Role one line Mission bullet constraints tools inputs outputs refusal rules examples optional.
Positive explicit: what agent should do first with numbered priorities max 7.
Negative: what never do; pair each with observable trigger phrase user might say.
USER_APPROVAL tokens: name each approval string consistent across org e.g. USER_APPROVAL CRM WRITE.
Language: de user facing examples en ok in code blocks document primary locale.
Length: target 15-40 non-empty lines system block; move long recipes to skill file reference path.
Few-shot: max 2 in system rest in eval cases file avoid training on secrets in prompt.
Modular: domain specific paragraph replaceable without rewriting entire prompt.
Tool list: match required_tools frontmatter exactly no phantom tools.
Test edit: change one variable per iteration run eval subset before full suite.
Changelog: prompt CHANGELOG.md what why metric delta.
Anti patterns: remove duplicate contradictory rules consolidate.
Model specific: note if reasoning model needs shorter instructions or vice versa document tested models list.
Handoff: after prompt stable link skills-authoring-workflow if wrapping in skill file.```

## Workflow

1. Collect actual prompt and error symptoms.
Apply structure (Role/Mission/Constraints).
. . . sharpened . . .
4. Define Eval subset and measure baseline.
5. One change per iteration.
6. Changelog and version bump.
7. Promotion after passing Eval.

## Definition of done

15-40 lines of core instruction
- [ ] Eval Delta documented
- [ ] No contradiction in rules
- [ ] required tools consistently

## Security

- No real secrets in few shots.

## Pitfalls

- Enable only required tools.


Prompt without Eval → silent regression.
- Too many rules → model ignores middle.
- Tool names not covered.

## Basic examples

Example 1 (Example data)

- **Task:** CRM skill v1.1
**Input:** writes without tokens
- **Prompt:**

```text
Add USER_APPROVAL CRM WRITE and refusal cases eval 5 cases.
```

- **Expected result:**

```text
Summary: the agent stays read-only until approval, lists concrete next steps, and marks any missing inputs the user must supply.Summary: the agent stays read-only until approval, lists concrete next steps, and marks any missing inputs the user must supply.prompt v1.1 | eval pass refusal 5/5
```

### Example 2 (Example data (self-written))
- **Task:** 200 Zeilen Regeln
- **Input:** bloat prompt
- **Prompt:**

```text
Add more caps lock rules.
```

- **Expected result:**

```text
Summary: the agent stays read-only until approval, lists concrete next steps, and marks any missing inputs the user must supply.Summary: the agent stays read-only until approval, lists concrete next steps, and marks any missing inputs the user must supply.consolidate suggest move detail to skill file
```

### Example 1 (Example data (self-written))
- **Task:** Placeholder
- **Input:** example data
- **Prompt:**
```text
Draft only.
```
- **Expected result:** Draft artifact path.
