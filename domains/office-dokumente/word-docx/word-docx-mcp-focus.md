---
id: word-docx-mcp-focus
title: "Word / DOCX: MCP/Skill-Fokus"
domain: office-dokumente
category: word-docx
tags:
  - word
  - office-dokumente
  - skill
target_agents:
  - hermes
  - grokbot
  - generic-mcp-agents
  - generic
required_tools:
  - name: Anthropic document skills (docx, pptx, xlsx, pdf)
    install: "https://github.com/anthropics/skills"
    version_notes: "199219 GitHub Stars"
  - name: Hermes-Skill microsoft-office
    install: "https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/productivity/productivity-microsoft-office"
    version_notes: "Teil des offiziellen Bundled-Katalogs."
inputs:
  - "Kontext/Briefing für Word / DOCX"
  - "Dateien, URLs oder IDs laut Aufgabe"
outputs:
  - "Dokumentiertes Ergebnis (Datei, Bericht oder Ticket-Update)"
risk_level: low
example_count: 3
version: "1.0.0"
updated: "2026-11-23"
---

## Zweck

Berichte, Briefe und Vorlagen als .docx erzeugen und prüfen.

## Wann nutzen

- Anfragen passen zur Kategorie **Word / DOCX**.
- Nicht nutzen, wenn ein menschlicher Freigabe-Prozess noch nicht geklärt ist (`risk_level: low`).

## Tool-Stack

| Tool | Rolle | Begründung |
|------|-------|------------|
| Anthropic document skills (docx, pptx, x | Skill | Aus Recherche 2026-11-23 |
| Hermes-Skill microsoft-office | Skill + CLI | Aus Recherche 2026-11-23 |
| MarkItDown | CLI / Bibliothek | Aus Recherche 2026-11-23 |
| ClawHub „Word / DOCX“ (ivangdavila) | Skill | Aus Recherche 2026-11-23 |

## System-Prompt / Instruktionen

```text
You are a specialist for Word / DOCX (office-dokumente/word-docx).
Use only tools listed in required_tools. Follow safety gates.
Workflow hint: - Skill explizit laden. Nach dem Schreiben: validate.py / docx_validate.py, soffice nach PDF, pdftoppm, Bilder ansehen.
```

## Arbeitsablauf

- Skill explizit laden. Nach dem Schreiben: validate.py / docx_validate.py, soffice nach PDF, pdftoppm, Bilder ansehen.
- Tabellenbreiten (DXA) nicht ueber den Satzspiegel summieren.

## Qualitätskriterien / Definition of Done

- [ ] Eingaben vollständig und dokumentiert
- [ ] Tool-Aufrufe nachvollziehbar (Log/Pfade)
- [ ] Ergebnis entspricht Kategorie-Beschreibung
- [ ] Bei Schreib-/Sendeaktionen: explizite Nutzerfreigabe

## Sicherheit & Freigaben

- Default-Seitengröße A4 in der docx-Skill. Eine gruene Validation ist kein visueller Beweis.
- Skills sind Workflows/Anweisungen (progressive disclosure), MCP sind Verbindungen und Tools. Beides kombinieren, nicht verwechseln. Quellen: https://code.claude.com/docs/en/features-overview , https://github.com/ComposioHQ/awesome-claude-skills
- Nur die MCPs/Skills aktivieren, die die Aufgabe braucht. Hermes filtert per include/exclude; OpenClaw hat Tool-Policy und Prompt-Budgets. Quellen: https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp , https://docs.openclaw.ai/skills/
- Keine Tokens oder Passwörter in Chat, Skill-Dateien oder Command-Argumente von Custom-MCPs schreiben. Grok-Bot-Wiki: OAuth-Tokens bleiben auf dem Connector-Backend; Command-Server dürfen keine Credentials in argv enthalten. Quelle: https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp
- Schreiben, Senden, Bezahlen, Deployen und Löschen nur nach expliziter Freigabe; gute Document-Skills verlangen einen Verify-Schritt (Datei erneut lesen, PDF/PNG rendern).

## Grundbeispiele

### Beispiel 1 (Beispieldaten)

- **Aufgabe:** Standard-Word / DOCX-Aufgabe im Agenten-Thread
- **Input:** Parameter-Satz für `word-docx` (Testdaten)
- **Prompt:**
```text
Nutze den empfohlenen Stack für Word / DOCX. Dokumentiere jeden Tool-Aufruf. Keine Schreibaktion ohne Freigabe.
```
- **Erwartetes Ergebnis:**
```text
Status: OK
Artefakt: output/{slug}-demo.txt
```

### Beispiel 2 (Beispieldaten)

- **Aufgabe:** Fehlerfall / Validierung in Word / DOCX
- **Input:** Unvollständige oder ungültige Eingabe
- **Prompt:**
```text
Erkenne fehlende Pflichtfelder, brich ab und liste konkrete Nachfragen.
```
- **Erwartetes Ergebnis:**
| Feld | Status |
|------|--------|
| input | fehlt |
| Aktion | keine Ausführung |

### Beispiel 3 (Praxisbeispiel)

- **Aufgabe:** Mit Claude Code und der offiziellen Anthropic-docx-Skill ein Briefing-Dokument erzeugen und validieren.
- **Input:** Inhaltliches Briefing (Titel, zwei H1, Listen, Preistabelle) im Tutorial des Autors.
- **Prompt:**
```text
Claude Code Plugin document-skills@anthropic-agent-skills, npm-Paket docx 9.15.3, skills/docx/scripts/office/validate.py, LibreOffice-Wrapper soffice.py, pdftoppm.
```
- **Erwartetes Ergebnis:**
  Ausgabe briefing.docx mit 10.354 Bytes. Validator: 25 Absätze, All validations PASSED. Beim ersten PDF-Render lief die Tabelle über den rechten Rand (Spaltenbreiten summierten auf 11.520 DXA); nach Korrektur auf 9.360 DXA Gesamtbreite war die Context-Spalte sichtbar.
- **Quelle:** https://aifrontierpost.com/articles/anthropic-official-agent-skills-tutorial/
