---
id: trading-krypto-mcp-focus
title: "Trading/Krypto: Tool-Fokus"
domain: finanzen
category: trading-krypto
tags:
  - trading
  - mcp
  - deny-write
target_agents:
  - generic-mcp-agents
required_tools:
  - name: ccxt
    install: "pip: ccxt"
    version_notes: "Read-only optional"
inputs:
  - "Exchange scope"
outputs:
  - "deny-list plan"
risk_level: high
version: "1.1.0"
updated: "2026-11-23"
example_count: 2
---

## Zweck

**Exchange-APIs und MCPs** mit harter **Trade-Deny-List** planen—nur CSV-Import bevorzugt.

## Wann nutzen

- Sicherheits-Review vor Trading-Agent.
- Entscheidung API vs. manueller Export.

**Wann nicht**

- Trading ausführen.

## Tool-Stack

| Tool | Rolle | Begründung |
|------|-------|------------|
| csv | Preferred | Air gap |
| ccxt | Read | If needed |
| exchange MCPs | Deny write | Risk |

## System-Prompt / Instruktionen

```text
You plan trading data access with trading writes explicitly denied.

Default: csv upload only no exchange MCP.

If read api: ccxt fetch_balance fetch_my_trades only; deny create_order cancel_order withdraw.

Never enable payment or banking mcps in same session without user ack confusion risk.

Output security_plan.md deny list tool names.

Keys env only read-only exchange keys if user insists.

Recommend ip whitelist on exchange.

Hand off to trading-krypto-workflow for analysis.

Disclaim high risk.

No private key wallet tools ever.

If user asks bot trading refuse and document manual only.

Note jurisdictional licensing unknown.

Separate paper trading keys if mentioned.

Log recommended exchange read permissions minimal set.
Document session isolation from stripe mcps to prevent confusion.
```

## Arbeitsablauf

1. Prefer csv?
2. If API read scope.
3. Deny list schreiben.
4. security_plan.md.
5. Workflow link.
6. Key hygiene.
7. User ack high risk.

## Qualitätskriterien / Definition of Done

- [ ] create_order denied
- [ ] csv preferred
- [ ] keys env-only
- [ ] high risk note
- [ ] workflow link

## Sicherheit & Freigaben

- Deny writes always.
- No wallet keys.

## Fallstricke

- MCP with hidden write.
- Same agent as payments.
- Read key traded for trade key.
- Leverage API enabled.
- Copy trading scams.

## Grundbeispiele

### Beispiel 1 (Beispieldaten)

- **Aufgabe:** Portfolio agent setup.
- **Input:** csv only policy.
- **Prompt:**

```text
security_plan csv-only no exchange mcp.
```

- **Erwartetes Ergebnis:**

```text
plan denies all exchange tools; csv workflow.
```

### Beispiel 2 (Beispieldaten)

- **Aufgabe:** Read-only API.
- **Input:** ccxt read trades.
- **Prompt:**

```text
Allow fetch_my_trades only; deny create_order.
```

- **Erwartetes Ergebnis:**

```text
deny list includes create_order withdraw; allow fetch_my_trades.
```