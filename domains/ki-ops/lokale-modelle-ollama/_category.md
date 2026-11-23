# Lokale Modelle / Ollama

- **Domain:** `ki-ops`
- **Kategorie:** `lokale-modelle-ollama`
- **Stand:** 2026-11-23

## Kurzbeschreibung

Lokale LLMs betreiben, quantisieren, Kontext und Persistenz konfigurieren.

## Empfohlener Tool-Stack

- Ollama oder vergleichbare Runtime, ausreichend Kontext, eigene Evals bevor Modelle getauscht werden

## MCP-Server und Skills

| Name | Typ | URL | Einsatz | Installation | Popularitaet | Quelle | Unverified? |
|---|---|---|---|---|---|---|---|
| Ollama (lokal, typisch per CLI statt MCP) | CLI / Runtime | https://ollama.com | Lokale LLMs dienen, oft direkt vom Agenten oder als OpenAI-kompatibler Endpoint. Kein star-geprueftes offizielles Ollama-MCP in dieser Recherche festgehalten. | Installer von ollama.com; Agent-Provider auf lokalen Endpoint zeigen (Hermes: hermes model). | Popularitaet von Ollama selbst hier nicht neu per API gemessen. | https://hermes-agent.nousresearch.com/docs/getting-started/quickstart | ja, markiert |

## Typische Workflows

- Hardware passend waehlen, Kontextlimit und Persistenz setzen, Qualitaet mit eigener Pruefung messen.

## Fallstricke

- Skills sind Workflows/Anweisungen (progressive disclosure), MCP sind Verbindungen und Tools. Beides kombinieren, nicht verwechseln. Quellen: https://code.claude.com/docs/en/features-overview , https://github.com/ComposioHQ/awesome-claude-skills
- Nur die MCPs/Skills aktivieren, die die Aufgabe braucht. Hermes filtert per include/exclude; OpenClaw hat Tool-Policy und Prompt-Budgets. Quellen: https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp , https://docs.openclaw.ai/skills/
- Keine Tokens oder Passwörter in Chat, Skill-Dateien oder Command-Argumente von Custom-MCPs schreiben. Grok-Bot-Wiki: OAuth-Tokens bleiben auf dem Connector-Backend; Command-Server dürfen keine Credentials in argv enthalten. Quelle: https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp
- Schreiben, Senden, Bezahlen, Deployen und Löschen nur nach expliziter Freigabe; gute Document-Skills verlangen einen Verify-Schritt (Datei erneut lesen, PDF/PNG rendern).

## Quellen

- https://hermes-agent.nousresearch.com/docs/getting-started/quickstart
- https://ollama.com
- https://github.com/punkpeye/awesome-mcp-servers
- https://hermes-agent.nousresearch.com/docs/reference/skills-catalog
- https://docs.openclaw.ai/skills/
- https://github.com/NousResearch/hermes-agent
