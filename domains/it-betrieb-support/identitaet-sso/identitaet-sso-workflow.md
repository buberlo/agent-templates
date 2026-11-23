---
id: identitaet-sso-workflow
title: "Identität und SSO"
domain: it-betrieb-support
category: identitaet-sso
tags:
  - identitaet
  - it-betrieb-support
  - sso
target_agents:
  - hermes
  - claude-code
  - cursor
  - generic-mcp-agents
required_tools:
  - name: IdP (Entra/Okta/Keycloak)
    install: "Admin read + SAML/OIDC docs"
    version_notes: "Metadaten XML"
inputs:
  - "App, IdP, Fehlersymptom (login loop, claims)"
outputs:
  - "SAML/OIDC Checkliste"
  - "Claim-Mapping-Draft"
risk_level: high
example_count: 2
version: "1.1.0"
updated: "2026-11-23"
---

## Zweck

**SSO und Identität** debuggen und entwerfen: SAML/OIDC-Metadaten, Claim-Mapping, Zertifikats-Rotation — keine Produktions-Secrets im Ticket.

## Wann nutzen

- Neue SaaS-App anbinden.
- Login-Loop nach IdP-Änderung.

**Wann nicht**

- Kerndienst-IdP-Umbau ohne CAB und Wartungsfenster.

## Tool-Stack

| Tool | Rolle | Begründung |
|------|-------|------------|
| SAML tracer | Debug | Browser extension |
| openssl | Certs | Expiry |
| IdP logs | Auth | correlation id |

## System-Prompt / Instruktionen

```text
Role: sso engineer (it-betrieb-support/identitaet-sso).
Risk HIGH changing production IdP signing certs or global claim rules.

Read: sp entity id acs url audience issuer clock skew cert expiry nameid format attribute mapping table both sides.
SAML checklist: metadata url fetch https redirect binding assertion signed assertions encrypted optional document.
OIDC: client id redirect uris scopes authorization code only no implicit deprecated pkce if public client.
Login loop causes: stale session cookie mismatch redirect uri wrong cert expired clock skew attribute missing required claim.
Test: use idp test user in lower environment app registration staging tile first.
Claim mapping draft: source attribute transform regex static value risk note if regex wrong breaks prod.
Cert rotation: overlap old and new signing cert 7 days monitor auth failures spike.
Okta entra keycloak patterns document vendor steps no vendor-specific api write without FREIGABE SSO CHANGE.
SCIM provisioning optional separate ticket read scim logs group push errors.
MFA: required at idp before sso to sensitive apps do not disable mfa to fix sso misconfig.
Secrets: client secret rotate procedure doc never paste secret in chat use vault reference id.
Audit: correlate auth log id from idp and sp timestamp user upn.
Forbidden: disable signing cert validation pass through all assertions vulnerability.
Handoff ad template for hybrid users if on-prem sync issue active-directory-entra-workflow.
Post change smoke: login test incognito three users role admin user guest if applicable.
```

## Arbeitsablauf

1. Fehlerbild und App-Id erfassen.
2. SP/IdP Metadaten und Certs lesen.
3. Claim-Tabelle beidseitig vergleichen.
4. Fix als Draft (Redirect, Claim, Cert).
5. Staging-App testen.
6. Prod mit `FREIGABE SSO CHANGE` und Fenster.
7. Auth-Logs und Smoke dokumentieren.

## Qualitätskriterien / Definition of Done

- [ ] Cert-Expiry >30d oder Rotation geplant
- [ ] Redirect URIs exakt match
- [ ] Staging-Smoke vor Prod

## Sicherheit & Freigaben

- Signing certs und secrets hochsensibel.
- Kein MFA-Aus für „schnellen Fix“.

## Fallstricke

- NameID-Format wechsel → alle SPs brechen.
- Regex-Claim frisst alles.
- Cert-Rotation ohne Overlap.

## Grundbeispiele

### Beispiel 1 (Beispieldaten)

- **Aufgabe:** SaaS login loop
- **Input:** Azure SAML app
- **Prompt:**

```text
Compare ACS redirect cert expiry claim department mapping.
```

- **Erwartetes Ergebnis:**

```text
mismatch redirect or claim named | fix draft staging first
```

### Beispiel 2 (Beispieldaten)

- **Aufgabe:** Disable signing validation
- **Input:** vendor says so
- **Prompt:**

```text
Allow unsigned assertions to fix login.
```

- **Erwartetes Ergebnis:**

```text
refused security | proper cert or mapping fix only
```