---
id: esphome-device-yaml-review-v1
title: "ESPHome device YAML review before flashing"
domain: hardware-embedded
category: arduino-esp32
tags:
  - esphome
  - esp32
  - yaml
  - firmware
  - iot
  - home-assistant
target_agents:
  - hermes
  - grokbot
  - claude-code
  - cursor
  - codex
  - openclaw
required_tools:
  - name: ESPHome CLI
    install: "https://esphome.io/guides/cli/"
    version_notes: "esphome config validates the YAML; esphome compile validates and builds firmware."
  - name: homeassistant-mcp
    install: "https://github.com/tevonsb/homeassistant-mcp"
    version_notes: "Optional read-only lookup of entity names in Home Assistant."
  - name: filesystem MCP server
    install: "https://github.com/modelcontextprotocol/servers/tree/main/src/filesystem"
    version_notes: "Reads the device YAML and secrets.yaml without editing either file."
inputs:
  - "Path to the ESPHome device YAML and the secrets.yaml file"
  - "Board type, ESPHome version, and whether this is a first flash or an OTA update"
  - "Optional Home Assistant entity names to confirm with homeassistant-mcp"
outputs:
  - "review-report.md with findings, severity, and security notes"
  - "Suggested unified diff for the human to apply in the editor"
risk_level: medium
example_count: 2
version: "1.0.0"
updated: "2026-11-28"
---

## Purpose

Review an ESPHome device YAML before a first flash or an OTA update: validate the configuration, check secrets handling and security settings, flag pin conflicts and risky options, and produce a review report with a suggested diff. The human applies changes and flashes the device; this template never edits the YAML and never runs the flash.

## When to use

- Before the first flash of a new ESP32 board running ESPHome.
- Before an OTA update that changes wifi, api, ota, or web_server settings.
- When a device YAML was copied from a forum post and the pins and secrets need a review.
- When several devices share an API key or a web_server password and you need to separate them.

### When not to use

- For deep firmware debugging that needs a serial console and a logic analyzer.
- When the YAML targets an ESPHome version older than the installed CLI without a compatibility check.
- As a security audit of the whole home network or the router configuration.

## Tool stack

| Tool | Role | Rationale |
|------|------|-----------|
| ESPHome CLI | Validate and compile | esphome config checks YAML; esphome compile builds firmware |
| homeassistant-mcp | Optional entity check | Read-only lookup of entity names in Home Assistant |
| filesystem MCP | File access | Reads the device YAML and secrets.yaml without edits |
| Text diff (human editor) | Apply changes | Human reviews the suggested unified diff |

## System prompt

```text
You review an ESPHome device YAML before a first flash or an OTA update, reading the device file and secrets.yaml without editing either file.
You run esphome config <file> to validate the configuration and check that secrets are redacted in the output unless the human passes --show-secrets.
You run esphome compile <file> when the human asks for a full build check, and you report compiler errors with the exact YAML line when available.
You verify that every credential uses a !secret reference and that secrets.yaml is listed in .gitignore, never committed to version control.
You require api: encryption: key: !secret api_key with a unique key per device and you flag any reused or missing API key.
You check that web_server, when enabled, has auth with a password from secrets.yaml, and you suggest disabling web_server when the user does not need it.
You flag pin conflicts, strapping-pin use, and pins reserved for flash or USB on the target board, citing the YAML line for each conflict.
You check wifi, api, ota, logger, and web_server blocks for missing fields, plain-text passwords, and options that expose the device on the local network.
You treat the firmware image as sensitive because it carries Wi-Fi credentials and the API key, and you tell the human not to share the .bin file.
You write review-report.md with a findings table, a severity column, and a suggested diff in unified diff format for the human to apply in the editor.
You never flash, compile-to-device, or call esphome run, and you never write to the YAML or secrets files.
You ask for the board type and ESPHome version so pin and option checks match the installed toolchain.
You list each finding with the block name, the YAML key path, and a concrete fix, and you mark unverified items as needing human review.
```

## Workflow

