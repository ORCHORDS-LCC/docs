# DarkGate Technique Response Playbook

## Target technique

**S1111 — DarkGate**

- Platforms: Windows

DarkGate first emerged in 2018 and has evolved into an initial access and data gathering tool associated with various criminal cyber operations. Written in Delphi and named "DarkGate" by its author, DarkGate is associated with credential theft, cryptomining, cryptotheft, and pre-ransomware actions. DarkGate use increased significantly starting in 2022 and is under active development by its author, who provides it as a Malware-as-a-Service offering.

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
- S1111: https://attack.mitre.org/software/S1111
- Reviewed: 2026-10-27
