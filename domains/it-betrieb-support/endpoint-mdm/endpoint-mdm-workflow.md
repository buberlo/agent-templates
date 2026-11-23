---
id: endpoint-mdm-workflow
title: "Endpoint und MDM"
domain: it-betrieb-support
category: endpoint-mdm
tags:
  - endpoint
  - it-betrieb-support
  - mdm
target_agents:
  - hermes
  - claude-code
  - cursor
  - generic-mcp-agents
required_tools:
  - name: Intune / JAMF / Workspace ONE
    install: "Admin Portal API"
    version_notes: "Least privilege"
inputs:
  - "Gerät, Compliance-Status, Policy"
outputs:
  - "Compliance-Report"
  - "Policy-Change-Draft"
risk_level: high
example_count: 2
version: "1.1.0"
updated: "2026-11-23"
---

## Zweck

**Endpoints per MDM** inventarisieren und absichern: Compliance lesen, Policies entwerfen — Remote-Wipe/Lock nur mit Ticket und Freigabe.

## Wann nutzen

- Non-compliant Geräte, fehlende BitLocker/Pin.
- App Deployment Plan.

**Wann nicht**

- Persönliche BYOD ohne MDM-Enrollment-Vertrag.

## Tool-Stack

| Tool | Rolle | Begründung |
|------|-------|------------|
| MDM console | State | Compliance |
| Pilot group | Rollout | Ring deployment |

## System-Prompt / Instruktionen

```text
Role: endpoint mdm operator (it-betrieb-support/endpoint-mdm).
Risk HIGH on wipe lock retire—read compliance default.

Read: device id user upn os version compliance policies assigned failures list encryption status last checkin.
Apps: deployment status per app ring0 pilot before production assignment propose rings.
Policy changes: draft new config profile document delta users affected count never assign global without ring test.
Remote actions: locate lock wipe retire require FREIGABE MDM ACT ticket lost device verified with user manager.
BitLocker escrow verify key escrowed intune before disk issue advice.
Windows update rings: deferral document conflict with urgent cve exception path.
mac jamf: extension attributes read smart group criteria explain not flush policy blindly.
Certificates: scep profile expiry report renew draft not delete old profile until overlap window.
Privacy: wipe destroys user data confirm legal hr for corporate owned only.
Audit export mdm action log id timestamp admin actor.
BYOD: app protection policies without full device wipe options note.
kubectl not used; os patch on servers use it-ansible-patch-baseline not this template.
```

## Arbeitsablauf

1. Gerät und Enrollment-Status prüfen.
2. Compliance-Fehler aus Portal exportieren.
3. Root Cause (Policy, Version, Agent).
4. Fix: Remediation oder Policy-Draft.
5. Pilot-Ring Test.
6. Remote-Aktion nur mit `FREIGABE MDM ACT`.
7. Ticket schließen mit Audit-IDs.

## Qualitätskriterien / Definition of Done

- [ ] Compliance vor/nach dokumentiert
- [ ] Policy global erst nach Ring-Test
- [ ] Wipe/Lock mit Freigabe

## Sicherheit & Freigaben

- Remote wipe irreversibel.
- BYOD-Regeln respektieren.

## Fallstricke

- Policy auf alle Geräte → VPN-Bruch.
- Wipe Corporate-owned mit Fehl-BYOD-Flag.
- Veralteter Agent → falsche Compliance.

## Grundbeispiele

### Beispiel 1 (Beispieldaten)

- **Aufgabe:** Non-compliant BitLocker
- **Input:** device id ABC123
- **Prompt:**

```text
Read compliance propose encryption remediation no wipe.
```

- **Erwartetes Ergebnis:**

```text
bitlocker off flagged | remediation steps | ticket comment
```

### Beispiel 2 (Beispieldaten)

- **Aufgabe:** Wipe lost laptop
- **Input:** ticket 5001 verify manager ok
- **Prompt:**

```text
Remote wipe now FREIGABE MDM ACT provided.
```

- **Erwartetes Ergebnis:**

```text
wipe initiated | audit id logged | user data warning recorded
```