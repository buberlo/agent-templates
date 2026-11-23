# Code-Review

- **Domain:** `software-development`
- **Category:** `code-review`
- **As of:** 2026-11-23

## Summary

Check PRs and diffs, apply security and quality gates.

## Recommended tool stack

- gh/GitHub MCP + Review-Skills
- Semgrep optional

## MCP servers and skills

| Name | Type | URL | Use | Install | Popularity | Source | Unverified |
|---|---|---|---|---|---|---|---|
| GitHub Official MCP | MCP | https://github.com/github/github-mcp-server | Repos, Issues, PRs, Code Search, Actions. | Remote z. B. claude mcp add --transport http github https://api.githubcopilot.com/mcp/ with PAT header (Claude-Code-Docs) or lokaler Server aus dem Repo. | 34.686 Stars | https://code.claude.com/docs/en/mcp | no (as cited) |
| Hermes-Skill github / ClawHub Github | Skill + CLI | https://hermes-agent.nousresearch.com/docs/reference/skills-catalog |GitHub over the gh-CLI: PRs, Issues, Reviews, Repos, Auth. On ClawHub, Github (steipete) is one of the most installed skills.| Hermes: bundled (/github). OpenClaw: openclaw skills install aus ClawHub (Owner steipete). | ClawHub-Downloads Github (steipete): 174.624, 585 Registry-Stars (Leaderboard 23.11.2026). | https://clawhubtrends.com/leaderboard.html | no (as cited) |
| semgrep MCP (Hermes catalog) | MCP | https://github.com/NousResearch/hermes-agent/tree/main/optional-mcps/semgrep | Statische Checks im Agent-Workflow. | hermes mcp install semgrep | Nous-approved optional-mcps catalog entry (listing 2026-11-23). | https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp | no (as cited) |
| Hermes-Skill requesting-code-review | Skill | https://hermes-agent.nousresearch.com/docs/reference/skills-catalog | Pre-Commit-Review: Security-Scan, Quality Gates, Auto-Fix. | Bundled software-development/requesting-code-review. | Bundled. | https://hermes-agent.nousresearch.com/docs/reference/skills-catalog | no (as cited) |

## Typical workflows

- Claude-Code-Docs enthalten den illustrativen Prompt Review PR #456 and suggest improvements (kein gemessenes Praxisergebnis).

## Pitfalls

- Skills are workflows/instructions (progressive disclosure); MCP servers are connections and tools. Combine both; do not conflate them. Sources: https://code.claude.com/docs/en/features-overview , https://github.com/ComposioHQ/awesome-claude-skills
- Enable only the MCPs/skills the task needs. Hermes filters via include/exclude; OpenClaw has tool policy and prompt budgets. Sources: https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp , https://docs.openclaw.ai/skills/
- Do not put tokens or passwords in chat, skill files, or custom MCP command arguments. Grok Bot wiki: OAuth tokens stay on the connector backend; command servers must not pass credentials in argv. Source: https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp
- Write, send, pay, deploy, and delete only after explicit approval; good document skills require a verify step (re-read the file, render PDF/PNG).

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
