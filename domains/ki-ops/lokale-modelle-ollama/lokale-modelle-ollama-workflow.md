---
id: lokale-modelle-ollama-workflow
title: "Lokale Modelle (Ollama)"
domain: ki-ops
category: lokale-modelle-ollama
tags:
  - ollama
  - ki-ops
  - local
target_agents:
  - hermes
  - grokbot
  - generic-mcp-agents
  - generic
required_tools:
  - name: Ollama
    install: "https://ollama.com/download"
    version_notes: "GPU/RAM beachten"
inputs:
  - "Hardware (RAM/VRAM), Modellwahl"
  - "Prompt/Skill zum Test"
outputs:
  - "Modell-Install- und Testprotokoll"
  - "Quantisierungs-Empfehlung"
risk_level: low
example_count: 2
version: "1.1.0"
updated: "2026-11-23"
---

## Zweck

**Lokale LLMs** mit Ollama betreiben: Modellwahl, Quantisierung, Smoke-Test — Offline und datensouverän, ohne unrealistiche Hardware-Versprechen.

## Wann nutzen

- Prototyping ohne Cloud-Kosten.
- Strikte Datenresidenz.

**Wann nicht**

- Wenn 70B+ auf 8GB RAM erwartet wird.

## Tool-Stack

| Tool | Rolle | Begründung |
|------|-------|------------|
| ollama pull/run | Runtime | Einfach |
| Modelfile | Custom | System prompt pin |

## System-Prompt / Instruktionen

```text
Role: local model operator (ki-ops/lokale-modelle-ollama).
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
Security: bind 11434 localhost only warn if exposed lan.
```

## Arbeitsablauf

1. RAM/VRAM erfassen.
2. Passendes Modell empfehlen (Größe + Quant).
3. `ollama pull` und `ollama run` Smoke.
4. API-Curl-Test.
5. Optional Modelfile mit System-Pin.
6. Qualitäts-Snippet vs. Cloud-Bedarf ehrlich.
7. Bind-Adresse und Firewall prüfen.

## Qualitätskriterien / Definition of Done

- [ ] Modell passt zur Hardware
- [ ] API-Smoke erfolgreich
- [ ] Nicht 0.0.0.0 ohne Warnung

## Sicherheit & Freigaben

- Ollama-API nicht öffentlich binden.

## Fallstricke

- 70B auf CPU → unbenutzbar langsam.
- Altes Modell ohne `pull` → veraltete Weights.
- Offenes 11434 → LAN-Leak.

## Grundbeispiele

### Beispiel 1 (Beispieldaten)

- **Aufgabe:** Laptop 16GB RAM
- **Input:** deutsche Zusammenfassung
- **Prompt:**

```text
Recommend ollama model and smoke test api.
```

- **Erwartetes Ergebnis:**

```text
llama3.2:3b or mistral 7b q4 | curl generate ok
```

### Beispiel 2 (Beispieldaten)

- **Aufgabe:** Expose API LAN
- **Input:** OLLAMA_HOST=0.0.0.0
- **Prompt:**

```text
Share model with coworkers on wifi.
```

- **Erwartetes Ergebnis:**

```text
warn authentication absent | suggest vpn or reverse proxy auth
```