# AN0510 Analytic 0510 Outcome Lesson

## Authoritative description

- Technique: **AN0510 — Analytic 0510**
- Platforms: Windows

Detection correlates file creation or modification of `.lnk` (shortcut) files in autostart locations with anomalous parent-child process lineage or unsigned binaries. Defenders should watch for LNK creation/modification events outside of known software installations, patch events, or OS updates. Flag shortcut targets pointing to suspicious locations or unknown binaries, particularly those written by script interpreters or spawned from phishing delivery chains.

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
- AN0510: https://attack.mitre.org/detectionstrategies/DET0180#AN0510
- Reviewed: 2026-10-27

## Boundary

This lesson is derived from the published technique description. It does not invent an incident, prescribe one implementation, or claim the technique has been addressed.
