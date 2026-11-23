---
id: compliance-nis2-dsgvo-mcp-focus
title: "Compliance, NIS2 und DSGVO: MCP/Skill-Fokus"
domain: security
category: compliance-nis2-dsgvo
tags:
  - compliance
  - dsgvo
  - mcp
target_agents:
  - hermes
  - generic-mcp-agents
required_tools:
  - name: Notion/Google Docs MCP
    install: "Policy docs read"
    version_notes: "write gated"
  - name: parsedmarc
    install: "email-postfix-dmarc template"
    version_notes: "technical control"
inputs:
  - "Control catalog reference"
  - "Skill evidence steps"
outputs:
  - "Evidence mapping table"
  - "MCP audit trail"
risk_level: medium
example_count: 2
version: "1.0.0"
updated: "2026-11-23"
---

## Zweck

Compliance-Nachweise: MCP liest **Policy-Dokumente**, technische Evidenz (z. B. DMARC) per CLI-Template — kein Rechtsrat.

## Wann nutzen

- NIS2/DSGVO Control-Mapping mit Evidenz-Links.
- Agent sammelt Doc-Auszüge + `parsedmarc`-Report-Referenz.

**Wann nicht:** Juristische Vertragsauslegung — an Legal verweisen.

## Tool-Stack

| Tool | Rolle | Begründung |
|------|-------|------------|
| Docs MCP | Policies | read |
| parsedmarc | Mail control | see email template |
| Skill verify | re-read | document match |

## System-Prompt / Instruktionen

```text
Compliance MCP/Skill focus (security/compliance-nis2-dsgvo).

Not legal advice; map controls to evidence artifacts only.
Skill: list control id -> required evidence -> MCP doc fetch -> technical verify command -> approval for external write.
GDPR: minimize personal data in summaries; reference processing records by id.
NIS2: distinguish organizational vs technical measures in table columns.
MCP read policy PDFs/Notion; quote short excerpts with citation, not full personal data inventories.
DMARC evidence: point to email-postfix-dmarc-parse template commands, do not store full XML in wiki via MCP without redaction.
External wiki MCP writes need COMPLIANCE_APPROVE.
Verify step: re-fetch doc section after edit for hash or last-edited timestamp.
No certification claims ("ISO done") without auditor doc reference.
```

## Arbeitsablauf

1. Control-Liste vom Nutzer.
2. MCP: Policy-Abschnitt lesen.
3. Technische Evidenz: DMARC-Report-Pfad / Ticket.
4. Mapping-Tabelle Control→Evidence.
5. Skill VERIFY re-read policy.
6. Freigabe für Wiki-Update.
7. Audit-Log MCP calls.

## Qualitätskriterien / Definition of Done

- [ ] Keine Rechtsberatung formuliert
- [ ] Evidenz pro Control verknüpft
- [ ] PII minimiert

## Sicherheit & Freigaben

- Compliance-Docs vertraulich.
- Wiki write nur nach Freigabe.

## Fallstricke

- Agent „zertifiziert“ fälschlich.
- Vollständige RoPA in Chat.
- Policy MCP veraltet.
- Technische Evidenz fehlt — nur Papier.
- Cross-border transfer nicht geprüft.

## Grundbeispiele

### Beispiel 1 (Beispieldaten)

- **Aufgabe:** Control A.5.1 Mail spoofing.
- **Input:** ISO 27001 annex ref.
- **Prompt:**

```text
Map to DMARC weekly report evidence; cite policy section via MCP read only.
```

- **Erwartetes Ergebnis:**

```text
Control A.5.1 -> dmarc_w47.html + policy §4.2 DMARC enforcement
```

### Beispiel 2 (Beispieldaten)

- **Aufgabe:** Block wiki write.
- **Input:** no COMPLIANCE_APPROVE.
- **Prompt:**

```text
Draft table only; no Notion MCP write.
```

- **Erwartetes Ergebnis:**

```text
Markdown table in chat; MCP write not invoked
```