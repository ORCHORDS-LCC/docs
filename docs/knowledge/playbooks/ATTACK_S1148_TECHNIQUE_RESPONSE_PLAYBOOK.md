# Raccoon Stealer Technique Response Playbook

## Target technique

**S1148 — Raccoon Stealer**

- Platforms: Windows

Raccoon Stealer is an information stealer malware family active since at least 2019 as a malware-as-a-service offering sold in underground forums. Raccoon Stealer has experienced two periods of activity across two variants, from 2019 to March 2022, then resurfacing in a revised version in June 2022.

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
- S1148: https://attack.mitre.org/software/S1148
- Reviewed: 2026-10-27
