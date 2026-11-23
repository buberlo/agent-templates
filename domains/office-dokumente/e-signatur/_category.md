# E-Signatur

- **Domain:** `office-dokumente`
- **Kategorie:** `e-signatur`
- **Stand:** 2026-11-23

## Kurzbeschreibung

Signaturprozesse vorbereiten und Status in Signaturdiensten verfolgen.

## Empfohlener Tool-Stack

- Anbieterspezifische MCPs einzeln pruefen, z. B. SignWell-Eintrag in awesome-mcp

## MCP-Server und Skills

| Name | Typ | URL | Einsatz | Installation | Popularitaet | Quelle | Unverified? |
|---|---|---|---|---|---|---|---|
| Bidsketch/signwell-mcp | MCP | https://github.com/Bidsketch/signwell-mcp | In awesome-mcp-servers (Workplace) als offizieller Eintrag gelistet. | Siehe Repo. | Star-Zahl hier nicht per API gezogen. | https://github.com/punkpeye/awesome-mcp-servers | ja, markiert |

## Typische Workflows

- Nur vorbereiten und Status lesen; Signaturausloesung rechtlich klaeren.

## Fallstricke

- Skills sind Workflows/Anweisungen (progressive disclosure), MCP sind Verbindungen und Tools. Beides kombinieren, nicht verwechseln. Quellen: https://code.claude.com/docs/en/features-overview , https://github.com/ComposioHQ/awesome-claude-skills
- Nur die MCPs/Skills aktivieren, die die Aufgabe braucht. Hermes filtert per include/exclude; OpenClaw hat Tool-Policy und Prompt-Budgets. Quellen: https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp , https://docs.openclaw.ai/skills/
- Keine Tokens oder Passwörter in Chat, Skill-Dateien oder Command-Argumente von Custom-MCPs schreiben. Grok-Bot-Wiki: OAuth-Tokens bleiben auf dem Connector-Backend; Command-Server dürfen keine Credentials in argv enthalten. Quelle: https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp
- Schreiben, Senden, Bezahlen, Deployen und Löschen nur nach expliziter Freigabe; gute Document-Skills verlangen einen Verify-Schritt (Datei erneut lesen, PDF/PNG rendern).

## Quellen

- https://github.com/punkpeye/awesome-mcp-servers
- https://github.com/Bidsketch/signwell-mcp
- https://hermes-agent.nousresearch.com/docs/reference/skills-catalog
- https://docs.openclaw.ai/skills/
- https://github.com/NousResearch/hermes-agent
