---
id: trading-krypto-workflow
domain: finanzen
title: "Trading- und Krypto-Read-Only"
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
  - "Export CSV Börsen/Wallet"
  - "Berichtszeitraum"
outputs:
  - "portfolio_report.md"
  - "UNKNOWN tax note"
risk_level: high
version: "1.1.0"
updated: "2026-11-23"
example_count: 2
---

## Zweck

**Portfolio- und Trade-Exporte** auswerten—Performance, Exposure—**keine Trades, keine Orders**, keine Anlageberatung.

## Wann nutzen

- CSV von Börse/Wallet für Übersicht.
- Risiko-Exposure Bucket.
- Vorbereitung Steuerberater (Daten nur).

**Wann nicht**

- Automatisches Trading.
- Hebel-Produktempfehlung.
- Seed/Private Keys anfassen.

## Tool-Stack

| Tool | Rolle | Begründung |
|------|-------|------------|
| pandas | Trades | PnL ESTIMATE |
| ccxt | Optional read | Wenn user keys |
| csv | Export | Universal |

## System-Prompt / Instruktionen

```text
You analyze trading/crypto exports read-only—no place order, no withdraw, no transfer.

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
Do not simulate liquidations or margin calls as advice.
```

## Arbeitsablauf

1. CSV schema.
2. Trades normalisieren.
3. Positions aggregate.
4. Exposure.csv.
5. ESTIMATE PnL.
6. portfolio_report.md disclaimers.
7. Keine Order-APIs.

## Qualitätskriterien / Definition of Done

- [ ] No trade API calls
- [ ] ESTIMATE labels
- [ ] No keys stored
- [ ] Investment disclaimer
- [ ] Addresses masked

## Sicherheit & Freigaben

- High risk.
- No keys in chat.
- No trade execution.

## Fallstricke

- PnL ohne Fees.
- Wrong fifo.
- Live price drift.
- Phishing fake csv.
- Tax misinterpreted.

## Grundbeispiele

### Beispiel 1 (Beispieldaten)

- **Aufgabe:** Kraken export Q4.
- **Input:** trades.csv.
- **Prompt:**

```text
portfolio_report exposure ESTIMATE fifo; read only.
```

- **Erwartetes Ergebnis:**

```text
report with disclaimer; exposure by asset; no orders.
```

### Beispiel 2 (Beispieldaten)

- **Aufgabe:** Buy order ablehnen.
- **Input:** buy 1 btc now.
- **Prompt:**

```text
Reject order; analysis only.
```

- **Erwartetes Ergebnis:**

```text
Rejection message; no API trade.
```