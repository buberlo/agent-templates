# Trading und Krypto

- **Domain:** `finanzen`
- **Kategorie:** `trading-krypto`
- **Stand:** 2026-11-23

## Kurzbeschreibung

Marktdaten und Research (Twelve Data, Robinhood-Katalogeinträge); Trading nur mit klaren Limits.

## Empfohlener Tool-Stack

- Daten-MCPs klar von Order-Routing trennen

## MCP-Server und Skills

| Name | Typ | URL | Einsatz | Installation | Popularitaet | Quelle | Unverified? |
|---|---|---|---|---|---|---|---|
| robinhood MCP (Hermes-Katalog) | MCP | https://github.com/NousResearch/hermes-agent/tree/main/optional-mcps/robinhood | Katalogeintrag – Schreibrechte vor Live-Nutzung in der Vendor-Doku pruefen. | hermes mcp install robinhood | Nous-approved optional-mcps-Katalogeintrag (Listing 23.11.2026). | https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp | nein (so belegt) |
| twelve-data MCP (Hermes-Katalog) | MCP | https://github.com/NousResearch/hermes-agent/tree/main/optional-mcps/twelve-data | Marktdaten aus dem Nous-Katalog. | hermes mcp install twelve-data | Nous-approved optional-mcps-Katalogeintrag (Listing 23.11.2026). | https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp | nein (so belegt) |
| ClawHub „Polymarket“ (joelchance) | Skill | https://clawhubtrends.com/leaderboard.html | Sehr hohe Downloads; nicht als Anlageberatung behandeln. | openclaw skills install (Owner joelchance) und openclaw skills verify. | 172.358 Downloads, 112 Registry-Stars (ClawHub Leaderboard 23.11.2026). | https://clawhubtrends.com/leaderboard.html | nein (so belegt) |
| ClawHub „Stock Analysis“ (udiedrichsen) | Skill | https://clawhubtrends.com/leaderboard.html | Im Leaderboard mit Warnmarkierung. Im Leaderboard mit Warnmarkierung – vor Nutzung verifizieren. | openclaw skills install (Owner udiedrichsen) und openclaw skills verify. | 48.766 Downloads, 227 Registry-Stars (ClawHub Leaderboard 23.11.2026). | https://clawhubtrends.com/leaderboard.html | nein (so belegt) |

## Typische Workflows

- Research und Daten ja; automatisches Handeln nur mit schriftlichen Limits und gesonderter Freigabe.

## Fallstricke

- Warnmarkierte Skills. Markt-Skills koennen irrefuehren.
- Keine Tokens oder Passwörter in Chat, Skill-Dateien oder Command-Argumente von Custom-MCPs schreiben. Grok-Bot-Wiki: OAuth-Tokens bleiben auf dem Connector-Backend; Command-Server dürfen keine Credentials in argv enthalten. Quelle: https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp
- Keine stillen Zahlungen, Trades oder Ueberweisungen.
- Skills sind Workflows/Anweisungen (progressive disclosure), MCP sind Verbindungen und Tools. Beides kombinieren, nicht verwechseln. Quellen: https://code.claude.com/docs/en/features-overview , https://github.com/ComposioHQ/awesome-claude-skills
- Nur die MCPs/Skills aktivieren, die die Aufgabe braucht. Hermes filtert per include/exclude; OpenClaw hat Tool-Policy und Prompt-Budgets. Quellen: https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp , https://docs.openclaw.ai/skills/
- Schreiben, Senden, Bezahlen, Deployen und Löschen nur nach expliziter Freigabe; gute Document-Skills verlangen einen Verify-Schritt (Datei erneut lesen, PDF/PNG rendern).

## Quellen

- https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp
- https://clawhubtrends.com/leaderboard.html
- https://github.com/NousResearch/hermes-agent/tree/main/optional-mcps/robinhood
- https://github.com/NousResearch/hermes-agent/tree/main/optional-mcps/twelve-data
- https://github.com/punkpeye/awesome-mcp-servers
- https://hermes-agent.nousresearch.com/docs/reference/skills-catalog
- https://docs.openclaw.ai/skills/
- https://github.com/NousResearch/hermes-agent
