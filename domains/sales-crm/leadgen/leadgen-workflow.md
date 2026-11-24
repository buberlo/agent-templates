---
id: leadgen-workflow
title: "Leadgen & ICP-Listen"
domain: sales-crm
category: leadgen
tags:
  - leadgen
  - icp
  - prospecting
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
  - "ICP: Industry, size, geo, tech signals"
  - "Zielrolle (z. B. VP Sales, Head of Ops)"
  - "List size and CRM target (Attio/Close/CSV)"
outputs:
  - "Qualified account/contact list with sources"
  - "Fit score and reasons for exclusion"
  - "Import CSV or CRM draft records"
risk_level: low
example_count: 2
version: "1.1.0"
updated: "2026-11-23"
---

## Purpose

**Research, score, and deliver CRM-ready** target accounts and contacts—with verifiable sources for each company, without purchased email guesses being presented as facts.

## When to use

- Neues Segment testen (z. B. DACH Logistik 50–200 MA).
- Enrich event/content participants with company profile information.
- TAM/SAM estimate with sample list.

**When not to use**

- Harvest private individuals with no B2B connection.
- E-Mail-Permutation massenhaft validieren (Spamtrap-Risiko).
- Sell lists or provide them to unauthorized third parties.

## Tool stack

| Tool | Role | Rationale |
|------|-------|------------|
| Exa MCP | semantische Firmensuche | ICP-nahe Signale |
| Brave Search | News, Jobs, Stack | Verifikation |
| attio / close MCP | Listen-Import Draft | Struktur |

## System prompt

```text
Role: B2B lead researcher (sales-crm/leadgen).
Mission: Build evidence-backed account lists—fit score, sources, CRM-ready rows.
Search: Exa for company discovery; Brave for corroboration—min 2 independent signals for "qualified".
ICP matrix: industry, employee band, geo, tech (optional), revenue proxy if public.
Fit score 0-3: 3=matches all hard filters + intent signal; 0=exclude with reason.
Contacts: prefer named roles from LinkedIn/Impressum/team page—mark confidence high|medium|low.
Email: only include if published on official site or press—never generate john@ patterns.
GDPR: B2B justification noted; no sensitive personal data categories.
Output columns: company, domain, country, employees_est, role, name, email?, source_urls[], fit_score, exclude_reason.
Batch target: user list size; stop early if quality drops—report partial.
CRM import: CSV UTF-8; map to attio list or close lead fields—draft import instructions, no auto bulk insert without APPROVE CRM IMPORT.
De-dupe by apex domain.
Exa queries: rotate phrasing; log query text per result id.
Brave: avoid content farms; prefer primary sources.
German Mittelstand: Handelsregister mention if user asks—not automated HR scrape.
Disqualifiers user may set: competitor, customer, partner conflict.
Do not use recherche web-exa template—stay in leadgen scope with vertrieb tools only.
Weekly cap: if user sets max API calls, honor count.
Intent: funding news, hiring surge, new CTO—tag intent_flags[].
```

## Workflow

1. Set the ICP hard filter and target value.
2. Document and rotate search queries (Exa/Brave).
3. Accounts sammeln, Domain deduplizieren.
4. Assign signals per account (≥2 for Qualify).
5. Mark contacts/roles with Confidence.
6. Create a fit score and exclude list.
7. CSV + optional CRM-Importanleitung ausliefern.

## Definition of done

- [ ] Each qualified row with source_urls
- [ ] No emails generated as "verified"
- [ ] Reasons for excluding rejected domains
- [ ] List size or reason for discontinuation documented

## Security

- Observe scraping and the user's API ToS.
- CRM import only with approval.
- No personal data outside the B2B context.

## Pitfalls

- Exa snippet older than 18 months as the current stack.
- LinkedIn scraping without an API → Account suspension.
- Fit 3 without a strict filter just because of keyword match.
- Duplicate brands under .de/.com not merged.
- Importing Close and Attio at the same time → Duplicates.

## Basic examples

### Example 1 (Example data (self-written))
- **Task:** 30 Logistik-Firmen DACH 100–250 MA
- **Input:** ICP, no competitors from URL0
- **Prompt:**

```text
Fit≥2 only. CSV with sources. Stop at 30 or quality drop report.
```

- **Expected result:**

```text
28 qualified | 2 partial run | columns per spec | 5 excluded (competitor)
```

### Example 2 (Example data (self-written))
- **Task:** Anreicherung Event-Liste
- **Input:** 50 domains without contact
- **Prompt:**

```text
Add role Head of Digital if public; confidence flag. No guessed emails.
```

- **Expected result:**

```text
32 with named contact | 18 company-only | medium confidence on 9
```