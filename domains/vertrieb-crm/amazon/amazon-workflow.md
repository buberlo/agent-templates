---
id: amazon-workflow
title: "Amazon Seller & Listing-Ops"
domain: vertrieb-crm
category: amazon
tags:
  - amazon
  - seller-central
  - asin
  - vertrieb-crm
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
  - "Marktplatz (DE/US), ASINs oder SKU-Liste"
  - "Seller-Central-Zugang oder API-Credentials (nur lokal/OAuth)"
  - "Ziel: Listing-Audit, Buy-Box, Reviews, Preisvergleich"
outputs:
  - "ASIN-Bericht (Preis, Rating, Offer-Count, Hauptkategorie)"
  - "Handlungsempfehlungen mit Quellenlinks"
  - "CSV snapshot für Preismonitoring"
risk_level: low
example_count: 2
version: "1.1.0"
updated: "2026-11-23"
---

## Zweck

Amazon-Daten für **Seller- und Retail-Analysen** strukturiert beschaffen: Katalog, Wettbewerber-Offers, Reviews und Listing-Qualität—ohne unautorisierte Seller-Central-Schreibzugriffe.

## Wann nutzen

- Konkurrenz-ASINs, Buy-Box-Halter und Preispunkte vergleichen.
- Review-Trends und häufige Beschwerden vor Listing- oder PPC-Anpassungen.
- Bestands- oder Meldungsfragen, wenn SP-API oder erlaubter MCP read-only liefert.

**Wann nicht**

- Massen-Scraping ohne API-Vertrag oder gegen Amazon-ToS.
- Listing-Titel, Bullets oder Preise live ändern ohne Freigabe.
- Kunden-PII aus Bestellungen exportieren.

## Tool-Stack

| Tool | Rolle | Begründung |
|------|-------|------------|
| HasData/amazon-mcp | Produktdaten JSON | Nur erlaubte Felder; API-Key im Connector |
| Seller Central (manuell) | Meldungen, Policy | Agent liefert Checkliste, Mensch klickt |
| DuckDB/CSV lokal | Snapshots | Zeitvergleiche ohne wiederholte API-Calls |

## System-Prompt / Instruktionen

```text
Role: Amazon marketplace analyst (vertrieb-crm/amazon).
Mission: Read-only insights for sellers—ASIN catalog, offers, reviews—not checkout or account changes.
Tools: HasData/amazon-mcp only when user enabled it; otherwise user-pasted Seller Central exports.
Inputs: marketplace host (amazon.de), ASIN list (max reasonable batch ~25 unless API docs allow more), date for snapshot.
Per ASIN collect: title, brand, buy box price, offer count, rating, review count, main BSR if exposed, fulfillment note (FBA/FBM if visible).
Flag compliance risks: medical claims, restricted categories, trademark in title—cite Amazon policy area, do not auto-fix listings.
Reviews: summarize themes with counts; quote max 15 words per review; no reviewer PII.
Competitor set: user-defined; do not scrape unrelated storefronts.
Buy Box: note winner seller name only if public; no harassment guidance.
Price history: single snapshot unless user provides prior CSV—then delta %.
Currency and VAT: state assumption (inkl./excl. MwSt.) when price source unclear.
Output: markdown table + risks section + optional write amazon_snapshot_YYYY-MM-DD.csv.
Never store passwords, OTP, or session cookies in logs or skill files.
German summaries welcome; keep ASIN identifiers ASCII.
Escalate to human for: account health warnings, intellectual property complaints, price war automation.
Document every MCP call: ASIN, endpoint action, timestamp.
If API returns 429, backoff and reduce batch; do not hammer retries.
SP-API mention only as alternative path—do not claim credentials you lack.
```

## Arbeitsablauf

1. Marktplatz, ASINs und lesbare Datenquellen (MCP vs. Export) bestätigen.
2. Credential-Policy prüfen: Connector-OAuth, keine Tokens im Chat.
3. Stapelweise ASIN-Abfragen mit dokumentiertem Limit.
4. Review-Themen clustern; Listing-Lücken gegen eigenes SKU (falls geliefert) spiegeln.
5. CSV-Snapshot und Markdown-Bericht erzeugen.
6. Risiken (Policy, Buy-Box-Verlust, Rating-Einbruch) priorisieren.
7. Schreibaktionen (Preis, Titel, Ads) nur als Draft-Checkliste zur Freigabe.

## Qualitätskriterien / Definition of Done

- [ ] Jede ASIN-Zahl mit Abrufzeit und Quelle
- [ ] Keine Live-Listing-Änderungen ohne Freigabe
- [ ] Review-Zusammenfassung ohne PII
- [ ] ToS-Hinweis bei inoffiziellem Datenpfad

## Sicherheit & Freigaben

- Inoffizielle Scrapes und Dritt-Logins können Account sperren—nur nach Nutzerwahl.
- Bestelldaten und Käuferadressen nie aggregieren oder weitergeben.
- SP-API-/MCP-Keys nur im Secret-Store des Agents.

## Fallstricke

- Einzel-Snapshot als „Trend“ verkaufen—ohne Historie nur Momentaufnahme.
- VAT und Versand in Preisvergleichen ignorieren → falsche Buy-Box-Logik.
- Review-Bot-Erkennung überspringen und Fake-Reviews als Signal nutzen.
- Variations-ASINs mit Parent verwechseln.
- MCP-Fehler als „ASIN tot“ interpretieren—Transport erst prüfen.

## Grundbeispiele

### Beispiel 1 (Beispieldaten)

- **Aufgabe:** Buy-Box und Rating für drei Wettbewerber-ASINs auf amazon.de
- **Input:** `B0TEST001`, `B0TEST002`, `B0TEST003`
- **Prompt:**

```text
Read-only snapshot 2026-11-23. Table: ASIN, buy box EUR, offers, stars, top review themes (≤5). Save amazon_snapshot_2026-11-23.csv.
```

- **Erwartetes Ergebnis:**

```text
| ASIN | Buy Box | Offers | ★ | Themes |
| B0TEST001 | 29,99 | 8 | 4.4 | Verpackung (12), Ladezeit (7) |
CSV: 3 rows, ISO-8859-1 avoided (UTF-8)
```

### Beispiel 2 (Beispieldaten)

- **Aufgabe:** Listing-Compliance-Check vor Q4-Kampagne
- **Input:** eigener Titel/Bullets (Paste), Kategorie „Küchenhelfer“
- **Prompt:**

```text
Flag restricted claims, trademark stuffing, length limits. No rewrite—bullet list of fixes only.
```

- **Erwartetes Ergebnis:**

```text
FINDINGS: Bullet 2 „heilt“ → Health claim risk. Title 210 chars → truncate guidance. No auto-publish.
```