# WIRTE Technique Response Playbook

## Target technique

**G0090 — WIRTE**


WIRTE is a cyberespionage actor, believed to be a subgroup of the Hamas-affiliated Gaza Cybergang, that has been active since at least August 2018. WIRTE has targeted diplomatic, financial, military, legal, and technology organizations across the Middle East, North Africa, and in Europe to gather intelligence. WIRTE has remained persistently active despite the ongoing Israel-Hamas conflict and has expanded their operations to include wiper malware attacks against Israeli targets.

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
- G0090: https://attack.mitre.org/groups/G0090
- Reviewed: 2026-10-27
