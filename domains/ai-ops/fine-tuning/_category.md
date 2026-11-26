# Fine-tuning

- **Domain:** `ai-ops`
- **Category:** `fine-tuning`
- **As of:** 2026-11-23

## Summary

Modelle auf eigenen Daten nachtrainieren (Axolotl and vergleichbare Toolchains).

## Recommended tool stack

- Hermes mentions Axolotl as a slash command example in the skills documentation

## MCP servers and skills

| Name | Type | URL | Use | Install | Popularity | Source | Unverified |
|---|---|---|---|---|---|---|---|
| Axolotl (slash example in Hermes skills docs) | Skill / Toolchain | https://hermes-agent.nousresearch.com/docs/user-guide/features/skills | The official skills page cites /axolotl help me fine-tune Llama 3 on my dataset as a usage example. Check on the system with hermes skills list whether the skill is bundled or hub-installed. | Per docs, slash command /axolotl after installation. | Mentioned in the features documentation, not listed in the bundled catalog table of this research. | https://hermes-agent.nousresearch.com/docs/user-guide/features/skills | yes, flagged |

## Typical workflows

- Set the task, allowed tools, and definition of done.
- Read or research first, then draft, then request approval for any action that has effects.
- Recheck the output (file, URL, ticket) and cite the source.
- Clarify dataset rights, run baseline eval, execute small run, re-evaluate.

## Pitfalls

- Skills are workflows/instructions (progressive disclosure), MCP are connections and tools. Combine the two, not confuse them. Sources: https://code.claude.com/docs/en/features-overview , https://github.com/ComposioHQ/awesome-claude-skills
- Enable only the MCPs/Skills that the task needs. Hermes filters per include/exclude; OpenClaw has tool policy and prompt budgets. Sources: https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp , https://docs.openclaw.ai/skills/
- Do not write tokens or passwords in chat, skill files or command arguments of custom MCPs. Grok Bot wiki: OAuth tokens remain on the connector backend; Command servers must not contain credentials in argv. Source: https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp
- Write, send, pay, deploy and delete only after explicit approval; good document skills require a verify step (read the file again, render PDF/PNG).

## Sources

- https://hermes-agent.nousresearch.com/docs/user-guide/features/skills
- https://github.com/punkpeye/awesome-mcp-servers
- https://hermes-agent.nousresearch.com/docs/reference/skills-catalog
- https://docs.openclaw.ai/skills/
- https://github.com/NousResearch/hermes-agent
- https://code.claude.com/docs/en/features-overview
- https://github.com/ComposioHQ/awesome-claude-skills
- https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp
- https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp
