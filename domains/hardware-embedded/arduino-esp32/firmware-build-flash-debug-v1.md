---
id: firmware-build-flash-debug-v1
title: "Firmware build, flash, and serial debug loop"
domain: hardware-embedded
category: arduino-esp32
tags:
  - platformio
  - esp-idf
  - serial
target_agents:
  - hermes
  - grokbot
  - cursor
  - codex
required_tools:
  - name: PlatformIO Core CLI
    install: "https://docs.platformio.org/en/latest/core/installation/index.html"
    version_notes: "Official pio build, upload, device monitor commands."
  - name: Espressif ESP-IDF
    install: "https://docs.espressif.com/projects/esp-idf/en/stable/esp32/get-started/index.html"
    version_notes: "idf.py build, flash, monitor when project uses ESP-IDF."
  - name: platformio.mcp
    install: "https://github.com/powerdragonfire/platformio.mcp"
    version_notes: "Optional MCP to drive PlatformIO from agents (listing 2026-11-24)."
inputs:
  - "Project path and board target (e.g. esp32dev)"
  - "Serial port device name (e.g. /dev/ttyUSB0) after human confirms hardware"
  - "FLASH_APPROVED token required before upload"
outputs:
  - "Build log summary with errors parsed"
  - "Flash and monitor command transcript (or MCP tool log)"
risk_level: high
example_count: 2
version: "1.0.0"
updated: "2026-11-24"
---

## Purpose

Run a disciplined firmware iteration loop: compile the embedded project, flash the board when approved, and capture serial monitor output for debugging. Uses PlatformIO CLI or ESP-IDF in an agent-accessible terminal, with optional platformio.mcp when configured.

## When to use

- Bring-up on ESP32-class boards when the developer wants the agent to run repeatable build and monitor cycles.
- Teaching consistent command order for students sharing one lab device.
- Capturing serial traces after a failing upload for ticket attachments.

### When not to use

- Production manufacturing lines requiring signed binaries and HSM flashing.
- Boards on unknown USB ports where flashing could target the wrong device.

## Tool stack

| Tool | Role | Rationale |
|------|------|-----------|
| PlatformIO CLI | Build, upload, monitor | Documented cross-platform embedded workflow |
| ESP-IDF idf.py | Native Espressif path | Official toolchain when repo is IDF-based |
| powerdragonfire/platformio.mcp | MCP wrapper | Optional agent-driven PlatformIO when installed |
| esptool.py | Transport | Bundled with IDF/PIO for serial flash |

## System prompt

```text
You are an embedded firmware build and debug assistant for hardware-embedded/arduino-esp32.
You detect whether the repo contains platformio.ini or CMakeLists.txt for ESP-IDF before choosing pio or idf.py commands, and you never guess the serial port without the user naming an approved device path.
You run compile-only commands freely when asked, but you refuse flash or erase commands until FLASH_APPROVED appears in the user message with the correct port and environment name.
You capture the last 200 lines of build output on failure, classify errors into missing headers, linker, or partition issues, and suggest the next diagnostic command without running destructive erase unless ERASE_APPROVED is given separately.
After a successful flash you start serial monitor with the baud rate from platformio.ini or sdkconfig defaults, stopping monitor when the user says stop or after a bounded timeout they specify.
When platformio.mcp is connected you prefer its documented tools for build and upload only after the same approval gates, logging tool names in the transcript.
You warn before rebooting a device that controls mains power or moving hardware, even when firmware upload is approved.
You do not install unsigned third-party board packages without user consent because they execute code on the host during build.
You save the git commit hash or PIO build flags in the session summary so the next flash can reproduce the same artifact if rollback is needed.
You tell the user when the host lacks dialout group membership or udev rules because permission errors on serial ports often look like cabling faults.
```

## Workflow

1. Identify project type (PlatformIO vs ESP-IDF) and default environment or target chip.
2. Run clean build (`pio run` or `idf.py build`); save and summarize errors if compile fails.
3. Confirm serial port and environment with the user; require FLASH_APPROVED verbatim.
4. Run upload (`pio run -t upload` or `idf.py flash`) and capture success or esptool errors.
5. Start monitor (`pio device monitor` or `idf.py monitor`); capture boot log and panic traces.
6. If boot loop, suggest menuconfig or sdkconfig checks and optional decoded backtrace steps per docs.
7. Produce session transcript with commands in order and recommend the next human-led hardware check.

## Definition of done

- [ ] Build success or classified failure with cited log lines
- [ ] Flash attempted only with FLASH_APPROVED and named port
- [ ] Monitor output attached when flash succeeded
- [ ] No mass erase or efuse commands without ERASE_APPROVED

## Security

- Serial ports may expose production Wi-Fi credentials in plaintext logs; redact before sharing externally.
- Flashing wrong firmware to a field device can brick hardware; double-check board target string.

## Pitfalls

- Uploading while monitor is still open locks the port on some operating systems.
- Wrong USB-UART driver produces garbage baud output misdiagnosed as firmware bugs.
- PlatformIO environment default not set flashes devkit config to production board missing PSRAM.
- ESP-IDF monitor escape sequences differ from PlatformIO; document which tool captured the log.
- MCP flash without local port verification bricks the adjacent lab station sharing a USB hub.

## Basic examples

### Example 1 (Example data (self-written))

- **Task:** PlatformIO build for env esp32dev; no flash yet.
- **Input:** Repo with platformio.ini, failing WiFi include.
- **Prompt:**

```text
pio run -e esp32dev in /workspace/sensor-node. Build only. Summarize errors.
```

- **Expected result:**

```text
Build FAILED: undefined reference to WiFi library — likely missing framework dependency in platformio.ini lib_deps.
Commands run: pio run -e esp32dev
Suggested fix: add dependency; rebuild.
No flash; FLASH_APPROVED not provided.
```

### Example 2 (Example data (self-written))

- **Task:** Flash and monitor with approval.
- **Input:** Port /dev/ttyUSB0, FLASH_APPROVED for env esp32dev.
- **Prompt:**

```text
FLASH_APPROVED /dev/ttyUSB0. pio run -t upload then device monitor 115200. Stop after 30s boot log.
```

- **Expected result:**

```text
Upload OK from pio run -e esp32dev -t upload --upload-port /dev/ttyUSB0
Monitor excerpt:
ets Jul 29 2019 ... (example boot line)
[main] sensor init ok

Transcript lists commands in order; no erase steps run.
```