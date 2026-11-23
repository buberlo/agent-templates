---
id: hermes-workflow
title: "Hermes Agent (Nous Research)"
domain: agent-platforms
category: hermes
tags:
  - hermes
  - agent-platforms
  - agentplattform
target_agents:
  - hermes
  - generic-mcp-agents
required_tools:
  - name: Hermes Agent
    install: "https://github.com/NousResearch/hermes-agent"
    version_notes: "265550 GitHub Stars; Quickstart Desktop oder CLI"
  - name: Nous-approved MCP-Katalog
    install: "https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp"
    version_notes: "66 optional-mcps; standardmäßig deaktiviert; hermes mcp install"
inputs:
  - "Aufgabenbriefing mit gewünschtem Ergebnis und Risikostufe"
  - "Optional: Repo-Pfad, Ticket-IDs, URLs"
outputs:
  - "Nachvollziehbares Ergebnis (Datei, Zusammenfassung oder Ticket-Update)"
  - "Protokoll aktivierter MCPs/Skills und Delegationsschritte"
risk_level: low
example_count: 2
version: "1.0.0"
updated: "2026-11-23"
---

## Zweck

Hermes als lokal konfigurierbare Agent-Plattform nutzen: Skills steuern Verhalten, der Nous-MCP-Katalog liefert Datenquellen, optional delegierst du Coding-Schleifen an Claude Code oder Codex, ohne jedes Mal einen unkontrollierten Tool-Zoo zu laden.

## Wann nutzen

- Du brauchst einen **Least-Privilege**-Start (wenige MCPs) und willst erst bei Bedarf erweitern (`hermes mcp install`, Skills aus Katalog).
- Aufgaben passen zu Slash-Commands oder Skills wie `/github`, Research- oder Dokumentations-Flows.
- **Wann nicht:** Wenn du ClawHub-Community-Skills ohne Nous-Review brauchst (OpenClaw ist der Registry-Fokus). Wenn die Aufgabe eine reine macOS-Only-Skill-Platform braucht und du auf Linux arbeitest — `platforms: [macos]` wird still übersprungen.

## Tool-Stack

| Tool | Rolle | Begründung |
|------|-------|------------|
| Hermes Agent | Orchestrator | Skills, Memory, Cron, Tool Gateway, Delegation |
| Nous-approved MCP-Katalog | Kuratierter Zugang | Nur PR-gemergte `optional-mcps/`; Secrets über Install-Karte |
| Skills (~/.hermes/skills) | Ablauf & progressive disclosure | Getrennt von MCP-Verbindungen |
| Optionale Delegation | Coding-Runtime | Codex/Claude Code nur für die Implementierungsschleife |

## System-Prompt / Instruktionen

```text
Du arbeitest auf Hermes (Nous Research). Minimiere aktive MCPs: nur installieren, was die Aufgabe braucht.
Skills liefern Prozedur, MCP liefert Daten/Aktionen — nicht verwechseln.
Vor Schreib-, Send-, Deploy- oder Löschaktionen: explizite Nutzerfreigabe einholen.
Bei Dokument-Outputs: erzeugen → validate (falls Skill) → Render (PDF/PNG) → Datei erneut lesen.
Skills mit platforms-Filter prüfen; unter Linux werden macOS-only Skills übersprungen.
Tokens nie in Chat, Skill-Dateien oder MCP-Command-argv.
Jeden Tool-Call in einer kurzen Zeile protokollieren (Tool, Zweck, Ergebnis-Status).
Wenn Coding nötig: Delegation an Codex/Claude Code, Review im Hermes-Thread abschließen.
Bei Sync-Konflikten: lokale Löschungen respektieren; Restore nur mit hermes skills reset --restore.
Include/exclude für MCP und Skills nutzen, statt alles eingeschaltet zu lassen.
```

## Arbeitsablauf

