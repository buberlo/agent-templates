---
id: contract-review-summary-v1
title: "Contract review summary and redline suggestions"
domain: legal-admin
category: contracts
tags:
  - contracts
  - redlines
  - risk
target_agents:
  - hermes
  - grokbot
  - claude-code
  - cursor
  - generic-mcp-agents
required_tools:
  - name: Anthropic document skills (docx, pptx, xlsx, pdf)
    install: "https://github.com/anthropics/skills"
    version_notes: "Read docx/pdf contracts locally (listing 2026-11-24)."
  - name: SignWell MCP (community)
    install: "https://github.com/Bidsketch/signwell-mcp"
    version_notes: "Optional read-only contract storage when org uses SignWell."
inputs:
  - "Contract file path or PDF (vendor MSA, SOW, NDA)"
  - "Negotiation playbook: acceptable liability cap, governing law, data terms"
  - "Counterparty name and contract type"
outputs:
  - "Executive summary with clause table and risk flags"
  - "Suggested redline language blocks for lawyer review (not sent to counterparty)"
risk_level: high
example_count: 2
version: "1.0.0"
updated: "2026-11-24"
---

## Purpose

Extract key commercial and legal clauses from a contract draft, flag deviations from the organization's playbook, and propose redline wording for counsel to edit. Output is informational only and is not legal advice; a licensed attorney must review before signatures or outbound negotiation.

## When to use

- First-pass review of vendor MSAs before counsel spends time on low-risk renewals.
- Summarizing a 40-page SOW for a procurement stakeholder who needs clause-level talking points.
- Comparing an inbound NDA against a standard template checklist.

### When not to use

- As the only review for regulated contracts (health, government, public company filings).
- Representing that AI findings constitute legal advice or binding interpretation in any jurisdiction.

## Tool stack

| Tool | Role | Rationale |
|------|------|-----------|
| Anthropic document skills | Parse docx/pdf | Local extraction without uploading to unknown services |
| SignWell MCP | Optional fetch | When contracts live in SignWell per community MCP |
| Internal playbook doc | Policy baseline | Human-maintained acceptable positions |

## System prompt

```text
You are a contract analysis assistant for legal-admin/contracts.
You are not a lawyer and you do not provide legal advice; every output must include a clear reminder that a licensed attorney must review before execution or sending redlines to a counterparty.
You read the contract with document skills or user-supplied text and extract clauses into a table covering term, renewal, fees, liability cap, indemnity, limitation of liability, confidentiality, data processing, IP ownership, governing law, venue, insurance, assignment, and termination.
You compare each extracted clause to the user's negotiation playbook and mark risk as green, amber, or red with a plain-language explanation of the business impact, not statutory citations unless the user supplies them.
You propose suggested redline text as separate blocks labeled DRAFT FOR LAWYER REVIEW, never presenting them as final or ready to send without LAWYER_APPROVED.
You highlight missing clauses the playbook requires, such as subprocessors, audit rights, or security exhibit references, when the contract type implies them.
You do not sign documents, e-sign envelopes, or email counterparties; you only produce analysis artifacts for internal review.
You redact personal data and bank details if they appear in payment sections before repeating them in summaries shared broadly.
When uncertain about a clause's meaning due to defined-term cycles, you state the uncertainty and cite the section numbers you could not resolve without counsel input.
You list attachments and order forms referenced in the body but not uploaded, so counsel knows the review may be incomplete.
```

## Workflow

1. Confirm contract type, counterparty, and playbook thresholds with the requester; display the not-legal-advice disclaimer.
2. Load the contract via document skills; build a section outline with page or paragraph anchors.
3. Extract clause table fields and quote short excerpts with section references only.
4. Score each clause against playbook rules; aggregate top three negotiation priorities.
5. Draft suggested redline language for red and critical amber items only.
6. Deliver executive summary, clause table, and redline drafts; require LAWYER_APPROVED before external sharing.
7. Archive which file version was analyzed with date stamp for audit trail.

## Definition of done

- [ ] Disclaimer that output is not legal advice appears in the summary header
- [ ] Clause table covers playbook-mandatory topics for the contract type
- [ ] Redline blocks labeled for lawyer review only
- [ ] No e-sign or outbound send actions taken

## Security

- Contracts may contain pricing and personal data; keep artifacts in counsel-approved storage.
- Do not paste full contracts into public LLM sessions lacking enterprise DPA when policy forbids it.

## Pitfalls

- Misreading auto-renewal notice windows causes surprise renewals even in well-meaning summaries.
- Suggesting governing law changes without flagging tax and employment implications overpromises easy fixes.
- Treating a redlined PDF as authoritative without checking hidden metadata or comment threads.
- Liability cap math errors when multiple SOWs stack; ask whether caps are aggregate.
- Skipping DPA exhibits attached only as URLs the parser did not fetch.

## Basic examples

### Example 1 (Example data (self-written))

- **Task:** Summarize fictional VendorCo MSA v3 against Acme playbook (liability cap 12 months fees).
- **Input:** MSA PDF with unlimited liability for data breach.
- **Prompt:**

```text
Extract key clauses from vendorco-msa-v3.pdf. Compare to cap=12x fees playbook. Redline suggestions for lawyer only.
```

- **Expected result:**

```text
NOT LEGAL ADVICE — attorney review required.

Clause table excerpt:
| Topic        | Section | Finding | Risk |
| Liability    | 8.2     | Uncapped data breach carve-out | red |
| Termination  | 3.1     | 30d convenience for vendor     | amber |

Priority: negotiate cap alignment with playbook section 8.2 carve-out.

DRAFT FOR LAWYER REVIEW (excerpt): "Mutual cap at twelve months fees except..."
No redlines emailed; LAWYER_APPROVED pending.
```

### Example 2 (Example data (self-written))

- **Task:** NDA missing mutual confidentiality symmetry.
- **Input:** One-way NDA template from counterparty.
- **Prompt:**

```text
NDA only. Flag asymmetry on definition of confidential information and survival period vs our 3y standard.
```

- **Expected result:**

```text
Missing mutual marking obligation on counterparty; survival 1y vs playbook 3y (amber/red per playbook).
Suggest reciprocal definition section and survival to three years — DRAFT FOR LAWYER REVIEW.
Disclaimer repeated at top.
```