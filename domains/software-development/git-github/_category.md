# Git and GitHub

- **Domain:** `software-development`
- **Category:** `git-github`
- **As of:** 2026-11-23

## Summary

Commits, branches, PRs, issues about gh CLI or official GitHub MCP.

## Recommended tool stack

- gh CLI (Skill) and/or Official GitHub MCP
- Read-only wo moeglich

## MCP servers and skills

| Name | Type | URL | Use | Install | Popularity | Source | Unverified |
|---|---|---|---|---|---|---|---|
| GitHub Official MCP | MCP | https://github.com/github/github-mcp-server | Repos, Issues, PRs, Code Search, Actions. | Remote z. B. claude mcp add --transport http github https://api.githubcopilot.com/mcp/ with PAT header (Claude-Code-Docs) or lokaler Server aus dem Repo. | 34.686 Stars | https://code.claude.com/docs/en/mcp | no (as cited) |
| Hermes-Skill github / ClawHub Github | Skill + CLI | https://hermes-agent.nousresearch.com/docs/reference/skills-catalog |GitHub over the gh-CLI: PRs, Issues, Reviews, Repos, Auth. On ClawHub, Github (steipete) is one of the most installed skills.| Hermes: bundled (/github). OpenClaw: openclaw skills install aus ClawHub (Owner steipete). | ClawHub-Downloads Github (steipete): 174.624, 585 Registry-Stars (Leaderboard 23.11.2026). | https://clawhubtrends.com/leaderboard.html | no (as cited) |

## Typical workflows

- Auth unique (gh auth login), then PRs/issues about the skill. Community Tip: Use read-only URLs of the GitHub server.

## Pitfalls

- Fine-grained PAT nur auf noetige Repos. Kein Token in argv bei Grok-Bot-Command-MCPs.
- Skills are workflows/instructions (progressive disclosure); MCP servers are connections and tools. Combine both; do not conflate them. Sources: https://code.claude.com/docs/en/features-overview , https://github.com/ComposioHQ/awesome-claude-skills
- Enable only the MCPs/skills the task needs. Hermes filters via include/exclude; OpenClaw has tool policy and prompt budgets. Sources: https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp , https://docs.openclaw.ai/skills/
- Do not put tokens or passwords in chat, skill files, or custom MCP command arguments. Grok Bot wiki: OAuth tokens stay on the connector backend; command servers must not pass credentials in argv. Source: https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp
- Write, send, pay, deploy, and delete only after explicit approval; good document skills require a verify step (re-read the file, render PDF/PNG).

## Sources

- https://code.claude.com/docs/en/mcp
- https://github.com/github/github-mcp-server
- https://x.com/tooltierai/status/2122012506868584772
- https://clawhubtrends.com/leaderboard.html
- https://hermes-agent.nousresearch.com/docs/reference/skills-catalog
- https://github.com/punkpeye/awesome-mcp-servers
- https://docs.openclaw.ai/skills/
- https://github.com/NousResearch/hermes-agent
