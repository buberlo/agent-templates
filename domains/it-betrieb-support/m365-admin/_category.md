# Microsoft 365 Admin

- **Domain:** `it-betrieb-support`
- **Kategorie:** `m365-admin`
- **Stand:** 2026-11-23

## Kurzbeschreibung

Tenants, Lizenzen, Exchange/SharePoint-Administration über Graph oder Admin-Center-Automatisierung.

## Empfohlener Tool-Stack

- Microsoft Graph / Admin Center ueber gepruefte Connectoren, Least Privilege
- Hermes microsoft-office ist nicht Tenant-Admin

## MCP-Server und Skills

| Name | Typ | URL | Einsatz | Installation | Popularitaet | Quelle | Unverified? |
|---|---|---|---|---|---|---|---|
| Hermes-Skill microsoft-office | Skill + CLI | https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/productivity/productivity-microsoft-office | docx/pptx/xlsx offline ueber Python-CLIs (python-docx, python-pptx, openpyxl). Office-App nicht noetig; PDF-Render nur mit LibreOffice. | Bundled in Hermes (~/.hermes/skills/), Scripts im Skill-Ordner. | Teil des offiziellen Bundled-Katalogs. | https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/productivity/productivity-microsoft-office | nein (so belegt) |
| Grok Bot / Connectoren wo Microsoft 365 angeboten wird | Plugin | https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp | Account-Plugins nach Katalog; Admin-APIs nur wenn der verbundene Account sie hat. | Connect Apps, Admin-Consent im Tenant. | Produktdoku. | https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp | nein (so belegt) |

## Typische Workflows

- Lesen und Reporten zuerst; Lizenz- oder User-Aenderungen nie still.

## Fallstricke

- Remote nur mit Einwilligung und sichtbarer Sitzung.
- Keine Tokens oder Passwörter in Chat, Skill-Dateien oder Command-Argumente von Custom-MCPs schreiben. Grok-Bot-Wiki: OAuth-Tokens bleiben auf dem Connector-Backend; Command-Server dürfen keine Credentials in argv enthalten. Quelle: https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp
- Skills sind Workflows/Anweisungen (progressive disclosure), MCP sind Verbindungen und Tools. Beides kombinieren, nicht verwechseln. Quellen: https://code.claude.com/docs/en/features-overview , https://github.com/ComposioHQ/awesome-claude-skills
- Nur die MCPs/Skills aktivieren, die die Aufgabe braucht. Hermes filtert per include/exclude; OpenClaw hat Tool-Policy und Prompt-Budgets. Quellen: https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp , https://docs.openclaw.ai/skills/
- Schreiben, Senden, Bezahlen, Deployen und Löschen nur nach expliziter Freigabe; gute Document-Skills verlangen einen Verify-Schritt (Datei erneut lesen, PDF/PNG rendern).

## Quellen

- https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/productivity/productivity-microsoft-office
- https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp
- https://github.com/punkpeye/awesome-mcp-servers
- https://hermes-agent.nousresearch.com/docs/reference/skills-catalog
- https://docs.openclaw.ai/skills/
- https://github.com/NousResearch/hermes-agent
