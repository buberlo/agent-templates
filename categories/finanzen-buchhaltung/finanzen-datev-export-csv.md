---
id: finanzen-datev-export-csv
title: "DATEV-Export aus Buchungsliste"
category: finanzen-buchhaltung
tags:
  - datev
  - csv
  - export
target_agents:
  - hermes
  - generic
required_tools:
  - name: python
    install: "pip: pandas"
    version_notes: "DATEV Format 7.0"
  - name: libreoffice
    install: "optional Calc"
    version_notes: "Manuelle Prüfung"
inputs:
  - "Interne Buchungsliste"
  - "Kontenrahmen SKR03/04"
  - "Steuerberater-Mandanten-Nr."
outputs:
  - "DATEV CSV"
  - "Validierungslog"
risk_level: medium
version: "1.0.0"
updated: "2026-11-23"
---

## Zweck

Interne Buchungsdaten in DATEV-kompatibles CSV für den Steuerberater transformieren.

## Wann nutzen

- Monatsbatch vor Übergabe.
- Nicht ohne Abstimmung des exakten DATEV-Formats mit Kanzlei.

## Tool-Stack

| Tool | Rolle | Begründung |
|------|-------|------------|
| pandas | Transformation | Regelbasiert |
| DATEV Spec | Feldmapping | Offizielle Spalten |
| Validator Script | Pflichtfelder | Fehler vor Export |

## System-Prompt / Instruktionen

```text
Map internal ledger to DATEV CSV per agreed SKR and format version.
Validate: Belegdatum, Umsatz, Soll/Haben-Konto, BU-Schlüssel.
Output encoding ISO-8859-1 if required by Kanzlei.
No export until validation log is clean or signed off.
```

## Arbeitsablauf

1. Mapping-Tabelle laden.
2. Transform + Summenprüfung.
3. Validator laufen lassen.
4. Stichprobe in Calc.
5. Übergabe mit Log.

## Qualitätskriterien / Definition of Done

- [ ] Validator 0 Fehler
- [ ] Summe Soll = Summe Haben
- [ ] Format von Kanzlei bestätigt

## Sicherheit & Freigaben

- Finanzdaten DSGVO/GOdB.
- Export nur über sicheren Kanal.

## Beispiele

**Eingabe:** `buchungen_nov.xlsx`, SKR03
**Erwartetes Ergebnis:** `EXTF_nov.csv`, `validation.log`
