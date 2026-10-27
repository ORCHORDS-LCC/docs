# AN0388 Analytic 0388 Outcome Lesson

## Authoritative description

- Technique: **AN0388 — Analytic 0388**
- Platforms: Windows

Execution of InstallUtil.exe from .NET framework directories with arguments specifying non-standard or attacker-supplied assemblies, especially when followed by suspicious child process creation or script execution. Detection also includes correlation of newly created binaries prior to InstallUtil invocation and anomalous command-line usage compared to historical baselines.

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
- AN0388: https://attack.mitre.org/detectionstrategies/DET0138#AN0388
- Reviewed: 2026-10-27

## Boundary

This lesson is derived from the published technique description. It does not invent an incident, prescribe one implementation, or claim the technique has been addressed.
