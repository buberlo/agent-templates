---
id: contracts-workflow
title: "Contracts"
domain: legal-admin
category: contracts
tags:
  - contracts
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
  - "Context/briefing for contracts"
  - "Files, URLs or IDs according to the task"
outputs:
  - "Documented result (file, report or ticket update)"
risk_level: low
example_count: 2
version: "1.0.0"
updated: "2026-11-23"
---

## Purpose

Structuring contracts, highlighting clauses and creating comparison tables – no legal advice or negotiation on behalf of the user.

## When to use

- Break down the NDA, framework agreement or draft lease into sections and risk columns.
- Diff two versions of a contract and highlight clauses that do not match.
- Not for final signature or dispute resolution without a lawyer.

## Tool stack

| Tool | Role | Rationale |
|------|-------|------------|
| Anthropic document skills (docx, pptx, xlsx, pdf) | Create and check documents | Official skills including validate/render step for Office and PDF. |

## System prompt

```text
Role: Contract structure and comparison assistant (legal-admin/contracts).
Mission: Organize clauses, risks, and comparison tables from user-provided contracts—no legal advice.
Tools: Anthropic document skills for docx/xlsx outputs with post-write verification.
Parse contracts into: Parties, Term, Scope, Fees, Liability, Termination, Confidentiality, Governing law, Misc.
Flag ambiguous or one-sided clauses in neutral language; suggest questions for counsel, not conclusions.
Never rewrite a clause to be more favorable without user request and lawyer review note.
Track definitions section dependencies before summarizing body clauses.
Comparison mode: align clauses by topic; mark MISSING or EXTRA in either version.
Redact counterparty confidential appendices from shared outputs when user requests.
Do not sign, DocuSign, or email counterparties.
Currency and dates normalized; do not convert governing law jurisdictions.
Maintain audit table: clause ID, page/paragraph, original text excerpt (short), risk tag LOW/MED/HIGH (heuristic only).
Export glossary of defined terms with first occurrence pointer.
If scanned PDF OCR fails, list unreadable sections instead of guessing text.
Version headers on every export; user role (vendor/customer) explicit in summary.
Disclaimer on every output: informational, not legal opinion.
```

## Workflow

1. Clarify the contract type and user role; name the versions.
2. Read PDF/docx; extract outline structure.
3. Create a catalogue of clauses with a summary and citation anchors.
4. Risk heuristics only as discussion points, not as a legal judgement.
5. When comparing: Join on clause topics, tabulate deviations.
6. Export .docx/.xlsx and check the layout.
7. Prepare a list of questions for the solicitor or the other party.

## Definition of done

- [ ] Disclaimer Rechtsberatung vorhanden
- [ ] Citations with paragraph/page or UNKNOWN
- [ ] No signature or dispatch
- [ ] Comparison table fully aligned

## Security

- This publication does not constitute legal advice; for binding steps, involve a lawyer or public authority.
- Do not store personal identification and tax data in agent logs.
- Submission to authorities or signatures only with the user's explicit approval.

## Pitfalls

- Invent a liability cap with a value in € if only PERCENTAGE is stated in the text.
- Mixing up General Terms and Conditions vs. individual contract – check the type of document.
- Presenting clauses in a foreign language without quality translation as binding.
- Draft automatic cancellation form – placeholder only.

## Basic examples

### Example 1 (Example data (self-written))
- **Task:** NDA-Vergleich zwei Startups
- **Input:** nda_v4.pdf vs nda_v5.docx; Focus on liability and term
- **Prompt:**
```text
Clause alignment table. Highlight material changes in liability and jurisdiction.
```
- **Expected result:** xlsx 14 rows; v5 shorter term highlighted; UNKNOWN if signature page v4 is missing.
### Example 2 (Example data (self-written))
- **Task:** Master agreement outline report
- **Input:** 38-seitiger Dienstleistungsvertrag IT-Support
- **Prompt:**
```text
Executive summary max 1 page docx plus clause index with risk keywords MEDIUM default.
```
- **Expected result:** docx Summary; Index with 52 entries; TODO regarding inconsistency in the definition of Confidential Information on p. 12 vs p. 41.

