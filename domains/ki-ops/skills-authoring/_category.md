# Skills authoring

- **Domain:** `ki-ops`
- **Kategorie:** `skills-authoring`
- **Stand:** 2026-11-23

## Kurzbeschreibung

SKILL.md nach Agent-Skills-Standard schreiben, testen und veröffentlichen.

## Empfohlener Tool-Stack

- SKILL.md nach Agent-Skills-Standard
- OpenClaw Workshop mit Proposal-Review
- Hermes Skill-Dirs

## MCP-Server und Skills

| Name | Typ | URL | Einsatz | Installation | Popularitaet | Quelle | Unverified? |
|---|---|---|---|---|---|---|---|
| Agent Skills Standard / Anthropic skills repo | Standard + Beispiele | https://github.com/anthropics/skills | Frontmatter name/description, progressive disclosure, optionale scripts/references. | Marketplace add / Kopie nach ~/.claude/skills oder ~/.hermes/skills bzw. OpenClaw skills/. | 199.219 Stars | https://code.claude.com/docs/en/skills/ | nein (so belegt) |
| OpenClaw Skill Workshop | Plattform-Feature | https://docs.openclaw.ai/skills/ | Agent entwirft PROPOSAL.md, Mensch reviewed und openclaw skills workshop apply. | Feature-Set u. a. in 2026.6.1-Guides beschrieben; Befehle in der aktuellen CLI pruefen. | 395.081 Stars | https://www.elegantsoftwaresolutions.com/blog/openclaw-skill-workshop-power-user-guide-2026-6-1 | nein (so belegt) |

## Typische Workflows

- Kurze description (OpenClaw rechnet ca. 24 Tokens plus Felder je Skill). Body erst laden wenn noetig.
- Workshop: create → evaluate → apply, nie still auf SKILL.md schreiben lassen.

## Fallstricke

- ClawHub-Skills vor der Nutzung prüfen (`openclaw skills verify`). Im Februar 2026 auditierte Koi Security 2.857 Registry-Skills und bewertete 341 als schadhaft (ca. 12 %). Quellen: https://thehackernews.com/2026/02/researchers-find-341-malicious-clawhub.html , https://docs.openclaw.ai/skills/
- Hermes-Skills mit platforms: [macos] werden unter Linux still übersprungen. Quelle: https://x.com/JayQinQT/status/2120856724668133406
- Zu lange Descriptions sprengen das Skills-Prompt-Budget.
- Skills sind Workflows/Anweisungen (progressive disclosure), MCP sind Verbindungen und Tools. Beides kombinieren, nicht verwechseln. Quellen: https://code.claude.com/docs/en/features-overview , https://github.com/ComposioHQ/awesome-claude-skills
- Nur die MCPs/Skills aktivieren, die die Aufgabe braucht. Hermes filtert per include/exclude; OpenClaw hat Tool-Policy und Prompt-Budgets. Quellen: https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp , https://docs.openclaw.ai/skills/
- Keine Tokens oder Passwörter in Chat, Skill-Dateien oder Command-Argumente von Custom-MCPs schreiben. Grok-Bot-Wiki: OAuth-Tokens bleiben auf dem Connector-Backend; Command-Server dürfen keine Credentials in argv enthalten. Quelle: https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp
- Schreiben, Senden, Bezahlen, Deployen und Löschen nur nach expliziter Freigabe; gute Document-Skills verlangen einen Verify-Schritt (Datei erneut lesen, PDF/PNG rendern).

## Quellen

- https://code.claude.com/docs/en/skills/
- https://docs.openclaw.ai/skills/
- https://hermes-agent.nousresearch.com/docs/user-guide/features/skills
- https://github.com/anthropics/skills
- https://www.elegantsoftwaresolutions.com/blog/openclaw-skill-workshop-power-user-guide-2026-6-1
- https://github.com/punkpeye/awesome-mcp-servers
- https://hermes-agent.nousresearch.com/docs/reference/skills-catalog
- https://github.com/NousResearch/hermes-agent
