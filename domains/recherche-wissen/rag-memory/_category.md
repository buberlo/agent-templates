# RAG und Memory

- **Domain:** `recherche-wissen`
- **Kategorie:** `rag-memory`
- **Stand:** 2026-11-23

## Kurzbeschreibung

Langzeitgedächtnis, Wissensgraphen, Vault-Index und Retrieval für Agenten.

## Empfohlener Tool-Stack

- Plattform-Memory oder mem0/Graphiti
- Obsidian/Vault als sichtbarer Store

## MCP-Server und Skills

| Name | Typ | URL | Einsatz | Installation | Popularitaet | Quelle | Unverified? |
|---|---|---|---|---|---|---|---|
| mem0 | Plattform / Memory-Layer | https://github.com/mem0ai/mem0 | Drop-in Long-Term Memory fuer Agenten. | Siehe Repo (SDK; Community-MCPs separat pruefen). | 69.369 Stars | https://github.com/mem0ai/mem0 | nein (so belegt) |
| Graphiti | Knowledge Graph | https://github.com/getzep/graphiti | Echtzeit-Knowledge-Graph fuer Agenten; Community-MCP-Server existieren (Sterne deutlich kleiner als das Kernrepo). | Kernbibliothek laut Repo; MCP-Wrapper separat auf Pflegezustand pruefen. | 33.021 Stars | https://github.com/getzep/graphiti | nein (so belegt) |
| Obsidian-Skills (Hermes bundled, ClawHub steipete) | Skill | https://hermes-agent.nousresearch.com/docs/reference/skills-catalog | Vault lesen, suchen, Notizen anlegen/editieren – haeufiger Memory-/Wissens-Layer. | Hermes bundled /obsidian. OpenClaw: ClawHub-Skill Obsidian (steipete). | ClawHub: 92.458 Downloads, 381 Stars (Leaderboard 23.11.2026). | https://clawhubtrends.com/leaderboard.html | nein (so belegt) |
| ClawHub „Memory Setup“ (jrbobbyhansen-pixel) | Skill | https://clawhubtrends.com/leaderboard.html | Community-Memory-Setup-Skill; vor Nutzung pruefen. | openclaw skills install (Owner jrbobbyhansen-pixel) und openclaw skills verify. | 40.215 Downloads, 122 Registry-Stars (ClawHub Leaderboard 23.11.2026). | https://clawhubtrends.com/leaderboard.html | nein (so belegt) |
| ClawHub „Elite Longterm Memory“ (nextfrontierbuilds) | Skill | https://clawhubtrends.com/leaderboard.html | Haeufig installiertes Memory-Skill; vor Nutzung pruefen. | openclaw skills install (Owner nextfrontierbuilds) und openclaw skills verify. | 57.040 Downloads, 205 Registry-Stars (ClawHub Leaderboard 23.11.2026). | https://clawhubtrends.com/leaderboard.html | nein (so belegt) |

## Typische Workflows

- Wichtige Fakten bewusst persistieren; Memory nicht ungeprueft in Anweisungen uebernehmen.

## Fallstricke

- ClawHub-Skills vor der Nutzung prüfen (`openclaw skills verify`). Im Februar 2026 auditierte Koi Security 2.857 Registry-Skills und bewertete 341 als schadhaft (ca. 12 %). Quellen: https://thehackernews.com/2026/02/researchers-find-341-malicious-clawhub.html , https://docs.openclaw.ai/skills/
- Community-Graphiti-MCPs sind kleiner und teils aelter – Pflegezustand pruefen.
- Skills sind Workflows/Anweisungen (progressive disclosure), MCP sind Verbindungen und Tools. Beides kombinieren, nicht verwechseln. Quellen: https://code.claude.com/docs/en/features-overview , https://github.com/ComposioHQ/awesome-claude-skills
- Nur die MCPs/Skills aktivieren, die die Aufgabe braucht. Hermes filtert per include/exclude; OpenClaw hat Tool-Policy und Prompt-Budgets. Quellen: https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp , https://docs.openclaw.ai/skills/
- Keine Tokens oder Passwörter in Chat, Skill-Dateien oder Command-Argumente von Custom-MCPs schreiben. Grok-Bot-Wiki: OAuth-Tokens bleiben auf dem Connector-Backend; Command-Server dürfen keine Credentials in argv enthalten. Quelle: https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp
- Schreiben, Senden, Bezahlen, Deployen und Löschen nur nach expliziter Freigabe; gute Document-Skills verlangen einen Verify-Schritt (Datei erneut lesen, PDF/PNG rendern).

## Quellen

- https://github.com/mem0ai/mem0
- https://github.com/getzep/graphiti
- https://clawhubtrends.com/leaderboard.html
- https://hermes-agent.nousresearch.com/docs/reference/skills-catalog
- https://github.com/punkpeye/awesome-mcp-servers
- https://docs.openclaw.ai/skills/
- https://github.com/NousResearch/hermes-agent
