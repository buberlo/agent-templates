---
id: e-signature-workflow
title: "E-Signature Preparation and Verification"
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
  - "Signature checklist"
  - "Optional vorbereitetes Paket"
risk_level: high
example_count: 2
version: "1.1.0"
updated: "2026-11-23"
---

## Purpose

**Prepare and technically verify contracts for e-signature**—fields, signing order, signature level—**the agent does not sign** and does not trigger a QES.

## When to use

- PDF before Uebergabe an DocuSign/Adobe/ EU-QES-Dienst.
- Check already signed PDFs for signature chains.
- Checklist for Legal/Compliance.

**When not to use**

- Agent as signierende Person or Notar-Ersatz.
- Automatischer Versand an Gegenpartei without Legal-approval.
- Tax powers of attorney without specialist review.

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
Document timezone on signature timestamps UTC display.
```

## Workflow

1. PDF-Integritaet with qpdf check.
2. Field- and pagesinventar.
3. Signatur-Policy with User abstimmen (SES/AES/QES).
4. Write checklist for portal setup.
5. after User-Signaturlauf: Audit-Report (when file zurueck).
6. Hash and Version archivieren.
7. No envelope send by agent.

## Definition of done

- [ ] Checklist complete (fields, signing order, exhibits)
- [ ] SHA256 dokumentiert
- [ ] No signing process by agent
- [ ] Audit only technisch, no Rechtsberatung
- [ ] approval before Versand dokumentiert

## Security

- Contracts are strictly confidential.
- no Private Keys.
- Sending only via authorized signature tool by a human.

## Pitfalls

- Signature field on wrong page.
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
checklist.md; sha256 of msa.pdf; signer1 then signer2; no envelope id.
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
audit.md: 2 signatures found; timestamps listed; UNKNOWN legal validity.
```