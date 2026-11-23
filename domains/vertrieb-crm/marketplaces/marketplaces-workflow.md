---
id: marketplaces-workflow
title: "Marktplatz-übergreifend (eBay, Otto, Kaufland …)"
domain: vertrieb-crm
category: marketplaces
tags:
  - marketplace
  - multichannel
target_agents:
  - hermes
  - grokbot
  - generic-mcp-agents
  - generic
required_tools:
  - name: HasData/amazon-mcp
    install: "https://github.com/HasData/amazon-mcp"
    version_notes: "Stars hier nicht per API gezogen."
inputs:
  - "Marktplätze und Seller-Exports je Plattform"
  - "SKU/ EAN Mapping-Tabelle"
  - "Frage: Preisparität, Buybox, Listing-Status"
outputs:
  - "Paritätsmatrix (Preis, Verfügbarkeit, Gebühren grob)"
  - "Listings mit Status-Fehlern"
  - "Empfehlung welcher Kanal priorisiert wird (nur Analyse)"
risk_level: low
example_count: 2
version: "1.1.0"
updated: "2026-11-23"
---

## Zweck

Mehrere **Dritt-Marktplätze** neben Amazon vergleichen: Listing-Status, Preisparität, Gebührennäherung—zentrale SKU-Wahrheit vorausgesetzt.

## Wann nutzen

- Expansion auf eBay/Otto/Kaufland mit Bestandsspiegelung planen.
- Preisabweichung >X % zwischen Kanälen finden.
- Feed-Fehler aus Marktplatz-Reports clustern.

**Wann nicht**

- Unbekannte Marktplatz-API ohne Dokumentation live ansteuern.
- Gebotsmanipulation auf Auktionsplattformen.

## Tool-Stack

| Tool | Rolle | Begründung |
|------|-------|------------|
| Plattform-Exports | Ground truth | Vendor-CSV |
| HasData/amazon-mcp | Amazon-Referenz | Optional Vergleich |
| SKU-Map | Join-Key | Nutzerpflege |

## System-Prompt / Instruktionen

```text
Role: marketplace parity analyst (vertrieb-crm/marketplaces).
Mission: Compare listings across user-supplied marketplace exports—no unauthorized scraping of eBay/Otto sites.
Inputs: marketplace list, SKU map file, tolerance % for price delta default 3.
Per marketplace columns normalize: sku, ean, price, stock, status, fees_optional.
Join on sku then ean fallback—log unjoined rows.
Parity table: highlight where price diff > tolerance or stock 0 on one channel only.
Fees: if user provides fee sheet, compute margin estimate disclaimer rough.
Amazon row optional via MCP read-only for same EAN—label source.
Status errors: inactive, suppressed, missing image—aggregate count by marketplace.
Recommendations: prioritize channel by margin and stock—advisory only.
German marketplaces: note VAT included price assumption.
Output: parity_YYYY-MM-DD.csv, summary_de.md.
No listing create/update API calls.
Legal: respect each marketplace partner terms on data use.
Feed schedules: note if export stale >24h.
Promotional prices: compare base vs promo columns if present.
Variant explosion: collapse to parent SKU when user map says so.
```

## Arbeitsablauf

1. Marktplätze und Export-Format dokumentieren.
2. SKU/EAN-Map validieren.
3. Felder normalisieren und joinen.
4. Preis- und Bestands-Parität berechnen.
5. Status-Fehler aggregieren.
6. Kurz-Empfehlung je SKU-Cluster.
7. Report ohne Feed-Schreiben ausliefern.

## Qualitätskriterien / Definition of Done

- [ ] Unjoined SKUs gezählt
- [ ] Toleranz % dokumentiert
- [ ] Keine Listing-API-Writes
- [ ] Export-Alter je Quelle notiert

## Sicherheit & Freigaben

- Partner-API-Keys geschützt halten.
- Wettbewerbsdaten nicht aus Login-Sessions scrapen.

## Fallstricke

- Promo-Preis mit Basispreis vergleichen.
- EAN-Mehrdeutigkeit bei Bundles.
- Zeitzone bei Tages-Exporten.
- Amazon MCP Momentaufnahme vs. gestern Feed.
- Gebühren ohne Versandkostenmodell.

## Grundbeispiele

### Beispiel 1 (Beispieldaten)

- **Aufgabe:** Parität Amazon vs Kaufland
- **Input:** zwei CSVs, MAP, 3% tolerance
- **Prompt:**

```text
parity csv + top 10 worst deltas.
```

- **Erwartetes Ergebnis:**

```text
11 SKUs over 3% | example SKU-991 +7.2% Kaufland higher
```

### Beispiel 2 (Beispieldaten)

- **Aufgabe:** Unterdrückte Listings
- **Input:** eBay export status column
- **Prompt:**

```text
Count by status, list sku for suppressed.
```

- **Erwartetes Ergebnis:**

```text
suppressed: 8 | missing image: 3 | sku list attached
```