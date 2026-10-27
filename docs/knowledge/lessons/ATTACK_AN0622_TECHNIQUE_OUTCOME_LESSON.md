# AN0622 Analytic 0622 Outcome Lesson

## Authoritative description

- Technique: **AN0622 — Analytic 0622**
- Platforms: Windows

Abuse of mmc.exe to execute non-Microsoft or user-staged .msc files and malicious COM CLSIDs. Behavioral chain: (1) suspicious mmc.exe invocation with /a or -Embedding and non-standard .msc path → (2) COM activation of non-baseline CLSIDs by mmc.exe → (3) mmc.exe loads non-baseline DLLs (user-writable/UNC/unsigned) → (4) optional network/DNS activity from mmc.exe.

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
- AN0622: https://attack.mitre.org/detectionstrategies/DET0222#AN0622
- Reviewed: 2026-10-27

## Boundary

This lesson is derived from the published technique description. It does not invent an incident, prescribe one implementation, or claim the technique has been addressed.
