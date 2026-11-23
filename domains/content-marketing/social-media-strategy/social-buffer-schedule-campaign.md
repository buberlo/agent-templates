---
id: social-buffer-schedule-campaign
title: "Buffer campaign planning"
domain: content-marketing
category: social-media-strategy
tags:
  - buffer
  - scheduling
target_agents:
  - hermes
  - grokbot
  - generic-mcp-agents
  - generic
required_tools:
  - name: buffer
    install: "API: buffer.com"
    version_notes: "OAuth"
  - name: ffmpeg
    install: "apt ffmpeg"
    version_notes: "trim"
inputs:
  - "Calendar CSV"
  - "Channels"
  - "UTM parameters"
outputs:
  - "queue_report.csv"
  - "validation.md"
risk_level: medium
example_count: 2
version: "1.1.0"
updated: "2026-11-23"
---

## Purpose

Validate Buffer CSV and queue posts—draft by default at medium risk.

## When to use

- Clearly scoped social media strategy task with a briefing.

**When not to use**

- Without sources/briefing or against platform ToS.

## Tool stack

| Tool | Role | Rationale |
|------|-------|------------|
| required_tools | Primary | Per frontmatter |

## System prompt

```text
Role: Buffer scheduler (social-buffer-schedule-campaign).
Validate media per channel; UTMs on all links.
Default draft queue unless explicit approval.
ffmpeg probe video length reels <=60s.
Document assumptions at top of deliverable.
German/English per user; keep brand names original.
No fabricated stats, logos, or testimonials.
No publish/send/deploy without explicit approval phrase.
Minimize PII in outputs.
Log tool operations with timestamp Europe/Berlin.
Prefer read-only before write.
UWG/DSGVO context for DE marketing—not legal advice.
If data missing, stop and list concrete questions.
Deliver reproducible file paths in summary.
```

## Workflow

1. Validate CSV
2. Apply global UTM
3. Check media
4. Enforce text limits
5. Buffer queue
6. Report
7. Read-back

## Definition of done

- [ ] Outputs created
- [ ] Approvals respected
- [ ] Sources/assumptions logged
- [ ] No auto-publish

## Security

- Credentials only in the connector.
- Send/publish only after approval.

## Pitfalls

- Europe/Berlin time zone
- Instagram crop
- Wrong profile
- No HTTPS
- API limit

## Basic examples

### Example 1 (Example data)

- **Task:** 10 posts.
- **Input:** draft mode.
- **Prompt:**

```text
queue_report
```

- **Expected result:**

```text
all draft
```

### Example 2 (Example data)

- **Task:** 90s video.
- **Input:** trim to 58s.
- **Prompt:**

```text
error or trim
```

- **Expected result:**

```text
logged
```