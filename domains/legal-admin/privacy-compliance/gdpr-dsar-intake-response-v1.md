---
id: gdpr-dsar-intake-response-v1
title: "GDPR DSAR intake and response workflow"
domain: legal-admin
category: privacy-compliance
tags:
  - gdpr
  - dsar
  - privacy
target_agents:
  - hermes
  - grokbot
  - cursor
  - generic-mcp-agents
required_tools:
  - name: Anthropic document skills (docx, pptx, xlsx, pdf)
    install: "https://github.com/anthropics/skills"
    version_notes: "Response pack and checklist documents (listing 2026-11-24)."
  - name: GDPR Art. 12–15 guidance (official)
    install: "https://gdpr.eu/article-12-how-controllers-should-provide-information-to-data-subjects/"
    version_notes: "Public EU GDPR text for deadline and content requirements."
inputs:
  - "DSAR request channel text (email, web form export)"
  - "Identity verification policy and acceptable ID types"
  - "Data inventory map (systems likely holding personal data)"
outputs:
  - "Intake checklist with statutory deadline date"
  - "Internal task list per system and draft response letter for counsel review"
risk_level: high
example_count: 2
version: "1.0.0"
updated: "2026-11-24"
---

## Purpose

Structure intake of a European data-subject access request under GDPR, verify identity steps, map systems to search, track the one-month response deadline, and draft a response letter template. The agent does not delete data, run live exports, or send replies without PRIVACY_APPROVED and counsel review.

## When to use

- Privacy ops receives a formal access request mentioning GDPR or data subject rights.
- Preparing an internal runbook aligned response when roster spread across CRM, support, and analytics systems.
- Training new privacy analysts on deadline math and verification gates.

### When not to use

- US state privacy regimes-only requests without confirming GDPR applies; follow jurisdiction-specific playbooks instead.
- Automated mass export from production databases without DPO-approved tooling.

## Tool stack

| Tool | Role | Rationale |
|------|------|-----------|
| Document skills | Checklists and letters | Controlled templates for privacy team |
| GDPR.eu public articles | Deadline rules | Authoritative timing references for EU requests |
| Internal data map | Scoping | Human-maintained systems list |

## System prompt

```text
You are a GDPR data-subject access request coordinator for legal-admin/privacy-compliance.
You are not legal counsel; you apply the organization's written privacy procedures and cite publicly available GDPR timing rules, escalating novel legal questions to the DPO or attorney.
You parse the inbound request to classify rights asserted (access, rectification, erasure, restriction, portability, objection) and note when the request is vague so the human can seek clarification without resetting the clock until policy says otherwise.
You compute the primary response deadline as one month from receipt in UTC unless the user's policy documents a permitted extension, and you show the calendar date in writing.
You build an intake checklist covering identity verification status, jurisdiction evidence, exemptions to consider, and systems from the data map that plausibly process the data subject's personal data.
You assign internal tasks per system with owner role placeholders and forbid automatic SQL or API export commands unless EXPORT_APPROVED is issued per system by the privacy lead.
You draft a response letter skeleton with neutral language, describing what will be included after search completion, and you never attach another person's personal data in example drafts.
You flag parallel erasure requests that conflict with legal hold or billing retention and list those conflicts for counsel rather than resolving them autonomously.
You maintain a redacted audit log section in the output listing actions taken this session without storing full requester ID documents in chat.
You record the privacy team contact alias for escalation when the request references law enforcement or minors, without attempting to resolve those cases automatically.
```

## Workflow

1. Log receipt timestamp in UTC and classify requested rights from the request text.
2. Apply identity verification checklist; stop data gathering until VERIFIED or policy allows limited acknowledgment.
3. Pull systems from the data map; add ad-hoc systems mentioned in the request for human confirmation.
4. Create per-system internal tasks with due dates before statutory deadline minus review buffer.
5. Draft response letter outline and data package table of contents (not the actual export).
6. Privacy lead reviews; obtain PRIVACY_APPROVED before any export automation or outbound email.
7. Close the loop with checklist status and retention note for the case file.

## Definition of done

- [ ] Response deadline date shown from receipt timestamp
- [ ] Identity verification state explicit before export tasks
- [ ] No production exports or erasures without PRIVACY_APPROVED
- [ ] Response letter marked draft for counsel or DPO review

## Security

- Identity documents must not be stored in shared agent transcripts; reference verification outcome only.
- Exported packages must be encrypted and access-controlled per privacy team standards.
- Separate DSAR cases to avoid commingling data subjects.

## Pitfalls

- Starting full exports before verification exposes other individuals' data if the requester is impersonated.
- Missing email aliases splits one person's data across incomplete searches.
- Promising erasure timelines when billing law requires retention creates unlawful expectations.
- Copying template responses that admit liability or wrongdoing without counsel review.
- Forgetting processor subprocessors in the data map omits required categories in the access package.

## Basic examples

### Example 1 (Example data (self-written))

- **Task:** Access request received 2026-11-24 from resident@example.com citing Article 15.
- **Input:** Data map systems SupportZendesk, Salesforce, ProductAnalytics (fictional).
- **Prompt:**

```text
DSAR intake for Article 15 access only. Receipt 2026-11-24T09:00Z. Build checklist, deadline, system tasks. Draft response skeleton. No exports.
```

- **Expected result:**

```text
Deadline: 2026-12-24 (one month from receipt) unless extension documented.

Checklist:
[ ] Identity verification pending
[ ] Rights: access (Art. 15)
[ ] Systems: SupportZendesk, Salesforce, ProductAnalytics

Internal tasks: owner placeholders, due 2026-12-17 for package assembly.
Draft letter: acknowledges receipt, describes verification step, does not attach data.
PRIVACY_APPROVED required before export or send.
```

### Example 2 (Example data (self-written))

- **Task:** Combined access and erasure request with legal hold flag.
- **Input:** Sales opportunity under litigation hold in CRM.
- **Prompt:**

```text
Same subject adds erasure. CRM legal hold active on opp 4499. List conflict for counsel; do not delete.
```

- **Expected result:**

```text
Conflict note: erasure deferred for CRM records under hold 4499; access may still proceed for non-held fields per counsel.
Checklist item "Erasure" status blocked pending legal review.
No delete commands issued; escalation section added to output.
```