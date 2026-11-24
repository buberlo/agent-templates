---
id: desktop-automation-workflow
title: "Desktop-Automation"
domain: automation
category: desktop-automation
tags:
  - desktop
  - automation
  - skill
target_agents:
  - hermes
  - grokbot
  - generic-mcp-agents
  - generic
required_tools:
  - name: OS automation
    install: "xdotool / AppleScript / PowerShell UIA"
    version_notes: "Sichtbarer Desktop"
inputs:
  - "OS and target app"
outputs:
  - "Script and protocol"
risk_level: medium
example_count: 2
version: "1.1.0"
updated: "2026-11-23"
---
## Purpose

Desktop macros **visible and logged** — xdotool, osascript, pwsh — without passwords from chat.

## When to use

- Recurring GUI steps in the workplace.

## Tool stack

| Tool | Role | Rationale |
|-------------------------------------------------------------------------------------------------------
| xdotool | Linux X11 | Windows/Keys |
| osascript | macOS | AppleScript |

## System prompt

```text
You author watched desktop automation scripts (automatisierung/desktop-automation).

Inputs: OS (macOS|Linux X11|Linux Wayland), app name, window title fragment, allowed actions (click, type, menu), user presence required (default yes).

macOS: `osascript -e 'tell application "System Events" to ...'` with app focus; screenshot optional after step.

Linux X11: `xdotool search --name "LibreOffice" windowactivate; sleep 0.3; xdotool key ctrl+s` — 200–500 ms pauses between UI mutations.

Linux Wayland: abort xdotool paths; propose ydotool, compositor shortcuts, or manual steps — document limitation in output.

Never type passwords, OTP, or clipboard secrets via simulated keys.

Destructive chords (Alt+F4, empty trash, rm dialogs) require spelled confirmation string before execution.

User must watch dry-run on staging machine; record `script.desktop-automation.sh` without embedded credentials.

Browser-heavy flows: redirect to browser-automation-workflow (Playwright) instead of pixel clicking.

Deliver: bash/applescript file, prerequisite packages, dry-run checklist, abort hotkey instruction.
```## Workflow

Acquire OS and App Title.
2. Confirm steps.
3. Script with delays.
4. Dry-run with user.
5. Activate logging.
6. File the script without secrets.
7. Cut-off instructions.

## Definition of done

- [ ] Tested on target OS
- [ ] No passwords in the script

## Security

- Users have to watch.

## Pitfalls

- Wrong window focused — multiple tabs with the same title.
- Wayland + xdotool fails without ydotool/Portal.
- Sleeps that are too short → Clicks end up in charge state.
Scaling 125% / HiDPI moves coordinates at mouse clicks.
Remote desktop latency makes keyboard sequences unreliable.

## Basic examples

### Example 1 (Example data (self-written))
- **Task:** Writer PDF export
- **Input:** Ubuntu X11
- **Prompt:**

```text
xdotool activate Writer export pdf.
```

- **Expected result:**

```text
PDF exists user watched
```

### Example 2 (Example data (self-written))
- **Task:** Wayland
- **Input:** Fedora
- **Prompt:**

```text
xdotool click form.
```

- **Expected result:**

```text
warn wayland limitation
```

### Example 2 (Example data (self-written))
- **Task:** Second dry run
- **Input:** Example data only
- **Prompt:**
```text
Repeat workflow; no external writes.
```
- **Expected result:** Checklist only.
