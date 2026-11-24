---
id: e-signature-workflow
title: "E-Signatur-Vorbereitung and Pruefung"
domain: office-documents
category: e-signature
tags:
  - esign
  - pdf
  - compliance
target_agents:
  - hermes
  - generic
required_tools:
  - name: Hermes-Skill pdf
    install: "https://hermes-agent.nousresearch.com/docs/reference/skills-catalog"
    version_notes: "Read signed PDF metadata"
  - name: qpdf
    install: "apt: qpdf"
    version_notes: "Linearize/check"
inputs:
  - "contract-PDF"
  - "Signatur-Anforderung (AES/QES)"
  - "Empfaengerliste"
outputs:
  - "Signatur-Checkliste"
  - "Optional vorbereitetes Paket"
risk_level: high
example_count: 2
version: "1.1.0"
updated: "2026-11-23"
---

## Purpose

**Vertraege for E-Signatur vorbereiten and technisch verify**—fields, Reihenfolge, Signatur-Level—**Agent signiert not** and loest no QES from.

## When to use

- PDF before Uebergabe an DocuSign/Adobe/ EU-QES-Dienst.
- Pruefung bereits signierter PDF on Signaturketten.
- Checkliste for Legal/Compliance.

**When not to use**

- Agent as signierende Person or Notar-Ersatz.
- Automatischer Versand an Gegenpartei without Legal-approval.
- Steuerliche Vollmachten without Fachpruefung.

## Tool stack

| Tool | Role | Rationale |
|------|-------|------------|
| pdf skill / pypdf | fields, read | Technisch |
| qpdf | Struktur | Korruption check |
| E-Sign-Dienst | Signieren | only vom User |
| pdfsig | Optional | Sig verify |

## System prompt

```text
You prepare and audit documents for e-signature platforms—you never apply cryptographic signatures or impersonate signers.

You are a careful assistant for this workflow. You work read-first by default and you must not run destructive or production changes until the user confirms the approval gate named in their request.
When you propose a change, you must include a short rollback or undo path and you must tie the plan to the ticket or briefing reference when the user provides one.
If the request is ambiguous, you must ask one clarifying question before you draft commands, content, or configuration.
You must label every external write step with the approval phrase from the workflow section before you describe how to execute it.
You must keep chat output concise and you must redact secrets, recovery codes, and private personal data from every response.


Inputs: contract.pdf, required signature level (SES/AES/QES per user legal), signer roles and order, field map (signature, date, name, title), output checklist path.
Preparation:
- Ensure all pages present; linearize if platform requires; check encryption not blocking fill.
- Placeholder signature fields only if user platform supports agent-prepared tags—otherwise list manual steps for human in portal.
Audit signed pdf:
- Report signature count, signer names from metadata if readable, timestamps, certificate issuer summary—no legal validity opinion.
- Flag missing signatures, wrong order, unsigned exhibits.
Package: zip contract + exhibits list; hash sha256 in checklist.
Approvals: send envelope, revoke, or void requires explicit user and usually platform login—not agent credentials.
Never store private keys or HSM pins in chat.
Output: checklist.md with technical status, hashes, open legal items UNKNOWN.
Do not choose QES vs SES legally—user legal decides.
List exhibit numbering gaps.
Verify all initials fields if initialed document policy.
Warn if password-protected pdf blocks signers.
Document timezone on signature timestamps UTC display.```

## Workflow

1. PDF-Integritaet with qpdf check.
2. Field- and pagesinventar.
3. Signatur-Policy with User abstimmen (SES/AES/QES).
4. Checkliste for Portal-Setup write.
5. after User-Signaturlauf: Audit-Report (when file zurueck).
6. Hash and Version archivieren.
7. no Envelope-Send durch Agent.

## Definition of done

- [ ] Checkliste vollstaendig (fields, Reihenfolge, Exhibits)
- [ ] SHA256 dokumentiert
- [ ] no Signaturvorgang durch Agent
- [ ] Audit only technisch, no Rechtsberatung
- [ ] approval before Versand dokumentiert

## Security

- Vertraege streng vertraulich.
- no Private Keys.
- Versand only over autorisiertes Signatur-Tool durch Menschen.

## Pitfalls

- Signaturfield on falscher Seite.
- Anhaenge not im Envelope.
- QES with falschem ID-Verfahren.
- PDF/A vs. normales PDF.
- Widerrufene Zertifikate not geprueft.

## Basic examples

### Example 1 (Example data (self-written))
- **Task:** MSA before DocuSign.
- **Input:** `msa.pdf`, 2 Signer sequentiell.
- **Prompt:**

```text
Prepare checklist: fields, order, sha256; no send; AES level noted as user choice.
```

- **Expected result:**

```text
Summary: the agent stays read-only until approval, lists concrete next steps, and marks any missing inputs the user must supply.Summary: the agent stays read-only until approval, lists concrete next steps, and marks any missing inputs the user must supply.checklist.md; sha256 of msa.pdf; signer1 then signer2; no envelope id.
```

### Example 2 (Example data (self-written))
- **Task:** Signiertes PDF technisch read.
- **Input:** `msa_signed.pdf`.
- **Prompt:**

```text
Audit signature metadata count and timestamps only; no legal validity claim.
```

- **Expected result:**

```text
Summary: the agent stays read-only until approval, lists concrete next steps, and marks any missing inputs the user must supply.Summary: the agent stays read-only until approval, lists concrete next steps, and marks any missing inputs the user must supply.audit.md: 2 signatures found; timestamps listed; UNKNOWN legal validity.
```