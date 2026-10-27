# AN0964 Analytic 0964 Outcome Lesson

## Authoritative description

- Technique: **AN0964 — Analytic 0964**
- Platforms: macOS

User pastes an obfuscated command into Terminal.app/iTerm2 that decodes or downloads code and executes. Detects Terminal/iTerm2 spawning bash/zsh/python with suspicious pipeline/base64 patterns followed by file writes in ~/Library or /tmp and outbound network connections.

## Reusable lesson

This technique should be treated as an explicit review question when it is relevant to the system or organisation, rather than assumed to be covered by a generic control statement or by tooling that reports a related signal.

## Apply the lesson

1. Define the real scope before judging coverage.
2. Inspect current technical, process, governance, or operational evidence.
3. Separate documented intent from verified behaviour.
4. Record partial coverage and unresolved gaps instead of converting them into a pass.
5. Revisit when the underlying scope, threat environment, technology, suppliers, or mission materially changes.

## Source

- MITRE ATT&CK: https://attack.mitre.org/
- AN0964: https://attack.mitre.org/detectionstrategies/DET0340#AN0964
- Reviewed: 2026-10-27

## Boundary

This lesson is derived from the published technique description. It does not invent an incident, prescribe one implementation, or claim the technique has been addressed.
