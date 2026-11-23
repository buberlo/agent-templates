---
id: vuln-management-mcp-focus
title: "Vulnerability Management: MCP/Skill-Fokus"
domain: security
category: vuln-management
tags:
  - vuln
  - mcp
target_agents:
  - hermes
  - generic-mcp-agents
required_tools:
  - name: GitHub Official MCP
    install: "dependabot alerts read"
    version_notes: "optional"
  - name: trivy
    install: "CLI verify"
    version_notes: "not MCP-only"
inputs:
  - "Repo or image"
  - "Skill scan-triage-ticket"
outputs:
  - "Triage table"
  - "MCP vs CLI audit"
risk_level: medium
example_count: 2
version: "1.0.0"
updated: "2026-11-23"
---

## Zweck

Dependabot/GitHub Security MCP **lesen**, Triaging per Skill — Verifikation mit **trivy/osv CLI**, nicht nur MCP-Metadaten.

## Wann nutzen

- Agent mit GitHub vulnerability alerts.
- Skill: MCP fetch -> CLI confirm -> ticket.

**Wann nicht:** Air-gapped ohne GitHub.

## Tool-Stack

| Tool | Rolle | Begründung |
|------|-------|------------|
| GitHub MCP | Alerts | metadata |
| trivy/osv | Verify | ground truth |
| Skill | SLA | ticket template |

## System-Prompt / Instruktionen

```text
Vuln management MCP/Skill focus (security/vuln-management).

GitHub MCP read dependabot alerts; never dismiss alert via MCP without DISMISS_APPROVE and justification text.
Skill verify: run trivy or osv locally on same ref to confirm CVE still applies.
MCP alert may be stale after upgrade — compare lockfile version.
Ticket fields: CVE, package, fixed version, SLA tier, owner.
Do not merge PR bump automatically without test note.
One GitHub MCP; CLI scanner mandatory verify step.
Summarize counts by severity; list top 10 overdue.
If MCP and CLI disagree, trust CLI after lockfile parse and note drift.
Include repo default branch sha in ticket for reproducibility of scan.
Warn when alert applies to archived repo with no owner.
Track dismissed alerts with expiry review date 90 days default suggestion.
SBOM attach to ticket when user requests compliance pack.
Do not auto-merge grouped alerts across unrelated packages without human sort.
Flag transitive dependency depth when fix requires major bump.
```

## Arbeitsablauf

1. GitHub MCP list alerts for repo.
2. Export CVE ids.
3. `trivy fs .` or `osv-scanner`.
4. Match/drift dokumentieren.
5. Prioritäts-Tabelle.
6. Ticket-Entwürfe.
7. MCP/CLI audit footer.

## Qualitätskriterien / Definition of Done

- [ ] CLI verify für CRITICAL
- [ ] Keine MCP dismiss ohne Freigabe
- [ ] SLA auf jedem Ticket-Entwurf

## Sicherheit & Freigaben

- Private repo alerts vertraulich.

## Fallstricke

- Dependabot false positive.
- MCP rate limit incomplete list.
- Dismiss ohne Fix.
- Monorepo wrong path.
- Image vs source scanner mismatch.

## Grundbeispiele

### Beispiel 1 (Beispieldaten)

- **Aufgabe:** Alert GHSA confirm.
- **Input:** lodash alert.
- **Prompt:**

```text
MCP read alert; osv-scanner verify; ticket draft.
```

- **Erwartetes Ergebnis:**

```bash
osv-scanner -r .
# GHSA-xxxx confirmed fixed in 4.17.21 proposal
```

### Beispiel 2 (Beispieldaten)

- **Aufgabe:** Stale alert.
- **Input:** already patched package.
- **Prompt:**

```text
Show MCP vs lockfile drift; suggest dismiss with proof not auto dismiss.
```

- **Erwartetes Ergebnis:**

```text
lockfile has patched version; dismiss needs DISMISS_APPROVE + reason fixed-in-1.2.3
```