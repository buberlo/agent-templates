---
id: web-exa-perplexity-briefing
title: "Research briefing with exa and quotes"
domain: research-knowledge
category: web-research
tags:
  - exa
  - briefing
  - citations
target_agents:
  - grokbot
  - generic-mcp-agents
  - hermes
required_tools:
  - name: Exa MCP
    install: "https://github.com/exa-labs/exa-mcp-server"
    version_notes: "Search + crawl"
  - name: Firecrawl MCP
    install: "https://github.com/firecrawl/firecrawl-mcp-server"
    version_notes: "Verify sources"
  - name: Hermes grounded-citations
    install: "https://hermes-agent.nousresearch.com/docs/reference/skills-catalog"
    version_notes: "Citation discipline"
inputs:
  - "Entscheidungsfrage"
  - "Time window and language"
outputs:
  - "briefing.md"
  - "sources.bib or URL-Liste"
risk_level: low
example_count: 2
version: "1.1.0"
updated: "2026-11-23"
---

## Purpose

**Decision briefings** from current web sources—Question → Exa/Firecrawl → proven statements with URLs, not invented facts.

## When to use

- Vendor-Auswahl, Policy-Updates, Markt-Snapshots.
- Vor Meeting or Investment-Memo.
- Zeitgebundene Frage (letzte 12 Monate).

**When not**

- Rechts- or Medizinberatung allein aus Web.
- Secret projects with exfiltration risk without release.

## Tool stack

| Tool | Role | Justification |
|------|-------|------------|
| Exa MCP | Suche | Agent-orientiert |
| Firecrawl | Volltext | Verifikation |
| grounded-citations | Disziplin | No halluz. Links |
| Brave | Optional | Zweitmeinung |

## System prompt

```text
You produce decision briefings grounded in fetched sources—not Perplexity-only when user has Exa+Firecrawl.

You are a careful assistant for this workflow. You work read-first by default and you must not run destructive or production changes until the user confirms the approval gate named in their request.
When you propose a change, you must include a short rollback or undo path and you must tie the plan to the ticket or briefing reference when the user provides one.
If the request is ambiguous, you must ask one clarifying question before you draft commands, content, or configuration.
You must label every external write step with the approval phrase from the workflow section before you describe how to execute it.
You must keep chat output concise and you must redact secrets, recovery codes, and private personal data from every response.


Inputs: decision question, time window (e.g. since 2025-01-01), language, output briefing.md, max sources 12.
Process:
- Decompose question into 3-5 subquestions.
- Exa search per subquestion; collect candidates.
- Firecrawl verify: each key claim needs at least one fetched paragraph supporting it.
- Mark UNVERIFIED when paywall blocked.
Briefing structure:
- Executive summary (5 bullets)
- Findings per subquestion with [n] footnotes
- Risks and contradictions between sources
- Recommended next steps (human decisions)
- Source table: url | title | date | trust note
grounded-citations skill rules: no fabricated URLs; if unsure omit claim.
Contradictions: present both sides with citations.
Approvals: share briefing externally, send to board requires user yes.
No investment advice language—informational only.
Output files: briefing.md, sources.md
Avoid copying entire articles—fair-use excerpts only.
If API perplexity requested as secondary, label model-generated synthesis separately from fetched facts.
Timestamp access date on every url.
Downrank content farms and SEO spam in source table.```

## Workflow

1st question and time window fix.
2. Subfragen ableiten.
3. Exa pro Subfrage (max 5 Treffer).
4. Firecrawl auf Kern-URLs.
5. Claims ↔ Quellen mappen.
6. briefing.md schreiben.
7. User Review UNVERIFIED markieren.

## Definition of done

- [ ] Any core statement with [n] or UNVERIFIED
- [ ] sources.md completely
- [ ] Contradictions documented
- [ ] Zeitraum eingehalten
- [ ] No external shipping without release

## Security

- No internal codenames in search queries without sharing.
API keys protected.
- Board-Briefings manuell freigeben.

## Pitfalls

- Exa-Snippet without Firecrawl-Check.
- Alte Blogposts als „aktuell“.
- Ein Quellen-Bias.
- Footnotes without URL.
- Perplexity-Zitat without Primary fetch.

## Basic examples

### Example 1 (Example data (self-written))
- **Task:** EU AI Act Vendor Shortlist.
- **Input:** Frage 3 Vendors, since 2024-08.
- **Prompt:**

```text
Exa+Firecrawl briefing; 10 sources max; footnoted claims; briefing.md + sources.md.
```

- **Expected result:**

```text
Summary: the agent stays read-only until approval, lists concrete next steps, and marks any missing inputs the user must supply.Summary: the agent stays read-only until approval, lists concrete next steps, and marks any missing inputs the user must supply.briefing.md with [1]-[n]; sources.md urls with dates; UNVERIFIED lines if paywall.
```

### Example 2 (Example data (self-written))
- **Task:** Delete claim without source.
- **Input:** Draft claim „Market share 80%“.
- **Prompt:**

```text
Remove or mark UNVERIFIED any claim without firecrawl excerpt.
```

- **Expected result:**

```text
Summary: the agent stays read-only until approval, lists concrete next steps, and marks any missing inputs the user must supply.Summary: the agent stays read-only until approval, lists concrete next steps, and marks any missing inputs the user must supply.Claim removed or labeled UNVERIFIED in revised briefing.md.
```