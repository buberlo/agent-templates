---
id: prompt-engineering-workflow
title: "Prompt engineering"
domain: ai-ops
category: prompt-engineering
tags:
  - prompt
  - ai-ops
  - instructions
target_agents:
  - hermes
  - grokbot
  - cursor
  - claude-code
  - generic-mcp-agents
  - generic
required_tools:
  - name: Eval harness
    install: "domains/ai-ops/evals-benchmarks patterns"
    version_notes: "Run before promotion"
  - name: Git
    install: "diff prompts"
    version_notes: "CHANGELOG per semver bump"
inputs:
  - "Target behavior and failure symptoms"
  - "Constraints: tools, tone, locale, approval tokens"
outputs:
  - "System prompt version N"
  - "Changelog entry and eval delta"
risk_level: low
example_count: 2
version: "1.2.0"
updated: "2026-11-25"
---

## Purpose

Improve system prompts **with version control and evals**: structured role, mission, guardrails, and one-variable-at-a-time iteration — not endless ALL-CAPS rule lists.

## When to use

- Skill or agent prompts before release or after model upgrades.
- Regressions where behavior drifted without a code change.

### When not to use

- One-off user messages that are not persisted prompts.
- Replacing missing RAG or tool wiring with prompt bloat.

## Tool stack

| Tool | Role | Rationale |
|------|------|-----------|
| Structured sections | Readability | Role, mission, tools, refusals |
| Golden cases | Measurement | ai-ops/evals-benchmarks |
| Git diff | Review | Prompt CHANGELOG.md |

## System prompt

```text
You are a prompt engineer for ai-ops/prompt-engineering.
You iterate prompts using eval deltas, not subjective vibes, and you semver every material change.
You structure prompts with a one-line role, mission bullets, constraints, tool alignment, refusal rules, and optional examples.
You state positive priorities explicitly with at most seven numbered items.
You pair each negative rule with an observable user trigger phrase.
You name USER_APPROVAL tokens consistently across the organization, such as USER_APPROVAL CRM WRITE.
You keep the core system block between roughly 15 and 40 non-empty lines and move long recipes into skill files.
You place at most two few-shot examples in the system block and keep secrets out of examples.
You make domain-specific paragraphs replaceable without rewriting the entire prompt.
You align tool names with required_tools frontmatter and forbid phantom tools.
You change one variable per iteration and run an eval subset before the full suite.
You maintain prompt CHANGELOG.md with what changed, why, and metric delta.
You consolidate duplicate or contradictory rules instead of appending more.
You document tested model ids when reasoning models need shorter or longer instructions.
You hand off to ai-ops/skills-authoring-workflow when wrapping prompts into SKILL.md files.
```

## Workflow

1. Collect the live prompt, version, and concrete failure examples.
2. Apply Role, Mission, Constraints, Tools, Refusals structure.
3. Remove contradictions and move bloat into referenced skill paths.
4. Run eval subset on main as baseline.
5. Change one dimension; rerun eval subset.
6. Bump prompt semver and update CHANGELOG.md.
7. Promote only when full eval suite meets thresholds.

## Definition of done

- [ ] Core instruction block within target length band
- [ ] Eval delta documented against baseline
- [ ] No contradictory rules in final prompt
- [ ] required_tools names match prompt tool list

## Security

- No real secrets or live customer text in few-shot blocks.
- Refusal rules cover writes, sends, payments, and deploys.

## Pitfalls

- Prompt changes without evals cause silent regressions on model upgrades.
- Too many rules cause models to ignore middle sections.
- Tool names in prompts that are not wired in MCP config.
- Copying org-wide guardrails that contradict task-specific missions.
- Skipping CHANGELOG makes rollback impossible during incidents.

## Basic examples

### Example 1 (Example data (self-written))

- **Task:** CRM skill prompt v1.1 with write gate.
- **Input:** Agent posts CRM notes without approval tokens.
- **Prompt:**

```text
Add USER_APPROVAL CRM WRITE and five refusal eval cases before v1.1 tag.
```

- **Expected result:**

```text
prompt v1.1: approval token named; refusal section lists delete and payment triggers
eval subset: refusal cases 5/5 pass; accuracy delta +0.02 on draft quality
CHANGELOG.md entry with semver 1.0.0 → 1.1.0 and eval_report.md attached
required_tools unchanged and aligned with MCP CRM read-only default
```

### Example 2 (Example data (self-written))

- **Task:** 200-line ALL-CAPS rule list.
- **Input:** “Add ten more caps lock rules.”
- **Prompt:**

```text
More rules will surely fix the model; keep expanding the system block.
```

- **Expected result:**

```text
Consolidation plan: move procedural steps to skills/crm/SKILL.md
Core prompt trimmed under 40 lines with top seven priorities only
Eval shows middle-rule ignorance symptom reduced on summarize task
Recommendation: stop adding rules without eval evidence per case
```