---
id: chat-messaging-workflow
title: "Chat und Messaging"
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
  - name: Grok Bot Slack-Plugin
    install: "https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp"
    version_notes: "Produktdoku."
inputs:
  - "Kanal oder Chat-ID"
  - "Zeitraum / letzte N Nachrichten"
  - "Ton und Freigabe für Senden"
outputs:
  - "Thread-Zusammenfassung"
  - "Nachrichtenentwurf (optional gesendet nach OK)"
risk_level: low
example_count: 2
version: "1.1.0"
updated: "2026-11-23"
---

## Zweck

**Slack, iMessage und ähnliche Kanäle** lesen, Threads bündeln und **Antworten nur nach Freigabe** posten—inkl. @mentions und Kanal-Kontext.

## Wann nutzen

- Team fragt nach Digest eines Channels oder DM-Threads.
- Antwortentwurf für Slack/iMessage, Versand durch Mensch oder explizites OK.
- Plattform-Skill (Slack OpenClaw, Hermes imessage auf macOS) ist verfügbar.

**Wann nicht**

- WhatsApp/Telegram ohne offiziellen, policy-konformen Connector.
- Linux-Host für **iMessage** (Skill plattformgebunden, wird übersprungen).
- Krisenkommunikation ohne abgestimmtes Messaging-Leitbild.

## Tool-Stack

| Tool | Rolle | Begründung |
|------|-------|------------|
| OpenClaw Slack-Skill | Kanal lesen/posten | Breite ClawHub-Nutzung |
| Hermes imessage | macOS iMessage/SMS | Native imsg CLI |
| Grok Slack-Plugin | OAuth als User | Nur erlaubte Kanäle |

## System-Prompt / Instruktionen

```text
You handle team chat for kommunikation/chat-messaging: read threads, summarize, draft replies; post/send only after user approval.

Inputs: platform (slack | imessage), channel_or_chat_id, since (ISO time or "last 24h"), goal (summarize | draft_reply | list_action_items), tone (formal DE default).

Slack flow:
- Fetch channel history with thread replies; note authors and timestamps.
- Summarize decisions, open questions, owners.
- Draft reply in thread or channel; show exact text before postMessage.

iMessage flow (macOS only):
- List recent messages for handle; never send without "SEND to <handle>".

Rules:
- Respect user channel membership (Grok: cannot post where user has no access).
- No secrets, tokens, or attachment exfiltration in summaries.
- Mark uncertain attributions with [?].

Deliver: summary.md, draft message block, list of message IDs referenced.
```

## Arbeitsablauf

1. Plattform wählen und Zugang prüfen (`openclaw skills verify` bei ClawHub-Skills).
2. Slack: Channel-ID und `since` setzen; History inkl. Threads laden.
3. Nachrichten deduplizieren; Entscheidungen und offene Punkte extrahieren.
4. Antwortentwurf im Zielton schreiben; Länge an Kanalnorm anpassen.
5. Entwurf dem Nutzer zeigen; auf `SEND` oder Anpassung warten.
6. Bei Freigabe: `chat.postMessage` oder iMessage-Send mit bestätigtem Text.
7. `output/chat-log.md` mit Message-IDs und Zeitstempeln archivieren.

## Qualitätskriterien / Definition of Done

- [ ] Zusammenfassung referenziert echte Autoren/Zeiten
- [ ] Keine gesendete Nachricht ohne dokumentiertes OK
- [ ] Thread-Kontext bei Slack-Replies korrekt (thread_ts wenn nötig)
- [ ] Plattformlimits dokumentiert (iMessage auf macOS)

## Sicherheit & Freigaben

- Interne Strategie-Chats nicht in öffentliche Summaries kopieren.
- Screenshots/Anhänge nur mit Freigabe weiterverarbeiten.
- OAuth-Plugins: keine Token in Prompts.

## Fallstricke

- Reply im falschen Thread → Informationslärm.
- @channel ohne Freigabe → Notification-Storm.
- iMessage-Skill auf Linux still disabled → leerer Output ohne Fehlermeldung.
- Grok postet als User → Verwechslung mit menschlicher Stimme.
- Rate-Limits bei großen Backfills.

## Grundbeispiele

### Beispiel 1 (Beispieldaten)

- **Aufgabe:** #product Digest 24h.
- **Input:** Slack `#product`, since `2026-11-22T09:00:00+01:00`.
- **Prompt:**

```text
Summarize decisions and action items from #product last 24h; draft one paragraph standup update, do not post.
```

- **Erwartetes Ergebnis:**

```text
Decisions: Ship v2.1 Friday; defer mobile redesign.
Action items: @maria API spec by Wed; @tom QA checklist.
Draft (not posted): "Guten Morgen — v2.1 bleibt Freitag..."
```

### Beispiel 2 (Beispieldaten)

- **Aufgabe:** Fehlende Channel-ID.
- **Input:** Nur Name "product" ohne Workspace-Kontext.
- **Prompt:**

```text
Post update to product channel.
```

- **Erwartetes Ergebnis:**

```text
Abbruch: channel_id unbekannt.
Nachfrage: Workspace + Channel-ID oder invite link?
Kein postMessage ausgeführt.
```