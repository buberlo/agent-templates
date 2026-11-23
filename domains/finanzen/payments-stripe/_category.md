# Payments (Stripe u. a.)

- **Domain:** `finanzen`
- **Kategorie:** `payments-stripe`
- **Stand:** 2026-11-23

## Kurzbeschreibung

Zahlungsprovider, Kunden, Produkte und Abos über offizielle Toolkits/MCPs.

## Empfohlener Tool-Stack

- Offizielles Stripe Agent Toolkit / Hermes-Katalog stripe
- Keine Live-Charges ohne Freigabe

## MCP-Server und Skills

| Name | Typ | URL | Einsatz | Installation | Popularitaet | Quelle | Unverified? |
|---|---|---|---|---|---|---|---|
| Stripe Agent Toolkit | Toolkit / MCP-faehig | https://github.com/Stripe/agent-toolkit | Offizielle Werkzeuge, um Stripe in AI-Produkte und Agenten einzubinden. | Siehe Repo; in Hermes optional-mcps: stripe. | 2.083 Stars | https://github.com/Stripe/agent-toolkit | nein (so belegt) |
| paypal MCP (Hermes-Katalog) | MCP | https://github.com/NousResearch/hermes-agent/tree/main/optional-mcps/paypal | PayPal aus dem Nous-Katalog. | hermes mcp install paypal | Nous-approved optional-mcps-Katalogeintrag (Listing 23.11.2026). | https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp | nein (so belegt) |
| square MCP (Hermes-Katalog) | MCP | https://github.com/NousResearch/hermes-agent/tree/main/optional-mcps/square | Square aus dem Nous-Katalog. | hermes mcp install square | Nous-approved optional-mcps-Katalogeintrag (Listing 23.11.2026). | https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp | nein (so belegt) |

## Typische Workflows

- Testdaten/Sandbox zuerst, Live nur mit explizitem Auftrag und Limits.

## Fallstricke

- Refunds und Payouts sind irreversibel sichtbar.
- Keine Tokens oder Passwörter in Chat, Skill-Dateien oder Command-Argumente von Custom-MCPs schreiben. Grok-Bot-Wiki: OAuth-Tokens bleiben auf dem Connector-Backend; Command-Server dürfen keine Credentials in argv enthalten. Quelle: https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp
- Keine stillen Zahlungen, Trades oder Ueberweisungen.
- Skills sind Workflows/Anweisungen (progressive disclosure), MCP sind Verbindungen und Tools. Beides kombinieren, nicht verwechseln. Quellen: https://code.claude.com/docs/en/features-overview , https://github.com/ComposioHQ/awesome-claude-skills
- Nur die MCPs/Skills aktivieren, die die Aufgabe braucht. Hermes filtert per include/exclude; OpenClaw hat Tool-Policy und Prompt-Budgets. Quellen: https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp , https://docs.openclaw.ai/skills/
- Schreiben, Senden, Bezahlen, Deployen und Löschen nur nach expliziter Freigabe; gute Document-Skills verlangen einen Verify-Schritt (Datei erneut lesen, PDF/PNG rendern).

## Quellen

- https://github.com/Stripe/agent-toolkit
- https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp
- https://github.com/NousResearch/hermes-agent/tree/main/optional-mcps/paypal
- https://github.com/NousResearch/hermes-agent/tree/main/optional-mcps/square
- https://github.com/punkpeye/awesome-mcp-servers
- https://hermes-agent.nousresearch.com/docs/reference/skills-catalog
- https://docs.openclaw.ai/skills/
- https://github.com/NousResearch/hermes-agent
