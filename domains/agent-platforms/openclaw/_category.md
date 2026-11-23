# OpenClaw

- **Domain:** `agent-platforms`
- **Category:** `opencla w
- **As of:** 2026-11-23

## Summary

Gateway, ClawHub, Skill Workshop, MCP, Android-Companion, Skill-Verify.

## Recommended tool stack

- Gateway auf dem Computer
Skills from Workspace/ClawHub with Verify
- MCP unter mcp.servers + Tool-Policy
- Do not misunderstand companion apps as hosts

## MCP Server and Skills

| Name | Type | URL | Use | Install | Popularity | Source | Unverified |
|---|---|---|---|---|---|---|---|

| OpenClaw | Agent-Plattform | https://github.com/openclaw/openclaw | Self-hosted Gateway, Skills, Plugins, MCP, Kanaele, Android-Companion. | Docs auf docs.openclaw.ai; CLI openclaw skills\|mcp\|plugins. | 395.081 Stars (API 23.11.2026). | https://docs.openclaw.ai/ | no (as cited) |
| ClawHub | Registry | https://github.com/openclaw/clawhub |Public Skill and Plugin Registry, Semver, Downloads, Security Scan Summaries, openclaw skills verify.| openclaw skills install @owner/skill, openclaw plugins install clawhub:<pkg>, optional npm i -g clawhub zum Publizieren. | 9.559 Stars; Site clawhub.ai / docs. | https://docs.openclaw.ai/clawhub | no (as cited) |

## Typical workflows

- Skill Workshop for new procedures (proposal review). MCP add in Settings or CLI. Connect Android via QR to an existing gateway.
- Prompt-Budget: OpenClaw kuerzt Skill-Beschreibungen, wenn skills.limits.maxSkillsPromptChars greift.

## Pitfalls

- Check ClawHub skills before use (`openclaw skills verify`). In February 2026, Koi Security audited 2,857 registry skills and rated 341 as defective (about 12%). Sources: https://thehackernews.com/2026/02/researchers-find-341-malicious-clawhub.html
- Loading-Order kann Workspace-Skills ueber Bundled legen.
- Older .clawdhub metadata is no longer read (rename on .clawhub).
- Leaderboard entries with warning marking and extremely few registry stars are particularly critical despite high downloads.
- Skills are workflows/instructions (progressive disclosure), MCP are connections and tools. Combine the two, not confuse them. Sources: https://code.claude.com/docs/en/features-overview , https://github.com/ComposioHQ/awesome-claude-skills
Activate only the MCPs/Skills that the task needs. Hermes filters per include/exclude; OpenClaw has tool policy and prompt budgets. Sources: https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp
- Do not write tokens or passwords in chat, skill files or command arguments of custom MCPs. Grok bot wiki: OAuth tokens remain on the connector backend; Command servers must not contain credentials in argv. Source: https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp
- Write, send, pay, deploy and delete only after explicit approval; good document skills require a Verify step (re-read file, render PDF/PNG).

## Sources

- https://docs.openclaw.ai/
- https://docs.openclaw.ai/skills/
- https://docs.openclaw.ai/clawhub
- https://docs.openclaw.ai/tools/mcp
- https://docs.openclaw.ai/platforms/android/
- https://clawhubtrends.com/leaderboard.html
- https://thehackernews.com/2026/02/researchers-find-341-malicious-clawhub.html
- https://www.paloaltonetworks.com/blog/security-operations/clawhavoc-ai-agent-skills-poisoning/
- https://github.com/openclaw/openclaw
- https://github.com/openclaw/clawhub
- https://github.com/punkpeye/awesome-mcp-servers
- https://hermes-agent.nousresearch.com/docs/reference/skills-catalog
- https://github.com/NousResearch/hermes-agent
