# Fine-Tuning

- **Domain:** `ki-ops`
- **Kategorie:** `fine-tuning`
- **Stand:** 2026-11-23

## Kurzbeschreibung

Modelle auf eigenen Daten nachtrainieren (Axolotl und vergleichbare Toolchains).

## Empfohlener Tool-Stack

- Hermes nennt Axolotl als Slash-Beispiel in der Skills-Doku

## MCP-Server und Skills

| Name | Typ | URL | Einsatz | Installation | Popularitaet | Quelle | Unverified? |
|---|---|---|---|---|---|---|---|
| Axolotl (in Hermes-Skills-Doku als Slash-Beispiel) | Skill / Toolchain | https://hermes-agent.nousresearch.com/docs/user-guide/features/skills | Die offizielle Skills-Seite nennt /axolotl help me fine-tune Llama 3 on my dataset als Nutzungsbeispiel. Ob der Skill bundled oder Hub-installiert ist, am System mit hermes skills list pruefen. | Laut Docs Slash-Command /axolotl nach Installation. | In der Features-Doku erwaehnt, nicht in der Bundled-Catalog-Tabelle dieser Recherche aufgefuehrt. | https://hermes-agent.nousresearch.com/docs/user-guide/features/skills | ja, markiert |

## Typische Workflows

- Datensatz-Rechte klaeren, Baseline-Eval, kleines Run, erneut evalen.

## Fallstricke

- Skills sind Workflows/Anweisungen (progressive disclosure), MCP sind Verbindungen und Tools. Beides kombinieren, nicht verwechseln. Quellen: https://code.claude.com/docs/en/features-overview , https://github.com/ComposioHQ/awesome-claude-skills
- Nur die MCPs/Skills aktivieren, die die Aufgabe braucht. Hermes filtert per include/exclude; OpenClaw hat Tool-Policy und Prompt-Budgets. Quellen: https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp , https://docs.openclaw.ai/skills/
- Keine Tokens oder Passwörter in Chat, Skill-Dateien oder Command-Argumente von Custom-MCPs schreiben. Grok-Bot-Wiki: OAuth-Tokens bleiben auf dem Connector-Backend; Command-Server dürfen keine Credentials in argv enthalten. Quelle: https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp
- Schreiben, Senden, Bezahlen, Deployen und Löschen nur nach expliziter Freigabe; gute Document-Skills verlangen einen Verify-Schritt (Datei erneut lesen, PDF/PNG rendern).

## Quellen

- https://hermes-agent.nousresearch.com/docs/user-guide/features/skills
- https://github.com/punkpeye/awesome-mcp-servers
- https://hermes-agent.nousresearch.com/docs/reference/skills-catalog
- https://docs.openclaw.ai/skills/
- https://github.com/NousResearch/hermes-agent
