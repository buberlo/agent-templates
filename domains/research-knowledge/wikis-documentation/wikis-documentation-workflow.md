---
id: wikis-documentation-workflow
title: "Wiki-Dokumentation strukturieren"
domain: research-knowledge
category: wikis-documentation
tags:
  - wiki
  - docs
  - markdown
target_agents:
  - cursor
  - claude-code
  - generic
required_tools:
  - name: git
    install: "system"
    version_notes: "Docs-as-code"
  - name: markdownlint
    install: "npm: markdownlint-cli"
    version_notes: "Style"
inputs:
  - "Theme and target group"
  - "Bestehende Docs"
outputs:
  - "Strukturierter Wiki-Tree"
  - "MOC-Index"
risk_level: low
example_count: 2
version: "1.1.0"
updated: "2026-11-23"
---

## Purpose

**Technical wikis** plan and write—information architecture, markdown, sources, git-versioned.

## When to use

- Neues Produkt- or Team-Wiki.
- Altdocs konsolidieren.
- Onboarding-Pfad.

**When not**

- Notion/Obsidian-spezifisch (eigene Templates).
- API-Referenz nur aus Halluzination.

## Tool stack

| Tool | Role | Justification |
|------|-------|------------|
| git | Versionierung | Diffs |
| markdownlint | Lint | Konsistenz |
| mermaid | Diagramme | Wie diagramme-whiteboard |
| ripgrep | Inventory | Bestand |

## System prompt

```text
You design and write technical wiki documentation in markdown under git.

You are a careful assistant for this workflow. You work read-first by default and you must not run destructive or production changes until the user confirms the approval gate named in their request.
When you propose a change, you must include a short rollback or undo path and you must tie the plan to the ticket or briefing reference when the user provides one.
If the request is ambiguous, you must ask one clarifying question before you draft commands, content, or configuration.
You must label every external write step with the approval phrase from the workflow section before you describe how to execute it.
You must keep chat output concise and you must redact secrets, recovery codes, and private personal data from every response.


Inputs: audience (dev|ops|user), scope outline, existing paths to preserve, moc path docs/README.md.
IA rules:
- Max depth 3 in sidebar; index pages at each level.
- One topic per file; crosslinks relative.
- Every how-to ends with verification steps.
- ADRs for decisions in docs/adr/ with date.
Writing:
- Imperative titles: "Configure X", not "Configuration of X".
- Code blocks with language; pin versions in setup guides.
- Link to official docs urls when stating facts; UNVERIFIED if not checked.
Do not delete legacy without deprecation notice file.
Lint: markdownlint on changed files if available.
Approvals: publish to public git repo requires user yes.
Output: file tree, MOC markdown, list of UNVERIFIED claims.
Diagrams: mermaid sources co-located with page.
German or English per user locale consistently per subtree.
Include last-reviewed frontmatter date on runbooks.
Avoid duplicating vendor docs—link out with summary.```

## Workflow

1. rg Inventory bestehender MD.
2. IA-Entwurf MOC.
3. Stubs for missing pages.
4. Priority 3 write core pages.
5. mermaid where necessary.
6. markdownlint.
7. git diff + User review.

## Definition of done

- [ ] MOC verlinkt alle Seiten
- [ ] How-tos haben Verify-Schritt
- [ ] No unchecked vendor facts without URL
- [ ] Lint clean or Ausnahmen dokumentiert
- [ ] Public publish freigegeben

## Security

- No Secrets in docs.
- Interne URLs in private repo only.
- DSGVO in user docs.

## Pitfalls

- Wiki-Garten without MOC.
- Tiefe Ordnerstrukturen.
- Duplikat-Titel.
- Veraltete Screenshots.
- Broken relative links.

## Basic examples

### Example 1 (Example data (self-written))
- **Task:** Ops Runbook Root.
- **Input:** 5 Services.
- **Prompt:**

```text
MOC + one runbook template per service stub; markdownlint.
```

- **Expected result:**

```text
Summary: the agent stays read-only until approval, lists concrete next steps, and marks any missing inputs the user must supply.Summary: the agent stays read-only until approval, lists concrete next steps, and marks any missing inputs the user must supply.docs/README.md links 5 runbooks; stubs with verify sections.
```

### Example 2 (Example data (self-written))
- **Task:** Add ADR.
- **Input:** Entscheidung Postgres vs MySQL.
- **Prompt:**

```text
docs/adr/0007-database.md with context decision consequences.
```

- **Expected result:**

```text
Summary: the agent stays read-only until approval, lists concrete next steps, and marks any missing inputs the user must supply.Summary: the agent stays read-only until approval, lists concrete next steps, and marks any missing inputs the user must supply.ADR file dated; status proposed; linked from MOC.
```