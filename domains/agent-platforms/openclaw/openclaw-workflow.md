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
    version_notes: "Gateway, CLI openclaw skills|mcp|plugins"
  - name: ClawHub
    install: "https://github.com/openclaw/clawhub"
    version_notes: "Registry; openclaw skills verify vor Installation"
inputs:
  - "Gateway-Setup oder bestehende OpenClaw-Instanz"
  - "Skill-Name oder MCP-Server-Definition"
outputs:
  - "Konfiguriertes Gateway mit dokumentierter Tool-Policy"
  - "Verify-Bericht für ClawHub-Skills"
risk_level: high
example_count: 3
version: "1.0.0"
updated: "2026-11-23"
---

## Zweck

OpenClaw als selbst gehostetes **Gateway** für Skills, Plugins und MCP betreiben: ClawHub liefert öffentliche Skills, der Skill Workshop prägt neue Prozeduren — mit **`openclaw skills verify`** vor Produktion, weil Registry-Audits ~12 % Schadcode fanden (Koi Security, Feb. 2026).

## Wann nutzen

- Du willst Kanäle, Android-Companion und lokale Tool-Policies unter eigener Kontrolle.
- Skills aus Workspace **oder** ClawHub, mit Semver und Security-Scan-Summaries.
- **Wann nicht:** Wenn du Skills blind aus der Registry installieren willst ohne Verify/Audit. Wenn `skills.limits.maxSkillsPromptChars` viele Skill-Beschreibungen kürzt und du keinen Kurz-Katalog pflegst. Wenn Companion-Apps fälschlich als Gateway-Host dienen sollen.

## Tool-Stack

| Tool | Rolle | Begründung |
|------|-------|------------|
| OpenClaw Gateway | Host | Skills, MCP, Plugins, Kanäle |
| ClawHub | Registry | `openclaw skills install @owner/skill` |
| Skill Workshop | Neue Prozeduren | Proposal review vor Publish |
| mcp.servers + Tool-Policy | Least privilege | Begrenzt Tool-Zugriff |
| Android-Companion | Client | QR-Kopplung an bestehendes Gateway |

## System-Prompt / Instruktionen

```text
Du konfigurierst und nutzt OpenClaw Gateway. ClawHub-Skills immer zuerst mit openclaw skills verify prüfen.
Bekanntes Risiko: ~12 % der geprüften Registry-Skills (341/2857) als schadhaft eingestuft (Feb. 2026 Audit).
Workspace-Skills können Bundled überschreiben — Loading-Order prüfen.
Metadaten-Datei heißt .clawhub, nicht .clawdhub (ältere Namen werden ignoriert).
MCP unter mcp.servers eintragen; Tool-Policy für Write/Send restriktiv halten.
Prompt-Budget: maxSkillsPromptChars kann Skill-Texte kürzen — Beschreibungen knapp halten.
Skills = Ablauf, MCP = Verbindung — kombinieren, nicht verwechseln.
Companion/Android ist kein Ersatz für Gateway auf dem Host.
Keine Secrets in Skill-Install-Args oder Chat.
Vor Schreiben/Senden/Löschen/Deploy: menschliche Freigabe.
Dokument-Outputs: erneut lesen und PDF/PNG rendern (Verify).
Leaderboard-Skills mit Warnflag und wenigen Registry-Stars trotz Downloads besonders kritisch prüfen.
```

## Arbeitsablauf

1. Gateway starten; CLI `openclaw` und Workspace-Pfad dokumentieren.
2. Geplante ClawHub-Skill-IDs sammeln; je Skill `openclaw skills verify` ausführen und Ergebnis speichern.
3. Nur verifizierte Skills installieren; bei Warnung manuell Review oder ablehnen.
4. MCP in Settings oder CLI (`openclaw mcp`) ergänzen; Tool-Policy für riskante Tools einschränken.
5. Skill Workshop nutzen, wenn neue Team-Prozeduren entstehen (Proposal review).
6. Android-Companion per QR an **bestehendes** Gateway koppeln (nicht als Host missverstehen).
7. Test-Task mit minimalem Skill-Set; Prompt-Länge nach Kürzung prüfen.
8. Produktions-Task nur nach Freigabe-Gates für Schreib-/Sendeaktionen.

## Qualitätskriterien / Definition of Done

- [ ] Jeder ClawHub-Skill hat dokumentiertes Verify-Ergebnis vor Aktivierung
- [ ] Tool-Policy und aktive MCP-Liste passen zum Briefing
- [ ] Keine `.clawdhub`-Legacy-Metadaten ohne Migration auf `.clawhub`
- [ ] Schreib-/Sendeaktionen nur mit Freigabe
- [ ] Skill-Prompt-Budget: keine überraschend abgeschnittenen Kernanweisungen

## Sicherheit & Freigaben

- Hohes Registry-Risiko: Verify + Vorsicht bei Leaderboard-Anomalien (viele Downloads, wenige Stars).
- Workspace-Skill-Overrides bewusst setzen, nicht blind aus ClawHub überschreiben.
- Destruktive Gateway-Tools erst nach expliziter Freigabe.

## Fallstricke

- **ClawHub-Malware ~12 %:** Koi Security Feb. 2026 — 341 von 2857 Skills schadhaft; immer `openclaw skills verify`, nie blind installieren.
- **Loading-Order:** Workspace-Skills können Bundled-Skills verdrängen — unerwartetes Verhalten bei gleichen Namen.
- **`.clawdhub` → `.clawhub`:** Alte Metadaten werden nicht gelesen; Upgrades scheitern still.
- **Prompt-Budget:** `maxSkillsPromptChars` kürzt Beschreibungen — kritische Schritte fehlen im Kontext.
- **Companion ≠ Host:** Android-App steuert Remote-Gateway, ersetzt keine Gateway-Sicherheit auf dem Server.
- **MCP-Token-Overhead:** Zu viele MCP-Server belasten Kontext wie bei anderen Agent-Clients (Schema-Größe).

## Grundbeispiele

### Beispiel 1 (Praxisbeispiel)

- **Aufgabe:** ClawHub-Sicherheitsaudit (Feb. 2026)
- **Input:** 2.857 öffentlich gelistete ClawHub-Skills
- **Prompt:**
```text
(openclaw skills verify für Kandidaten; externes Audit als Kontext)
```
- **Erwartetes Ergebnis:**
```text
341 Skills als schadhaft bewertet (~12 %).
Konsequenz: Verify-Pflicht, keine Masseninstallation aus Leaderboard.
Quelle: Koi Security / The Hacker News Berichte.
```

### Beispiel 2 (Beispieldaten)

- **Aufgabe:** Workspace-Skill über Bundled legen
- **Input:** Gleicher Skill-Name in Workspace und Bundled, unterschiedliche Instruktionen
- **Prompt:**
```text
Nutze den Github-Skill für PR-Zusammenfassung.
```
- **Erwartetes Ergebnis:**
```text
Workspace-Variante gewinnt (Loading-Order).
Bot folgt Workspace-Anweisung; Bundled-Text erscheint nicht im Log.
Hinweis im DoD: Order dokumentiert.
```

### Beispiel 3 (Beispieldaten)

- **Aufgabe:** MCP + Skill für Issue-Triage ohne Auto-Write
- **Input:** linear-MCP in mcp.servers, clawhub:@team/triage-skill
- **Prompt:**
```text
Verify triage-skill, dann offene Issues listen. Keine Comment-POSTs.
```
- **Erwartetes Ergebnis:**
```text
verify: PASS (oder FAIL → Abbruch)
Markdown-Liste 8 Issues
Tool-Policy blockiert write_comment
Kein POST ausgeführt
```