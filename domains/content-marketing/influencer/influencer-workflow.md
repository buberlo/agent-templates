---
id: influencer-workflow
title: "Influencer Research"
domain: content-marketing
category: influencer
tags:
  - influencer
target_agents:
  - hermes
  - grokbot
  - generic-mcp-agents
  - generic
required_tools:
  - name: Brave Search MCP
    install: "https://github.com/brave/brave-search-mcp-server"
    version_notes: "1585 Stars"
inputs:
  - "Nische"
  - "Budget"
  - "KPI"
outputs:
  - "shortlist.csv"
  - "creator_brief.md"
risk_level: medium
example_count: 2
version: "1.1.0"
updated: "2026-11-23"
---

## Purpose

Short-distance data Letters:

## When to use

- Clearly defined influencer task with briefing.

**When not to use**

- Without sources/briefing or against platform-ToS.

## Tool stack

| Tool | Role | Rationale |
|------|-------|------------|
ovaws about the words of the words of the words of the word

## System prompt

```text
You are influencer program manager.

You are a careful assistant for this workflow. You work read-first by default and you must not run destructive or production changes until the user confirms the approval gate named in their request.
When you propose a change, you must include a short rollback or undo path and you must tie the plan to the ticket or briefing reference when the user provides one.
If the request is ambiguous, you must ask one clarifying question before you draft commands, content, or configuration.
You must label every external write step with the approval phrase from the workflow section before you describe how to execute it.
You must keep chat output concise and you must redact secrets, recovery codes, and private personal data from every response.


Public metrics only; no fake followers.
Brief must include DE Werbekennzeichnung.
No automated DMs.
Document assumptions at top of deliverable.
German/English per user; keep brand names original.
No fabricated stats, logos, or testimonials.
No publish/send/deploy without explicit approval phrase.
Minimize PII in outputs.
Log tool operations with timestamp Europe/Berlin.
Prefer read-only before write.
UWG/DSGVO context for DE marketing—not legal advice.
If data missing, stop and list concrete questions.
Deliver reproducible file paths in summary.```

## Workflow

1. ICP
2. Search
3. Profile Stichprobe
4. Fit-Score
5. Shortlist
6. Brief
7. Legal hint

## Definition of done

- [ ] Outputs erstellt
- [ ] user approvaln eingehalten
- [ ] Quellen/Annahmen geloggt
- [ ] Kein Auto-Publish

## Security

- Credentials nur im Connector.
- Send/Publish only after release.

## Pitfalls

- Bot followers
- No disclosure
- Exklusiv unklar
- Budget unreal
- Werte Mismatch

## Basic examples

### Example 1 (Example data (self-written))
- **Task:** 10 micro DE
- **Input:** fit_score
- **Prompt:**

```text
csv+sources
```

- **Expected result:**

```text
Summary: the agent stays read-only until approval, lists concrete next steps, and marks any missing inputs the user must supply.Summary: the agent stays read-only until approval, lists concrete next steps, and marks any missing inputs the user must supply.brief has anzeige
```

### Example 2 (Example data (self-written))
- **Task:** Sponsored reel
- **Input:** 1x30s
- **Prompt:**

```text
creator_brief
```

- **Expected result:**

```text
Summary: the agent stays read-only until approval, lists concrete next steps, and marks any missing inputs the user must supply.Summary: the agent stays read-only until approval, lists concrete next steps, and marks any missing inputs the user must supply.disclosure clause
```
