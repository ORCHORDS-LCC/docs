# AN0595 Analytic 0595 Outcome Lesson

## Authoritative description

- Technique: **AN0595 — Analytic 0595**
- Platforms: Windows

Adversary modifies or replaces the Terminal Services DLL (`termsrv.dll`) or changes the associated `ServiceDll` Registry value to load an arbitrary or patched DLL that enables persistent and enhanced RDP access. This may include binary replacement, registry tampering, and unexpected module loads by the `svchost.exe -k termsvcs` process.

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
- AN0595: https://attack.mitre.org/detectionstrategies/DET0212#AN0595
- Reviewed: 2026-10-27

## Boundary

This lesson is derived from the published technique description. It does not invent an incident, prescribe one implementation, or claim the technique has been addressed.
