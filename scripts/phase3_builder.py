from __future__ import annotations


def render_body(
    *,
    zweck: str,
    wann: list[str],
    tools: list[tuple[str, str, str]],
    system_prompt: str,
    steps: list[str],
    dod: list[str],
    safety: list[str],
    pitfalls: list[str],
    examples: list[dict],
) -> str:
    wann_md = "\n".join(f"- {w}" for w in wann)
    tool_md = "\n".join(
        f"| {n} | {r} | {b} |" for n, r, b in tools
    )
    steps_md = "\n".join(f"{i}. {s}" for i, s in enumerate(steps, 1))
    dod_md = "\n".join(f"- [ ] {d}" for d in dod)
    safety_md = "\n".join(f"- {s}" for s in safety)
    pit_md = "\n".join(f"- {p}" for p in pitfalls)

    ex_parts: list[str] = []
    for i, ex in enumerate(examples, 1):
        ex_parts.append(
            f"""### Beispiel {i} (Beispieldaten)

- **Aufgabe:** {ex["aufgabe"]}
- **Input:** {ex["input"]}
- **Prompt:**
```text
{ex["prompt"].strip()}
```
- **Erwartetes Ergebnis:** {ex["ergebnis"]}"""
        )

    sp = system_prompt.strip()
    if len([ln for ln in sp.splitlines() if ln.strip()]) < 10:
        raise ValueError("system prompt needs at least 10 non-empty lines")

    return f"""## Zweck

{zweck}

## Wann nutzen

{wann_md}

## Tool-Stack

| Tool | Rolle | Begründung |
|------|-------|------------|
{tool_md}

## System-Prompt / Instruktionen

```text
{sp}
```

## Arbeitsablauf

{steps_md}

## Qualitätskriterien / Definition of Done

{dod_md}

## Sicherheit & Freigaben

{safety_md}

## Fallstricke

{pit_md}

## Grundbeispiele

{chr(10).join(ex_parts)}
"""