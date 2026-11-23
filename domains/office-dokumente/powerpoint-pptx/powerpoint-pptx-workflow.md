---
id: powerpoint-pptx-workflow
title: "PowerPoint / PPTX"
domain: office-dokumente
category: powerpoint-pptx
tags:
  - powerpoint
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
  - name: ClawHub „Powerpoint / PPTX“ (ivangdavila)
    install: "https://clawhubtrends.com/leaderboard.html"
    version_notes: "41.155 Downloads, 122 Registry-Stars (ClawHub Leaderboard 23.11.2026)."
inputs:
  - "Kontext/Briefing für PowerPoint / PPTX"
  - "Dateien, URLs oder IDs laut Aufgabe"
outputs:
  - "Dokumentiertes Ergebnis (Datei, Bericht oder Ticket-Update)"
risk_level: low
example_count: 3
version: "1.0.0"
updated: "2026-11-23"
---

## Zweck

Folien und Decks programmatisch erzeugen, prüfen und als Bilder rendern.

## Wann nutzen

- Anfragen passen zur Kategorie **PowerPoint / PPTX**.
- Nicht nutzen, wenn ein menschlicher Freigabe-Prozess noch nicht geklärt ist (`risk_level: low`).

## Tool-Stack

| Tool | Rolle | Begründung |
|------|-------|------------|
| Anthropic document skills (docx, pptx, x | Skill | Aus Recherche 2026-11-23 |
| Hermes-Skill microsoft-office | Skill + CLI | Aus Recherche 2026-11-23 |
| ClawHub „Powerpoint / PPTX“ (ivangdavila | Skill | Aus Recherche 2026-11-23 |

## System-Prompt / Instruktionen

```text
You are a specialist for PowerPoint / PPTX (office-dokumente/powerpoint-pptx).
Use only tools listed in required_tools. Follow safety gates.
Workflow hint: - Structured deck. Nach Build: validate.py, slide_text.py, soffice/pptx_render, Folienbilder lesen.
```

## Arbeitsablauf

- Structured deck. Nach Build: validate.py, slide_text.py, soffice/pptx_render, Folienbilder lesen.
- Farben als FF0000 ohne #; Layout 10x5,625 Zoll beachten.

## Qualitätskriterien / Definition of Done

- [ ] Eingaben vollständig und dokumentiert
- [ ] Tool-Aufrufe nachvollziehbar (Log/Pfade)
- [ ] Ergebnis entspricht Kategorie-Beschreibung
- [ ] Bei Schreib-/Sendeaktionen: explizite Nutzerfreigabe

## Sicherheit & Freigaben

- validate.py braucht Python >=3.10. Falsche Zahlen in Callouts erkennt der XML-Checker nicht.
- Skills sind Workflows/Anweisungen (progressive disclosure), MCP sind Verbindungen und Tools. Beides kombinieren, nicht verwechseln. Quellen: https://code.claude.com/docs/en/features-overview , https://github.com/ComposioHQ/awesome-claude-skills
- Nur die MCPs/Skills aktivieren, die die Aufgabe braucht. Hermes filtert per include/exclude; OpenClaw hat Tool-Policy und Prompt-Budgets. Quellen: https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp , https://docs.openclaw.ai/skills/
- Keine Tokens oder Passwörter in Chat, Skill-Dateien oder Command-Argumente von Custom-MCPs schreiben. Grok-Bot-Wiki: OAuth-Tokens bleiben auf dem Connector-Backend; Command-Server dürfen keine Credentials in argv enthalten. Quelle: https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp
- Schreiben, Senden, Bezahlen, Deployen und Löschen nur nach expliziter Freigabe; gute Document-Skills verlangen einen Verify-Schritt (Datei erneut lesen, PDF/PNG rendern).

## Grundbeispiele

### Beispiel 1 (Beispieldaten)

- **Aufgabe:** Standard-PowerPoint / PPTX-Aufgabe im Agenten-Thread
- **Input:** Parameter-Satz für `powerpoint-pptx` (Testdaten)
- **Prompt:**
```text
Nutze den empfohlenen Stack für PowerPoint / PPTX. Dokumentiere jeden Tool-Aufruf. Keine Schreibaktion ohne Freigabe.
```
- **Erwartetes Ergebnis:**
```text
Status: OK
Artefakt: output/{slug}-demo.txt
```

### Beispiel 2 (Beispieldaten)

- **Aufgabe:** Fehlerfall / Validierung in PowerPoint / PPTX
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

- **Aufgabe:** Ein kurzes Briefing-Deck mit der offiziellen Anthropic-pptx-Skill erzeugen und validieren.
- **Input:** Tutorial-Briefing, das als PowerPoint ausgegeben werden sollte.
- **Prompt:**
```text
pptxgenjs 4.0.1, skills/pptx/scripts/office/validate.py, python-pptx zum Gegenlesen.
```
- **Erwartetes Ergebnis:**
  Datei briefing.pptx, Validator All validations PASSED. Gegenlesen ergab drei Folien im Format 10 x 5,625 Zoll (LAYOUT_16x9), inklusive Text und Speaker Notes. Hinweis des Autors: Hex-Farben ohne #, Koordinaten jenseits der Kante werden nicht geclippt.
- **Quelle:** https://aifrontierpost.com/articles/anthropic-official-agent-skills-tutorial/
