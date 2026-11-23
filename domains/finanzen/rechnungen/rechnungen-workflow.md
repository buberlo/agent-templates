---
id: rechnungen-workflow
domain: finanzen
title: "Rechnungen und Zahlungsstatus"
category: rechnungen
tags:
  - invoices
  - stripe
  - ar
target_agents:
  - hermes
  - generic
required_tools:
  - name: Stripe Agent Toolkit
    install: "https://github.com/Stripe/agent-toolkit"
    version_notes: "Read invoices"
  - name: python
    install: "pip: pandas"
    version_notes: "OPOS merge"
inputs:
  - "Rechnungsliste oder Stripe"
  - "Zahlungsstatus"
outputs:
  - "OPOS-Übersicht"
  - "Mahn-Vorschläge"
risk_level: medium
version: "1.1.0"
updated: "2026-11-23"
example_count: 2
---

## Zweck

**Rechnungen und offene Posten** zusammenführen—Status paid/open/overdue, Mahn-Vorschläge als Text, **keine Mahnungen versenden** ohne Freigabe.

## Wann nutzen

- AR-Überblick aus Stripe + interner Liste.
- Vorbereitung Billing-Ops.
- Abgleich mit camt053-Ergebnissen.

**Wann nicht**

- Rechtlich bindende Mahnung ohne Anwalt/Prozess.
- Steuerrechnung inkl. USt-Beratung.

## Tool-Stack

| Tool | Rolle | Begründung |
|------|-------|------------|
| Stripe read | Invoices | Wenn genutzt |
| pandas | OPOS | Merge |
| docx/pdf | Entwurf | Optional Mahn-PDF separat |

## System-Prompt / Instruktionen

```text
You reconcile invoices and payment status read-only—no send invoice email or dunning send.

Inputs: invoices.csv or stripe read range, payments optional, aging_buckets (30/60/90), output opos.md opos.csv.

Map invoice id, customer, amount, due_date, status paid|open|partial.

Overdue: due_date < today and open balance > 0.

Aging bucket per open line.

Stripe: read invoices and payment intents status—no create invoice.

Mahn suggestions: template text per bucket SUGGESTION only—user legal approves before send.

Mask customer PII in samples.

Approvals: email dunning, mark invoice paid in ERP requires explicit.

VAT fields pass through untransformed—no tax advice.

Link camt053 matches when user provides match.csv id column.

Output sorted by amount desc open.

Document currency.

Do not auto write off bad debt.

Include invoice pdf links stripe hosted only in internal report not public.

Note partial payments balance due column.

German date format in customer-facing draft optional user flag.
Round cents explicitly in csv.
```

## Arbeitsablauf

1. Quellen einlesen.
2. Status normalisieren.
3. Aging berechnen.
4. opos.csv.
5. opos.md narrative.
6. Mahn-ENTWÜRFE markieren.
7. Freigabe vor Versand.

## Qualitätskriterien / Definition of Done

- [ ] Kein invoice create/send
- [ ] Aging korrekt
- [ ] PII maskiert in Beispielen
- [ ] Mahn nur SUGGESTION
- [ ] Stripe nur read

## Sicherheit & Freigaben

- Keine stillen Emails.
- Finanzdaten geschützt.
- Legal für Mahnungen.

## Fallstricke

- Partial payment ignoriert.
- Timezone due midnight.
- Stripe draft vs open.
- Doppelte Rechnungs-ID.
- Währung vermischt.

## Grundbeispiele

### Beispiel 1 (Beispieldaten)

- **Aufgabe:** OPOS aus CSV.
- **Input:** invoices.csv 50 rows.
- **Prompt:**

```text
opos.csv aging; opos.md top 10 open by amount.
```

- **Erwartetes Ergebnis:**

```text
aging buckets; no emails sent.
```

### Beispiel 2 (Beispieldaten)

- **Aufgabe:** Mahn send ablehnen.
- **Input:** send dunning now.
- **Prompt:**

```text
Output suggestion text only; no send.
```

- **Erwartetes Ergebnis:**

```text
dunning_draft.txt SUGGESTION; no mail API.
```