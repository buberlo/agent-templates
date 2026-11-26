---
id: desktop-automation-workflow
title: "Desktop GUI automation"
domain: automation
category: desktop-automation
tags:
  - desktop
  - automation
  - scripting
target_agents:
  - hermes
  - cursor
  - claude-code
  - generic-mcp-agents
required_tools:
  - name: xdotool
    install: "https://github.com/jordansissel/xdotool"
    version_notes: "X11 only; Wayland needs ydotool or compositor shortcuts"
  - name: osascript
    install: "https://ss64.com/mac/osascript.html"
    version_notes: "macOS AppleScript and System Events"
  - name: PowerShell UI Automation
    install: "https://learn.microsoft.com/en-us/windows/win32/winauto/uiauto-usepatterns"
    version_notes: "Windows UI Automation patterns for supported apps"
inputs:
  - "Operating system and display server (X11, Wayland, macOS, Windows)"
  - "Target application window title or process name"
  - "Allowed actions: menu navigation, save, export — no passwords from chat"
outputs:
  - "Script file with pauses between UI mutations"
  - "Dry-run checklist the user executes while watching"
  - "Abort hotkey or kill instruction"
risk_level: medium
example_count: 2
version: "1.2.0"
updated: "2026-11-26"
---

## Purpose

Automate visible desktop GUI steps with short, logged scripts so a human can watch each mutation and stop unsafe chords before data loss.

## When to use

- Repetitive export or save flows in desktop apps without APIs.
- Internal tools that only expose native dialogs for PDF or CSV export.
- Temporary macros while an API integration is scheduled.

### When not to use

- Browser-only flows — use `automation/browser-automation/browser-automation-workflow` with Playwright instead.
- Headless servers without a logged-in graphical session the user can see.

## Tool stack

| Tool | Role | Rationale |
|------|------|-----------|
| xdotool | Linux X11 keys and focus | Window search and key sequences |
| osascript | macOS automation | System Events tells for menu and save |
| PowerShell UIA | Windows control patterns | MS docs for supported automation peers |

## System prompt

```text
You write watched desktop automation scripts for automation/desktop-automation-workflow.
You begin by confirming OS, display server, target app, and whether the user will remain at the keyboard during dry-run and live run.
On macOS you generate osascript that focuses the application via System Events and inserts 200 to 500 millisecond pauses between UI changes.
On Linux X11 you use xdotool search and windowactivate with similar pauses; on Wayland you stop xdotool paths and document ydotool, compositor shortcuts, or manual steps instead.
On Windows you prefer UI Automation patterns from Microsoft docs rather than raw mouse coordinates when the control exposes an automation peer.
You never type passwords, one-time codes, or clipboard secrets through simulated keys; the user enters sensitive input manually unless a lab fixture is documented.
You require a spelled confirmation string before destructive chords such as emptying trash, confirming delete dialogs, or Alt+F4 on unsaved work.
You redirect browser-heavy sequences to Playwright templates because pixel clicking in Chrome is brittle compared to browser automation.
You deliver a script file path, prerequisite packages, dry-run checklist, and abort instruction such as killing the script process.
You log each step in comments: window title fragment, action, and expected visible outcome after the pause.
You size delays for HiDPI and fractional scaling because coordinate clicks drift when scaling is not one hundred percent.
```

## Workflow

1. Confirm OS, Wayland versus X11, and target application name.
2. Walk through human steps; mark decision points and destructive dialogs.
3. Draft script with explicit sleeps between focus changes and key presses.
4. User executes dry-run while screen sharing or sitting at the machine.
5. Enable logging to a timestamped file without embedding credentials.
6. Store script in repo without secrets; document required packages.
7. Provide disable or uninstall steps and when to retire the macro for an API.

## Definition of done

- [ ] Script tested on the target OS and display server stated in inputs
- [ ] No passwords or OTP literals in the script or chat transcript
- [ ] Destructive actions gated on user confirmation strings
- [ ] Wayland limitation documented when xdotool is inappropriate

## Security

- Desktop macros can exfiltrate visible data; run only on trusted machines.
- Users must watch the display; unattended macros are out of scope.
- Remote desktop latency can desynchronize key sequences; warn before cloud RDP.

## Pitfalls

- Wrong window focused when multiple windows share similar titles.
- Wayland sessions block legacy X11 tools without ydotool or portal helpers.
- Pauses that are too short send keystrokes before dialogs finish opening.
- HiDPI scaling shifts click coordinates when scripts use raw mouse events.
- RDP or VNC lag reorders key chords and saves to the wrong document.

## Basic examples

### Example 1 (Example data (self-written))

- **Task:** Export PDF from LibreOffice Writer on Ubuntu X11.
- **Input:** Ubuntu 22.04 X11, window title contains `Weekly Report.odt`, user watching.
- **Prompt:**

```text
xdotool macro: focus Writer, Ctrl+Shift+O export dialog, choose PDF, save to ~/exports/report.pdf.
```

- **Expected result:** Shell script with window search, activate, key sequences, half-second sleeps, and comments per step. Dry-run checklist asks user to verify focus before export. Expected file path `~/exports/report.pdf` after user confirms the save dialog. No password typing included.

### Example 2 (Example data (self-written))

- **Task:** Wayland attempt with xdotool form click.
- **Input:** Fedora 40 Wayland, user wants xdotool click on a GTK form.
- **Prompt:**

```text
Use xdotool to click Submit on my Wayland desktop form.
```

- **Expected result:** Agent refuses bare xdotool on Wayland, explains limitation with link to xdotool project notes, suggests ydotool or manual completion, and offers Playwright if the form is in a browser. No script claimed as executed.