# Secrets Management

- **Domain:** `security`
- **Kategorie:** `secrets-management`
- **Stand:** 2026-11-23

## Kurzbeschreibung

Geheimnisse erkennen, rotieren, aus Chats fernhalten und in Vaults halten.

## Empfohlener Tool-Stack

- Secret-Scanner, Vault, nie Chat als Speicher

## MCP-Server und Skills

| Name | Typ | URL | Einsatz | Installation | Popularitaet | Quelle | Unverified? |
|---|---|---|---|---|---|---|---|
| Policy: keine Secrets im Prompt | Praxisregel | https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp | Grok-Bot-Wiki: keine Keys in Custom-MCP-Argumenten; Tokens auf Connector-Backend. | Prozess, kein Install. | n/a | https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp | nein (so belegt) |

## Typische Workflows

- Leak gefunden → rotieren, aus Git entfernen, Scanner in CI.

## Fallstricke

- Keine Tokens oder Passwörter in Chat, Skill-Dateien oder Command-Argumente von Custom-MCPs schreiben. Grok-Bot-Wiki: OAuth-Tokens bleiben auf dem Connector-Backend; Command-Server dürfen keine Credentials in argv enthalten. Quelle: https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp
- Keine Angriffs- oder Umgehungsanleitungen in diesen Templates.
- Skills sind Workflows/Anweisungen (progressive disclosure), MCP sind Verbindungen und Tools. Beides kombinieren, nicht verwechseln. Quellen: https://code.claude.com/docs/en/features-overview , https://github.com/ComposioHQ/awesome-claude-skills
- Nur die MCPs/Skills aktivieren, die die Aufgabe braucht. Hermes filtert per include/exclude; OpenClaw hat Tool-Policy und Prompt-Budgets. Quellen: https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp , https://docs.openclaw.ai/skills/
- Schreiben, Senden, Bezahlen, Deployen und Löschen nur nach expliziter Freigabe; gute Document-Skills verlangen einen Verify-Schritt (Datei erneut lesen, PDF/PNG rendern).

## Quellen

- https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp
- https://github.com/punkpeye/awesome-mcp-servers
- https://hermes-agent.nousresearch.com/docs/reference/skills-catalog
- https://docs.openclaw.ai/skills/
- https://github.com/NousResearch/hermes-agent
