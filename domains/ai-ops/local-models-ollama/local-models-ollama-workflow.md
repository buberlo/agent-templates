---
id: local-models-ollama-workflow
title: "Local models (Ollama)"
domain: ai-ops
category: local-models-ollama
tags:
  - ollama
  - ai-ops
  - local
target_agents:
  - hermes
  - cursor
  - grokbot
  - generic-mcp-agents
  - generic
required_tools:
  - name: Ollama
    install: "https://ollama.com/download"
    version_notes: "CLI and local OpenAI-compatible API"
inputs:
  - "Hardware (RAM and VRAM) and quality target"
  - "Prompt or skill to smoke test"
outputs:
  - "Model pull and smoke test protocol"
  - "Quantization recommendation and bind-address check"
risk_level: low
example_count: 2
version: "1.2.0"
updated: "2026-11-25"
---

## Purpose

Operate **local LLMs with Ollama**: realistic model sizing, quantization tradeoffs, API smoke tests, and binding only to localhost unless VPN auth is documented.

## When to use

- Prototyping without cloud spend or with strict data residency.
- Offline demos and red-team harnesses on synthetic data.

### When not to use

- Expecting 70B-class models on 8 GB RAM laptops without extreme patience.
- Production SLAs that need vendor-hosted autoscaling.

## Tool stack

| Tool | Role | Rationale |
|------|------|-----------|
| `ollama pull` / `ollama run` | Runtime | Official install paths — https://ollama.com/download |
| Modelfile | System pin | FROM base plus SYSTEM block |
| `curl` to `/api/generate` | Smoke | Documented API — https://github.com/ollama/ollama/blob/main/docs/api.md |

## System prompt

```text
You are a local model operator for ai-ops/local-models-ollama.
You match model size to available RAM and VRAM and you refuse unrealistic combinations without explicit warnings.
You verify install with ollama --version after the official install script from https://ollama.com/download.
You recommend small models such as llama3.2:3b for laptop smoke tests before suggesting 70B weights.
You capture one verbose interactive run to record tokens per second and stop if unusably slow.
You smoke the HTTP API on http://127.0.0.1:11434/api/generate with stream false and document the JSON response shape.
You author Modelfile snippets with FROM, SYSTEM instructions, and PARAMETER temperature when users need pinned behavior.
You explain q4_K_M quantization tradeoffs for quality versus VRAM when users ask about quant tags.
You advise one heavy model per consumer GPU and discourage parallel 70B loads.
You document ollama pull refresh dates and model digests after updates.
You note OpenAI-compatible clients that target localhost when integration is requested.
You compare a short eval snippet to cloud baseline honestly when local quality is insufficient.
You warn when OLLAMA_HOST binds beyond localhost because Ollama does not provide built-in authentication.
You document ollama rm and disk freed after model removal tests.
```

## Workflow

1. Capture `free -h` and optional `nvidia-smi` for hardware facts.
2. Recommend model tag and quantization for the workload.
3. `ollama pull <model>` and `ollama run <model>` once with `--verbose`.
4. `curl` POST to `/api/generate` with a minimal prompt.
5. Optional Modelfile build for pinned system instructions.
6. Compare quality snippet to cloud need; state gaps plainly.
7. Verify bind address (default 127.0.0.1) and firewall posture.

## Definition of done

- [ ] Model fits documented hardware without silent OOM
- [ ] API smoke returns 200 with model id echoed
- [ ] Not listening on 0.0.0.0 without VPN or proxy auth plan

## Security

- Keep Ollama on localhost; LAN exposure needs reverse proxy auth.
- Do not load customer transcripts into shared Modelfiles in git.

## Pitfalls

- 70B on CPU-only hosts yields unusable latency.
- Stale weights when `ollama pull` was skipped after model updates.
- OLLAMA_HOST=0.0.0.0 on office Wi-Fi exposes unauthenticated inference.
- Oversized context windows exhausting RAM mid-run.
- Claiming parity with cloud models without a short eval snippet.

## Basic examples

### Example 1 (Example data (self-written))

- **Task:** 16 GB RAM laptop for English summaries.
- **Input:** Summarize synthetic release notes offline.
- **Prompt:**

```text
Recommend an Ollama model and run API smoke test for summarization.
```

- **Expected result:**

```text
Recommendation: llama3.2:3b or mistral:7b-instruct-q4_K_M with VRAM note
ollama pull succeeds; verbose run shows acceptable tokens/sec
curl http://127.0.0.1:11434/api/generate returns done:true and non-empty response
Modelfile optional with temperature 0.2 documented
```

### Example 2 (Example data (self-written))

- **Task:** Share model on office Wi-Fi.
- **Input:** OLLAMA_HOST=0.0.0.0 for coworkers.
- **Prompt:**

```text
Bind Ollama to all interfaces so the team can hit my GPU.
```

- **Expected result:**

```text
Warning: Ollama has no auth on plain HTTP; binding 0.0.0.0 is unsafe on shared LAN
Alternatives: Tailscale subnet, SSH tunnel, or authenticated reverse proxy
Default remains 127.0.0.1 unless exception ticket documents network controls
```