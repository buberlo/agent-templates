# Code-Review

- **Domain:** `software-development`
- **Category:** `code-review`
- **As of:** 2026-11-23

## Summary

Review PRs and diffs, apply security and quality gates.

## Recommended tool stack

- gh/GitHub MCP + Review-Skills
- Semgrep optional

## MCP servers and skills

| Name | Type | URL | Use | Install | Popularity | Source | Unverified |
|---|---|---|---|---|---|---|---|
| GitHub Official MCP | MCP | https://github.com/github/github-mcp-server | Repos, issues, PRs, code search, Actions. | Remote, e.g. claude mcp add --transport http github https://api.githubcopilot.com/mcp/ with PAT header (Claude Code docs) or local server from the repo. | 34,686 stars | https://code.claude.com/docs/en/mcp | no (as cited) |
| Hermes skill github / ClawHub Github | Skill + CLI | https://hermes-agent.nousresearch.com/docs/reference/skills-catalog | GitHub via the gh CLI: PRs, issues, reviews, repos, auth. On ClawHub, Github (steipete) is one of the most installed skills. | Hermes: bundled (/github). OpenClaw: openclaw skills install from ClawHub (owner steipete). | ClawHub downloads for Github (steipete): 174,624, 585 registry stars (leaderboard 23 Nov 2026). | https://clawhubtrends.com/leaderboard.html | no (as cited) |
| semgrep MCP (Hermes catalog) | MCP | https://github.com/NousResearch/hermes-agent/tree/main/optional-mcps/semgrep | Static checks in the agent workflow. | hermes mcp install semgrep | Nous-approved optional-mcps catalog entry (listing 23 Nov 2026). | https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp | no (as cited) |
| Hermes-Skill requesting-code-review | Skill | https://hermes-agent.nousresearch.com/docs/reference/skills-catalog | Pre-Commit-Review: Security-Scan, Quality Gates, Auto-Fix. | Bundled software-development/requesting-code-review. | Bundled. | https://hermes-agent.nousresearch.com/docs/reference/skills-catalog | no (as cited) |

## Typical workflows

- Set the task, allowed tools, and definition of done.
- Read or research first, then draft, then request approval for any action that has effects.
- Recheck the output (file, URL, ticket) and cite the source.
- Claude Code docs include the illustrative prompt Review PR #456 and suggest improvements (not a measured real-world result).

## Pitfalls

- Skills are workflows/instructions (progressive disclosure), MCP are connections and tools. Combine the two, not confuse them. Sources: https://code.claude.com/docs/en/features-overview , https://github.com/ComposioHQ/awesome-claude-skills
- Enable only the MCPs/Skills that the task needs. Hermes filters per include/exclude; OpenClaw has tool policy and prompt budgets. Sources: https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp , https://docs.openclaw.ai/skills/
- Do not write tokens or passwords in chat, skill files or command arguments of custom MCPs. Grok Bot wiki: OAuth tokens remain on the connector backend; Command servers must not contain credentials in argv. Source: https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp
- Write, send, pay, deploy and delete only after explicit approval; good document skills require a verify step (read the file again, render PDF/PNG).

## Sources

- https://code.claude.com/docs/en/mcp
- https://hermes-agent.nousresearch.com/docs/reference/skills-catalog
- https://github.com/github/github-mcp-server
- https://clawhubtrends.com/leaderboard.html
- https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp
- https://github.com/NousResearch/hermes-agent/tree/main/optional-mcps/semgrep
- https://github.com/punkpeye/awesome-mcp-servers
- https://docs.openclaw.ai/skills/
- https://github.com/NousResearch/hermes-agent
- https://api.githubcopilot.com/mcp/
- https://code.claude.com/docs/en/features-overview
- https://github.com/ComposioHQ/awesome-claude-skills
- https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp
