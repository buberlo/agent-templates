---
id: dokumente-libreoffice-mail-merge
domain: office-dokumente
title: "Serienbrief mit LibreOffice und CSV"
category: word-docx
tags:
  - libreoffice
  - mail-merge
  - odt
target_agents:
  - hermes
  - generic
required_tools:
  - name: libreoffice
    install: "apt: libreoffice"
    version_notes: "24.x headless"
  - name: python
    install: "system python3"
    version_notes: "uno bridge für Automation"
inputs:
  - "ODT-Vorlage"
  - "CSV Empfänger"
  - "Platzhalter-Mapping"
outputs:
  - "PDF pro Empfänger"
  - "Versandliste"
risk_level: medium
version: "1.0.0"
updated: "2026-11-23"
example_count: 2
---

## Zweck

Personalisierte Anschreiben oder Zertifikate aus einer Vorlage massenhaft erzeugen.

## Wann nutzen

- Einladungen, Mahnungen, Teilnahmebescheinigungen.
- Nicht für E-Mail-Versand ohne separaten Freigabe-Workflow.

## Tool-Stack

| Tool | Rolle | Begründung |
|------|-------|------------|
| LibreOffice Writer | Mail merge | Offen, headless |
| CSV | Datenquelle | Einfach aus CRM |
| soffice | CLI Export PDF | Automatisierbar |

## System-Prompt / Instruktionen

```text
Run LibreOffice mail merge headless.
Validate CSV columns match template fields before merge.
Export one PDF per row; filename pattern {id}_{lastname}.pdf
Log failures per row without stopping entire batch.
```

## Arbeitsablauf

1. Vorlage-Felder gegen CSV prüfen.
2. Testlauf mit 3 Zeilen.
3. Vollbatch headless.
4. PDFs stichprobenartig öffnen.
5. Versandliste ohne PII an unbefugte.

## Qualitätskriterien / Definition of Done

- [ ] 100 % Zeilen mit PDF
- [ ] Platzhalter korrekt ersetzt
- [ ] Dateinamen eindeutig

## Sicherheit & Freigaben

- CSV enthält PII; Zugriff beschränken.
- Inhalt vor Massenversand von Fachabteilung freigegeben.

## Grundbeispiele

### Beispiel 1 (Beispieldaten)

_Siehe vorheriger Abschnitt; bei Migration ergänzt._

### Beispiel 2 (Beispieldaten)

- **Aufgabe:** Validierung
- **Input:** n/a
- **Prompt:** `validate output`
- **Erwartetes Ergebnis:** OK

## Beispiele (Legacy)

**Eingabe:** `brief.odt`, `kunden.csv` (200 Zeilen)
**Erwartetes Ergebnis:** `out/pdf/*.pdf`, `merge.log`