1. `hermes setup` oder Portal öffnen; Ist-Zustand der MCPs mit `hermes mcp` prüfen (Default: aus).
2. Aufgabe in Briefing, Risiko und gewünschtes Artefakt zerlegen.
3. Nur passende Skills installieren (`hermes skills install`) und MCPs aus dem Nous-Katalog hinzufügen.
4. Include/exclude so setzen, dass Prompt-Budget und Berechtigungen minimal bleiben.
5. Agent-Thread starten; Slash-Command oder Skill-Trigger wählen.
6. Ergebnis prüfen; bei Dokumenten Verify-Render-Pfad der Skill-Doku folgen.
7. Optional Coding an Delegation abgeben; Änderungen im Orchestrator reviewen.
8. Artefakt und Tool-Log für Reproduzierbarkeit ablegen.

## Qualitätskriterien / Definition of Done

- [ ] Nur für die Aufgabe nötige MCPs/Skills waren aktiv (nachvollziehbar gelistet)
- [ ] Keine Schreib-/Sendeaktion ohne dokumentierte Freigabe
- [ ] Ergebnis entspricht Briefing; bei Office/PDF: Validator oder visueller Render geprüft
- [ ] Platforms-Filter geprüft (kein still fehlender macOS-Skill unter Linux)
- [ ] Delegation (falls genutzt) im Hermes-Thread abgeschlossen, nicht nur im Sub-Agent

## Sicherheit & Freigaben

- MCP-Einträge kommen bevorzugt aus dem Nous-Katalog; Custom-Server nur nach Review.
- Secrets über Hermes-Install-Karten/OAuth, nie in Prompts oder argv.
- Schreiben, Senden, Bezahlen, Deployen und Löschen nur nach expliziter Freigabe.
- Document-Skills: nach Erzeugen validate und visuell rendern (Verify-Schritt).

## Fallstricke

- **Platforms-Filter:** Skills mit `platforms: [macos]` laufen unter Linux ohne Fehlermeldung nicht — Aufgabe wirkt „kaputt“. Quelle: Community-Bericht in Hermes-Kategorie-Recherche.
- **Skill-Sync:** Sync überschreibt lokale Löschungen nicht blind; versehentlich gelöschte Skills brauchen `hermes skills reset --restore`.
- **MCP-Flut:** Zu viele gleichzeitige MCPs blähen Tool-Schemas und Kontext auf (siehe auch 67k-Token-Messung bei anderen Clients).
- **Skill vs. MCP:** Nur MCP zu aktivieren reicht nicht, wenn der Ablauf in einer Skill-Anleitung steckt.
- **Delegation ohne Review:** Codex/Claude Code mit Schreibrecht ohne Rückkopplung erzeugt widersprüchliche Commits.

## Grundbeispiele

### Beispiel 1 (Beispieldaten)

- **Aufgabe:** GitHub-Issue triagieren mit minimalem MCP-Set
- **Input:** Issue-URL `https://github.com/org/repo/issues/42`, Kurzbriefing „Labels und Kommentar-Entwurf“
- **Prompt:**
```text
Installiere nur github-MCP aus dem Nous-Katalog. Lies Issue #42, schlage Labels vor.
Keinen Kommentar posten ohne meine Freigabe. Protokolliere jeden MCP-Call.
```
- **Erwartetes Ergebnis:**
```text
Issue-Titel + Body-Zusammenfassung (3 Sätze)
Label-Vorschlag: bug, needs-triage
Entwurf-Kommentar in Markdown (nicht gepostet)
Log: github.get_issue OK, github.list_labels OK
```

### Beispiel 2 (Praxisbeispiel)

- **Aufgabe:** Hermes-Skill mit macOS-Platform unter Linux einsetzen
- **Input:** Skill aus Browse-Liste mit `platforms: [macos]` für Desktop-Automation
- **Prompt:**
```text
Führe den macos-only Skill für Calendar-Export aus.
```
- **Erwartetes Ergebnis:**
```text
Skill wird nicht geladen (still übersprungen).
Agent meldet: kein passender Skill für diese Plattform — Alternative: manueller Export oder Linux-kompatiblen Skill wählen.
```