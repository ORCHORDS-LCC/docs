# AN1295 Analytic 1295 Outcome Lesson

## Authoritative description

- Technique: **AN1295 — Analytic 1295**
- Platforms: Linux

Detection of binaries spawning encrypted sessions using OpenSSL or curl to external services with mismatched ports/protocols. Identifies behavior where internal services simulate trusted cloud service traffic patterns.

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
- AN1295: https://attack.mitre.org/detectionstrategies/DET0470#AN1295
- Reviewed: 2026-10-27

## Boundary

This lesson is derived from the published technique description. It does not invent an incident, prescribe one implementation, or claim the technique has been addressed.
