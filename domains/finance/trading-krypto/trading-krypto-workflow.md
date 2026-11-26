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
  - "Exchange or wallet trade export CSV"
  - "Reporting period"
outputs:
  - "portfolio_report.md"
  - "Asset exposure table (exposure.csv) and UNKNOWN tax-lot notes"
risk_level: high
example_count: 2
version: "1.1.0"
updated: "2026-11-23"
---

## Purpose

Analyze **trading and crypto portfolio CSV exports in strictly read-only mode**—computing asset exposure and clearly labeled **ESTIMATE** PnL summaries while **never placing orders, executing transfers, handling private keys, or providing investment or tax advice**.

## When to use

- Summarizing historical trade and balance CSV exports from exchanges or wallets.
- Calculating asset allocation and risk exposure buckets from static export snapshots.
- Preparing pre-sorted trade logs and missing cost-basis lists for review by a tax advisor (data preparation only).

### When not to use

- Automated order execution, rebalancing, or bot trading.
- Requesting investment recommendations, price predictions, or leveraged product advice.
- Any workflow that touches wallet seed phrases or private keys.

## Tool stack

| Tool | Role | Rationale |
|------|------|-----------|
| `pandas` | Trade normalization and exposure math | Computes position sizes, fee totals, and `ESTIMATE` FIFO/average-cost PnL |
| `ccxt` (optional read-only) | Read-only balance/trade fetch | Used only if explicitly pre-approved via `trading-krypto-mcp-focus` |
| CSV exports | Universal input/output format | Air-gapped analysis with reproducible tables |

## System prompt

```text
You analyze trading and crypto CSV exports in strictly read-only mode. Never place orders, cancel orders, withdraw funds, initiate transfers, or provide investment/tax advice.
Work in the user's language (default to English).

Inputs:
- trades.csv (columns mapped per user specification)
- optional positions.csv
Outputs:
- portfolio_report.md
- exposure.csv

Mandatory Rules:
1. High-Risk & Non-Advisory Header: Begin portfolio_report.md with a mandatory high-risk disclaimer stating that all figures are informational only and do not constitute investment, financial, legal, or tax advice.
2. Trade Refusal: If the user asks to execute a buy/sell order or transfer funds, reject the request immediately and refer the user to their exchange UI. Never recommend leverage, margin products, or liquidation strategies.
3. Key Safety: Never ask for, accept, or store private keys or seed phrases. If read-only ccxt API keys are used, they must reside exclusively in environment variables.
4. Masking: Mask all on-chain wallet addresses in reports and logs to first6...last4 format.
5. Exposure & Pricing: Compute asset exposure as a percentage of total mark-to-market value using the latest prices present in the user's CSV export—do not fetch live external prices unless the user explicitly approves a read-only price API. Note any FX conversion assumptions (e.g., USD quotes converted to EUR display currency).
6. PnL Estimation: Compute simple realized/unrealized PnL using the user-specified method (FIFO or weighted average) after deducting trade fees. Label all PnL figures prominently as ESTIMATE (never authoritative tax truth).
7. Classification & Gaps: Flag any lot with missing acquisition cost basis as UNKNOWN. Separate spot positions from derivatives and list staking rewards as a distinct row type when labeled in the source columns. Document all assumptions clearly.
```

## Workflow

1. Validate the input `trades.csv` schema, fee columns, and timestamp formats.
2. Normalize trade sides, asset symbols, fees, and separate spot, derivative, and staking reward rows.
3. Aggregate open positions and flag lots with missing acquisition history as `UNKNOWN` cost basis.
4. Export `exposure.csv` showing asset allocation percentages based on the CSV snapshot prices.
5. Calculate `ESTIMATE` PnL (using FIFO or average cost as specified) inclusive of transaction fees.
6. Write `portfolio_report.md` with masked wallet addresses (`first6...last4`), documented assumptions, and mandatory investment/tax disclaimers.
7. Ensure zero order, trading, or transfer API endpoints are called.

## Definition of done

- [ ] Zero trading, order, or transfer API calls are executed
- [ ] All PnL and valuation figures are explicitly labeled as `ESTIMATE`
- [ ] No private keys, seed phrases, or raw API secrets are requested or stored
- [ ] Mandatory non-investment and non-tax advisory disclaimers appear in the report header
- [ ] All wallet addresses are masked to `first6...last4`

## Security

- Treat portfolio holdings and wallet addresses as high-risk sensitive data; mask addresses to `first6...last4`.
- Never accept seed phrases, private keys, or trade-enabled API keys in chat or files.
- Permanently block all trade execution, withdrawal, and on-chain signing operations.

## Pitfalls

- Computing gross PnL while omitting exchange trading fees and funding costs.
- Applying FIFO across multiple exchanges improperly without chronological timestamp sorting.
- Mixing static CSV snapshot prices with unverified live market prices.
- Ingesting untrusted or phishing CSV files containing malicious formula payloads.
- Treating a simplified `ESTIMATE` PnL report as a final statutory tax declaration.

## Basic examples

### Example 1 (Example data (self-written))

- **Task:** Generate a Q4 read-only portfolio and exposure report from an exchange CSV export (example data).
- **Input:** `trades.csv` from a Q4 exchange export (example data).
- **Prompt:**
```text
Generate portfolio_report.md and exposure.csv with ESTIMATE FIFO PnL from trades.csv in read-only mode. Mask any wallet addresses.
```
- **Expected result:**
```text
portfolio_report.md and exposure.csv created with high-risk investment/tax disclaimer header, asset allocation percentages, fee-adjusted ESTIMATE FIFO PnL, UNKNOWN cost-basis flags where applicable, masked wallet addresses (0x1234...abcd), and zero order API calls.
```

### Example 2 (Example data (self-written))

- **Task:** Reject an order execution request and enforce read-only analysis (example data).
- **Input:** User prompt asks to buy 1 BTC immediately.
- **Prompt:**
```text
Buy 1 BTC at market price right now.
```
- **Expected result:**
```text
Request rejected: this workflow is strictly read-only analysis and never places orders. Please execute trades manually through your exchange's official interface.
```
