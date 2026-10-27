# Analytic 1501 Technique Response Playbook

## Target technique

**AN1501 — Analytic 1501**

- Platforms: Windows

Detects adversary abuse of Transactional NTFS (TxF) and undocumented process loading mechanisms (e.g., NtCreateProcessEx) to create a hollowed process from an uncommitted, maliciously tainted file image in memory, later executed via NtCreateThreadEx.

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
- AN1501: https://attack.mitre.org/detectionstrategies/DET0544#AN1501
- Reviewed: 2026-10-27
