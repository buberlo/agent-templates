# Microsoft 365 admin

- **Domain:** `it-operations-support`
- **Category:** `m365-admin`
- **As of:** 2026-11-23

## Summary

Tenants, licences, Exchange/SharePoint administration via Graph or Admin Centre automation.

## Recommended tool stack

- Microsoft Graph / Admin Center via vetted connectors, least privilege
- Hermes Microsoft Office is not a tenant admin

## MCP servers and skills

| Name | Type | URL | Use | Install | Popularity | Source | Unverified |
|---|---|---|---|---|---|---|---|
| Hermes-Skill microsoft-office | Skill + CLI | https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/productivity/productivity-microsoft-office | docx/pptx/xlsx offline via Python CLIs (python-docx, python-pptx, openpyxl). No Office app required; PDF render only with LibreOffice. | Bundled in Hermes (~/.hermes/skills/), scripts in the skill folder. | Part of the official bundled catalog. | https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/productivity/productivity-microsoft-office | no (as cited) |
| Grok Bot / connectors where Microsoft 365 is offered | Plugin | https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp | Account plugins according to catalogue; admin APIs only if the linked account has them. | Connect apps, admin consent in the tenant. | Product documentation. |https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp | no (as cited) |

## Typical workflows

- Read and report first; never make licence or user changes silently.

## Pitfalls

- Remote access only with consent and a visible session.
- Do not write any tokens or passwords in chats, skill files or command arguments of custom MCPs. Grok Bot Wiki: OAuth tokens remain on the connector backend; command servers must not contain any credentials in argv. Source:https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp
- Skills are workflows/instructions (progressive disclosure); MCPs are connections and tools. Combine both; do not confuse them. Sources: https://code.claude.com/docs/en/features-overview , https://github.com/ComposioHQ/awesome-claude-skills
- Only activate the MCPs/skills that the task needs. Hermes filters by include/exclude; OpenClaw has tool policies and prompt budgets. Sources:https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp , https://docs.openclaw.ai/skills/
- Write, send, pay, deploy, and delete only after explicit approval; good document skills require a verify step (re-read file, render PDF/PNG).

## Sources

- https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/productivity/productivity-microsoft-office
- https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp
- https://github.com/punkpeye/awesome-mcp-servers
- https://hermes-agent.nousresearch.com/docs/reference/skills-catalog
- https://docs.openclaw.ai/skills/
- https://github.com/NousResearch/hermes-agent
