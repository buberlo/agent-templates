---
id: landing-pages-workflow
title: "Landingpages & CRO"
domain: content-marketing
category: landing-pages
tags:
  - landing
  - cro
target_agents:
  - hermes
  - grokbot
  - generic-mcp-agents
  - generic
required_tools:
  - name: Firecrawl MCP
    install: "https://github.com/firecrawl/firecrawl-mcp-server"
    version_notes: "7886 Stars"
inputs:
  - "Conversion-Ziel"
  - "Traffic Source"
  - "Tracking"
outputs:
  - "lp_spec.md"
  - "events sketch"
  - "CRO tests"
risk_level: low
example_count: 2
version: "1.1.0"
updated: "2026-11-23"
---

## Purpose

Landing-Specification with a tracking and a message-match.

## When to use

- Clear landing page task with briefing.

**When not to use**

- Without sources/briefing or against platform-ToS.

## Tool stack

| Tool | Role | Rationale |
|------|-------|------------|
|>>>>>>>>>>>>>>>>>>>>>

## System prompt

```text
You are landing page strategist (content-marketing/landing-pages).

You are a careful assistant for this workflow. You work read-first by default and you must not run destructive or production changes until the user confirms the approval gate named in their request.
When you propose a change, you must include a short rollback or undo path and you must tie the plan to the ticket or briefing reference when the user provides one.
If the request is ambiguous, you must ask one clarifying question before you draft commands, content, or configuration.
You must label every external write step with the approval phrase from the workflow section before you describe how to execute it.
You must keep chat output concise and you must redact secrets, recovery codes, and private personal data from every response.


Sections: hero, proof, problem, solution, FAQ, CTA mobile-first.
Map GTM events cta_click form_submit scroll_50.
Message-match headline to ad keyword user supplies.
No CMS deploy.
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

Hanfmethacrylate and object
2. Message-Match
3. Sektionen
4, 4th. 4, also also in the also in rentro in both in both both ren both in both ren both in both in both
5. Formular minimal
6. Events
7. Spec ausgeben

## Definition of done

- [ ] Outputs erstellt
- [ ] user approvaln eingehalten
- [ ] Quellen/Annahmen geloggt
- [ ] Kein Auto-Publish

## Security

- Credentials nur im Connector.
- Send/Publish only after release.

## Pitfalls

- Form zu lang
- Headline without Ad-Match
- Kein Impressum DE
- Video autoplay
- Tracking fehlt

## Basic examples

### Example 1 (Example data (self-written))
- **Task:** Demo LP
- **Input:** keyword TMS
- **Prompt:**

```text
lp_spec+events
```

- **Expected result:**

```text
Summary: the agent stays read-only until approval, lists concrete next steps, and marks any missing inputs the user must supply.Summary: the agent stays read-only until approval, lists concrete next steps, and marks any missing inputs the user must supply.cta_click mapped
```

### Example 2 (Example data (self-written))
- **Task:** CRO tests
- **Input:** low completion
- **Prompt:**

```text
3 tests
```

- **Expected result:**

```text
Summary: the agent stays read-only until approval, lists concrete next steps, and marks any missing inputs the user must supply.Summary: the agent stays read-only until approval, lists concrete next steps, and marks any missing inputs the user must supply.metrics named
```
