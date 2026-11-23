# Claude Code

- **Domain:** `agent-platforms`
- **Category:** `claude-code`
- **As of:** 2026-11-23

## Summary

Skills, MCP, slash commands, delegation, and official Anthropic document skills.

## Recommended tool stack

- Built-in repo tools + skills + MCP via `claude mcp add`
- document-skills for Office

## MCP servers and skills

| Name | Type | URL | Use | Install | Popularity | Source | Unverified |
|---|---|---|---|---|---|---|---|
| Claude Code | CLI agent | https://github.com/anthropics/claude-code | Terminal coding agent, skills, MCP, slash commands. | Official install docs; `claude mcp add --transport http <name> <url>`. | 156,765 stars | https://code.claude.com/docs/en/mcp | no (as documented) |
| Anthropic document skills (docx, pptx, xlsx, pdf) | Skill | https://github.com/anthropics/skills | Official agent skills to create and verify Office and PDF files; verify step (validate.py, render to PDF/PNG) is part of the guide. | Claude Code: `/plugin marketplace add anthropics/skills` and `/plugin install document-skills@anthropic-agent-skills`. | 199,219 stars | https://aifrontierpost.com/articles/anthropic-official-agent-skills-tutorial/ | no (as documented) |
| GitHub Official MCP | MCP | https://github.com/github/github-mcp-server | Repos, issues, PRs, code search, Actions. | Remote e.g. `claude mcp add --transport http github https://api.githubcopilot.com/mcp/` with PAT header (Claude Code docs) or local server from the repo. | 34,686 stars | https://code.claude.com/docs/en/mcp | no (as documented) |
| Context7 | MCP / platform | https://github.com/upstash/context7 | Pull current, version-specific library docs into agent context. | Package `@upstash/context7-mcp` or docs in the repo. | 65,314 stars | https://github.com/upstash/context7 | no (as documented) |
| Playwright MCP | MCP | https://github.com/microsoft/playwright-mcp | Local browser automation via accessibility snapshots, UI tests, and interaction with web apps. | `npx @playwright/mcp@latest` (official docs/repo). | 40,040 stars | https://playwright.dev/mcp/introduction | no (as documented) |

## Typical workflows

- Skill lives in `~/.claude/skills` or project `.claude/skills` or the plugin marketplace.
- Add MCP only when you would otherwise copy data from other tools (official guidance).

## Pitfalls

- MCP tool schemas can heavily burden context before the first question. In r/ClaudeAI one user reported 67,000 tokens of overhead. Source: https://www.reddit.com/r/ClaudeAI/comments/1ryz7zp/i_measured_my_mcp_token_overhead_67k_tokens/
- Skills are workflows/instructions (progressive disclosure); MCPs are connections and tools. Combine both; do not confuse them. Sources: https://code.claude.com/docs/en/features-overview , https://github.com/ComposioHQ/awesome-claude-skills
- MCP servers with external content: prompt-injection risk (Claude Code docs warning).
- Enable only the MCPs/skills the task needs. Hermes filters via include/exclude; OpenClaw has tool policy and prompt budgets. Sources: https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp , https://docs.openclaw.ai/skills/
- Do not put tokens or passwords in chat, skill files, or custom MCP command arguments. Grok Bot wiki: OAuth tokens stay on the connector backend; command servers must not put credentials in argv. Source: https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp
- Write, send, pay, deploy, and delete only after explicit approval; good document skills require a verify step (re-read file, render PDF/PNG).

## Sources

- https://code.claude.com/docs/en/mcp
- https://code.claude.com/docs/en/skills/
- https://code.claude.com/docs/en/features-overview
- https://aifrontierpost.com/articles/anthropic-official-agent-skills-tutorial/
- https://www.reddit.com/r/ClaudeAI/comments/1ryz7zp/i_measured_my_mcp_token_overhead_67k_tokens/
- https://github.com/anthropics/claude-code
- https://github.com/anthropics/skills
- https://github.com/github/github-mcp-server
- https://github.com/upstash/context7
- https://playwright.dev/mcp/introduction
- https://github.com/microsoft/playwright-mcp
- https://agentspulse.github.io/tutorials/claude-powerpoint-skill/
- https://github.com/punkpeye/awesome-mcp-servers
- https://hermes-agent.nousresearch.com/docs/reference/skills-catalog
- https://docs.openclaw.ai/skills/
- https://github.com/NousResearch/hermes-agent