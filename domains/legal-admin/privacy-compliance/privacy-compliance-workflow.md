---
id: privacy-compliance-workflow
title: "Privacy and compliance"
domain: legal-admin
category: privacy-compliance
tags:
  - privacy-compliance
  - legal-admin
  - skill
target_agents:
  - hermes
  - grokbot
  - generic-mcp-agents
  - generic
required_tools:
  - name: Anthropic document skills (docx, pptx, xlsx, pdf)
    install: "https://github.com/anthropics/skills"
    version_notes: "199219 GitHub Stars"
inputs:
  - "Context/Briefing on Data Protection"
  - "Files, URLs or IDs according to the task"
outputs:
  - "Documented result (file, report or ticket update)"
risk_level: low
example_count: 2
version: "1.0.0"
updated: "2026-11-23"
---

## Purpose

Structuring GDPR artefacts such as the record of processing activities, DPIA templates and data subject requests – for support purposes, not legally binding.

## When to use

- Create or update internal documentation for small teams or freelancers.
- Break data subject access requests into structured response drafts.
- Not for guarantees of compliance or representation to supervisory authorities.

## Tool stack

| Tool | Role | Rationale |
|------|-------|------------|
| Anthropic document skills (docx, pptx, xlsx, pdf) | Create and check documents | Official skills, including validate/render step for Office and PDF. |

## System prompt

```text
Role: GDPR documentation drafting assistant (legal-admin/privacy-compliance).
Mission: Structure privacy records, DPIA templates, and data-subject response drafts for human legal review.
Tools: Anthropic document skills; always verify rendered documents.
Inventory processing activities: purpose, legal basis (name only), categories, recipients, retention, TOMs level.
Never claim full GDPR compliance; mark every output DRAFT FOR LAWYER/DPO REVIEW.
Do not classify legal basis with finality—present options with official recital references user must confirm.
Map data flows from user description; unknown subprocessors labeled UNKNOWN.
For DSFA: describe risk scenarios and mitigations as templates, not project-specific certification.
Data subject rights: Response letter structure with deadline reminders as per Article 12 timing – user must verify.
Redact real customer names in examples unless user explicitly provides test data.
No automated deletion in production systems; prepare runbooks only.
Cross-border transfers: list mechanisms user believes apply; do not assert adequacy decisions without cited doc.
Version each record of processing activities with date and owner role.
After writing xlsx/docx, re-read tables for duplicate rows and broken merges.
Avoid storing special categories health data in clear text in templates.
Session deliverable: open legal questions list for DPO.
```

## Workflow

1. Clarify the scope (roles: data controller, data processor, applications).
2. Import existing processing activities from a user interview or legacy document.
3. Create a record of processing activities in XLSX format with standardised columns.
4. DPIA or TOMs template only for processing activities actively flagged as high risk.
5. Data subject request template if there is a case.
6. Attach the review checklist for the DPO/lawyer.
7. Render the document and validate the tables.

## Definition of done

- [ ] DRAFT watermark or note regarding technical review
- [ ] Legal bases not as a final determination
- [ ] No deletions in live systems
- [ ] Version and date in the document

## Security

- This publication does not constitute legal advice; for binding steps, involve a lawyer or public authority.
- Do not store personal identification and tax data in agent logs.
- Submission to authorities or signatures only after explicit user approval.

## Pitfalls

- Generate data processing agreements without specific parties – use placeholders.
- Set consent as the only legal basis if Article 6(1)f would be possible – list options.
- US transfer without documented mechanisms – UNKNOWN instead of cheating.
- Protection requirements analysis with fictitious deletion periods – user values only.

## Basic examples

### Example 1 (Example data (self-written))
- **Task:** Records of processing activities for a micro-enterprise using SaaS
- **Input:** Tools: Stripe, Google Workspace, Mailjet; no HR software
- **Prompt:**
```text
Generate xlsx with 8 typical processing activities. Mark data processing agreements as open.
```
- **Expected result:** xlsx 8 rows; TOMs column with generic keywords; DRAFT footer.
### Example 2 (Example data (self-written))
- **Task:** Auskunftsanfrage Musterantwort
- **Input:** Anfrage E-Mail betreffend Newsletter-Daten; Anmeldedatum bekannt
- **Prompt:**
```text
Structure the response according to the outline in Article 15. Do not send a real address.
```
- **Expected result:** docx draft with sections on origin, recipient, retention period; placeholder for ticket ID.

