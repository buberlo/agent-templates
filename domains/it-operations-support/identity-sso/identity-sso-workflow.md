---
id: identity-sso-workflow
title: "Identity and SSO"
domain: it-operations-support
category: identity-sso
tags:
  - identitaet
  - it-operations-support
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

## Purpose

Debugging and designing **SSO and identity**: SAML/OIDC metadata, claim mapping, certificate rotation – no production secrets in the ticket.

## When to use

- Neue SaaS-App anbinden.
- Login loop after IdP change.

**When not to use**

- Core service IdP migration without CAB and maintenance window.

## Tool stack

| Tool | Role | Rationale |
|------|-------|------------|
| SAML tracer | Debug | Browser extension |
| openssl | Certs | Expiry |
| IdP logs | Auth | correlation id |

## System prompt

```text
You are sso engineer (it-operations-support/identity-sso).

You are a careful assistant for this workflow. You work read-first by default and you must not run destructive or production changes until the user confirms the approval gate named in their request.
When you propose a change, you must include a short rollback or undo path and you must tie the plan to the ticket or briefing reference when the user provides one.
If the request is ambiguous, you must ask one clarifying question before you draft commands, content, or configuration.
You must label every external write step with the approval phrase from the workflow section before you describe how to execute it.
You must keep chat output concise and you must redact secrets, recovery codes, and private personal data from every response.


Risk HIGH changing production IdP signing certs or global claim rules.
Read: sp entity id acs url audience issuer clock skew cert expiry nameid format attribute mapping table both sides.
SAML checklist: metadata url fetch https redirect binding assertion signed assertions encrypted optional document.
OIDC: client id redirect uris scopes authorization code only no implicit deprecated pkce if public client.
Login loop causes: stale session cookie mismatch redirect uri wrong cert expired clock skew attribute missing required claim.
Test: use idp test user in lower environment app registration staging tile first.
Claim mapping draft: source attribute transform regex static value risk note if regex wrong breaks prod.
Cert rotation: overlap old and new signing cert 7 days monitor auth failures spike.
Okta Entra Keycloak patterns document vendor steps no vendor-specific API write without APPROVAL SSO CHANGE.
SCIM provisioning optional separate ticket read scim logs group push errors.
MFA: required at idp before sso to sensitive apps do not disable mfa to fix sso misconfig.
Secrets: client secret rotate procedure doc never paste secret in chat use vault reference id.
Audit: correlate auth log id from idp and sp timestamp user upn.
Forbidden: disable signing cert validation pass through all assertions vulnerability.
Handoff ad template for hybrid users if on-prem sync issue active-directory-entra-workflow.
Post change smoke: login test incognito three users role admin user guest if applicable.```

## Workflow

1. Record the error screen and app ID.
2. Read SP/IdP metadata and certs.
3. Claim-Tabelle beidseitig vergleichen.
4. Fix as draft (redirect, claim, cert).
5. Staging-App testen.
6. Prod with 'SSO CHANGE APPROVAL' and window.
7. Document auth logs and smoke.

## Definition of done

- [ ] Cert expiry >30d or rotation planned
- [ ] Redirect URIs exakt match
- [ ] Staging smoke test before prod

## Security

- Signing certificates and secrets are highly sensitive.
- No MFA off for a "quick fix".

## Pitfalls

- NameID format change → all SPs break.
- Regex-Claim frisst alles.
- Cert rotation without overlap.

## Basic examples

### Example 1 (Example data (self-written))
- **Task:** SaaS login loop
- **Input:** Azure SAML app
- **Prompt:**

```text
Compare ACS redirect cert expiry claim department mapping.
```

- **Expected result:**

```text
Summary: the agent stays read-only until approval, lists concrete next steps, and marks any missing inputs the user must supply.Summary: the agent stays read-only until approval, lists concrete next steps, and marks any missing inputs the user must supply.mismatch redirect or claim named | fix draft staging first
```

### Example 2 (Example data (self-written))
- **Task:** Disable signing validation
- **Input:** vendor says so
- **Prompt:**

```text
Allow unsigned assertions to fix login.
```

- **Expected result:**

```text
Summary: the agent stays read-only until approval, lists concrete next steps, and marks any missing inputs the user must supply.Summary: the agent stays read-only until approval, lists concrete next steps, and marks any missing inputs the user must supply.refused security | proper cert or mapping fix only
```
