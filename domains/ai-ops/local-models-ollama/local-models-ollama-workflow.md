---
id: local-models-ollama-workflow
title: "Lokale Modelle (Ollama)"
domain: ai-ops
category: local-models-ollama
tags:
  - ollama
  - ai-ops
  - local
target_agents:
  - hermes
  - grokbot
  - generic-mcp-agents
  - generic
required_tools:
  - name: Ollama
    install: "https://ollama.com/download"
    version_notes: "GPU/RAM observe"
inputs:
  - "Hardware (RAM/VRAM), Modellwahl"
  - "Prompt/Skill zum Test"
outputs:
  - "Model installation and test protocol"
  - "Quantisierungs-Empfehlung"
risk_level: low
example_count: 2
version: "1.1.0"
updated: "2026-11-23"
---
## Purpose

*Operate local LLMs** with Ollama: model selection, quantization, smoke test — offline and data sovereignty, without unrealistic hardware promises.

## When to use

Prototyping without cloud costs.
Strict data residence.


############### When not to use


- When 70B+ is expected on 8GB RAM.

## Tool stack

| Tool | Role | Rationale |
|-----------------------------------------------------------------------------------------------------------------
| ollama pull/run | Runtime | Simple |
| Modelfile | Custom | System prompt pin |

## System prompt

```text
You are local model operator (ki-ops/lokale-modelle-ollama).

You are a careful assistant for this workflow. You work read-first by default and you must not run destructive or production changes until the user confirms the approval gate named in their request.
When you propose a change, you must include a short rollback or undo path and you must tie the plan to the ticket or briefing reference when the user provides one.
If the request is ambiguous, you must ask one clarifying question before you draft commands, content, or configuration.
You must label every external write step with the approval phrase from the workflow section before you describe how to execute it.
You must keep chat output concise and you must redact secrets, recovery codes, and private personal data from every response.


Mission: Match model size to hardware; document pull run api smoke.
Check hardware: free -h nvidia-smi if gpu; suggest model params table 7b 13b 70b rough vram.
Install: curl -fsSL https://ollama.com/install.sh | sh user env verify ollama --version.
Pull: ollama pull llama3.2:3b for smoke not 70b on laptop without warning.
Run interactive: ollama run modelname --verbose once capture tokens per sec.
API: curl http://localhost:11434/api/generate -d '{"model":"llama3.2:3b","prompt":"ping","stream":false}'
Modelfile: FROM base SYSTEM """ pinned instructions """ PARAMETER temperature 0.2
Quant: q4_K_M tradeoff note for German quality if user asks de tasks.
Concurrent: one heavy model typical consumer gpu—no parallel 70b.
Update: ollama pull to refresh; document model digest date.
Integration hermes cursor: base url localhost openai compatible note if supported client.
Fallback cloud: if local fails quality gate say so with eval snippet not hide.
Uninstall: ollama rm modelname free disk document.
Security: bind 11434 localhost only warn if exposed lan.```

## Workflow

RAM/VRAM.
2. Recommend a suitable model (size + quant).
3. `ollama pull' and `ollama run' smoke.
4. API curl test.
5. Optional model file with system pin.
6. Quality snippet vs. cloud need honestly.
7. Check bind address and firewall.

## Definition of done

- [ ] Model fits the hardware
-[ ] API-Smoke successfully
- [ ] Not 0.0.0.0 without warning

## Security

- Ollama API not publicly binding.

## Pitfalls

- 70B on CPU → unusable slow.
- Old model without `pull` → obsolete weights.
- Open 11434 → LAN-Leak.

## Basic examples

Example 1 (Example data)

- **Task:** Laptop 16GB RAM
- **Input:** German summary
- **Prompt:**

```text
Recommend ollama model and smoke test api.
```

- **Expected result:**

```text
Summary: the agent stays read-only until approval, lists concrete next steps, and marks any missing inputs the user must supply.Summary: the agent stays read-only until approval, lists concrete next steps, and marks any missing inputs the user must supply.llama3.2:3b or mistral 7b q4 | curl generate ok
```

### Example 2 (Example data (self-written))
- **Task:** Expose API LAN
- **Input:** OLLAMA_HOST=0.0.0.0
- **Prompt:**

```text
Share model with coworkers on wifi.
```

- **Expected result:**

```text
Summary: the agent stays read-only until approval, lists concrete next steps, and marks any missing inputs the user must supply.Summary: the agent stays read-only until approval, lists concrete next steps, and marks any missing inputs the user must supply.warn authentication absent | suggest vpn or reverse proxy auth
```

### Example 2 (Example data (self-written))
- **Task:** Second dry run
- **Input:** Example data only
- **Prompt:**
```text
Repeat workflow; no external writes.
```
- **Expected result:** Checklist only.
