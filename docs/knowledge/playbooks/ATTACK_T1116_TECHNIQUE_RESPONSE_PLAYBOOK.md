# Code Signing Technique Response Playbook

## Target technique

**T1116 — Code Signing**

- Tactics: stealth
- Platforms: macOS, Windows

Code signing provides a level of authenticity on a binary from the developer and a guarantee that the binary has not been tampered with. However, adversaries are known to use code signing certificates to masquerade malware and tools as legitimate binaries . The certificates used during an operation may be created, forged, or stolen by the adversary. Code signing to verify software on first run can be used on modern Windows and macOS/OS X systems. It is not used on Linux due to the decentralized nature of the platform. Code signing certificates may be used to bypass security policies that require signed code to execute on a system.

## Preconditions

- the estate in scope is identified, with the systems the technique could apply to;
- an owner is accountable for detection and response;
- current telemetry and configuration can be inspected;
- the technique is applicable or requires an applicability decision.

## Procedure

1. Confirm the scope and owner.
2. Read the current technique description and the associated detection guidance.
3. Inventory the telemetry that would carry the technique's indicators.
4. Inspect whether the indicators are present in the environment.
5. Exercise the detection path and confirm it produces the expected signal.
6. Record gaps in detection coverage and assign remediation owners.
7. Record justified non-applicability or accepted detection gaps separately.
8. Set the next event-driven or periodic verification trigger.

## Failure handling

If the detection path does not produce the expected signal, treat the coverage as unverified, preserve the test evidence, and route the gap through the appropriate remediation or risk process.

## Completion evidence

Scope, owner, source version, telemetry inspected, tests performed, findings, exceptions, remediation links, reviewer, and next trigger.

## Source

- MITRE ATT&CK: https://attack.mitre.org/
- T1116: https://attack.mitre.org/techniques/T1116
- Reviewed: 2026-10-27
