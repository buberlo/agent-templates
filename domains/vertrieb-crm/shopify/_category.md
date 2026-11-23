# Shopify

- **Domain:** `vertrieb-crm`
- **Kategorie:** `shopify`
- **Stand:** 2026-11-23

## Kurzbeschreibung

Shopify-Katalog, Bestellungen und Store-Operationen für Agenten.

## Empfohlener Tool-Stack

- Shopify-bezogene MCPs aus awesome-mcp einzeln pruefen (viele inoffiziell oder zahlungspflichtig)

## MCP-Server und Skills

| Name | Typ | URL | Einsatz | Installation | Popularitaet | Quelle | Unverified? |
|---|---|---|---|---|---|---|---|
| forgemeshlabs/shopscout-mcp | MCP | https://github.com/forgemeshlabs/shopscout-mcp | In awesome-mcp als offizieller Eintrag gelistet: Shopify-Katalogsuche, Offer-Ranking, Shipping-Vergleich, x402-Bezahlung pro Call. | Siehe Repo (hosted, kostenpflichtige Calls laut Katalogtext). | Stars hier nicht per API gezogen. | https://github.com/punkpeye/awesome-mcp-servers | ja, markiert |

## Typische Workflows

- Katalog lesen, Preis/Bestand als Report, Aenderungen am Live-Shop nur mit Freigabe.

## Fallstricke

- Skills sind Workflows/Anweisungen (progressive disclosure), MCP sind Verbindungen und Tools. Beides kombinieren, nicht verwechseln. Quellen: https://code.claude.com/docs/en/features-overview , https://github.com/ComposioHQ/awesome-claude-skills
- Nur die MCPs/Skills aktivieren, die die Aufgabe braucht. Hermes filtert per include/exclude; OpenClaw hat Tool-Policy und Prompt-Budgets. Quellen: https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp , https://docs.openclaw.ai/skills/
- Keine Tokens oder Passwörter in Chat, Skill-Dateien oder Command-Argumente von Custom-MCPs schreiben. Grok-Bot-Wiki: OAuth-Tokens bleiben auf dem Connector-Backend; Command-Server dürfen keine Credentials in argv enthalten. Quelle: https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp
- Schreiben, Senden, Bezahlen, Deployen und Löschen nur nach expliziter Freigabe; gute Document-Skills verlangen einen Verify-Schritt (Datei erneut lesen, PDF/PNG rendern).

## Quellen

- https://github.com/punkpeye/awesome-mcp-servers
- https://github.com/forgemeshlabs/shopscout-mcp
- https://hermes-agent.nousresearch.com/docs/reference/skills-catalog
- https://docs.openclaw.ai/skills/
- https://github.com/NousResearch/hermes-agent
