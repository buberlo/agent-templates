---
id: generic-mcp-agents-mcp-focus
title: "Generische MCP-Agenten: MCP/Skill-Fokus"
domain: agent-platforms
category: generic-mcp-agents
tags:
  - generic
  - agent-platforms
  - katalog
target_agents:
  - hermes
  - grokbot
  - generic-mcp-agents
  - generic
required_tools:
  - name: punkpeye/awesome-mcp-servers
    install: "https://github.com/punkpeye/awesome-mcp-servers"
    version_notes: "Nur Directory"
  - name: modelcontextprotocol/servers
    install: "https://github.com/modelcontextprotocol/servers"
    version_notes: "Referenz-Server für Protocol-Tests"
inputs:
  - "Geplante MCP-Liste mit Transport"
  - "Skill-Markdown mit Tool-Zuordnung"
outputs:
  - "MCP minimization report"
  - "Skill-MCP mapping table"
risk_level: low
example_count: 3
version: "1.0.0"
updated: "2026-11-23"
---

## Zweck

**MCP/Skill-Fokus** für beliebige Agent-Plattformen: Welcher Server deckt welche Datenquelle ab, welcher Skill-Schritt ruft welches Tool auf, wo sitzen Verify-Render und Freigaben — unter Beachtung von Schema-Overhead, Grok-Transportregeln, Hermes-Platform-Filtern und ClawHub-Verify.

## Wann nutzen

- Du optimierst einen überladenen MCP-Stack (Symptom: langsame Starts, schlechte Antworten).
- Team dokumentiert Skill↔MCP-Matrix für Onboarding.
- **Wann nicht:** Wenn noch kein Skill existiert — zuerst Ablauf schreiben, dann MCP. Wenn du Reference-Server direkt in Produktion ohne Hardening nutzt.

## Tool-Stack

| Tool | Rolle | Begründung |
|------|-------|------------|
| awesome-mcp-servers | Shortlist | Einträge → Quell-Repos |
| modelcontextprotocol/servers | Lernen | Protocol, nicht Prod |
| Skill-Dokument | Orchestrierung | Steps, verify, gates |
| Plattform-MCP-CLI | Umsetzung | claude mcp / hermes mcp / openclaw mcp / Cursor settings |
| Tool allowlists | Safety | Read default |

## System-Prompt / Instruktionen

```text
MCP/Skill-Fokus für generische Agenten. Erstelle Tabelle: SkillStep | MCP | Tool | Read/Write | Freigabe.
Jede Datenquelle maximal ein MCP; Duplikate zusammenlegen.
Messe impliziten Overhead: wenige breite Server oft besser als viele spezialisierte.
Schema-Token-Problem: entferne ungenutzte MCPs vor großen Tasks (Referenz ~67k Overhead).
Skills tragen Verify für Dokumente (validate, render, re-read) — MCP write ersetzt das nicht.
ClawHub: verify (~12 % Malware Feb 2026) wenn Registry-Skills OpenClaw/Gateway tangieren.
Grok: Custom MCP HTTPS oder Box-Command; argv ohne Secrets.
Hermes: Skill platforms-Tag prüfen.
OpenClaw: Tool-Policy pro MCP-Tool.
Cursor/Claude: mcp.json ohne PAT; Injection auf MCP content.
Reference servers nur in Dev-Sandbox.
Abschluss: minimization report (vorher/nachher MCP count, geschätzter Tool count).
Write tools: Needs approval auf allen Plattformen wo verfügbar.
```

## Arbeitsablauf

1. Inventar: alle MCPs, Tool-Anzahl schätzen.
2. Skill-Dokument öffnen oder anlegen (Schritte nummeriert).
3. Pro Skill-Schritt MCP-Tool zuordnen oder „lokal“ markieren.
4. Duplikate und ungenutzte Server entfernen.
5. Transport-Regeln prüfen (Grok HTTPS/Box, kein Laptop-localhost).
6. Registry-Skills in Kette auf verify-Status prüfen.
7. Read-only Smoke pro verbleibendem MCP.
8. Matrix ins Repo committen; Secrets redacted.
9. Pilot-Task; Retrospektive im minimization report.

## Qualitätskriterien / Definition of Done

- [ ] Skill-MCP-Matrix vollständig für den Task
- [ ] MCP-Anzahl reduziert oder begründet
- [ ] Verify-Render in Skill für Dokument-Schritte
- [ ] Plattform-Transport-Regeln eingehalten
- [ ] Keine Secrets in Matrix/Config
- [ ] ClawHub/Registry in Kette verifiziert falls verwendet

## Sicherheit & Freigaben

- MCP-Content untrusted; Write-Gates im Skill verankert.
- Registry-verify bei ClawHub-Pfad.
- Reference-server nicht ungehärtet in Prod.

## Fallstricke

- **67k Overhead:** Matrix hilft nicht, wenn 10 MCPs bleiben — kürzen.
- **Zwei MCPs, eine Quelle:** Doppeltes Schema, widersprüchliche Tools.
- **Skill ohne Tool-Spalte:** Agent wählt falsches MCP-Tool.
- **Verify nur in MCP:** Office braucht Skill-Script + Render.
- **ClawHub ~12 %:** Skill aus Registry in Matrix ohne verify-Zeile.
- **Grok argv secrets:** In Matrix als Command-MCP notiert mit Key im Arg — verboten.

## Grundbeispiele

### Beispiel 1 (Praxisbeispiel)

- **Aufgabe:** Overhead reduzieren
- **Input:** 8 MCPs, 120 Tools geschätzt
- **Prompt:**
```text
Matrix bauen, auf 3 MCPs konsolidieren, Tool count neu schätzen.
```
- **Erwartetes Ergebnis:**
```text
Vorher: 8 MCPs / ~120 tools
Nachher: 3 MCPs / ~45 tools
minimization report committed (secrets redacted)
```

### Beispiel 2 (Beispieldaten)

- **Aufgabe:** Document-Schritt in Matrix
- **Input:** Skill step 5 „deliver pptx“
- **Prompt:**
```text
Zeige MCP nur für export wenn nötig; validate+render in Skill step 6–7.
```
- **Erwartetes Ergebnis:**
```text
| 5 | (local skill) | write deck | write | user |
| 6 | (local skill) | validate.py | read | auto |
| 7 | (local skill) | render png | read | auto |
Kein MCP in steps 6–7
```

### Beispiel 3 (Beispieldaten)

- **Aufgabe:** Grok Box-Command Zeile
- **Input:** Custom MCP via npx auf Bot-Box
- **Prompt:**
```text
Matrix-Eintrag: Command MCP ohne API_KEY in argv, nur env auf Box.
```
- **Erwartetes Ergebnis:**
```text
Command: npx @acme/mcp-server
Env: ACME_KEY (Box secret store)
Shared-bot Sichtbarkeit vermerkt
Kein localhost User-Laptop
```