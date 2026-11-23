# IaC / Terraform

- **Domain:** `devops-cloud`
- **Category:** `iac-terraform`
- **As of:** 2026-11-23

## Summary

Infrastructure as Code plan, modify and plan/apply upon release.

## Recommended tool stack

- Terraform/OpenTofu CLI in the terminal, plan as review artifact, Apply only with approval

## MCP servers and skills

| Name | Type | URL | Use | Install | Popularity | Source | Unverified |
|---|---|---|---|---|---|---|---|
| Terraform/OpenTofu CLI | CLI | https://www.terraform.io/ | Plan/apply via the terminal tool; no dedicated star MCP established as standard in this research. | Official distribution. | n/a | https://github.com/punkpeye/awesome-mcp-servers | yes, flagged |

## Typical workflows

- plan speichern, Mensch reviewed, erst dann apply.

## Pitfalls

- state-sizes and creds never in the chat or in skills.
- Skills are workflows/instructions (progressive disclosure); MCP servers are connections and tools. Combine both; do not conflate them. Sources: https://code.claude.com/docs/en/features-overview , https://github.com/ComposioHQ/awesome-claude-skills
- Enable only the MCPs/skills the task needs. Hermes filters via include/exclude; OpenClaw has tool policy and prompt budgets. Sources: https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp , https://docs.openclaw.ai/skills/
- Do not put tokens or passwords in chat, skill files, or custom MCP command arguments. Grok Bot wiki: OAuth tokens stay on the connector backend; command servers must not pass credentials in argv. Source: https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp
- Write, send, pay, deploy, and delete only after explicit approval; good document skills require a verify step (re-read the file, render PDF/PNG).

## Sources

- https://github.com/punkpeye/awesome-mcp-servers
- https://www.terraform.io/
- https://hermes-agent.nousresearch.com/docs/reference/skills-catalog
- https://docs.openclaw.ai/skills/
- https://github.com/NousResearch/hermes-agent
