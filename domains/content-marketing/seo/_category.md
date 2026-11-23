# SEO

- **Domain:** `content-marketing`
- **Category:** `seo`
- **As of:** 2026-11-23

## Summary

Technical and content SEO: audits, keywords, on-page, internal linking.

## Recommended tool stack

- Crawler + autorisierte Search-Console-Zugaenge
- Drittskills auf X waren oft Werbung – pruefen

## MCP servers and skills

| Name | Type | URL | Use | Install | Popularity | Source | Unverified |
|---|---|---|---|---|---|---|---|
| Firecrawl MCP | MCP | https://github.com/firecrawl/firecrawl-mcp-server |Web search, scraping and crawling as context for agents.| Official MCP repo, typically npx or hosted according to README. | 7.886 Stars; Upstream 207.417 Stars | https://github.com/firecrawl/firecrawl-mcp-server | no (as cited) |
| Brave Search MCP | MCP | https://github.com/brave/brave-search-mcp-server | Websuche ueber Brave Search API. | Offizielles Brave-Repo. | 1.585 Stars | https://github.com/brave/brave-search-mcp-server | no (as cited) |

## Typical workflows

- Crawl important URLs, issues as a list, fixes as a PR or CMS draft.

## Pitfalls

- Skills are workflows/instructions (progressive disclosure), MCP are connections and tools. Combine the two, not confuse them. Sources: https://code.claude.com/docs/en/features-overview , https://github.com/ComposioHQ/awesome-claude-skills
Activate only the MCPs/Skills that the task needs. Hermes filters per include/exclude; OpenClaw has tool policy and prompt budgets. Sources: https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp
- Do not write tokens or passwords in chat, skill files or command arguments of custom MCPs. Grok-bot-wiki: OAuth tokens remain on the connector backend; In the fore can see for or for fore and for the other. Source: https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp
- write, send, payend, de output and delete only after only after explicit approval; good document skills require a Verify step (read the file again, render PDF/PNG).

## Sources

- https://github.com/firecrawl/firecrawl-mcp-server
- https://x.com/Naruto79z/status/2119108886477033981
- https://github.com/brave/brave-search-mcp-server
- https://github.com/punkpeye/awesome-mcp-servers
- https://hermes-agent.nousresearch.com/docs/reference/skills-catalog
- https://docs.openclaw.ai/skills/
- https://github.com/NousResearch/hermes-agent
