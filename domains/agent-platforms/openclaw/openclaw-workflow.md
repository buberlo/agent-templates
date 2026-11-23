---
id: openclaw-workflow
title: "OpenClaw"
domain: agent-platforms
category: openclaw
tags:
  - openclaw
  - agent-platforms
  - agentplattform
target_agents:
  - openclaw
  - generic-mcp-agents
required_tools:
  - name: OpenClaw
    install: "https://github.com/openclaw/openclaw"
    version_notes: "mcp\"
  - name: ClawHub
    install: "https://github.com/openclaw/clawhub"
    version_notes: "9559 GitHub Stars"
inputs:
  - "Kontext/Briefing für OpenClaw"
  - "Dateien, URLs oder IDs laut Aufgabe"
outputs:
  - "Dokumentiertes Ergebnis (Datei, Bericht oder Ticket-Update)"
risk_level: high
example_count: 3
version: "1.0.0"
updated: "2026-11-23"
---

## Zweck

Gateway, ClawHub, Skill Workshop, MCP, Android-Companion, Skill-Verify.

## Wann nutzen

- Anfragen passen zur Kategorie **OpenClaw**.
- Nicht nutzen, wenn ein menschlicher Freigabe-Prozess noch nicht geklärt ist (`risk_level: high`).

## Tool-Stack

| Tool | Rolle | Begründung |
|------|-------|------------|
| OpenClaw | Agent-Plattform | Aus Recherche 2026-11-23 |
| ClawHub | Registry | Aus Recherche 2026-11-23 |

## System-Prompt / Instruktionen

```text
You are a specialist for OpenClaw (agent-platforms/openclaw).
Use only tools listed in required_tools. Follow safety gates.
Workflow hint: - Skill Workshop fuer neue Prozeduren (Proposal review). MCP add in Settings oder CLI. Android per QR an bestehendes Gat
```

## Arbeitsablauf

- Skill Workshop fuer neue Prozeduren (Proposal review). MCP add in Settings oder CLI. Android per QR an bestehendes Gateway koppeln.
- Prompt-Budget: OpenClaw kuerzt Skill-Beschreibungen, wenn skills.limits.maxSkillsPromptChars greift.

## Qualitätskriterien / Definition of Done

- [ ] Eingaben vollständig und dokumentiert
- [ ] Tool-Aufrufe nachvollziehbar (Log/Pfade)
- [ ] Ergebnis entspricht Kategorie-Beschreibung
- [ ] Bei Schreib-/Sendeaktionen: explizite Nutzerfreigabe

## Sicherheit & Freigaben

- ClawHub-Skills vor der Nutzung prüfen (`openclaw skills verify`). Im Februar 2026 auditierte Koi Security 2.857 Registry-Skills und bewertete 341 als schadhaft (ca. 12 %). Quellen: https://thehackernews.com/2026/02/researchers-find-341-malicious-clawhub.html , https://docs.openclaw.ai/skills/
- Loading-Order kann Workspace-Skills ueber Bundled legen.
- Aeltere .clawdhub-Metadaten werden nicht mehr gelesen (Rename auf .clawhub).
- Leaderboard-Eintraege mit Warnmarkierung und extrem wenigen Registry-Stars trotz hoher Downloads besonders kritisch sehen.
- Skills sind Workflows/Anweisungen (progressive disclosure), MCP sind Verbindungen und Tools. Beides kombinieren, nicht verwechseln. Quellen: https://code.claude.com/docs/en/features-overview , https://github.com/ComposioHQ/awesome-claude-skills
- Nur die MCPs/Skills aktivieren, die die Aufgabe braucht. Hermes filtert per include/exclude; OpenClaw hat Tool-Policy und Prompt-Budgets. Quellen: https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp , https://docs.openclaw.ai/skills/
- Keine Tokens oder Passwörter in Chat, Skill-Dateien oder Command-Argumente von Custom-MCPs schreiben. Grok-Bot-Wiki: OAuth-Tokens bleiben auf

## Grundbeispiele

### Beispiel 1 (Beispieldaten)

- **Aufgabe:** Standard-OpenClaw-Aufgabe im Agenten-Thread
- **Input:** Parameter-Satz für `openclaw` (Testdaten)
- **Prompt:**
```text
Nutze den empfohlenen Stack für OpenClaw. Dokumentiere jeden Tool-Aufruf. Keine Schreibaktion ohne Freigabe.
```
- **Erwartetes Ergebnis:**
```text
Status: OK
Artefakt: output/{slug}-demo.txt
```

### Beispiel 2 (Beispieldaten)

- **Aufgabe:** Fehlerfall / Validierung in OpenClaw
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

- **Aufgabe:** Dokumentierter Sicherheitsvorfall: oeffentlich gelistete Agent-Skills wurden unabhaengig geprueft.
- **Input:** 2.857 auf ClawHub gelistete Skills (Stand der Koi-Security-Pruefung, Februar 2026).
- **Prompt:**
```text
Unabhaengiges Audit (Koi Security); spaeter u. a. openclaw skills verify und Community-Pruef-Plugins.
```
- **Erwartetes Ergebnis:**
  341 Skills als schadhaft bewertet (ca. 12 %). Berichte ordnen den Grossteil einer koordinierten Kampagne zu. Konsequenz: Skills verifizieren, nicht blind installieren.
- **Quelle:** https://thehackernews.com/2026/02/researchers-find-341-malicious-clawhub.html
