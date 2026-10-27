# Analytic 0065 Technique Response Playbook

## Target technique

**AN0065 — Analytic 0065**

- Platforms: Windows

Adversary stages a lure that references a remote resource (e.g., LNK/SCF/Office template). When the user opens/renders the file or a shell enumerates icons, the host automatically attempts SMB or WebDAV authentication to the attacker host. The chain is: (1) lure file is created or modified in a user-exposed location → (2) user or system accesses the lure → (3) host makes outbound NTLM (SMB 139/445 or WebDAV over 80/443) to an untrusted destination → (4) repeated attempts from multiple users/hosts or from privileged workstations.

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
- AN0065: https://attack.mitre.org/detectionstrategies/DET0022#AN0065
- Reviewed: 2026-10-27
