# Out-of-Band Communications Channel Technique Response Playbook

## Target technique

**M1060 — Out-of-Band Communications Channel**


Establish secure out-of-band communication channels to ensure the continuity of critical communications during security incidents, data integrity attacks, or in-network communication failures. Out-of-band communication refers to using an alternative, separate communication path that is not dependent on the potentially compromised primary network infrastructure. This method can include secure messaging apps, encrypted phone lines, satellite communications, or dedicated emergency communication systems. Leveraging these alternative channels reduces the risk of adversaries intercepting, disrupting, or tampering with sensitive communications and helps coordinate an effective incident response.

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
- M1060: https://attack.mitre.org/mitigations/M1060
- Reviewed: 2026-10-27
