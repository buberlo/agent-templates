---
id: chat-messaging-mcp-focus
title: "Chat und Messaging: MCP/Skill-Fokus"
domain: kommunikation
category: chat-messaging
tags:
  - chat
  - kommunikation
  - skill
target_agents:
  - hermes
  - grokbot
  - generic-mcp-agents
  - generic
required_tools:
  - name: Hermes-Skill imessage
    install: "https://hermes-agent.nousresearch.com/docs/reference/skills-catalog"
    version_notes: "Bundled."
  - name: ClawHub „Slack“ (steipete)
    install: "https://clawhubtrends.com/leaderboard.html"
    version_notes: "42.838 Downloads, 140 Registry-Stars (ClawHub Leaderboard 23.11.2026)."
inputs:
  - "Zielplattform und erlaubte Aktionen"
  - "Tool-Policy / MCP-Include-Liste"
outputs:
  - "Tool-Matrix und Aktivierungsprotokoll"
  - "Test-Lesezugriff (Nachrichtenanzahl)"
risk_level: low
example_count: 2
version: "1.1.0"
updated: "2026-11-23"
---

## Zweck

**Chat-Tools minimal aktivieren**: Native Skills (Slack, imessage) vs. Grok-Plugins trennen, Policy setzen und Verbindung mit harmlosem Lese-Test prüfen.

## Wann nutzen

- Neues Agent-Setup für Messaging; Unsicherheit Skill vs. MCP vs. Plugin.
- Reduktion der Tool-Oberfläche (Prompt-Injection, Budget).
- Vergleich Hermes imessage vs. OpenClaw Slack auf einem Host.

**Wann nicht**

- Konkrete Inhaltsaufgabe (Thread zusammenfassen) → `chat-messaging-workflow`.
- Plattform ohne installierten Skill und ohne Plugin-OAuth.

## Tool-Stack

| Tool | Rolle | Begründung |
|------|-------|------------|
| Hermes imessage | macOS SMS/iMessage | Plattform skill, bundled |
| OpenClaw Slack | Bot/User-Token je Setup | Verifizierte Registry-Skills |
| Grok Slack-Plugin | Cloud OAuth | Keine Rechte-Erhöhung über User |

## System-Prompt / Instruktionen

```text
You design minimal chat tooling for kommunikation/chat-messaging: pick ONE primary read path and ONE optional send path.

Inputs: host OS, platforms needed, send_allowed (yes/no), hermes_include_mcp list, openclaw tool policy snippet.

Produce:
1) tool-matrix.md: platform → tool → install command → scopes
2) activation steps: hermes mcp include/exclude OR openclaw skills install + verify
3) read smoke test command (list 3 recent messages, redact bodies in log)
4) explicit disable list for send tools if send_allowed=no

Grok plugin: note posts as connected user, channel ACL unchanged.
iMessage: require darwin; if linux, state skill skipped and suggest SMS API alternative only if user provides approved MCP.

Never store tokens in skill markdown. Deliver verification transcript with timestamps.
```

## Arbeitsablauf

1. Host-OS und Zielplattformen erfassen (`uname -s` für imessage-Check).
2. `tool-matrix.md` aus Kategorie-Recherche befüllen.
3. Hermes: unnötige MCPs excluden; OpenClaw: `openclaw skills verify slack`.
4. Lese-Test: Slack `conversations.history limit=3` oder imessage list.
5. Send-Tools aus Policy entfernen, wenn nur Lesen gewünscht.
6. Ergebnis und Befehlsprotokoll in `output/messaging-tooling.md`.
7. Nutzer bestätigt Matrix vor Produktiv-Workflow.

## Qualitätskriterien / Definition of Done

- [ ] Genau ein primärer Lese-Stack dokumentiert
- [ ] Verify-Schritt für ClawHub-Skills erwähnt/ausgeführt
- [ ] Send-Tools deaktiviert oder mit Freigabe-Gate markiert
- [ ] Linux + imessage: expliziter Hinweis auf Skip

## Sicherheit & Freigaben

- ClawHub-Skills vor Produktion verifizieren (bekannte Registry-Risiken).
- Keine Bot-Tokens in Repos.
- Plugin-OAuth nur über offizielle Connect-Flows.

## Fallstricke

- Zwei Slack-Integrationen parallel → doppelte Posts.
- imessage ohne macOS → stilles Fehlschlagen.
- Grok in Kanal ohne User-Mitgliedschaft → 404 ohne klare Ursache.
- Zu breite MCP-Include-Liste → Kontext-Overflow.
- Send-Tool vergessen zu deaktivieren bei „nur lesen“-Auftrag.

## Grundbeispiele

### Beispiel 1 (Beispieldaten)

- **Aufgabe:** Slack read-only Agent.
- **Input:** OpenClaw, `send_allowed=no`.
- **Prompt:**

```text
Write tool-matrix and disable all post/send tools; smoke test #general read 3 messages.
```

- **Erwartetes Ergebnis:**

```text
Primary: openclaw slack (read)
Disabled: chat.postMessage, imessage send
Smoke: 3 messages fetched, subjects redacted in log
File: output/messaging-tooling.md
```

### Beispiel 2 (Beispieldaten)

- **Aufgabe:** macOS iMessage vorbereiten.
- **Input:** Darwin, Hermes bundled imessage.
- **Prompt:**

```text
Document imessage skill activation and list last 2 chats (handles redacted).
```

- **Erwartetes Ergebnis:**

```text
Platform: darwin — imessage skill active
Chats: +43***01 (2 msgs), team@*** (5 msgs)
Send: gated until user types SEND
```