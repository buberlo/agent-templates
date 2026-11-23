# CI/CD

- **Domain:** `devops-cloud`
- **Category:** `cicd`
- **As of:** 2026-11-23

## Summary

Pipelines (GitHub Actions, GitLab CI, CircleCI, Buildkite) read, adjust and analyze errors.

## Recommended tool stack

- GitHub MCP/Actions, CircleCI/Buildkite aus Hermes catalog

## MCP servers and skills

| Name | Type | URL | Use | Install | Popularity | Source | Unverified |
|---|---|---|---|---|---|---|---|
| GitHub Official MCP | MCP | https://github.com/github/github-mcp-server | Repos, Issues, PRs, Code Search, Actions. |Remote e.g. claude mcp add --transport http github https://api.githubcopilot.com/mcp/ with PAT header (Claude code docs) or local server from the repo.| 34.686 Stars | https://code.claude.com/docs/en/mcp | no (as documented) |
| circleci MCP (Hermes catalog) | MCP | https://github.com/NousResearch/hermes-agent/tree/main/optional-mcps/circleci | CircleCI aus dem Nous-catalog. | hermes mcp install circleci | Nous-approved optional-mcps catalog entry (listing 2026-11-23). | https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp | no (as documented) |
| buildkite MCP (Hermes catalog) | MCP | https://github.com/NousResearch/hermes-agent/tree/main/optional-mcps/buildkite | Buildkite aus dem Nous-catalog. | hermes mcp install buildkite | Nous-approved optional-mcps catalog entry (listing 2026-11-23). | https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp | no (as documented) |

## Typical workflows

- Log of failed jobs pick, locally reproduce, fix as PR.

## Pitfalls

- Never mirror pipeline secrets into chat.
- Skills are workflows/instructions (progressive disclosure); MCP servers are connections and tools. Combine both; do not conflate them. Sources: https://code.claude.com/docs/en/features-overview , https://github.com/ComposioHQ/awesome-claude-skills
- Enable only the MCPs/skills the task needs. Hermes filters via include/exclude; OpenClaw has tool policy and prompt budgets. Sources: https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp , https://docs.openclaw.ai/skills/
- Do not put tokens or passwords in chat, skill files, or custom MCP command arguments. Grok Bot wiki: OAuth tokens stay on the connector backend; command servers must not pass credentials in argv. Source: https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp
- Write, send, pay, deploy, and delete only after explicit approval; good document skills require a verify step (re-read the file, render PDF/PNG).

## Sources

- https://code.claude.com/docs/en/mcp
- https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp
- https://github.com/github/github-mcp-server
- https://github.com/NousResearch/hermes-agent/tree/main/optional-mcps/circleci
- https://github.com/NousResearch/hermes-agent/tree/main/optional-mcps/buildkite
- https://github.com/punkpeye/awesome-mcp-servers
- https://hermes-agent.nousresearch.com/docs/reference/skills-catalog
- https://docs.openclaw.ai/skills/
- https://github.com/NousResearch/hermes-agent
