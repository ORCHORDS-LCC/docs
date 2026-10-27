# AN0240 Analytic 0240 Outcome Lesson

## Authoritative description

- Technique: **AN0240 — Analytic 0240**
- Platforms: Windows

Defender observes execution of commands like `tasklist`, `sc query`, `reg query`, or PowerShell WMI/Registry queries targeting known backup products (e.g., Veeam, Acronis, CrashPlan). Behavior often includes parent-child lineage involving PowerShell or cmd.exe with discovery syntax, and enumeration of services, directories, or registry paths tied to backup software.

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
- AN0240: https://attack.mitre.org/detectionstrategies/DET0088#AN0240
- Reviewed: 2026-10-27

## Boundary

This lesson is derived from the published technique description. It does not invent an incident, prescribe one implementation, or claim the technique has been addressed.
