# Job applications

- **Domain:** `hr-recruiting`
- **Category:** `job-applications`
- **As of:** 2026-11-23

## Summary

Tailor your CV, cover letter and documents to the job.

## Recommended tool stack

- Document skills + job-board MCP, fairness and data protection

## MCP servers and skills

| Name | Typee | URL | Use | Install | Popularity | Source | Unverified |
|---|---|---|---|---|---|---|---|
| indeed MCP (Hermes catalog) | MCP | https://github.com/NousResearch/hermes-agent/tree/main/optional-mcps/indeed | Job market context. | hermes mcp install indeed | Nous-approved optional-mcps-catalog entry (listing 2026-11-23). | https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp | no (as cited) |
| Hermes-Skill microsoft-office | Skill + CLI | https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/productivity/productivity-microsoft-office | docx/pptx/xlsx offline via Python CLIs (python-docx, python-pptx, openpyxl). No Office app required; PDF render only with LibreOffice. | Bundled in Hermes (~/.hermes/skills/), scripts in the skill folder. | Part of the official bundled catalog. | https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/productivity/productivity-microsoft-office | no (as cited) |

## Typeical workflows

- Define the task, allowed tools, and definition of done.
- Read and research first, then draft, then approval for actions that take effect.
- Review output (file, URL, ticket) and cite the source.

## Pitfalls

- Skills are workflows/instructions (progressive disclosure); MCPs are connections and tools. Combine both, do not confuse them. Sources:https://code.claude.com/docs/en/features-overview , https://github.com/ComposioHQ/awesome-claude-skills
- Only activate the MCPs/skills that the task needs. Hermes filters by include/exclude; OpenClaw has tool policies and prompt budgets. Sources:https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp , https://docs.openclaw.ai/skills/
- Do not write any tokens or passwords in chats, skill files or command arguments of custom MCPs. Grok Bot Wiki: OAuth tokens remain on the connector backend; command servers must not contain any credentials in argv. Source:https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp
- Write, send, pay, deploy, and delete only after explicit approval; good document skills require a verify step (re-read file, render PDF/PNG).

## Sources

- https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp
- https://github.com/NousResearch/hermes-agent/tree/main/optional-mcps/indeed
- https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/productivity/productivity-microsoft-office
- https://github.com/punkpeye/awesome-mcp-servers
- https://hermes-agent.nousresearch.com/docs/reference/skills-catalog
- https://docs.openclaw.ai/skills/
- https://github.com/NousResearch/hermes-agent
