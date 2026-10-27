# AN1433 Analytic 1433 Outcome Lesson

## Authoritative description

- Technique: **AN1433 — Analytic 1433**
- Platforms: Windows

Detection focuses on unauthorized manipulation of .NET AppDomainManager behavior. Defenders may observe suspicious creation of new AppDomains within trusted processes, anomalous loading of assemblies via non-standard configuration files, or registry/environment variable changes redirecting AppDomainManager to malicious assemblies. Correlated events include config file tampering, new process creation of .NET host processes (e.g., w3wp.exe, powershell.exe) with modified runtime parameters, and module loads of unusual or unsigned .NET DLLs.

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
- AN1433: https://attack.mitre.org/detectionstrategies/DET0517#AN1433
- Reviewed: 2026-10-27

## Boundary

This lesson is derived from the published technique description. It does not invent an incident, prescribe one implementation, or claim the technique has been addressed.
