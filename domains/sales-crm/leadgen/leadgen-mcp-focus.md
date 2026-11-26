---
id: leadgen-mcp-focus
title: "Leadgen: Recherche-MCP vs. CRM-Import"
domain: sales-crm
category: leadgen
tags:
  - leadgen
  - exa
  - mcp
target_agents:
  - hermes
  - grokbot
  - generic-mcp-agents
  - generic
required_tools:
  - name: Exa MCP
    install: "https://github.com/exa-labs/exa-mcp-server"
    version_notes: "5264 GitHub Stars"
  - name: Brave Search MCP
    install: "https://github.com/brave/brave-search-mcp-server"
    version_notes: "1585 GitHub Stars"
  - name: attio MCP (Hermes-catalog)
    install: "https://github.com/NousResearch/hermes-agent/tree/main/optional-mcps/attio"
    version_notes: "Nous-approved optional-mcps-catalog entry (listing 2026-11-23)."
  - name: close MCP (Hermes-catalog)
    install: "https://github.com/NousResearch/hermes-agent/tree/main/optional-mcps/close"
    version_notes: "Nous-approved optional-mcps-catalog entry (listing 2026-11-23)."
inputs:
  - "Depth of research vs. CRM import in one session"
  - "API budget and allowed MCPs"
outputs:
  - "Routing-Entscheid recherchieren → CSV → CRM"
  - "Nutzungsprotokoll pro MCP"
risk_level: low
example_count: 2
version: "1.1.0"
updated: "2026-11-23"
---

## Purpose

**Decouple** leadgen sessions: first Exa/Brave for discovery, then optionally a CRM MCP for draft import—don't fully load all four MCPs at the same time.

## When to use

- Token budget is tight, but list + CRM are needed.
- Unklar, ob Exa alleine reicht vs. Brave-Verifikation.

**When not to use**

- Purely academic web search → URL0, not this focus template.

## Tool stack

| Tool | Role | Rationale |
|------|-------|------------|
| Exa MCP | Discovery | Breite semantische Treffer |
| Brave Search | Verify | Zweitquelle |
| attio / close | Import draft | Phase 2 only |

## System prompt

```text
You stage leadgen tooling (sales-crm/leadgen-mcp-focus).

Phase A – Research only: Exa MCP on; Brave for spot-check top N; attio/close OFF.
Deliver: CSV path and row count; cite queries used.

Phase B – CRM (optional): disable Exa if user confirms research complete; enable single CRM MCP (attio OR close, never both).
Deliver: import mapping YAML and dry-run row preview (5 rows)—no insert until APPROVE CRM IMPORT.

Do not use web-exa recherche template ids in this flow—Exa here is account discovery only.

If Brave and Exa disagree on company existence, downgrade fit_score and keep both URLs.

Rate limits: log HTTP 429; switch to smaller batch, do not add third search MCP.

Hermes include filter: recommend attio off during Phase A to save tokens.

User asks "just CSV": Phase B skipped entirely.

User asks "push to CRM": require CSV checksum match before Phase B.

Document phase transitions with timestamps.

German queries ok for DACH ICP; store query language in log.

Close import: warn about duplicate lead rules in workspace.

Attio lists: fetch list schema before mapping columns.

Never run Close sequences from this focus template.
```

## Workflow

1. Objective: Clarify whether only CSV or CSV+CRM.
2. Phase A: Activate Exa/Brave, CRM MCPs from policy.
3. Export the list and note the checksum.
4. User-Review-Gate.
5. Phase B optional: a CRM, mapping + dry run.
6. Wait for approval for insert.
7. Final report on phases and MCP usage.

## Definition of done

- [ ] Klare Phasentrennung im Log
- [ ] Maximum one CRM in Phase B
- [ ] Dry run before insert
- [ ] No web-exa research scope mixed in

## Security

- CRM-Bulk-Insert kann Duplikate massenhaft erzeugen.
- Do not log API keys in queries.

## Pitfalls

- attio active during Exa search → Context overflow.
- Brave for every line instead of a sample → Budget empty.
- Phase B without CSV review.
- Close+Attio parallel importieren.
- Exa result as a CRM company without domain normalization.

## Basic examples

### Example 1 (Example data (self-written))
- **Task:** CSV only, 20 accounts
- **Input:** ICP SaaS DACH
- **Prompt:**

```text
Phase A only. attio excluded. Deliver leads_dach_saas.csv.
```

- **Expected result:**

```text
Phase A complete | MCPs: exa, brave | CSV 20 rows | Phase B skipped
```

### Example 2 (Example data (self-written))
- **Task:** CSV dann Attio Dry-Run
- **Input:** `leads_dach_saas.csv` sha256 bekannt
- **Prompt:**

```text
Phase B attio mapping, 5-row preview, no insert.
```

- **Expected result:**

```text
mapping.yaml | preview ids match csv | awaiting FREIGAGE
```