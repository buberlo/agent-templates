---
id: tech-docs-workflow
title: "Technische Dokumentation"
domain: software-development
category: tech-docs
tags:
  - docs
  - adr
  - readme
target_agents:
  - hermes
  - claude-code
  - cursor
  - generic-mcp-agents
required_tools:
  - name: markdown
    install: "repo docs/"
    version_notes: "mdbook/docusaurus optional"
  - name: gh
    install: "link PRs"
    version_notes: "optional"
inputs:
  - "Zielgruppe (dev/onboarding/ops)"
  - "Theme and sources in the repo"
outputs:
  - "Doc page + links"
  - "Review checklist"
risk_level: low
example_count: 2
version: "1.0.0"
updated: "2026-11-23"
---

## Purpose

Maintain technical documentary **am code**: README, ADR, Runbooks — with verification against real commands in the repo.

## When to use

- Onboarding, Architektur-Entscheid, API-Doku.
- Nach Refactor Pfade aktualisieren.

**When not:** Marketing copy (content marketing).

## Tool stack

| Tool | Role | Justification |
|------|-------|------------|
| markdown | authoring | git tracked |
| mdbook/docusaurus | site | if project uses |
| commands from repo | verify | copy-paste real |

## System prompt

```text
Tech docs workflow (software-development/tech-docs).

Every command in docs must be copied from or tested against package.json/scripts.
ADR format: Context, Decision, Consequences, Status.
Link to source files with repo-relative paths.
Diagrams: mermaid when helpful; keep readable in GitHub preview.
Avoid stale version numbers; reference ranges or link to package.json.
Security: no internal URLs with tokens; use placeholders.
Deprecation banner on old pages pointing to replacement.
Define audience in first paragraph.
DoD: peer can follow doc cold start without asking.
Languages: German prose, English identifiers ok.
Update index/README TOC when adding pages.
```

## Workflow

1. Audience and scope.
2. Existing docs grep — avoid duplicate.
3. Outline + ADR if decision.
4. Write markdown; embed real commands.
5. Run documented commands verify.
6. TOC/README update.
7. PR with docs-only label.

## Definition of done

- [ ] Commands verified
- [ ] Links relative and valid
- [ ] No Secrets in Beispielen

## Security

- Interne Hostnamen nur wenn Repo private policy ok.

## Pitfalls

- Docs drift from scripts.
- Screenshot without Alt.
- ADR without consequences.
- Duplicated README and wiki.
- English/German mix confusing ops.

## Basic examples

### Example 1 (Example data (self-written))
- **Task:** ADR for DB choice.
- **Input:** choose Postgres.
- **Prompt:**

```text
Write docs/adr/0007-postgres.md with context/decision/consequences.
```

- **Expected result:**

```text
ADR 0007 Accepted — Postgres for JSON + extensions
```

### Example 2 (Example data (self-written))
- **Task:** Onboarding dev setup.
- **Input:** npm monorepo.
- **Prompt:**

```text
README setup from package.json scripts; verify npm run dev steps.
```

- **Expected result:**

```bash
npm ci && npm run dev
# documented in README matches package.json
```