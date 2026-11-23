# Technische Dokumentation

- **Domain:** `software-entwicklung`
- **Kategorie:** `tech-docs`
- **Stand:** 2026-11-23

## Kurzbeschreibung

READMEs, API-Docs, Architekturtexte; oft mit Context7 gegen aktuelle Bibliotheksdocs.

## Empfohlener Tool-Stack

- Context7 fuer Library-Docs
- DeepWiki fuer oeffentliche Repos
- MarkItDown

## MCP-Server und Skills

| Name | Typ | URL | Einsatz | Installation | Popularitaet | Quelle | Unverified? |
|---|---|---|---|---|---|---|---|
| Context7 | MCP / Plattform | https://github.com/upstash/context7 | Aktuelle, versionsspezifische Bibliotheksdokumentation in den Agent-Kontext holen. | Paket @upstash/context7-mcp bzw. Docs im Repo. | 65.314 Stars | https://github.com/upstash/context7 | nein (so belegt) |
| MarkItDown | CLI / Bibliothek | https://github.com/microsoft/markitdown | Dateien und Office-Dokumente nach Markdown wandeln – wird in Skills und MCP-Wrappern genutzt. | Python-Paket / Repo. | 197.975 Stars | https://github.com/microsoft/markitdown | nein (so belegt) |
| deepwiki MCP (Hermes-Katalog) | MCP | https://github.com/NousResearch/hermes-agent/tree/main/optional-mcps/deepwiki | Oeffentliche GitHub-Repos befragen. | hermes mcp install deepwiki | Nous-approved optional-mcps-Katalogeintrag (Listing 23.11.2026). | https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp | nein (so belegt) |

## Typische Workflows

- Immer versionsspezifische Docs ziehen, nicht Modellgedaechtnis fuer APIs verwenden.

## Fallstricke

- Skills sind Workflows/Anweisungen (progressive disclosure), MCP sind Verbindungen und Tools. Beides kombinieren, nicht verwechseln. Quellen: https://code.claude.com/docs/en/features-overview , https://github.com/ComposioHQ/awesome-claude-skills
- Nur die MCPs/Skills aktivieren, die die Aufgabe braucht. Hermes filtert per include/exclude; OpenClaw hat Tool-Policy und Prompt-Budgets. Quellen: https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp , https://docs.openclaw.ai/skills/
- Keine Tokens oder Passwörter in Chat, Skill-Dateien oder Command-Argumente von Custom-MCPs schreiben. Grok-Bot-Wiki: OAuth-Tokens bleiben auf dem Connector-Backend; Command-Server dürfen keine Credentials in argv enthalten. Quelle: https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp
- Schreiben, Senden, Bezahlen, Deployen und Löschen nur nach expliziter Freigabe; gute Document-Skills verlangen einen Verify-Schritt (Datei erneut lesen, PDF/PNG rendern).

## Quellen

- https://github.com/upstash/context7
- https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp
- https://github.com/microsoft/markitdown
- https://github.com/NousResearch/hermes-agent/tree/main/optional-mcps/deepwiki
- https://github.com/punkpeye/awesome-mcp-servers
- https://hermes-agent.nousresearch.com/docs/reference/skills-catalog
- https://docs.openclaw.ai/skills/
- https://github.com/NousResearch/hermes-agent
