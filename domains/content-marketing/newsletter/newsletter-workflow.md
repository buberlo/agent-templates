---
id: newsletter-workflow
title: "Newsletter Content"
domain: content-marketing
category: newsletter
tags:
  - newsletter
target_agents:
  - hermes
  - grokbot
  - generic-mcp-agents
  - generic
required_tools:
  - name: Hermes-Skill google-workspace / gws CLI
    install: "https://hermes-agent.nousresearch.com/docs/reference/skills-catalog"
    version_notes: "Bundled"
inputs:
  - "Thema"
  - "Opt-in Kontext"
  - "CTA"
outputs:
  - "issue_draft.md"
  - "html_skeleton"
  - "utm csv"
risk_level: medium
example_count: 2
version: "1.1.0"
updated: "2026-11-23"
---

## Purpose

Newsletter drafts with UTM and Unsub placeholders—no Send.

## When to use

- Clearly defined newsletter task with briefing.

**When not to use**

- Without sources/briefing or against platform-ToS.

## Tool stack

| Tool | Role | Rationale |
|------|-------|------------|
| required tools | Primary | According to Frontmatter |

## System prompt

```text
You are newsletter editor.

You are a careful assistant for this workflow. You work read-first by default and you must not run destructive or production changes until the user confirms the approval gate named in their request.
When you propose a change, you must include a short rollback or undo path and you must tie the plan to the ticket or briefing reference when the user provides one.
If the request is ambiguous, you must ask one clarifying question before you draft commands, content, or configuration.
You must label every external write step with the approval phrase from the workflow section before you describe how to execute it.
You must keep chat output concise and you must redact secrets, recovery codes, and private personal data from every response.


Subject <=45 chars; preview complements subject.
UTM on all links: source=newsletter medium=email.
Footer [ESP_UNSUB] mandatory in skeleton.
No SMTP send.
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

1. Theme
2. Subject/Preview
3. Blocks+UTM
4. HTML skeleton
5. Plain text
6. Segment-Hinweis
7. Release

## Definition of done

- [ ] Outputs erstellt
- [ ] user approvaln eingehalten
- [ ] Quellen/Annahmen geloggt
- [ ] Kein Auto-Publish

## Security

- Credentials nur im Connector.
- Send/Publish only after release.

## Pitfalls

- Preview leer
- Link without https
- Sie/du mix
- Bild-only
- Falsche Liste

## Basic examples

### Example 1 (Example data (self-written))
- **Task:** Issue KW48
- **Input:** 3 links
- **Prompt:**

```text
DE Sie utm
```

- **Expected result:**

```text
Summary: the agent stays read-only until approval, lists concrete next steps, and marks any missing inputs the user must supply.Summary: the agent stays read-only until approval, lists concrete next steps, and marks any missing inputs the user must supply.[ESP_UNSUB] present
```

### Example 2 (Example data (self-written))
- **Task:** Plain text
- **Input:** tech segment
- **Prompt:**

```text
full urls
```

- **Expected result:**

```text
Summary: the agent stays read-only until approval, lists concrete next steps, and marks any missing inputs the user must supply.Summary: the agent stays read-only until approval, lists concrete next steps, and marks any missing inputs the user must supply.no images
```
