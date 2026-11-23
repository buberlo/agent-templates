---
id: e-signatur-workflow
domain: office-dokumente
title: "E-Signatur-Vorbereitung und Prüfung"
category: e-signatur
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
  - "Vertrags-PDF"
  - "Signatur-Anforderung (AES/QES)"
  - "Empfängerliste"
outputs:
  - "Signatur-Checkliste"
  - "Optional vorbereitetes Paket"
risk_level: high
version: "1.1.0"
updated: "2026-11-23"
example_count: 2
---

## Zweck

**Verträge für E-Signatur vorbereiten und technisch prüfen**—Felder, Reihenfolge, Signatur-Level—**Agent signiert nicht** und löst keine QES aus.

## Wann nutzen

- PDF vor Übergabe an DocuSign/Adobe/ EU-QES-Dienst.
- Prüfung bereits signierter PDF auf Signaturketten.
- Checkliste für Legal/Compliance.

**Wann nicht**

- Agent als signierende Person oder Notar-Ersatz.
- Automatischer Versand an Gegenpartei ohne Legal-Freigabe.
- Steuerliche Vollmachten ohne Fachprüfung.

## Tool-Stack

| Tool | Rolle | Begründung |
|------|-------|------------|
| pdf skill / pypdf | Felder, lesen | Technisch |
| qpdf | Struktur | Korruption check |
| E-Sign-Dienst | Signieren | Nur vom Nutzer |
| pdfsig | Optional | Sig verify |

## System-Prompt / Instruktionen

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

## Arbeitsablauf

1. PDF-Integrität mit qpdf check.
2. Feld- und Seiteninventar.
3. Signatur-Policy mit Nutzer abstimmen (SES/AES/QES).
4. Checkliste für Portal-Setup schreiben.
5. Nach Nutzer-Signaturlauf: Audit-Report (wenn Datei zurück).
6. Hash und Version archivieren.
7. Kein Envelope-Send durch Agent.

## Qualitätskriterien / Definition of Done

- [ ] Checkliste vollständig (Felder, Reihenfolge, Exhibits)
- [ ] SHA256 dokumentiert
- [ ] Kein Signaturvorgang durch Agent
- [ ] Audit nur technisch, keine Rechtsberatung
- [ ] Freigabe vor Versand dokumentiert

## Sicherheit & Freigaben

- Verträge streng vertraulich.
- Keine Private Keys.
- Versand nur über autorisiertes Signatur-Tool durch Menschen.

## Fallstricke

- Signaturfeld auf falscher Seite.
- Anhänge nicht im Envelope.
- QES mit falschem ID-Verfahren.
- PDF/A vs. normales PDF.
- Widerrufene Zertifikate nicht geprüft.

## Grundbeispiele

### Beispiel 1 (Beispieldaten)

- **Aufgabe:** MSA vor DocuSign.
- **Input:** `msa.pdf`, 2 Signer sequentiell.
- **Prompt:**

```text
Prepare checklist: fields, order, sha256; no send; AES level noted as user choice.
```

- **Erwartetes Ergebnis:**

```text
checklist.md; sha256 of msa.pdf; signer1 then signer2; no envelope id.
```

### Beispiel 2 (Beispieldaten)

- **Aufgabe:** Signiertes PDF technisch lesen.
- **Input:** `msa_signed.pdf`.
- **Prompt:**

```text
Audit signature metadata count and timestamps only; no legal validity claim.
```

- **Erwartetes Ergebnis:**

```text
audit.md: 2 signatures found; timestamps listed; UNKNOWN legal validity.
```