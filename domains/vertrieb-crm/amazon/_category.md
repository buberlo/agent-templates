# Amazon

- **Domain:** `vertrieb-crm`
- **Kategorie:** `amazon`
- **Stand:** 2026-11-23

## Kurzbeschreibung

Amazon-Produkt-, Bestell- und Seller-Central-Daten (oft inoffizielle oder Seller-APIs).

## Empfohlener Tool-Stack

- Seller- oder Datenserver sind oft inoffiziell; Login-im-Browser-Varianten besonders vorsichtig behandeln

## MCP-Server und Skills

| Name | Typ | URL | Einsatz | Installation | Popularitaet | Quelle | Unverified? |
|---|---|---|---|---|---|---|---|
| HasData/amazon-mcp | MCP | https://github.com/HasData/amazon-mcp | Katalogeintrag: Produktdaten, Reviews, Seller als JSON. | Siehe Repo (typisch API-Key-Dienst). | Stars hier nicht per API gezogen. | https://github.com/punkpeye/awesome-mcp-servers | ja, markiert |

## Typische Workflows

- Nur Daten ziehen, die der Account oder die API erlaubt.

## Fallstricke

- Inoffiziell, ToS, Credential-Risiko bei Dritt-Logins.
- Skills sind Workflows/Anweisungen (progressive disclosure), MCP sind Verbindungen und Tools. Beides kombinieren, nicht verwechseln. Quellen: https://code.claude.com/docs/en/features-overview , https://github.com/ComposioHQ/awesome-claude-skills
- Nur die MCPs/Skills aktivieren, die die Aufgabe braucht. Hermes filtert per include/exclude; OpenClaw hat Tool-Policy und Prompt-Budgets. Quellen: https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp , https://docs.openclaw.ai/skills/
- Keine Tokens oder Passwörter in Chat, Skill-Dateien oder Command-Argumente von Custom-MCPs schreiben. Grok-Bot-Wiki: OAuth-Tokens bleiben auf dem Connector-Backend; Command-Server dürfen keine Credentials in argv enthalten. Quelle: https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp
- Schreiben, Senden, Bezahlen, Deployen und Löschen nur nach expliziter Freigabe; gute Document-Skills verlangen einen Verify-Schritt (Datei erneut lesen, PDF/PNG rendern).

## Quellen

- https://github.com/punkpeye/awesome-mcp-servers
- https://github.com/HasData/amazon-mcp
- https://hermes-agent.nousresearch.com/docs/reference/skills-catalog
- https://docs.openclaw.ai/skills/
- https://github.com/NousResearch/hermes-agent
