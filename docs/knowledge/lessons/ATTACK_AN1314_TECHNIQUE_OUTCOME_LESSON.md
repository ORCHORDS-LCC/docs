# AN1314 Analytic 1314 Outcome Lesson

## Authoritative description

- Technique: **AN1314 — Analytic 1314**
- Platforms: Windows

Cause→effect chain: (1) User-facing app (Office/PDF/archiver/browser) records an open/click or abnormal event, then (2) a downloaded file is created in a user-writable path and/or decompressed, (3) the parent user app spawns a living-off-the-land binary (e.g., powershell/cmd/mshta/rundll32/msiexec/wscript/expand/zip) or installer, and (4) immediate outbound HTTP(S)/DNS/SMB from the same lineage.

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
- AN1314: https://attack.mitre.org/detectionstrategies/DET0478#AN1314
- Reviewed: 2026-10-27

## Boundary

This lesson is derived from the published technique description. It does not invent an incident, prescribe one implementation, or claim the technique has been addressed.
