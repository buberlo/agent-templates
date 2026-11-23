# IaC / Terraform

- **Domain:** `devops-cloud`
- **Kategorie:** `iac-terraform`
- **Stand:** 2026-11-23

## Kurzbeschreibung

Infrastructure as Code planen, ändern und planen/apply nach Freigabe.

## Empfohlener Tool-Stack

- Terraform/OpenTofu CLI im Terminal, Plan als Review-Artefakt, Apply nur mit Freigabe

## MCP-Server und Skills

| Name | Typ | URL | Einsatz | Installation | Popularitaet | Quelle | Unverified? |
|---|---|---|---|---|---|---|---|
| Terraform/OpenTofu CLI | CLI | https://www.terraform.io/ | Plan/Apply ueber das Terminal-Tool; kein spezielles Star-MCP in dieser Recherche als Standard festgehalten. | Offizielle Distribution. | n/a | https://github.com/punkpeye/awesome-mcp-servers | ja, markiert |

## Typische Workflows

- plan speichern, Mensch reviewed, erst dann apply.

## Fallstricke

- State-Dateien und Cloud-Creds nie in den Chat oder in Skills kopieren.
- Skills sind Workflows/Anweisungen (progressive disclosure), MCP sind Verbindungen und Tools. Beides kombinieren, nicht verwechseln. Quellen: https://code.claude.com/docs/en/features-overview , https://github.com/ComposioHQ/awesome-claude-skills
- Nur die MCPs/Skills aktivieren, die die Aufgabe braucht. Hermes filtert per include/exclude; OpenClaw hat Tool-Policy und Prompt-Budgets. Quellen: https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp , https://docs.openclaw.ai/skills/
- Keine Tokens oder Passwörter in Chat, Skill-Dateien oder Command-Argumente von Custom-MCPs schreiben. Grok-Bot-Wiki: OAuth-Tokens bleiben auf dem Connector-Backend; Command-Server dürfen keine Credentials in argv enthalten. Quelle: https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp
- Schreiben, Senden, Bezahlen, Deployen und Löschen nur nach expliziter Freigabe; gute Document-Skills verlangen einen Verify-Schritt (Datei erneut lesen, PDF/PNG rendern).

## Quellen

- https://github.com/punkpeye/awesome-mcp-servers
- https://www.terraform.io/
- https://hermes-agent.nousresearch.com/docs/reference/skills-catalog
- https://docs.openclaw.ai/skills/
- https://github.com/NousResearch/hermes-agent
