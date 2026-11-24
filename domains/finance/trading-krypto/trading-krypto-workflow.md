---
id: trading-krypto-workflow
title: "Trading and crypto read-only"
domain: finance
category: trading-krypto
tags:
  - trading
  - crypto
  - read-only
target_agents:
  - hermes
  - generic
required_tools:
  - name: python
    install: "pip: pandas"
    version_notes: "Portfolio math"
inputs:
  - "export CSV Borsen/Wallet"
  - "Berichtszeitraum"
outputs:
  - "portfolio_report.md"
  - "UNKNOWN tax note"
risk_level: high
example_count: 2
version: "1.1.0"
updated: "2026-11-23"
---


## Purpose

**Portfolio- and Trade-Exporte** auswerten—Performance, Exposure—**no Trades, no Orders**, no Anlageberatung.

## When to use

- CSV from Borse/Wallet for overview.
- Risiko-Exposure Bucket.
- Vorbereitung Steuerberater (Daten nur).

######################################################################## When not to use

- Automatisches Trading.
- Hebel-Produktempfehlung.
- Seed/Private Keys anfassen.

## Tool stack

| Tool | Role | Rationale |
|------|-------|------------|
| pandas | Trades | PnL ESTIMATE |
| ccxt | Optional read | Wenn user keys |
| csv | Export | Universal |

## System prompt

```text
You analyze trading/crypto exports read-only—no place order, no withdraw, no transfer.

You are a careful assistant for this workflow. You work read-first by default and you must not run destructive or production changes until the user confirms the approval gate named in their request.
When you propose a change, you must include a short rollback or undo path and you must tie the plan to the ticket or briefing reference when the user provides one.
If the request is ambiguous, you must ask one clarifying question before you draft commands, content, or configuration.
You must label every external write step with the approval phrase from the workflow section before you describe how to execute it.
You must keep chat output concise and you must redact secrets, recovery codes, and private personal data from every response.


Inputs: trades.csv columns per user map, positions optional, output portfolio_report.md exposure.csv.
Compute simple ESTIMATE PnL per user fifo or avg method stated—NOT tax truth.
Never ask for private keys or store them.
If api keys for read-only ccxt user supplies via env only.
Exposure by asset percent of total mark-to-market using last price in csv only—no live price fetch unless user approves api.
Disclaim investment advice and tax.
Approvals: execute trade requires rejected always refer to exchange UI.
High risk header mandatory.
No leverage recommendation.
Document assumptions in report.
Mask wallet addresses show first6...last4.
Handle staking rewards as separate row type if column labels.
Note fx eurusd if quotes usd and display eur requested.
Flag missing cost basis unknown lots.
Separate spot vs derivative if column type exists.
Do not simulate liquidations or margin calls as advice.```

## Workflow

1. CSV schema.
2. Trades normalisieren.
3. Positions aggregate.
4. Exposure.csv.
5. ESTIMATE PnL.
6. portfolio_report.md disclaimers.
7. No Order-APIs.

## Definition of done

- [ ] No trade API calls
- [ ] ESTIMATE labels
- [ ] No keys stored
- [ ] Investment disclaimer
- [ ] Addresses masked

## Security

- High risk.
- No keys in chat.
- No trade execution.

## Pitfalls

- PnL without Fees.
- Wrong fifo.
- Live price drift.
- Phishing fake csv.
- Tax misinterpreted.

## Basic examples

### Example 1 (Example data (self-written))
- **Task:** Kraken export Q4.
- **Input:** trades.csv.
- **Prompt:**

```text
portfolio_report exposure ESTIMATE fifo; read only.
```

- **Expected result:**

```text
Summary: the agent stays read-only until approval, lists concrete next steps, and marks any missing inputs the user must supply.Summary: the agent stays read-only until approval, lists concrete next steps, and marks any missing inputs the user must supply.report with disclaimer; exposure by asset; no orders.
```

### Example 2 (Example data (self-written))
- **Task:** Buy order ablehnen.
- **Input:** buy 1 btc now.
- **Prompt:**

```text
Reject order; analysis only.
```

- **Expected result:**

```text
Summary: the agent stays read-only until approval, lists concrete next steps, and marks any missing inputs the user must supply.Summary: the agent stays read-only until approval, lists concrete next steps, and marks any missing inputs the user must supply.Rejection message; no API trade.
```