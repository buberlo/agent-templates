---
id: mobile-apps-workflow
title: "Mobile Apps"
domain: software-development
category: mobile-apps
tags:
  - mobile
  - react-native
  - flutter
target_agents:
  - hermes
  - claude-code
  - cursor
  - generic-mcp-agents
required_tools:
  - name: react-native / flutter
    install: "project toolchain"
    version_notes: "npx react-native run-android"
  - name: xcodebuild
    install: "iOS optional"
    version_notes: "Mac only"
inputs:
  - "Platform (iOS/Android/both)"
  - "Feature + store policy notes"
outputs:
  - "Buildable app changes"
  - "Device/simulator steps"
risk_level: medium
example_count: 2
version: "1.0.0"
updated: "2026-11-23"
---

## Purpose

Mobile Features in **React Native/Flutter**: Permissions, Deeplinks, Store-Richtlinien, Simulator-Smoke.

## When to use

- Neuer Screen, Push-Vorbereitung, Offline-Cache.
- Crash-Fix aus Stacktrace.

**When not:** Store release without review account release.

## Tool stack

| Tool | Role | Justification |
|------|-------|------------|
| Metro/flutter test | unit/widget | fast |
| simulators | smoke | platform SDK |
| fastlane | optional CI | user gated |

## System prompt

```text
Mobile apps workflow (software-development/mobile-apps).

Request permissions at runtime with rationale strings; Info.plist/AndroidManifest entries listed.
Safe area and notches handled; no hardcoded status bar padding.
Networking: certificate pinning only if project already uses; do not add casually.
Secure storage for tokens (Keychain/Keystore abstractions).
Deep links tested on cold start and warm.
react-native: npx react-native run-android --variant debug; ios if mac available.
flutter: flutter test && flutter analyze.
No tracking SDK without privacy manifest notes.
Offline: queue mutations with idempotency keys when spec says.
Accessibility: TalkBack/VoiceOver labels on icons.
Bundle id and signing not modified without explicit ask.
```

## Workflow

1. Stack erkennen (RN/Flutter).
2. Feature branch.
3. Implement screens + navigation.
4. `npm test` / `flutter test`.
5. Simulator run steps dokumentieren.
6. Manifest permissions diff review.
7. Release notes draft without submitting store.

## Definition of done

- [ ] analyze/lint clean
- [ ] Permissions dokumentiert
- [ ] Simulator smoke steps

## Security

- No API keys im JS bundle.
- Store upload only with release.

## Pitfalls

- iOS build without Mac — klar kommunizieren.
- Hermes vs JSC mismatch.
- Gradle version pin conflicts.
- Push cert expiry.
- 16KB page size Android future.

## Basic examples

### Example 1 (Example data)

- **Task:** RN login screen.
- **Input:** Android debug.
- **Prompt:**

```text
Secure token storage; jest test; document run-android.
```

- **Expected result:**

```bash
npm test -- Login.test.tsx
npx react-native run-android --variant debug
```

### Example 2 (Example data)

- **Task:** Flutter widget test.
- **Input:** cart badge.
- **Prompt:**

```text
Widget test count; flutter analyze clean.
```

- **Expected result:**

```bash
flutter test test/cart_badge_test.dart
flutter analyze
```