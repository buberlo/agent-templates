---
id: codex-agents-md-nested-overrides-v1
title: "Codex AGENTS.md nested overrides"
domain: agent-platforms
category: codex
tags:
  - codex
  - agents-md
  - monorepo
  - conventions
target_agents:
  - codex
  - cursor
  - claude-code
  - generic-mcp-agents
required_tools:
  - name: Codex AGENTS.md discovery
    install: "https://learn.chatgpt.com/docs/agent-configuration/agents-md"
    version_notes: "Global ~/.codex, nested AGENTS.override.md, 32 KiB default cap."
  - name: OpenAI Codex CLI
    install: "https://developers.openai.com/codex/cli/"
    version_notes: "`codex /init`, project_doc_max_bytes in config.toml."
inputs:
  - "Monorepo layout with at least two packages needing different test commands"
  - "Global ~/.codex/AGENTS.md preferences (optional)"
  - "Conflict rules the user wants documented between root and nested overrides"
outputs:
  - "Root AGENTS.md plus one nested AGENTS.override.md with non-overlapping scopes"
  - "Transcript of `codex --ask-for-approval never` listing loaded instruction sources"
risk_level: low
example_count: 2
version: "1.0.0"
updated: "2026-11-26"
---

## Purpose

Layer **Codex `AGENTS.md`** instructions in a monorepo: global defaults in `~/.codex`, repository root expectations, and **directory-specific `AGENTS.override.md`** files that win over sibling `AGENTS.md` in the same folder ([Codex AGENTS.md guide](https://learn.chatgpt.com/docs/agent-configuration/agents-md), [Codex CLI](https://developers.openai.com/codex/cli/)).

## When to use

- A monorepo mixes Node services and Rust crates with different test entrypoints.
- Platform team wants shared global lint rules but package teams need local overrides.
- Instruction files approach the **32 KiB** `project_doc_max_bytes` cap and need splitting.

### When not to use

- Single-package repos where root `AGENTS.md` alone stays well under the byte cap.
- Teams that have not adopted Codex CLI discovery (Hermes-only workflows without Codex delegation).

## Tool stack

| Tool | Role | Rationale |
|------|------|-----------|
| `~/.codex/AGENTS.md` | Global policy | First layer in merge order |
| Root `AGENTS.md` | Repo defaults | Shared CI and PR conventions |
| `AGENTS.override.md` | Local wins | Same directory beats `AGENTS.md` there |
| `~/.codex/config.toml` | Limits | `project_doc_max_bytes`, fallback filenames |

## System prompt

```text
You author Codex AGENTS.md files for agent-platforms/codex following discovery order documented at https://learn.chatgpt.com/docs/agent-configuration/agents-md and Codex CLI behavior at https://developers.openai.com/codex/cli/.
You create concise global guidance in ~/.codex/AGENTS.md only when the user explicitly wants cross-repo defaults; otherwise you focus on repository and nested overrides.
You place one AGENTS.md at the Git root covering shared commands such as lint, PR title format, and secret-handling rules every package inherits.
You add AGENTS.override.md in specialized directories when test or deploy commands diverge, using override files instead of duplicating entire root documents.
You keep each file under the combined project_doc_max_bytes budget, splitting nested files rather than pasting duplicate paragraphs.
You document which checks Codex must run after edits when AGENTS.md lists programmatic validators, matching OpenAI guidance that agents run listed checks after all changes.
You verify discovery by suggesting codex --ask-for-approval never with a prompt that lists instruction sources in merge order root to cwd.
You align AGENTS.md scope rules with CLAUDE.md or Cursor rules when the same repo uses multiple agents, noting direct user prompt precedence over AGENTS.md.
You never store API keys or customer data in AGENTS.md; reference secret store names only.
You deliver file contents, a merge-order diagram in prose, and expected codex listing output for the user's working directory.
```

## Workflow

1. Map monorepo packages and distinct test/build commands per directory.
2. Draft root `AGENTS.md` with shared conventions and links to official docs.
3. Add `AGENTS.override.md` only where commands or approval gates differ.
4. Optionally add `~/.codex/AGENTS.md` for personal preferences the user wants globally.
5. Run Codex from a nested directory; capture which files loaded and in what order.
6. If combined size nears 32 KiB, split instructions across deeper directories or raise `project_doc_max_bytes` with platform approval.
7. Cross-link from README or CONTRIBUTING so human contributors update AGENTS when CI commands change.
8. Run `/init` or equivalent only when bootstrapping empty repos; refine by hand afterward.

## Definition of done

- [ ] Root and nested AGENTS files committed with clear scope boundaries
- [ ] Codex discovery transcript shows expected merge order
- [ ] No contradictory commands between parent and child without explicit override note
- [ ] Byte-size budget documented or config.toml adjustment recorded

## Security

- AGENTS.md is world-readable in git; never embed credentials or private URLs with tokens.
- Overrides that relax security (skip tests, force push) require tech-lead review.

## Pitfalls

- Placing both `AGENTS.md` and `AGENTS.override.md` with conflicting text confuses humans even when override wins.
- Codex stops adding files once byte cap hit—later directories silently omitted from prompt.
- Assuming Hermes or Cursor read AGENTS.md automatically—they need parallel rules files.
- Empty AGENTS files are skipped; use comments sparingly and keep actionable lines.

## Basic examples

### Example 1 (Example data (self-written))

- **Task:** Monorepo with `apps/web` (npm) and `services/payments` (make).
- **Input:** Root requires `npm run lint` at root; payments override requires `make test-payments`.
- **Prompt:**

```text
Write root AGENTS.md and services/payments/AGENTS.override.md. Run codex from payments dir and list sources.
```

- **Expected result:**

```text
Root AGENTS.md: lint before PR, no secret files in git, link to Codex CLI docs.
services/payments/AGENTS.override.md: use make test-payments instead of npm test; security channel approval for key rotation.
Codex from services/payments reports sources: ~/.codex/AGENTS.md (if present), repo AGENTS.md, payments AGENTS.override.md in that order.
No combined size warning; files under 4 KiB each.
```

### Example 2 (Example data (self-written))

- **Task:** Approach 32 KiB cap; split docs across packages.
- **Input:** project_doc_max_bytes default 32768; ten packages with long checklists.
- **Prompt:**

```text
Split AGENTS guidance per package directory; document config.toml raise proposal only, do not change without approval.
```

- **Expected result:**

```text
Each package owns AGENTS.md with package-specific test matrix; root holds only shared policies under 8 KiB.
Discovery from packages/billing loads root + packages/billing/AGENTS.md without hitting cap.
Memo to user: optional project_doc_max_bytes increase listed with risk that oversized prompts dilute focus.
Codex still runs listed checks after doc-only edits when checks are declared in the nearest AGENTS file.
```