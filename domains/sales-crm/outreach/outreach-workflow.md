---
id: outreach-workflow
title: "1:1 Outreach & Sequencing"
domain: sales-crm
category: outreach
tags:
  - outreach
  - email
  - sdr
  - sales-crm
target_agents:
  - hermes
  - grokbot
  - generic-mcp-agents
  - generic
required_tools:
  - name: Hermes skills email-inbox-triage and himalaya
    install: "https://hermes-agent.nousresearch.com/docs/reference/skills-catalog"
    version_notes: "ClawHub figures: Leaderboard 23 Nov 2026."
  - name: Hermes-Skill google-workspace / gws CLI
    install: "https://hermes-agent.nousresearch.com/docs/reference/skills-catalog"
    version_notes: "Bundled-catalog."
  - name: attio MCP (Hermes-catalog)
    install: "https://github.com/NousResearch/hermes-agent/tree/main/optional-mcps/attio"
    version_notes: "Nous-approved optional-mcps-catalog entry (listing 2026-11-23)."
inputs:
  - "ICP, offer, CTA and maximum touch count"
  - "Contact list with assignable personalization hooks"
  - "Kanal: E-Mail, LinkedIn (manuell), Close Sequence"
outputs:
  - "Personalized email/LinkedIn drafts"
  - "Sequence plan with days and variants"
  - "Draft CRM activities for approval"
risk_level: medium
example_count: 2
version: "1.1.0"
updated: "2026-11-23"
---

## Purpose

Draft **hyper-relevant 1:1 messages**: evidence-based facts instead of mail-merge bullshit. Draft in Gmail/CRM—send only after human approval.

## When to use

- Neuer ICP-Test, 20–50 hochqualitative Mails.
- Follow-up chain after event/webinar with a real connection.
- Reactivation of outdated opportunities with a new use case.

**When not to use**

- Cold calling without opt-in where CAN-SPAM/UWG/GDPR prohibit it.
- LinkedIn automation or scraping of InMail limits.
- Deceptively personalized lies without a source.

## Tool stack

| Tool | Role | Rationale |
|------|-------|------------|
| Himalaya / GWS | Gmail Draft | No sending without approval |
| attio MCP | Context, Task | Activity draft |
| Close MCP | Sequence Step | If Close Team |

## System prompt

```text
Role: B2B outreach copywriter + ops (sales-crm/outreach).
Mission: Research-backed first touch and follow-ups—draft only, human sends.
Inputs: persona, pain, proof point, CTA type (call|reply|content), tone (DE business casual default).
Personalization: every opener must cite a source—LinkedIn post date, news URL, job change, tech stack page—not "I love your company".
Structure email: subject ≤50 chars, body ≤120 words first touch, one clear CTA, P.S. only if adds fact.
Follow-ups: 3-5 steps, each new angle—no "just bumping"; reference prior subject thread.
LinkedIn: connection note ≤280 chars; no automation claims.
Compliance: include unsubscribe only if marketing blast; 1:1 B2B DE note legal disclaimer lightweight—not legal advice.
CRM: draft activity text—do not set sent=true.
Anti-patterns block: fake mutual connection, fake "saw you on site" without proof, urgency manipulation.
Spintax: avoid—write variant A/B with diff hypothesis documented.
Deliverability: no links on first touch if user requests; plain text option.
Attio: link person id when provided; store draft id if API returns.
Close: sequence step as draft content only.
German/English: match recipient locale; keep product names in original brand spelling.
Log personalization_sources[] per contact for audit.
Batch: max 15 drafts per run for quality review unless user overrides.
Bounce handling: never retry guessed email patterns.
```

## Workflow

1. Clarify ICP, offer and prohibited claims.
2. Collect Hook + Source per contact (CRM/Manual).
3. Write initial contact draft (subject + body).
4. Follow-up matrix (days 3/7/14) with new value.
5. Create drafts in Gmail/CRM—status "draft".
6. Tick off the quality checklist for each email.
7. Invite users to approve sending; no SMTP sending.

## Definition of done

- [ ] Every email with a documented personalization source
- [ ] No shipping without explicit approval
- [ ] Word limit and CTA adhered to
- [ ] Legal context (B2B/newsletter) noted

## Security

- URL0—Avoid sending mass emails by mistake.
- Outreach texts may relate to the German Act Against Unfair Competition (UWG)/GDPR—no legal advice.
- Inbox tools only with user OAuth.

## Pitfalls

- Invent a ChatGPT hook → Damage to reputation if asked about it.
- Mark Gmail draft as "sent" in the CRM.
- Too many links in the first touch → spam folder.
- Activate Close Sequence without enrollment rules.
- English to German C-level without context.

## Basic examples

### Example 1 (Example data (self-written))
- **Task:** Erstkontakt an CTO Mittelstand Logistik
- **Input:** Hook: Blogpost 2026-11-10 zu Track-and-Trace API
- **Prompt:**

```text
DE, ≤120 words, CTA 20-min call. Subject options x3. Source cited in line 1.
```

- **Expected result:**

```text
Subject: Track-and-Trace Post + Frage zu EDI
Body cites URL and specific paragraph—no send, draft only.
```

### Example 2 (Example data (self-written))
- **Task:** Follow-up on day 7 with no response
- **Input:** Vorheriger Betreff, Case Study Link freigegeben
- **Prompt:**

```text
New angle: ROI snippet from case (public numbers only). ≤90 words.
```

- **Expected result:**

```text
References prior thread; adds one metric from case study PDF page 2.
```