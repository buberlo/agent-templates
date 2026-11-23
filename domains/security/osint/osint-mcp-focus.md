---
id: osint-mcp-focus
title: "OSINT (offen zugängliche Quellen): MCP/Skill-Fokus"
domain: security
category: osint
tags:
  - osint
  - mcp
target_agents:
  - hermes
  - generic-mcp-agents
required_tools:
  - name: Web Search / Fetch MCP
    install: "read-only browse"
    version_notes: "public URLs only"
  - name: whois/RDAP CLI
    install: "verify step"
    version_notes: "skill cross-check"
inputs:
  - "OSINT question scope"
  - "Skill citation rules"
outputs:
  - "Cited brief"
  - "MCP source log"
risk_level: medium
example_count: 2
version: "1.0.0"
updated: "2026-11-23"
---

## Zweck

OSINT per **MCP Fetch/Search** mit Skill-Pflicht: **doppelte Quelle**, keine verdeckten Login-MCPs, gleiche Policy wie `osint-workflow`.

## Wann nutzen

- Agent mit Web-MCP für öffentliche Quellen.
- Skill erzwingt Zitationsformat.

**Wann nicht:** Wenn Web-MCP authentifizierte Bereiche ohne ROE erreicht.

## Tool-Stack

| Tool | Rolle | Begründung |
|------|-------|------------|
| Fetch MCP | Pages | public |
| Skill | Citations | URL+date |
| RDAP CLI | Verify | domain facts |

## System-Prompt / Instruktionen

```text
OSINT MCP/Skill focus (security/osint).

MCP fetch only public URLs user lists or that are clearly public documentation.
Skill: question -> source1 MCP -> source2 independent -> synthesize with citations.
Cross-check RDAP via CLI when domain facts material.
No MCP tools that automate LinkedIn/private social scraping.
Log each URL fetched with timestamp in audit footer.
If MCP returns paywall/login wall, stop; do not bypass.
Refuse private individual targeting.
Minimize quoting; summarize with link.
Disable high-risk MCPs (port scan plugins) entirely for this skill.
Human review before external sharing of OSINT brief.
```

## Arbeitsablauf

1. Scope bestätigen.
2. MCP fetch Quelle A (vendor advisory).
3. MCP fetch Quelle B (independent news/registry).
4. CLI RDAP cross-check wenn Domain.
5. Brief mit Footnotes.
6. MCP audit log.
7. Kein weiterer Schritt bei Widerspruch ohne Klärung.

## Qualitätskriterien / Definition of Done

- [ ] ≥2 unabhängige Quellen für Kernfakten
- [ ] MCP audit vollständig
- [ ] Keine Policy-Verstöße

## Sicherheit & Freigaben

- Keine Umgehung von Paywalls/Logins.

## Fallstricke

- MCP halluziniert URL — verify HTTP status.
- Eine Quelle reicht nicht.
- Injection in fetched HTML.
- Alte Cache-Snapshot MCP.

## Grundbeispiele

### Beispiel 1 (Beispieldaten)

- **Aufgabe:** Vendor breach news check.
- **Input:** Vendor V.
- **Prompt:**

```text
Two-source MCP fetch; cite; refuse if only rumor blog.
```

- **Erwartetes Ergebnis:**

```text
[1] vendor status page [2] press wire; confidence medium
```

### Beispiel 2 (Beispieldaten)

- **Aufgabe:** Paywall hit.
- **Input:** financial times article.
- **Prompt:**

```text
Stop at paywall; suggest manual analyst review.
```

- **Erwartetes Ergebnis:**

```text
Fetch 402/paywall; no bypass; manual step noted
```