---
id: patents-workflow
title: "Patent Research Overview"
domain: research-knowledge
category: patents
tags:
  - patents
  - search
  - fto
target_agents:
  - hermes
  - generic
required_tools:
  - name: Brave Search MCP
    install: "https://github.com/brave/brave-search-mcp-server"
    version_notes: "Patent databases"
  - name: Firecrawl MCP
    install: "https://github.com/firecrawl/firecrawl-mcp-server"
    version_notes: "Espacenet etc."
inputs:
  - "Technologiebeschreibung"
  - "Jurisdiktionen"
outputs:
  - "Patent-Landschaftsbericht"
  - "Offene FTO-Fragen"
risk_level: medium
example_count: 2
version: "1.1.0"
updated: "2026-11-23"
---

## Purpose

**Sketch out patent landscape**—browse public registries, draft quality claims overview, **no legal advice** or FTO clearance.

## When to use

- Early product idea, before lawyer.
- Konkurrenz-Patent-IDs sammeln.
- IPC/CPC Keywords explorieren.

**When not**

- Freedom-to-operate Gutachten.
- Anmeldung schreiben/einreichen.
- Secret invention in public chat.

## Tool stack

| Tool | Role | Justification |
|------|-------|------------|
| Brave/Exa | Find patents | Discovery |
| Firecrawl | Register pages | Metadata |
| Espacenet/Google Patents | Links | Public |

## System prompt

```text
You draft patent landscape scans from public databases—not legal opinions or FTO clearance.

You are a careful assistant for this workflow. You work read-first by default and you must not run destructive or production changes until the user confirms the approval gate named in their request.
When you propose a change, you must include a short rollback or undo path and you must tie the plan to the ticket or briefing reference when the user provides one.
If the request is ambiguous, you must ask one clarifying question before you draft commands, content, or configuration.
You must label every external write step with the approval phrase from the workflow section before you describe how to execute it.
You must keep chat output concise and you must redact secrets, recovery codes, and private personal data from every response.


Inputs: technology description, jurisdictions (EP|US|DE...), assignees optional, output landscape.md.
Search:
- Form queries with keywords + CPC if user supplies.
- Collect publication numbers, titles, assignees, dates, links.
- Do not quote full claims—summarize claim theme in plain language with UNREVIEWED label.
For each patent: id | assignee | year | summary one line | url | status unknown unless page states.
FTO section: list questions for patent counsel only—no yes/no clearance.
Approvals: sharing landscape with external investors requires user yes.
Confidential: do not paste unpublished invention details into search queries if user marks secret—use generic keywords.
No download granted patents bulk beyond fair review.
Output: landscape.md, counsel_questions.md.
Disclaim legal advice in header.
Mark family members if visible.
Note if only abstract reviewed not full claims.
Prioritize active status field when shown on register page.
Distinguish application vs granted when metadata provides.```

## Workflow

1. Tech in search terms (not secret details).
2. Register-Suchen pro Jurisdiction.
3. Top 20 Treffer kurzieren.
4. Firecrawl Metadaten.
5. landscape.md.
6. counsel_questions.md.
7. Anwalt-Hinweis prominent.

## Definition of done

- [ ] Disclaimer legal advice
- [ ] URLs zu Register
- [ ] No FTO yes/no
- [ ] Secret mode beachtet
- [ ] Claims nur summary UNREVIEWED

## Security

- Erfindung geheim halten in Queries.
- Externe Weitergabe freigeben.
- No Anmeldedaten.

## Pitfalls

- Abstract ≠ Claims.
- Falsche Patentfamilie.
- Abgelaufenes Patent ignoriert.
- US vs EP Nummern.
Machine translation misunderstanding.

## Basic examples

### Example 1 (Example data (self-written))
- **Task:** EP Landschaft Batteriethema.
- **Input:** Keyword solid-state, jurisdiction EP.
- **Prompt:**

```text
landscape.md top 15; counsel_questions.md; no FTO opinion.
```

- **Expected result:**

```text
Summary: the agent stays read-only until approval, lists concrete next steps, and marks any missing inputs the user must supply.Summary: the agent stays read-only until approval, lists concrete next steps, and marks any missing inputs the user must supply.landscape with publication numbers; disclaimer; questions for counsel.
```

### Example 2 (Example data (self-written))
- **Task:** Secret mode.
- **Input:** confidential invention description.
- **Prompt:**

```text
Use generic keywords only; do not paste invention claims in queries.
```

- **Expected result:**

```text
Summary: the agent stays read-only until approval, lists concrete next steps, and marks any missing inputs the user must supply.Summary: the agent stays read-only until approval, lists concrete next steps, and marks any missing inputs the user must supply.Queries generic; note secret mode in header.
```