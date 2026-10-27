# T1116 Code Signing Outcome Lesson

## Authoritative description

- Technique: **T1116 — Code Signing**
- Tactics: stealth
- Platforms: macOS, Windows

Code signing provides a level of authenticity on a binary from the developer and a guarantee that the binary has not been tampered with. However, adversaries are known to use code signing certificates to masquerade malware and tools as legitimate binaries . The certificates used during an operation may be created, forged, or stolen by the adversary. Code signing to verify software on first run can be used on modern Windows and macOS/OS X systems. It is not used on Linux due to the decentralized nature of the platform. Code signing certificates may be used to bypass security policies that require signed code to execute on a system.

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
- T1116: https://attack.mitre.org/techniques/T1116
- Reviewed: 2026-10-27

## Boundary

This lesson is derived from the published technique description. It does not invent an incident, prescribe one implementation, or claim the technique has been addressed.
