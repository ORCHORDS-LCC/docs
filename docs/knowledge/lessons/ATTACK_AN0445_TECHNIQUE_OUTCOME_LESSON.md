# AN0445 Analytic 0445 Outcome Lesson

## Authoritative description

- Technique: **AN0445 — Analytic 0445**
- Platforms: Windows

Detection of msiexec.exe execution where command-line arguments reference remote MSI packages, UNC paths, HTTP/HTTPS URLs, or DLLs, correlated with subsequent module loads and/or network connections to previously unseen destinations. The behavioral chain links process creation of msiexec.exe with suspicious parameters, network activity to retrieve payloads, and module loading indicative of malicious installation or DLL execution.

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
- AN0445: https://attack.mitre.org/detectionstrategies/DET0158#AN0445
- Reviewed: 2026-10-27

## Boundary

This lesson is derived from the published technique description. It does not invent an incident, prescribe one implementation, or claim the technique has been addressed.
