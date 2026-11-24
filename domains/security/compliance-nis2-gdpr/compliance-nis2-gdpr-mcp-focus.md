---
id: compliance-nis2-gdpr-mcp-focus
title: "Compliance, NIS2 and GDPR: MCP/skill focus"
domain: security
category: compliance-nis2-gdpr
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

## Purpose

Compliance-evidence: MCP liest **Policy-Dokumente**, technische Evidenz (z. B. DMARC) per CLI-Template — kein legal advice.

## When to use

- NIS2/DSGVO control mapping with evidence links.
- Agent collects doc excerpts + `parsedmarc` report reference.

**When not to use:** Juristische Vertragsauslegung — an Legal verweisen.

## Tool stack

| Tool | Role | Rationale |
|------|-------|------------|
| Docs MCP | Policies | read |
| parsedmarc | Mail control | see email template |
| Skill verify | re-read | document match |

## System prompt

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

## Workflow

1. Control-Liste vom User.
2. MCP: Policy-Abschnitt lesen.
3. Technische Evidenz: DMARC-Report-Pfad / Ticket.
4. Mapping-Tabelle Control→Evidence.
5. Skill VERIFY re-read policy.
6. Release for Wiki Update.
7. Audit-Log MCP calls.

## Definition of done

- [ ] No Rechtsberatung formuliert
- [ ] Evidence per control linked
- [ ] PII minimiert

## Security

- Compliance-Docs vertraulich.
Wiki write only after release.

## Pitfalls

- Agent "certified" wrongly.
- Full RoPA in chat.
- Policy MCP veraltet.
- Technische Evidenz fehlt — nur Papier.
- Cross-border transfer not checked.

## Basic examples

### Example 1 (Example data (self-written))
- **Task:** Control A.5.1 Mail spoofing.
- **Input:** ISO 27001 annex ref.
- **Prompt:**

```text
Map to DMARC weekly report evidence; cite policy section via MCP read only.
```

- **Expected result:**

```text
Control A.5.1 -> dmarc_w47.html + policy §4.2 DMARC enforcement
```

### Example 2 (Example data (self-written))
- **Task:** Block wiki write.
- **Input:** no COMPLIANCE_APPROVE.
- **Prompt:**

```text
Draft table only; no Notion MCP write.
```

- **Expected result:**

```text
Markdown table in chat; MCP write not invoked
```