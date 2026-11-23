# Backend und APIs

- **Domain:** `software-entwicklung`
- **Kategorie:** `backend-apis`
- **Stand:** 2026-11-23

## Kurzbeschreibung

Services, APIs, Auth und serverseitige Logik.

## Empfohlener Tool-Stack

- Repo-Tools + Context7 + DB-MCP im Read-only wo moeglich

## MCP-Server und Skills

| Name | Typ | URL | Einsatz | Installation | Popularitaet | Quelle | Unverified? |
|---|---|---|---|---|---|---|---|
| Context7 | MCP / Plattform | https://github.com/upstash/context7 | Aktuelle, versionsspezifische Bibliotheksdokumentation in den Agent-Kontext holen. | Paket @upstash/context7-mcp bzw. Docs im Repo. | 65.314 Stars | https://github.com/upstash/context7 | nein (so belegt) |
| supabase MCP (Hermes-Katalog) | MCP | https://github.com/NousResearch/hermes-agent/tree/main/optional-mcps/supabase | Projekte/SQL; Community empfiehlt Read-only-Mode. Hosted-URL in Drittrepos mcp.supabase.com – Repo supabase/supabase-mcp war per API 404. | hermes mcp install supabase | Nous-approved optional-mcps-Katalogeintrag (Listing 23.11.2026). | https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp | nein (so belegt) |
| Sentry MCP | MCP | https://github.com/getsentry/sentry-mcp | Produktionsfehler, Issues und Kontext fuer Coding-Agenten. | Offizielles getsentry/sentry-mcp Repo. | 973 Stars | https://github.com/getsentry/sentry-mcp | nein (so belegt) |

## Typische Workflows

- API-Vertrag zuerst, dann Implementation und Tests.

## Fallstricke

- Destructive SQL durch DB-MCPs – Read-only-Mode bevorzugen.
- Skills sind Workflows/Anweisungen (progressive disclosure), MCP sind Verbindungen und Tools. Beides kombinieren, nicht verwechseln. Quellen: https://code.claude.com/docs/en/features-overview , https://github.com/ComposioHQ/awesome-claude-skills
- Nur die MCPs/Skills aktivieren, die die Aufgabe braucht. Hermes filtert per include/exclude; OpenClaw hat Tool-Policy und Prompt-Budgets. Quellen: https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp , https://docs.openclaw.ai/skills/
- Keine Tokens oder Passwörter in Chat, Skill-Dateien oder Command-Argumente von Custom-MCPs schreiben. Grok-Bot-Wiki: OAuth-Tokens bleiben auf dem Connector-Backend; Command-Server dürfen keine Credentials in argv enthalten. Quelle: https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp
- Schreiben, Senden, Bezahlen, Deployen und Löschen nur nach expliziter Freigabe; gute Document-Skills verlangen einen Verify-Schritt (Datei erneut lesen, PDF/PNG rendern).

## Quellen

- https://x.com/tooltierai/status/2122012506868584772
- https://github.com/upstash/context7
- https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp
- https://github.com/NousResearch/hermes-agent/tree/main/optional-mcps/supabase
- https://github.com/getsentry/sentry-mcp
- https://github.com/punkpeye/awesome-mcp-servers
- https://hermes-agent.nousresearch.com/docs/reference/skills-catalog
- https://docs.openclaw.ai/skills/
- https://github.com/NousResearch/hermes-agent
