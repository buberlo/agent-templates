# Coding

- **Domain:** `software-development`
- **Category:** `coding`
- **As of:** 2026-11-23

## Summary

Implement features, fix bugs, change code in repositories.

## Recommended tool stack

- Agent-native Edit/Terminal + Context7 + GitHub MCP + Tests
- Delegation an Claude Code/Codex wo vorgesehen

## MCP servers and skills

| Name | Type | URL | Use | Install | Popularity | Source | Unverified |
|---|---|---|---|---|---|---|---|
| Context7 | MCP / Plattform | https://github.com/upstash/context7 | Aktuelle, versionsspezifische Bibliotheksdokumentation in den Agent-Kontext holen. | Paket @upstash/context7-mcp bzw. Docs im Repo. | 65.314 Stars | https://github.com/upstash/context7 | no (as cited) |
| GitHub Official MCP | MCP | https://github.com/github/github-mcp-server | Repos, Issues, PRs, Code Search, Actions. | Remote z. B. claude mcp add --transport http github https://api.githubcopilot.com/mcp/ with PAT header (Claude-Code-Docs) or lokaler Server aus dem Repo. | 34.686 Stars | https://code.claude.com/docs/en/mcp | no (as cited) |
| Hermes-Skill github / ClawHub Github | Skill + CLI | https://hermes-agent.nousresearch.com/docs/reference/skills-catalog |GitHub over the gh-CLI: PRs, Issues, Reviews, Repos, Auth. On ClawHub, Github (steipete) is one of the most installed skills.| Hermes: bundled (/github). OpenClaw: openclaw skills install aus ClawHub (Owner steipete). | ClawHub-Downloads Github (steipete): 174.624, 585 Registry-Stars (Leaderboard 23.11.2026). | https://clawhubtrends.com/leaderboard.html | no (as cited) |
|Hermes-Skills claude-code and codex| Skill (Delegation) | https://hermes-agent.nousresearch.com/docs/reference/skills-catalog | Coding-Aufgaben an Claude Code CLI bzw. OpenAI Codex CLI delegieren. | Bundled autonomous-ai-agents/. | Bundled. | https://hermes-agent.nousresearch.com/docs/reference/skills-catalog | no (as cited) |

## Typical workflows

- Community-Default-Stack in Posts: Context7, GitHub MCP, Playwright MCP, Chrome DevTools MCP, oft plus Sentry.
- Feature, Akzeptanzkriterien, Testdatei zuerst (Hermes TDD-Skill).

## Pitfalls

- MCP tool schemas can put a lot of stress on the context even before the first question comes up. In r/ClaudeAI, a user reported 67,000 token overhead. Source: https://www.reddit.com/r/ClaudeAI/comments/1ryz7zp/i measured my mcp token overhead 67k tokens/
- Veraltete APIs without Context7/Docs-MCP.
- Skills are workflows/instructions (progressive disclosure); MCP servers are connections and tools. Combine both; do not conflate them. Sources: https://code.claude.com/docs/en/features-overview , https://github.com/ComposioHQ/awesome-claude-skills
- Enable only the MCPs/skills the task needs. Hermes filters via include/exclude; OpenClaw has tool policy and prompt budgets. Sources: https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp , https://docs.openclaw.ai/skills/
- Do not put tokens or passwords in chat, skill files, or custom MCP command arguments. Grok Bot wiki: OAuth tokens stay on the connector backend; command servers must not pass credentials in argv. Source: https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp
- Write, send, pay, deploy, and delete only after explicit approval; good document skills require a verify step (re-read the file, render PDF/PNG).

## Sources

- https://github.com/upstash/context7
- https://code.claude.com/docs/en/mcp
- https://x.com/tooltierai/status/2122012506868584772
- https://x.com/AnylancerInc/status/2116384700449149180
- https://github.com/github/github-mcp-server
- https://clawhubtrends.com/leaderboard.html
- https://hermes-agent.nousresearch.com/docs/reference/skills-catalog
- https://github.com/punkpeye/awesome-mcp-servers
- https://docs.openclaw.ai/skills/
- https://github.com/NousResearch/hermes-agent
