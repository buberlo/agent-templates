# Fine-tuning

- **Domain:** `ai-ops`
- **Category:** 'fine-tuning'
- **As of:** 2026-11-23

## Summary

Retrain models on their own data (Axolotl and comparable toolchains).

## Recommended tool stack

- Hermes names Axolotl as slash example in the skills documentary

MCP servers and skills

| Name | Type | URL | Use | Install | Popularity | Source | Unverified |
|---|---|---|---|---|---|---|---|
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
| Axolotl (in Hermes Skills documentary as a slash example) | Skill / Toolchain | https://hermes-agent.nousresearch.com/docs/user-guide/features/skills | The official skills page mentions /axolotl help me fine-tune Llama 3 on my dataset as an example of use. Whether the skill is bundled or hub-installed, check the system with hermes skills list. | According to Docs Slash-Command /axolotl after installation. | Mentioned in the feature documentary, not listed in the Bundled Catalog table of this research. | https://hermes-agent.nousresearch.com/docs/user-guide/features/skills | yes, marked |

Typical workflows

- Clarify record rights, baseline eval, small run, evale again.

## Pitfalls

- Skills are workflows/instructions (progressive disclosure), MCP are connections and tools. Combine the two, not confuse them. Sources: https://code.claude.com/docs/en/features-overview https://github.com/ComposioHQ/awesome-claude-skills
Activate only the MCPs/Skills that the task needs. Hermes filters per include/exclude; OpenClaw has tool policy and prompt budgets. Sources: https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp
- Do not write tokens or passwords in chat, skill files or command arguments of custom MCPs. Grok bot wiki: OAuth tokens remain on the connector backend; Command servers must not contain credentials in argv. Source: https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp
- Write, send, pay, deploy and delete only after explicit approval; good document skills require a Verify step (re-read file, render PDF/PNG).

## Sources

- https://hermes-agent.nousresearch.com/docs/user-guide/features/skills
- https://github.com/punkpeye/awesome-mcp-servers
- https://hermes-agent.nousresearch.com/docs/reference/skills-catalog
- https://docs.openclaw.ai/skills/
- https://github.com/NousResearch/hermes-agent
