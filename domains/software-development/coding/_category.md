# Coding

- **Domain:** `software-development`
- **Category:** `coding`
- **As of:** 2026-11-23

## Summary

Implement features, fix bugs, modify code in repositories.

## Recommended tool stack

- Agent-native Edit/Terminal + Context7 + GitHub MCP + Tests
- Delegation an Claude Code/Codex wo vorgesehen

## MCP servers and skills

| Name | Type | URL | Use | Install | Popularity | Source | Unverified |
|---|---|---|---|---|---|---|---|
| Context7 | MCP / Plattform | https://github.com/upstash/context7 | Aktuelle, versionsspezifische librarysdokumentation in den Agent-Kontext holen. | Paket @upstash/context7-mcp bzw. Docs im Repo. | 65,314 Stars | https://github.com/upstash/context7 | no (as cited) |
| GitHub Official MCP | MCP | https://github.com/github/github-mcp-server | Repos, issues, PRs, code search, Actions. | Remote, e.g. claude mcp add --transport http github https://api.githubcopilot.com/mcp/ with PAT header (Claude Code docs) or local server from the repo. | 34,686 stars | https://code.claude.com/docs/en/mcp | no (as cited) |
| Hermes skill github / ClawHub Github | Skill + CLI | https://hermes-agent.nousresearch.com/docs/reference/skills-catalog | GitHub via the gh CLI: PRs, issues, reviews, repos, auth. On ClawHub, Github (steipete) is one of the most installed skills. | Hermes: bundled (/github). OpenClaw: openclaw skills install from ClawHub (owner steipete). | ClawHub downloads for Github (steipete): 174,624, 585 registry stars (leaderboard 23 Nov 2026). | https://clawhubtrends.com/leaderboard.html | no (as cited) |
| Hermes-Skills claude-code and codex | Skill (Delegation) | https://hermes-agent.nousresearch.com/docs/reference/skills-catalog | Delegate coding tasks to the Claude Code CLI or the OpenAI Codex CLI. | Bundled autonomous-ai-agents/. | Bundled. | https://hermes-agent.nousresearch.com/docs/reference/skills-catalog | no (as cited) |

## Typical workflows

- Set the task, allowed tools, and definition of done.
- Read or research first, then draft, then request approval for any action that has effects.
- Recheck the output (file, URL, ticket) and cite the source.
- Community-Default-Stack in Posts: Context7, GitHub MCP, Playwright MCP, Chrome DevTools MCP, oft plus Sentry.
- Feature, Akzeptanzkriterien, Testdatei zuerst (Hermes TDD-Skill).

## Pitfalls

- Skills are workflows/instructions (progressive disclosure), MCP are connections and tools. Combine the two, not confuse them. Sources: https://code.claude.com/docs/en/features-overview , https://github.com/ComposioHQ/awesome-claude-skills
- Enable only the MCPs/Skills that the task needs. Hermes filters per include/exclude; OpenClaw has tool policy and prompt budgets. Sources: https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp , https://docs.openclaw.ai/skills/
- Do not write tokens or passwords in chat, skill files or command arguments of custom MCPs. Grok Bot wiki: OAuth tokens remain on the connector backend; Command servers must not contain credentials in argv. Source: https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp
- Write, send, pay, deploy and delete only after explicit approval; good document skills require a verify step (read the file again, render PDF/PNG).
- MCP tool schemas can heavily burden the context even before the first question is asked. In r/ClaudeAI, a user reported 67,000 tokens of overhead. Source: https://www.reddit.com/r/ClaudeAI/comments/1ryz7zp/i_measured_my_mcp_token_overhead_67k_tokens/
- Outdated APIs without Context7/docs MCP.

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
- https://api.githubcopilot.com/mcp/
- https://code.claude.com/docs/en/features-overview
- https://github.com/ComposioHQ/awesome-claude-skills
- https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp
- https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp
