# Data Staged Mitigation Technique Response Playbook

## Target technique

**T1074 — Data Staged Mitigation**


Identify system utilities, remote access or third-party tools, users or potentially malicious software that may be used to store compressed or encrypted data in a publicly writeable directory, central location, or commonly used staging directories (e.g. recycle bin) that is indicative of non-standard behavior, and audit and/or block them by using file integrity monitoring tools where appropriate. Consider applying data size limits or blocking file writes of common compression and encryption utilities such as 7zip, RAR, ZIP, or zlib on frequently used staging directories or central locations and monitor attempted violations of those restrictions.

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
- T1074: https://attack.mitre.org/mitigations/T1074
- Reviewed: 2026-10-27
