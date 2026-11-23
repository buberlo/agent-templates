# Remote-Support

- **Domain:** `it-betrieb-support`
- **Kategorie:** `remote-support`
- **Stand:** 2026-11-23

## Kurzbeschreibung

Fernwartung mit Einwilligung, z. B. MeshCentral, plus klare Zustimmung und Sichtbarkeit.

## Empfohlener Tool-Stack

- MeshCentral oder vergleichbares Remote-Tool mit ausdruecklicher Zustimmung
- MCP nur mit scoped, ablaufendem Token

## MCP-Server und Skills

| Name | Typ | URL | Einsatz | Installation | Popularitaet | Quelle | Unverified? |
|---|---|---|---|---|---|---|---|
| meshcentral-mcp (EynaExp) | MCP | https://github.com/EynaExp/meshcentral-mcp | Community-MCP fuer MeshCentral: Geraete listen, Befehle, Power-Aktionen. Sehr niedriges Star-Signal – vor Produktion pruefen. Nur mit Einwilligung und scoped Token. | Siehe Repo. | 5 Stars | https://github.com/EynaExp/meshcentral-mcp | nein (so belegt) |
| Tailscale (Netzwerkpfad) | Netzwerk / Docs | https://tailscale.com/docs/develop-with-ai | Tailscale-Docs beschreiben AI-hilfreiche Docs-Anbindungen. MeshCentral-ueber-Tailscale ist in Community-Discussions beschrieben. Das ist ein Netzwerkweg, kein verstecktes Remote. | Tailscale auf Admin- und Server-Seite. | meshcentral-mcp hat nur 5 Stars – experimentell. | https://tailscale.com/docs/develop-with-ai | nein (so belegt) |

## Typische Workflows

- Vor jeder Session: Nutzer informieren, sichtbare Sitzung, Befehle loggen.
- Kein Reset/Firmware an Fremdgeraeten ohne Auftrag.

## Fallstricke

- Community-MCP mit 5 Stars ist kein Produktionsstandard. Immer Consent.
- Remote nur mit Einwilligung und sichtbarer Sitzung.
- Keine Tokens oder Passwörter in Chat, Skill-Dateien oder Command-Argumente von Custom-MCPs schreiben. Grok-Bot-Wiki: OAuth-Tokens bleiben auf dem Connector-Backend; Command-Server dürfen keine Credentials in argv enthalten. Quelle: https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp
- Skills sind Workflows/Anweisungen (progressive disclosure), MCP sind Verbindungen und Tools. Beides kombinieren, nicht verwechseln. Quellen: https://code.claude.com/docs/en/features-overview , https://github.com/ComposioHQ/awesome-claude-skills
- Nur die MCPs/Skills aktivieren, die die Aufgabe braucht. Hermes filtert per include/exclude; OpenClaw hat Tool-Policy und Prompt-Budgets. Quellen: https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp , https://docs.openclaw.ai/skills/
- Schreiben, Senden, Bezahlen, Deployen und Löschen nur nach expliziter Freigabe; gute Document-Skills verlangen einen Verify-Schritt (Datei erneut lesen, PDF/PNG rendern).

## Quellen

- https://github.com/EynaExp/meshcentral-mcp
- https://tailscale.com/docs/develop-with-ai
- https://github.com/punkpeye/awesome-mcp-servers
- https://hermes-agent.nousresearch.com/docs/reference/skills-catalog
- https://docs.openclaw.ai/skills/
- https://github.com/NousResearch/hermes-agent
