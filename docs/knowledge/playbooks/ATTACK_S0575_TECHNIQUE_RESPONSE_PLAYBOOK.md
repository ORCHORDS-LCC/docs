# Conti Technique Response Playbook

## Target technique

**S0575 — Conti**

- Platforms: Windows

Conti is a Ransomware-as-a-Service (RaaS) that was first observed in December 2019. Conti has been deployed via TrickBot and used against major corporations and government agencies, particularly those in North America. As with other ransomware families, actors using Conti steal sensitive files and information from compromised networks, and threaten to publish this data unless the ransom is paid.

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
- S0575: https://attack.mitre.org/software/S0575
- Reviewed: 2026-10-27
