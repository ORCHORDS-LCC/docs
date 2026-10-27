# AN1210 Analytic 1210 Outcome Lesson

## Authoritative description

- Technique: **AN1210 — Analytic 1210**
- Platforms: macOS

Detection centers on DYLD_INSERT_LIBRARIES and DYLD_LIBRARY_PATH abuse. Defender perspective: monitor for modification of these environment variables in shell or plist files, file creation of dylibs in user-controlled paths, and correlation of environment variable usage with unexpected module loads by user applications. Suspicious indicators include processes with DYLD_INSERT_LIBRARIES set, execution of applications loading untrusted dylibs, and anomalies in module load history.

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
- AN1210: https://attack.mitre.org/detectionstrategies/DET0435#AN1210
- Reviewed: 2026-10-27

## Boundary

This lesson is derived from the published technique description. It does not invent an incident, prescribe one implementation, or claim the technique has been addressed.
