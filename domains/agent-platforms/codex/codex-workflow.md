---
id: codex-workflow
title: "Codex"
domain: agent-platforms
category: codex
tags:
  - codex
  - agent-platforms
  - skill
target_agents:
  - codex
  - generic-mcp-agents
required_tools:
  - name: Hermes-Skill codex
    install: "https://hermes-agent.nousresearch.com/docs/reference/skills-catalog"
    version_notes: "Bundled; delegiert an OpenAI Codex CLI"
  - name: OpenClaw MCP serve / ACP
    install: "https://docs.openclaw.ai/cli/mcp/serve"
    version_notes: "Bridge openclaw mcp serve oder openclaw acp"
inputs:
  - "Feature-Briefing oder PR-Beschreibung"
  - "Repo-URL oder Pfad; Orchestrator (Hermes/OpenClaw)"
outputs:
  - "Branch/Diff aus Codex-Schleife"
  - "Review-Zusammenfassung im Orchestrator-Thread"
risk_level: low
example_count: 2
version: "1.0.0"
updated: "2026-11-23"
---

## Zweck

OpenAI **Codex CLI** als fokussierte Coding-Runtime einsetzen — oft **von Hermes delegiert** (`Hermes-Skill codex`) oder über **OpenClaw** (`openclaw mcp serve` / `openclaw acp`). Der Orchestrator hält Kontext und Freigaben; Codex liefert Implementierungsschleifen.

## Wann nutzen

- Hermes/OpenClaw soll planen, auditieren und freigeben; Codex schreibt Code in isolierter Schleife.
- OpenClaw-Gateway soll als MCP-Server für externe Clients (Codex, Claude Code) dienen.
- **Wann nicht:** Wenn zwei Agenten parallel ohne Lock auf dasselbe Repo schreiben. Wenn du Office-Verify (document-skills Render) in Codex erwartest statt im Orchestrator/Skill. Wenn keine Rückkopplung in den Parent-Thread geplant ist.

## Tool-Stack

| Tool | Rolle | Begründung |
|------|-------|------------|
| Hermes-Skill codex | Delegation | Bundled Skill aus Skills-Katalog |
| OpenAI Codex CLI | Coding-Runtime | MCP-fähig wie andere Clients |
| openclaw mcp serve | Brücke | OpenClaw als MCP für Codex |
| openclaw acp | Alternative Host | OpenClaw hostet Coding-Runtime |
| Parent Orchestrator | Review | Hermes/OpenClaw-Thread mit Freigabe |

## System-Prompt / Instruktionen

```text
Du nutzt Codex als Coding-Runtime unter einem Orchestrator (Hermes oder OpenClaw).
Codex-Session nur für Implementierung, Tests und lokale Diffs — keine Produktions-Deploys ohne Parent-Freigabe.
Hermes-Skill codex: Aufgabe klar abgrenzen (Scope, Dateien, nicht ganze Monorepo umschreiben).
OpenClaw-Brücke: openclaw mcp serve (stdio) nur mit Tool-Policy, die Writes begrenzt.
Zwei Schreiber auf ein Repo: Serialisierung — ein aktiver Codex-Job pro Branch.
MCP in Codex minimal halten (Schema-Overhead wie bei anderen Clients).
Parent-Thread muss Diff und Teststatus zurückbekommen.
Keine API-Keys in Delegations-Prompt oder Codex-argv.
Nach Codex-Lauf: Orchestrator reviewt, merged nicht automatisch.
Skills im Parent definieren Verify (Lint/Test); Codex führt aus, Parent sign-off.
Bei ClawHub-Skills am Gateway: verify vor Nutzung durch Codex-Bridge.
Document-Verify (Render) bleibt Parent-/Skill-Aufgabe, nicht Codex allein.
```

## Arbeitsablauf

1. Orchestrator-Thread öffnen; Briefing und Akzeptanzkriterien festhalten.
2. Repo-Lock/Branch-Strategie klären (ein Codex-Job).
3. Hermes `codex`-Skill anstoßen oder OpenClaw `mcp serve` für Codex-Client konfigurieren.
4. Codex: implementieren, Tests laufen lassen, Diff erzeugen.
5. Ergebnis (Diff, Test-Log) an Parent zurückmelden.
6. Parent: Review, Security-Check, Freigabe für Push/Merge.
7. Optional zweite Codex-Runde nur nach Review-Kommentaren.
8. Abschluss im Orchestrator mit Links zu Commits/PR.

## Qualitätskriterien / Definition of Done

- [ ] Ein Schreiber pro Branch während Codex-Lauf
- [ ] Diff und Teststatus im Parent-Thread dokumentiert
- [ ] Kein Merge/Deploy ohne Parent-Freigabe
- [ ] MCP/Bridge-Policy verhindert unerwartete Remote-Writes
- [ ] Keine Secrets in Delegations-Metadaten

## Sicherheit & Freigaben

- OpenClaw-Bridge: Tool-Policy wie Gateway-Standard.
- Parent muss destructive Aktionen freigeben.
- Bei Registry-Skills am Gateway: ClawHub verify (~12 % Malware-Kontext).

## Fallstricke

- **Zwei Schreiber:** Hermes und Codex ändern parallel — Merge-Konflikte und Datenverlust.
- **Delegation ohne Review:** Codex pusht; Parent kennt Diff nicht.
- **MCP-Overhead:** Voller MCP-Stack in Codex + Parent — doppelter Schema-Druck.
- **openclaw acp vs. serve:** Falsche Brücke — Client sieht falsche Tools.
- **Skill vs. MCP:** Parent-Skill muss Verify-Schritte (Test/Lint) benennen.
- **ClawHub am Gateway:** Codex über Bridge nutzt kompromittierte Skills, wenn nicht verifiziert.

## Grundbeispiele

### Beispiel 1 (Beispieldaten)

- **Aufgabe:** Hermes delegiert kleines Feature
- **Input:** „Endpoint GET /health in Express ergänzen“, Repo lokal geklont
- **Prompt:**
```text
(Hermes) Nutze codex-Skill nur für src/routes/*. Codex: Implementierung + npm test. Kein git push.
```
- **Erwartetes Ergebnis:**
```text
Diff: +12 Zeilen health route
npm test: 14 passed
Parent-Thread: Review-OK, Nutzer gibt Push frei
```

### Beispiel 2 (Beispieldaten)

- **Aufgabe:** Parallele Schreiber — Fehlmodus
- **Input:** Gleicher Branch main, Hermes-Agent und Codex ohne Lock
- **Prompt:**
```text
Codex: Refactor auth; parallel Hermes: Update README auf main.
```
- **Erwartetes Ergebnis:**
```text
Merge-Konflikt in main
Parent stoppt: „Serialisiere Jobs — ein Branch, ein aktiver Writer“
Kein force-push
```