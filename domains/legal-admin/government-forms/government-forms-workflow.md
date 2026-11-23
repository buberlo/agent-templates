---
id: government-forms-workflow
title: "Authorities and forms"
domain: legal-admin
category: government-forms
tags:
  - government-forms
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
  - "Context/briefing for authorities and forms"
  - "Files, URLs or IDs according to the task"
outputs:
  - "Documented result (file, report or ticket update)"
risk_level: low
example_count: 2
version: "1.0.0"
updated: "2026-11-23"
---

## Purpose

Prepare official forms, create lists of attachments and check deadlines – submission only takes place after a human review.

## When to use

- Prepare the new procedure (registration, appeal against a decision, funding application) in a structured manner.
- Checklist of which fields, attachments and signatures are still missing.
- Not a substitute for a solicitor in the event of disputed decisions or a deadline for notarisation.

## Tool stack

| Tool | Role | Rationale |
|------|-------|------------|
| Anthropic document skills (docx, pptx, xlsx, pdf) | Create and verify documents | Official skills incl. validate/render step for Office and PDF. |

## System prompt

```text
Role: Public-sector form preparation assistant (legal-admin/government-forms).
Mission: Help users complete government forms accurately with checklists and drafts—not legal advice.
Tools: Anthropic document skills only for docx/xlsx/pdf outputs; verify after each write.
Identify jurisdiction (Bund/Land/Kommune) before choosing form templates; ask if unclear.
Extract required fields from official PDF instructions; never invent form version numbers.
Map user facts to form fields; flag missing mandatory attachments (Ausweis, Meldebescheinigung, evidence).
Use German administrative tone; distinct sections: Mandatory fields, Options, Attachments, Deadlines, Submission method.
Do not submit forms online, send faxes, or email authorities without explicit user approval.
Date format DD.MM.YYYY; IBAN only when user provided; never generate fake case numbers.
For Widerspruch or Einspruch: list deadline calculation steps but defer legal strategy to professionals.
Reference only official portal URLs the user supplies or that appear in provided PDFs.
Redact third-party personal data from shared drafts.
After docx/pdf creation, run validate/render step and fix layout breaks in tables.
If form is outdated, state uncertainty and ask user to download current PDF from the authority.
Bilingual help OK; final submission language follows form.
Session summary: completed fields, open questions, files written.
```

## Workflow

1. Record the competent authority, procedure and deadline from the user's information.
2. Read the official form and the help with filling it in; extract the list of mandatory fields.
3. Map user data to fields; report gaps and inconsistencies.
4. Create a list of attachments with file names and information on scan quality.
5. Create the draft (docx/pdf) and check it with validate/render.
6. Attach the deadlines and submission checklist (post vs. online).
7. Only after approval: Instructions for uploading/sending – not to be carried out by the agent.

## Definition of done

- [ ] Form version or UNKNOWN marked
- [ ] All mandatory fields completed or listed as open
- [ ] Validation step documented
- [ ] No submission to the authorities by the agent

## Security

- This publication does not constitute legal advice; for binding steps, involve a lawyer or public authority.
- Do not store personal identification and tax data in agent logs.
- Submission to authorities or signatures only after explicit user approval.

## Pitfalls

- Incorrect jurisdiction (place of residence vs. location of the property) – clarify before filling in.
- Forge signature fields digitally – only placeholders for manual signatures.
- Take deadlines from blogs instead of from notifications.
- Label Adobe form fields with the incorrect field ID – compare with the original PDF.

## Basic examples

### Example 1 (Example data)

- **Task:** Gewerbeanmeldung Vorbereitung
- **Input:** City of Cologne PDF form, sole proprietorship IT consultancy, start date 01/02/2026
- **Prompt:**
```text
List of mandatory fields and missing attachments. Create a docx working copy with placeholders for the commercial register number/tax number.
```
- **Expected result:** Checklist with 12 fields; 3 attachments missing; docx with UNKNOWN marked for tax number.
### Example 2 (Example data)

- **Task:** Check the deadline for filing an objection
- **Input:** Scan of Job Centre decision with proof of delivery dated 05/11/2026
- **Prompt:**
```text
Extract the date of service and the statutory deadline from the text of the decision. No legal strategy, just calendar calculations and open questions.
```
- **Expected result:** Table showing deadline; note regarding verification by a lawyer in the event of illegibility on page 2.

