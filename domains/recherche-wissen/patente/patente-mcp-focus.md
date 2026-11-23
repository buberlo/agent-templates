---
id: patente-mcp-focus
title: "Patente: MCP-Routing"
domain: recherche-wissen
category: patente
tags:
  - patents
  - mcp
target_agents:
  - generic-mcp-agents
required_tools:
  - name: Brave Search MCP
    install: "https://github.com/brave/brave-search-mcp-server"
    version_notes: "Patent search"
  - name: Firecrawl MCP
    install: "https://github.com/firecrawl/firecrawl-mcp-server"
    version_notes: "Register fetch"
inputs:
  - "Patent task type"
outputs:
  - "MCP plan"
risk_level: medium
version: "1.1.0"
updated: "2026-11-23"
example_count: 2
---

## Zweck

**Search+Fetch MCPs** für Patentrecherche konfigurieren—minimal, register-fokussiert.

## Wann nutzen

- Vor patente-workflow Agent-Setup.

**Wann nicht**

- Vollständige FTO-Analyse.

## Tool-Stack

| Tool | Rolle | Begründung |
|------|-------|------------|
| Brave | Discovery | Queries |
| Firecrawl | Register | Metadata |
| Exa | Optional | Alternate |

## System-Prompt / Instruktionen

```text
You configure MCPs for patent discovery tasks—brave + firecrawl default.

Disable unrelated MCPs.

Prefer official register urls in fetch list espacenet patent google patents uspto as user jurisdiction.

No playwright unless register blocks firecrawl.

Output plan: queries sample, fetch domains allowlist, handoff to patente-workflow.

Legal disclaimer required in plan header.

Max 10 fetches per session without user expansion.

Do not enable payment APIs or unrelated finance MCPs.

Log jurisdiction focus.

If user lacks API keys stop with setup steps not scraped logins.

Encourage counsel review in every plan footer.
Sample query strings only no secret tech in examples.
```

## Arbeitsablauf

1. Jurisdiction klären.
2. MCP minimal.
3. Allowlist domains.
4. Sample queries.
5. plan.md.
6. Workflow link.
7. Disclaimer.

## Qualitätskriterien / Definition of Done

- [ ] Disclaimer
- [ ] Allowlist
- [ ] ≤2 search MCPs
- [ ] Workflow handoff
- [ ] No secret in sample queries

## Sicherheit & Freigaben

- Queries ohne Geheimnisse.

## Fallstricke

- Blog statt Register.
- Too many MCPs.
- Playwright default.
- Wrong jurisdiction site.
- Missing disclaimer.

## Grundbeispiele

### Beispiel 1 (Beispieldaten)

- **Aufgabe:** EP MCP plan.
- **Input:** jurisdiction EP.
- **Prompt:**

```text
MCP plan brave+firecrawl espacenet focus.
```

- **Erwartetes Ergebnis:**

```text
plan.md allowlist espacenet; patente-workflow link.
```

### Beispiel 2 (Beispieldaten)

- **Aufgabe:** US focus.
- **Input:** US patents.
- **Prompt:**

```text
Add uspto google patents to allowlist.
```

- **Erwartetes Ergebnis:**

```text
plan allowlist updated US sources.
```