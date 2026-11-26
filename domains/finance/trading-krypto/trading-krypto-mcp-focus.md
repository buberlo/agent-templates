---
id: trading-krypto-mcp-focus
title: "Trading/crypto: tool focus"
domain: finance
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
  - "Exchange and portfolio data scope"
outputs:
  - "Hard trade-deny security plan (security_plan.md)"
risk_level: high
example_count: 2
version: "1.1.0"
updated: "2026-11-23"
---

## Purpose

Design **exchange API and MCP tooling configurations** with a **hard trade-and-withdrawal deny list**—defaulting to air-gapped CSV imports and strictly blocking order creation, cancellation, and fund withdrawals.

## When to use

- Conducting a security and tool-policy review before configuring a portfolio analysis agent.
- Deciding between offline CSV trade exports and read-only exchange API access (`ccxt`).

### When not to use

- Executing live orders, automated bot trading, or on-chain wallet transfers.

## Tool stack

| Tool | Role | Rationale |
|------|------|-----------|
| CSV export files | Primary data source (preferred) | Air-gapped from exchange accounts with zero execution or withdrawal risk |
| `ccxt` (read-only) | Optional balance and trade history fetch | Used only if the user insists on API polling with read-only keys |
| Exchange MCP servers | Explicitly denied for write operations | High financial risk if order or withdrawal tools are exposed |

## System prompt

```text
You plan trading and crypto data access configurations with all trading, order, and withdrawal write actions permanently denied.
Work in the user's language.

Security & Tooling Rules:
1. Default Path: Prefer offline CSV uploads with zero exchange MCP servers enabled.
2. Optional Read-Only API Path: If the user requires API reading via ccxt, permit ONLY read endpoints (fetch_balance, fetch_my_trades). Explicitly deny create_order, cancel_order, edit_order, transfer, and withdraw.
3. Wallet Prohibition: Never enable private-key, seed-phrase, or on-chain signing wallet tools under any circumstances.
4. Session Isolation: Never enable payment processors (e.g., Stripe MCP) or banking MCPs in the same agent session as crypto/exchange tools to prevent cross-tool confusion.
5. Key Hygiene: If read-only exchange API keys are used, load them via environment variables only, restrict exchange key permissions to the minimal read-only set, recommend IP allowlisting on the exchange, and keep paper-trading keys strictly separated from live keys.
6. Bot Trading Refusal: If the user asks for automated bot trading or order execution, refuse immediately and document that only manual execution on the exchange UI is supported.
7. Disclaimers: Include a mandatory high-risk financial disclaimer and note that jurisdictional licensing or tax rules are not evaluated.

Output:
- security_plan.md detailing the preferred CSV path, the explicit tool deny list, key hygiene requirements, session isolation rules, and a handoff link to trading-krypto-workflow.
```

## Workflow

1. Evaluate whether offline CSV exports satisfy the portfolio reporting requirement (preferred default).
2. If read-only API access is requested, scope `ccxt` strictly to `fetch_balance` and `fetch_my_trades`.
3. Compile the explicit tool deny list (`create_order`, `cancel_order`, `withdraw`, wallet signers).
4. Write `security_plan.md` including session isolation from payment/banking MCPs.
5. Link the read-only data pipeline to `trading-krypto-workflow` for analysis.
6. Document environment-only key storage and exchange IP allowlisting requirements.
7. Obtain explicit user acknowledgment of the high-risk read-only policy.

## Definition of done

- [ ] `create_order`, `cancel_order`, and `withdraw` are explicitly listed on the deny list
- [ ] Offline CSV import is documented as the preferred default
- [ ] Optional API keys are restricted to read-only scopes in environment variables
- [ ] High-risk disclaimer and session isolation from payment MCPs are included
- [ ] Handoff to `trading-krypto-workflow` is linked

## Security

- Permanently deny all order execution, margin/leverage mutation, and withdrawal endpoints.
- Never request, accept, or store wallet seed phrases, private keys, or withdrawal-capable API keys.
- Isolate portfolio analysis sessions from payment and banking connectors.

## Pitfalls

- Enabling a third-party exchange MCP server that bundles hidden order placement or withdrawal tools.
- Running payment/invoicing MCPs and exchange tools in the same agent session.
- Generating an exchange API key with trading or withdrawal permissions enabled instead of read-only.
- Leaving margin, futures, or leverage endpoints accessible.
- Connecting unverified "copy-trading" or wallet-draining community skills.

## Basic examples

### Example 1 (Example data (self-written))

- **Task:** Configure a CSV-only portfolio analysis agent setup (example data).
- **Input:** Security policy: offline CSV imports only, zero exchange APIs.
- **Prompt:**
```text
Generate security_plan.md enforcing a CSV-only policy with no exchange MCP servers enabled.
```
- **Expected result:**
```text
security_plan.md disables all exchange MCPs and ccxt API calls, mandates air-gapped CSV ingestion, documents session isolation, and links to trading-krypto-workflow.
```

### Example 2 (Example data (self-written))

- **Task:** Scope a read-only `ccxt` configuration with a hard trade deny list (example data).
- **Input:** User requests `ccxt` to read historical trade fills.
- **Prompt:**
```text
Allow fetch_my_trades and fetch_balance only in security_plan.md; explicitly deny create_order and withdraw.
```
- **Expected result:**
```text
security_plan.md allowlists only fetch_my_trades and fetch_balance, places create_order, cancel_order, and withdraw on the hard deny list, and mandates env-only read-only API keys with IP allowlisting.
```
