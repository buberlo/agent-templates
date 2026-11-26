# Git and GitHub

- **Domain:** `software-development`
- **Category:** `git-github`
- **As of:** 2026-11-23

## Summary

Commits, branches, PRs, issues via gh CLI or official GitHub MCP.

## Recommended tool stack

- gh CLI (skill) and/or official GitHub MCP
- Read-only wo moeglich

## MCP servers and skills

| Name | Type | URL | Use | Install | Popularity | Source | Unverified |
|---|---|---|---|---|---|---|---|
| GitHub Official MCP | MCP | https://github.com/github/github-mcp-server | Repos, issues, PRs, code search, Actions. | Remote, e.g. claude mcp add --transport http github https://api.githubcopilot.com/mcp/ with PAT header (Claude Code docs) or local server from the repo. | 34,686 stars | https://code.claude.com/docs/en/mcp | no (as cited) |
| Hermes skill github / ClawHub Github | Skill + CLI | https://hermes-agent.nousresearch.com/docs/reference/skills-catalog | GitHub via the gh CLI: PRs, issues, reviews, repos, auth. On ClawHub, Github (steipete) is one of the most installed skills. | Hermes: bundled (/github). OpenClaw: openclaw skills install from ClawHub (owner steipete). | ClawHub downloads for Github (steipete): 174,624, 585 registry stars (leaderboard 23 Nov 2026). | https://clawhubtrends.com/leaderboard.html | no (as cited) |

## Typical workflows

- Set the task, allowed tools, and definition of done.
- Read or research first, then draft, then request approval for any action that has effects.
- Recheck the output (file, URL, ticket) and cite the source.
- Authenticate once (gh auth login), then manage PRs/issues via the skill. Community tip: use read-only URLs of the GitHub server.

## Pitfalls

- Skills are workflows/instructions (progressive disclosure), MCP are connections and tools. Combine the two, not confuse them. Sources: https://code.claude.com/docs/en/features-overview , https://github.com/ComposioHQ/awesome-claude-skills
- Enable only the MCPs/Skills that the task needs. Hermes filters per include/exclude; OpenClaw has tool policy and prompt budgets. Sources: https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp , https://docs.openclaw.ai/skills/
- Do not write tokens or passwords in chat, skill files or command arguments of custom MCPs. Grok Bot wiki: OAuth tokens remain on the connector backend; Command servers must not contain credentials in argv. Source: https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp
- Write, send, pay, deploy and delete only after explicit approval; good document skills require a verify step (read the file again, render PDF/PNG).
- Fine-grained PAT scoped only to necessary repos. No token in argv for Grok Bot command MCPs.

## Sources

- https://code.claude.com/docs/en/mcp
- https://github.com/github/github-mcp-server
- https://x.com/tooltierai/status/2122012506868584772
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
