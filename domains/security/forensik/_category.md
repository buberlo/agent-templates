# Forensik (nur autorisiert)

- **Domain:** `security`
- **Kategorie:** `forensik`
- **Stand:** 2026-11-23

## Kurzbeschreibung

Hohe Flughöhe zu forensischen Werkzeugkategorien; keine Anleitungen zur Umgehung oder Ausbeutung.

> Keine Methodik, keine Umgehungsanleitungen.

## Empfohlener Tool-Stack

- Nicht Gegenstand detaillierter Verfahren in dieser Sammlung

## MCP-Server und Skills

_In dieser Recherche wurde kein spezifischer, ausreichend belegter Tool-Eintrag fuer die Kategorie festgehalten. Siehe Domain-Stack und Quellenkataloge._

## Typische Workflows

- Nur in autorisierten Verfahren durch zustaendige Stellen; hier keine Methodik.

## Fallstricke

- Keine forensischen Angriffs- oder Umgehungsverfahren in dieser Datei.
- Keine Angriffs- oder Umgehungsanleitungen in diesen Templates.
- Keine Tokens oder Passwörter in Chat, Skill-Dateien oder Command-Argumente von Custom-MCPs schreiben. Grok-Bot-Wiki: OAuth-Tokens bleiben auf dem Connector-Backend; Command-Server dürfen keine Credentials in argv enthalten. Quelle: https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp
- Skills sind Workflows/Anweisungen (progressive disclosure), MCP sind Verbindungen und Tools. Beides kombinieren, nicht verwechseln. Quellen: https://code.claude.com/docs/en/features-overview , https://github.com/ComposioHQ/awesome-claude-skills
- Nur die MCPs/Skills aktivieren, die die Aufgabe braucht. Hermes filtert per include/exclude; OpenClaw hat Tool-Policy und Prompt-Budgets. Quellen: https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp , https://docs.openclaw.ai/skills/
- Schreiben, Senden, Bezahlen, Deployen und Löschen nur nach expliziter Freigabe; gute Document-Skills verlangen einen Verify-Schritt (Datei erneut lesen, PDF/PNG rendern).

## Quellen

- https://github.com/punkpeye/awesome-mcp-servers
- https://hermes-agent.nousresearch.com/docs/reference/skills-catalog
- https://docs.openclaw.ai/skills/
- https://github.com/NousResearch/hermes-agent
