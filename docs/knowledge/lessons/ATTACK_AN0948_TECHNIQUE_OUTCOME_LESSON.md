# AN0948 Analytic 0948 Outcome Lesson

## Authoritative description

- Technique: **AN0948 — Analytic 0948**
- Platforms: macOS

Detects anomalous use of macOS XPC services for code execution. Monitors for processes invoking privileged XPC daemons with abnormal parameters, unexpected binaries communicating over NSXPCConnection, or helper tools executing code outside of their expected parent process lineage. Correlates process access attempts to system-level daemons, privilege escalations via XPC misconfigurations, and injection of malicious payloads through inter-process communication.

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
- AN0948: https://attack.mitre.org/detectionstrategies/DET0335#AN0948
- Reviewed: 2026-10-27

## Boundary

This lesson is derived from the published technique description. It does not invent an incident, prescribe one implementation, or claim the technique has been addressed.
