---
id: budget-workflow
domain: finanzen
title: "Budgetplanung und Abweichungen"
category: budget
tags:
  - budget
  - forecast
  - variance
target_agents:
  - hermes
  - generic
required_tools:
  - name: python
    install: "pip: pandas"
    version_notes: "Tabellen"
  - name: LibreOffice Calc
    install: "optional"
    version_notes: "Review"
inputs:
  - "Budget CSV und Ist"
  - "Perioden"
outputs:
  - "Variance-Report"
  - "Kommentar-Vorschläge"
risk_level: low
version: "1.1.0"
updated: "2026-11-23"
example_count: 2
---

## Zweck

**Budget vs. Ist** analysieren—Abweichungen pro Kostenstelle, keine automatischen Buchungen oder Zahlungen.

## Wann nutzen

- Monats- oder Quartals-Review.
- Projekt-Budget Tracking.
- Vorbereitung Management-Meeting.

**Wann nicht**

- Steuerliche Abschlüsse.
- Live-ERP-Schreibzugriff durch Agent.

## Tool-Stack

| Tool | Rolle | Begründung |
|------|-------|------------|
| pandas | Join/aggregate | Schnell |
| Calc/Excel | Pivot | Review |
| Stripe/Plaid | Optional read | Ist-Daten nur read |

## System-Prompt / Instruktionen

```text
You analyze budget vs actuals—read-only on financial sources unless user explicitly allows writes elsewhere.

Inputs: budget.csv (account, period, amount), actuals.csv same schema, tolerance_pct (default 5), output variance.md and variance.csv.

Normalize periods YYYY-MM; currency single EUR unless user notes FX.

Compute variance absolute and percent per account and rolled up total.

Flag accounts over tolerance RED; explain pattern hypotheses as SUGGESTION not fact.

No automatic budget adjustments in ERP.

If stripe/plaid read: summarize fees into actuals category only with user oauth—no payments.

Charts optional matplotlib user asks.

Approvals: share report with board requires user yes.

No investment advice.

Output tables sorted by largest absolute variance.

Document formulas used.

Exclude one-time items only if user marks column.

Handle missing actuals as MISSING not zero unless policy says zero.

Attach month label in file names variance_2026-11.csv.
Round display 2 decimals keep internal precision.
Separate capex opex if column provided.
```

## Arbeitsablauf

1. CSV schemas validieren.
2. Perioden alignen.
3. Join budget-actual.
4. Variance berechnen.
5. RED flags listen.
6. variance.md narrative.
7. Nutzer review in Calc.

## Qualitätskriterien / Definition of Done

- [ ] Summen konsistent
- [ ] Toleranz angewendet
- [ ] Keine ERP writes
- [ ] MISSING handling dokumentiert
- [ ] Freigabe extern

## Sicherheit & Freigaben

- Finanzdaten vertraulich.
- Read-only Banking.
- Keine stillen Zahlungen.

## Fallstricke

- Fehlende Monate als 0.
- Währungsmix.
- Einmaleffekte verfälschen.
- Falsche Kostenstelle mapping.
- Stripe fees doppelt.

## Grundbeispiele

### Beispiel 1 (Beispieldaten)

- **Aufgabe:** November Variance.
- **Input:** budget_nov.csv actuals_nov.csv tolerance 5%.
- **Prompt:**

```text
variance.csv and variance.md; red flags >5%.
```

- **Erwartetes Ergebnis:**

```text
variance files; red list accounts; totals match manual check.
```

### Beispiel 2 (Beispieldaten)

- **Aufgabe:** Missing actuals.
- **Input:** actuals missing account 4100.
- **Prompt:**

```text
Mark MISSING not zero for 4100.
```

- **Erwartetes Ergebnis:**

```text
Row 4100 status MISSING in csv.
```