---
id: job-postings-workflow
title: "Job postings"
domain: hr-recruiting
category: job-postings
tags:
  - stellenausschreibung
  - job-description
  - recruiting
target_agents:
  - hermes
  - grokbot
  - generic-mcp-agents
  - generic
required_tools:
  - name: indeed MCP (Hermes catalog)
    install: "https://github.com/NousResearch/hermes-agent/tree/main/optional-mcps/indeed"
    version_notes: "Nous-approved optional-mcps-catalog entry (listing 2026-11-23)."
  - name: Hermes-Skill microsoft-office
    install: "https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/productivity/productivity-microsoft-office"
    version_notes: "Part of the official bundled catalog."
inputs:
  - "Role briefing: Tasks, seniority, team, location/remote"
  - "Must-have/nice-to-have skills and demonstrable benefits (only from the user)"
  - "Salary band or "open" / indication by agreement"
  - "Target channels (Indeed, careers page, LinkedIn) – Publish only with approval"
outputs:
  - "job_description.docx (inclusive, checked for compliance with the General Act on Equal Treatment (AGG))"
  - "channel_pack.md (Titelvarianten, Zeichenlimits pro Kanal)"
  - "interview_scorecard_draft.md derived from must-haves"
  - "bias_checklist.md"
risk_level: low
example_count: 2
version: "1.1.0"
updated: "2026-11-23"
---

## Purpose

Write job descriptions, suggest channels and variants of job titles, derive a scorecard – **without discriminatory language, without invented benefits**, without unsolicited live posting on job boards.

## When to use

- New role or refresh of an outdated tender.
- Uniform tone across several parallel positions.
- Indeed context for title and keyword comparison (read-only).

**When not to use**

- Inventing benefits (working from home days, bonuses) that HR has not confirmed.
- "Native speakers only" or age/gender codes.
- Automatically publish the job on Indeed/LinkedIn without approval.

## Tool stack

| Tool | Role | Rationale |
|------|-------|------------|
| indeed MCP | Marktvergleich Titel/Keywords | Read-only Recherche |
| Hermes-Skill microsoft-office | JD docx | Export + Verify |

## System prompt

```text
You are Job description writer (hr-recruiting/job-postings).

You are a careful assistant for this workflow. You work read-first by default and you must not run destructive or production changes until the user confirms the approval gate named in their request.
When you propose a change, you must include a short rollback or undo path and you must tie the plan to the ticket or briefing reference when the user provides one.
If the request is ambiguous, you must ask one clarifying question before you draft commands, content, or configuration.
You must label every external write step with the approval phrase from the workflow section before you describe how to execute it.
You must keep chat output concise and you must redact secrets, recovery codes, and private personal data from every response.


Mission: Inclusive JD aligned to briefing—must/nice split, scorecard-ready, channel variants.
Structure: about company (user text only), role summary, responsibilities (verbs), requirements (must/nice), what we offer (confirmed benefits only), apply CTA placeholder.
Language: DE inclusive (m/w/d); EN if user asks; gender-neutral phrasing preferred.
Indeed MCP: compare 3 similar titles and top keywords—suggest title A/B, do not copy competitor JD text.
Salary: state only user band or "attractive by agreement"—no invented EUR figures.
Bias scan: flag and rewrite age-coded ("digital native"), unnecessary degree, "rockstar/ninja", mother tongue requirements unless legal necessity stated by user.
Benefits: each bullet needs [CONFIRMED] tag from user input or omit.
Channel pack: Indeed title length, LinkedIn teaser 220 chars, career page long form.
Scorecard: derive 6-10 criteria from must-haves for screening template cross-link.
No publish, no sponsored post, no API job create—draft and APPROVAL PUBLISH.
Accessibility: plain language level; avoid internal acronyms without expansion.
Legal: AGG notice if user template requires equal opportunity statement—use org boilerplate if provided.
Version jd_{role}_{date}; log assumptions at top of channel_pack.
Remote/hybrid: location field explicit per user (no "everywhere" without tax hint if user worried).```

## Workflow

1. Briefing and gathering confirmed benefits.
2. Indeed: Titel-/Keyword-Vergleich (optional, documented).
3. Write JD structure; separate must/nice requirements.
4. Bias check and gender-neutral language.
5. Create channel variants and character limits.
6. Derive the draft scorecard from the must-haves.
7. Write docx, verify, output publish instructions (manual).

## Definition of done

- [ ] No unconfirmed benefits or salary figures
- [ ] Bias-Checkliste durchgearbeitet; problematische Phrasen ersetzt
- [ ] Scorecard-Kriterien decken Must-Haves ab
- [ ] No live publishing carried out

## Security

- External publication only with HR/Marketing approval.
- No confidential internal information in JDs without approval.

## Pitfalls

- Copy Indeed title → SEO duplicate and incorrect seniority.
- “Fluent German” as a hard filter without reference to a role.
- Benefits taken over from previous job (gym closed).
- LinkedIn-Teaser abgeschnitten mitten im Wort.
- Scorecard with nice-to-haves weighted as must-haves.

## Basic examples

### Example 1 (Example data (self-written))
- **Task:** Senior Product Manager, Hybrid Wien, 4 Must-Haves
- **Input:** Benefits: 30 days of holiday confirmed, no salary
- **Prompt:**

```text
Indeed title research. JD DE inclusive. channel_pack + scorecard. No publish.
```

- **Expected result:**

```text
Summary: the agent stays read-only until approval, lists concrete next steps, and marks any missing inputs the user must supply.Summary: the agent stays read-only until approval, lists concrete next steps, and marks any missing inputs the user must supply.jd.docx | 2 title options cited | scorecard 8 criteria | benefits only 30 Tage
```

### Example 2 (Example data (self-written))
- **Task:** JD with fictitious stock options
- **Input:** User does not list any equity
- **Prompt:**

```text
Do not add equity unless confirmed.
```

- **Expected result:**

```text
Summary: the agent stays read-only until approval, lists concrete next steps, and marks any missing inputs the user must supply.Summary: the agent stays read-only until approval, lists concrete next steps, and marks any missing inputs the user must supply.JD without stock options | bias_check ok | ask about missing benefits
```
