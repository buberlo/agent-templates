---
id: openclaw-workflow
title: "OpenClaw"
domain: agent-platforms
category: openclaw
tags:
  - openclaw
  - agent-platforms
  - agent-platform
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
  - "Gateway-Setup or bestehende OpenClaw-Instanz"
  - "Skill-Name or MCP-Server-Definition"
outputs:
  - "Configured Gateway with Documented Tool Policy"
  - "Verify report for ClawHub skills"
risk_level: high
example_count: 3
version: "1.0.0"
updated: "2026-11-23"
---
## Purpose

OpenClaw as a self-hosted **gateway** for skills, plugins and MCP: ClawHub delivers public skills, the Skill Workshop shapes new procedures – with **`openclaw skills verify`** before production, because registry audits found ~12% malicious code (Koi Security, Feb. 2026).

## When to use

- You want channels, Android companion and local tool policies under your own control.
- Skills from Workspace **or* ClawHub, with Semver and Security Scan Summaries.

### When not to use

- If you want to install Skills blind from the registry without Verify/Audit. If `skills.limits.maxSkillsPromptChars` shortens many skill descriptions and you do not maintain a short catalogue. When Companion apps are incorrectly intended to serve as a gateway host.

## Tool stack

| Tool | Role | Rationale |
|------|-------|-----------|
| OpenClaw Gateway | Host | Skills, MCP, plugins, channels |
| ClawHub | Registry | `openclaw skills install @owner/skill` |
| Skill Workshop | Neue Prozeduren | Proposal review vor Publish |
| mcp.servers + Tool-Policy | Least privilege | Begrenzt Tool-Zugriff |
| Android companion | Client | QR pairing to existing gateway |

## System prompt

```text
You configure and use OpenClaw Gateway. Always check ClawHub skills first with openclaw skills verify.
Known risk: ~12% of audited registry skills (341/2857) classified as malicious (Feb. 2026 Audit).
Workspace skills can override bundled — check loading orders.
Metadata file is called .clawhub, not .clawdhub (older names are ignored).
MCP unter mcp.servers eintragen; Tool-Policy for Write/Send restriktiv halten.
Prompt budget: maxSkillsPromptChars can shorten skill texts — keep descriptions short.
Skills = Ablauf, MCP = Verbindung — kombinieren, not verwechseln.
The Android companion is not a replacement for the gateway on the host.
No Secrets in Skill-Install-Args or Chat.
Before Write/Send/Delete/Deploy: Human release.
Dokument-Outputs: erneut lesen and PDF/PNG rendern (Verify).
Leaderboard skills with Warnflag and few registry stars despite downloads particularly critical.
```

## Workflow

Starting the gateway; CLI `openclaw` and workspace path document.
2. Collect planned ClawHub skill IDs; execute each skill `openclaw skills verify` and save the result.
3. Nur verifizierte Skills installieren; bei Warnung manuell Review or ablehnen.
4. MCP in Settings or CLI (`openclaw mcp`); Restrict tool policy for risky tools.
5. Skill Workshop nutzen, wenn neue Team-Prozeduren entstehen (Proposal review).
6. Connect Android Companion to **existing** gateway via QR (not misunderstand as host).
7. Test task with minimal skill set; Check prompt length after reduction.
8. Production task only after share gates for write/send actions.

## Definition of done

- [ ] Jeder ClawHub-Skill hat dokumentiertes Verify-result vor Aktivierung
- [ ] Tool policy and active MCP list match the briefing
- [ ] No `.clawdhub`-Legacy-Metadaten without Migration auf `.clawhub`
- [ ] Write/send actions only with approval
- [ ] Skill prompt budget: no surprisingly cut-off core instructions

## Security

- Hohes Registry-Risiko: Verify + Vorsicht bei Leaderboard-Anomalien (viele Downloads, wenige Stars).
- Workspace skill overrides consciously put, not blindly overwrite from ClawHub.
Destructive gateway tools only after explicit release.

## Pitfalls

- **ClawHub-Malware ~12 %:** Koi Security Feb. 2026 — 341 von 2857 Skills schadhaft; immer `openclaw skills verify`, nie blind installieren.
**Loading Order:** Workspace skills can displace bundled skills — unexpected behavior on the same name.
- **`.clawdhub` → `.clawhub`:** Old metadata is not read; Upgrades fail silently.
- **Prompt budget:** `maxSkillsPromptChars` shortens descriptions — critical steps are missing in context.
- **Companion ≠ host:** The Android app controls a remote gateway; it does not replace gateway security on the server.
**MCP Token Overhead:** Too many MCP servers load context like other agent clients (schema size).

## Basic examples

### Example 1 (Example data (self-written))
- **Task:** ClawHub-Sicherheitsaudit (Feb. 2026)
*Input: 2,857 publicly listed ClawHub skills
- **Prompt:**
```text
(openclaw skills verify for Kandidaten; externes Audit als Kontext)
```
- **Expected result:**
```text
341 Skills als schadhaft bewertet (~12 %).
Konsequenz: Verify-Pflicht, no Masseninstallation aus Leaderboard.
Source: Koi Security / The Hacker News reports.
```

### Example 2 (Example data (self-written))
- **Task:** Put Workspace-Skill over Bundled
- **Input:** Same skill name in Workspace and Bundled, different instructions
- **Prompt:**
```text
Nutze den Github-Skill for PR-Zusammenfassung.
```
- **Expected result:**
```text
Workspace-Variante gewinnt (Loading-Order).
Bot folgt Workspace-Anweisung; Bundled-Text erscheint not im Log.
Hinweis im DoD: Order dokumentiert.
```

### Example 3 (Example data (self-written))
- **Task:** MCP + Skill for issue triage without auto-write
- **Input:** linear-MCP in mcp.servers, clawhub:@team/triage-skill
- **Prompt:**
```text
Verify triage-skill, dann offene Issues listen. No Comment-POSTs.
```
- **Expected result:**
```text
verify: PASS (or FAIL → Abbruch)
Markdown-Liste 8 Issues
Tool-Policy blockiert write_comment
No POST executed
```