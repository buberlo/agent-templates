# Bildgenerierung

- **Domain:** `medien`
- **Kategorie:** `bild-generierung`
- **Stand:** 2026-11-23

## Kurzbeschreibung

Generative Bilder über Modell-APIs, ComfyUI oder eingebaute Image-Tools der Agent-Plattform.

## Empfohlener Tool-Stack

- Plattform-eigene Image-Tools (z. B. Hermes Tool Gateway) oder Comfy/Cloud-MCPs

## MCP-Server und Skills

| Name | Typ | URL | Einsatz | Installation | Popularitaet | Quelle | Unverified? |
|---|---|---|---|---|---|---|---|
| comfy-cloud MCP (Hermes-Katalog) | MCP | https://github.com/NousResearch/hermes-agent/tree/main/optional-mcps/comfy-cloud | Comfy-Cloud aus dem Nous-MCP-Katalog. | hermes mcp install comfy-cloud | Nous-approved optional-mcps-Katalogeintrag (Listing 23.11.2026). | https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp | nein (so belegt) |
| cloudinary MCP (Hermes-Katalog) | MCP | https://github.com/NousResearch/hermes-agent/tree/main/optional-mcps/cloudinary | Medien-Assets ueber Cloudinary. | hermes mcp install cloudinary | Nous-approved optional-mcps-Katalogeintrag (Listing 23.11.2026). | https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp | nein (so belegt) |
| ClawHub „Nano Banana Pro“ (steipete) | Skill | https://clawhubtrends.com/leaderboard.html | Haeufig installiertes Bild-/Generative-Skill auf ClawHub. | openclaw skills install (Owner steipete) und openclaw skills verify. | 95.115 Downloads, 381 Registry-Stars (ClawHub Leaderboard 23.11.2026). | https://clawhubtrends.com/leaderboard.html | nein (so belegt) |

## Typische Workflows

- Prompt + Format + Markenfarben; Ausgabe dateibasiert pruefen.

## Fallstricke

- Skills sind Workflows/Anweisungen (progressive disclosure), MCP sind Verbindungen und Tools. Beides kombinieren, nicht verwechseln. Quellen: https://code.claude.com/docs/en/features-overview , https://github.com/ComposioHQ/awesome-claude-skills
- Nur die MCPs/Skills aktivieren, die die Aufgabe braucht. Hermes filtert per include/exclude; OpenClaw hat Tool-Policy und Prompt-Budgets. Quellen: https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp , https://docs.openclaw.ai/skills/
- Keine Tokens oder Passwörter in Chat, Skill-Dateien oder Command-Argumente von Custom-MCPs schreiben. Grok-Bot-Wiki: OAuth-Tokens bleiben auf dem Connector-Backend; Command-Server dürfen keine Credentials in argv enthalten. Quelle: https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp
- Schreiben, Senden, Bezahlen, Deployen und Löschen nur nach expliziter Freigabe; gute Document-Skills verlangen einen Verify-Schritt (Datei erneut lesen, PDF/PNG rendern).

## Quellen

- https://hermes-agent.nousresearch.com/docs/getting-started/quickstart
- https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp
- https://clawhubtrends.com/leaderboard.html
- https://github.com/NousResearch/hermes-agent/tree/main/optional-mcps/comfy-cloud
- https://github.com/NousResearch/hermes-agent/tree/main/optional-mcps/cloudinary
- https://github.com/punkpeye/awesome-mcp-servers
- https://hermes-agent.nousresearch.com/docs/reference/skills-catalog
- https://docs.openclaw.ai/skills/
- https://github.com/NousResearch/hermes-agent
