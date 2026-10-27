# AN1136 Analytic 1136 Outcome Lesson

## Authoritative description

- Technique: **AN1136 — Analytic 1136**
- Platforms: macOS

Abuse of extended attributes (xattrs) to hide payloads in com.apple.* or custom keys. Defender perspective: monitor suspicious use of xattr command with -w (write) and -p (print) flags, especially when followed by execution of interpreters like bash, Python, or osascript. Behavior chain includes: (1) suspicious file modification with new com.apple.* attributes, (2) attribute content inconsistent with expected metadata tags (e.g., high entropy), (3) subsequent process execution correlated with extraction of the attribute.

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
- AN1136: https://attack.mitre.org/detectionstrategies/DET0406#AN1136
- Reviewed: 2026-10-27

## Boundary

This lesson is derived from the published technique description. It does not invent an incident, prescribe one implementation, or claim the technique has been addressed.