1. Confirm the device YAML path, board type, ESPHome version, and whether this is a first flash or an OTA update.
2. Read the YAML and secrets.yaml with filesystem MCP; confirm secrets.yaml is ignored by version control.
3. Run esphome config <file> and capture validation errors plus the redacted output.
4. Run esphome compile <file> when requested and record compiler warnings tied to YAML lines.
5. Check pins against the target board, flag conflicts and strapping or flash pins, and note the YAML line for each.
6. Review wifi, api, ota, logger, and web_server for plain-text secrets, missing auth, and unsafe options.
7. Write review-report.md with findings, severity, and a unified diff suggestion; do not edit the source YAML.
8. Hand the report and diff to the human, who applies changes and runs the flash or OTA update.

## Definition of done

- [ ] esphome config ran and its validation result is quoted
- [ ] Every credential uses !secret and secrets.yaml is ignored by version control
- [ ] api encryption key is unique and present for this device
- [ ] web_server has auth or is disabled when unused
- [ ] review-report.md includes findings, severity, and a unified diff
- [ ] No flash or OTA action was taken and no YAML file was edited

## Security

- The firmware image contains Wi-Fi credentials and the API key; treat every .bin file as a secret.
- Keep secrets.yaml outside version control and out of chat, tickets, and screenshots.
- Use a unique API encryption key per device and rotate a key if it was shared.
- Enable OTA encryption as described in the ESPHome security guidance; it reuses the API encryption key, so the firmware image, which contains Wi-Fi credentials and the API key, stays confidential in transit.
- Give homeassistant-mcp read-only access and never store a long-lived token in the YAML.

## Pitfalls

- A YAML that passes esphome config can still fail at compile time when a component needs a library or board flag.
- Copying a pin number from a similar board can hit a strapping pin and stop the board from booting.
- Reusing an API key across devices means one leaked key exposes every device.
- web_server without auth publishes control endpoints to anyone on the local network.
- A secrets.yaml that is committed once stays in git history even after a later removal.
- An OTA update with a changed board or flash size can leave the device unreachable and need a wired recovery.

## Basic examples

### Example 1 (Example data (self-written))

- **Task:** Review fictional Acme Climate Node YAML before the first flash on an ESP32 board.
- **Input:** climate-node.yaml with wifi, api, ota, logger, web_server, and one DHT22 sensor; secrets.yaml holds the Wi-Fi password.
- **Prompt:**

```text
Review climate-node.yaml and secrets.yaml. Run esphome config, flag pin conflicts and unsafe api, ota, and web_server settings, and suggest a unified diff. Do not flash.
```

- **Expected result:**

```text
Validation: esphome config passed with 0 errors and 2 warnings (secrets redacted)
Findings:
| Severity | Block | Key | Issue | Fix |
| high | api | encryption | key missing | add key: !secret api_key |
| high | web_server | auth | no password | add auth with !secret web_password |
| medium | sensor | pin | GPIO2 shared with onboard LED | move to GPIO4 |
| low | logger | level | DEBUG in production | set level: INFO |
Pin check: GPIO2 is a strapping pin on this board; GPIO4 is free
Security: secrets.yaml is listed in .gitignore; no API encryption key yet, so generate a new unique 32-byte base64 key for this device
Suggested diff: 3 hunks in climate-node.yaml, 0 changes to secrets.yaml
Human action: apply diff, run esphome compile, then flash over USB
```

### Example 2 (Example data (self-written))

- **Task:** Check an ESPHome YAML copied from a forum post before reuse on a second device.
- **Input:** second-node.yaml reuses the API key from climate-node.yaml and has web_server with no auth.
- **Prompt:**

```text
Review second-node.yaml for reused keys and web_server auth. Compare with climate-node.yaml. Suggest a diff that adds a unique key and disables web_server. Do not edit or flash.
```

- **Expected result:**

```text
API: encryption key matches climate-node.yaml (reused key, high severity)
web_server: enabled with no auth on port 80 (high severity)
Secrets: wifi password is plain text in the YAML, not a !secret reference
Pin check: GPIO0 used for the relay conflicts with the boot strapping pin
Suggested diff: replace key with !secret api_key_second, remove the web_server block, move relay to GPIO5
secrets.yaml: add api_key_second with a new 32-byte base64 key
After the human applies the diff: re-run esphome config before compiling
Human action: apply diff, run esphome compile, then flash and confirm the entity in Home Assistant
```

## Sources

- https://esphome.io/guides/cli/
- https://esphome.io/guides/yaml/
- https://esphome.io/guides/security_best_practices/
- https://esphome.io/components/api/
- https://esphome.io/components/ota/
