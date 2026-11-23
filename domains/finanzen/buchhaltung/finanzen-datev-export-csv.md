---
id: finanzen-datev-export-csv
domain: finanzen
title: "DATEV-Export aus Buchungsliste"
category: buchhaltung
tags:
  - datev
  - csv
  - skr03
target_agents:
  - hermes
  - cursor
  - generic
required_tools:
  - name: python
    install: "pip: pandas"
    version_notes: "Transformation"
  - name: LibreOffice Calc
    install: "optional"
    version_notes: "Stichprobe vor Übergabe"
inputs:
  - "Interne Buchungsliste (CSV/XLSX)"
  - "SKR03 oder SKR04"
  - "Kanzlei-Formatversion (EXTF)"
outputs:
  - "DATEV-kompatible CSV"
  - "validation.log"
risk_level: medium
version: "1.1.0"
updated: "2026-11-23"
example_count: 2
---

## Zweck

**Interne Buchungsdaten** in ein von der Steuerkanzlei bestätigtes **DATEV-CSV (EXTF)** überführen—Pflichtfelder validieren, Summen prüfen, **kein Upload** ohne Freigabe.

## Wann nutzen

- Monatsbatch vor Steuerberater-Übergabe.
- Mapping SKR03/04 liegt schriftlich vor.
- Agent automatisiert Transform + Validator, Mensch gibt Export frei.

**Wann nicht**

- Ohne schriftliche Feldspezifikation der Kanzlei (Version 7.0 vs. andere).
- Steuerliche Bewertung oder Kontenwahl ohne Fachfreigabe.
- Direkter DATEV-Unternehmen-online-Import durch Bot.

## Tool-Stack

| Tool | Rolle | Begründung |
|------|-------|------------|
| pandas | ETL | Spaltenmapping |
| Validator (Script) | Pflichtfelder | Vor Übergabe |
| Kanzlei-Mapping-Tabelle | Spec | Source of truth |
| Calc | Stichprobe | Menschliche QA |

## System-Prompt / Instruktionen

```text
You transform internal ledger exports to DATEV CSV per Kanzlei mapping—not tax advisory.

Inputs: ledger.csv/xlsx, mapping.yaml (internal_col → DATEV field), SKR (03|04), FORMAT_VERSION from Steuerberater, mandant_number if required, encoding (ISO-8859-1 vs UTF-8 per Kanzlei).

Rules:
- Belegdatum, Umsatz, Soll/Haben-Konto, BU-Schlüssel, Belegfeld 1/2 as mapping defines.
- Soll/Haben sums must balance per batch; stop on imbalance > 0.01 EUR.
- No invented tax keys; UNKNOWN accounts → validation error list.

Transform steps in pandas; emit EXTF header row exactly as spec PDF states (user provides sample).

Validation log must list row-level errors with line numbers; zero blocking errors before export OR user sign-off on waivers.

Encoding: when Kanzlei demands ISO-8859-1, convert umlauts explicitly; log replacement chars.

Output files: EXTF_nov.csv, validation.log, transform_summary.md (row count, sum debit/credit).

Never email CSV to third parties; user chooses secure channel.

No DATEV API calls unless user provides separate integration scope.

Document mapping version hash in summary.

Round currency to 2 decimals banker's rounding unless mapping says else.

Keep Steuerschlüssel empty when user marks "Steuerberater fills".
```

## Arbeitsablauf

1. Kanzlei-Mapping und FORMAT_VERSION laden.
2. Interne Liste einlesen; Datentypen und Datum normalisieren.
3. Spaltentransform gemäß mapping.yaml.
4. Summen Soll/Haben je Batch prüfen.
5. Validator-Script → validation.log.
6. Bei 0 Fehler: CSV schreiben; sonst Fehlerliste an Buchhaltung.
7. Stichprobe 5 Zeilen in Calc; Freigabe Kanzlei-Kontakt.

## Qualitätskriterien / Definition of Done

- [ ] Validator: 0 blockierende Fehler oder dokumentierte Freigabe
- [ ] Summe Soll = Summe Haben (±0,01 €)
- [ ] Encoding laut Kanzlei-Vorgabe
- [ ] Kein Versand ohne Nutzerkanal-Wahl
- [ ] Mapping-Version im Summary

## Sicherheit & Freigaben

- Finanzdaten GOdB/DSGVO; Export nur sicherer Kanal.
- Keine Mandantennummern in öffentlichen Logs.
- Steuerberater bestätigt Format vor Produktiv-Batch.

## Fallstricke

- Falsche EXTF-Kopfzeile → kompletter Import abgelehnt.
- SKR03-Konto in SKR04-Export.
- Excel-Datum als Serienzahl falsch konvertiert.
- ISO-8859-1 ohne Umlaut-Test in Calc.
- BU-Schlüssel veraltet nach Gesetzesänderung.

## Grundbeispiele

### Beispiel 1 (Beispieldaten)

- **Aufgabe:** November-Buchungen EXTF SKR03.
- **Input:** `buchungen_nov.xlsx`, `mapping_skr03.yaml`, Encoding ISO-8859-1.
- **Prompt:**

```text
Transform to EXTF_nov.csv, validate all mandatory fields, balance check, write validation.log.
```

- **Erwartetes Ergebnis:**

```text
EXTF_nov.csv, validation.log (0 errors), transform_summary.md with 124 rows, debit=credit=48120.55.
```

### Beispiel 2 (Beispieldaten)

- **Aufgabe:** Ungültiges Konto abbrechen.
- **Input:** Zeile mit Konto `99999` nicht im Kontenplan.
- **Prompt:**

```text
Run validator only; expect blocking error on row 47 invalid account.
```

- **Erwartetes Ergebnis:**

```text
No EXTF export written; validation.log line: row 47 ACCOUNT_INVALID 99999.
```