# AN1307 Analytic 1307 Outcome Lesson

## Authoritative description

- Technique: **AN1307 — Analytic 1307**
- Platforms: macOS

MacOS environmental keying behavioral chain: (1) System information discovery through native utilities (system_profiler, sw_vers, hostname, dscl) and Security framework queries, (2) Hardware and software enumeration including serial numbers, installed applications, and system versions, (3) Network configuration assessment (networksetup, scutil) and wireless network discovery, (4) Keychain and security context validation, (5) Unified Logs correlation with cryptographic framework usage (CommonCrypto, Security.framework), (6) Application bundle execution following environmental validation.

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
- AN1307: https://attack.mitre.org/detectionstrategies/DET0474#AN1307
- Reviewed: 2026-10-27

## Boundary

This lesson is derived from the published technique description. It does not invent an incident, prescribe one implementation, or claim the technique has been addressed.
