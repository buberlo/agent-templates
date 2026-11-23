# Desktop-Automation

- **Domain:** `automatisierung`
- **Kategorie:** `desktop-automation`
- **Stand:** 2026-11-23

## Kurzbeschreibung

Computer-Use, OS-Automation, kontrollierte GUI-Steuerung.

## Empfohlener Tool-Stack

- Hermes computer-use Skill
- OS-Automation restriktiv

## MCP-Server und Skills

| Name | Typ | URL | Einsatz | Installation | Popularitaet | Quelle | Unverified? |
|---|---|---|---|---|---|---|---|
| Hermes-Skill computer-use | Skill | https://hermes-agent.nousresearch.com/docs/reference/skills-catalog | Desktop background-first steuern, bei Signal eskalieren. | Bundled autonomous-ai-agents/computer-use. | Bundled. | https://hermes-agent.nousresearch.com/docs/reference/skills-catalog | nein (so belegt) |
| ClawHub „Desktop Control“ (matagul) | Skill | https://clawhubtrends.com/leaderboard.html | Im Leaderboard mit Warnmarkierung, besonders sorgfaeltig verifizieren. Im Leaderboard mit Warnmarkierung – vor Nutzung verifizieren. | openclaw skills install (Owner matagul) und openclaw skills verify. | 53.032 Downloads, 335 Registry-Stars (ClawHub Leaderboard 23.11.2026). | https://clawhubtrends.com/leaderboard.html | nein (so belegt) |

## Typische Workflows

- Kleine, beobachtbare GUI-Schritte; bei Unklarheit stoppen.

## Fallstricke

- ClawHub-Skills vor der Nutzung prüfen (`openclaw skills verify`). Im Februar 2026 auditierte Koi Security 2.857 Registry-Skills und bewertete 341 als schadhaft (ca. 12 %). Quellen: https://thehackernews.com/2026/02/researchers-find-341-malicious-clawhub.html , https://docs.openclaw.ai/skills/
- Desktop-Control hat weitreichende Rechte.
- Nur die MCPs/Skills aktivieren, die die Aufgabe braucht. Hermes filtert per include/exclude; OpenClaw hat Tool-Policy und Prompt-Budgets. Quellen: https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp , https://docs.openclaw.ai/skills/
- Skills sind Workflows/Anweisungen (progressive disclosure), MCP sind Verbindungen und Tools. Beides kombinieren, nicht verwechseln. Quellen: https://code.claude.com/docs/en/features-overview , https://github.com/ComposioHQ/awesome-claude-skills
- Keine Tokens oder Passwörter in Chat, Skill-Dateien oder Command-Argumente von Custom-MCPs schreiben. Grok-Bot-Wiki: OAuth-Tokens bleiben auf dem Connector-Backend; Command-Server dürfen keine Credentials in argv enthalten. Quelle: https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp
- Schreiben, Senden, Bezahlen, Deployen und Löschen nur nach expliziter Freigabe; gute Document-Skills verlangen einen Verify-Schritt (Datei erneut lesen, PDF/PNG rendern).

## Quellen

- https://hermes-agent.nousresearch.com/docs/reference/skills-catalog
- https://clawhubtrends.com/leaderboard.html
- https://github.com/punkpeye/awesome-mcp-servers
- https://docs.openclaw.ai/skills/
- https://github.com/NousResearch/hermes-agent
