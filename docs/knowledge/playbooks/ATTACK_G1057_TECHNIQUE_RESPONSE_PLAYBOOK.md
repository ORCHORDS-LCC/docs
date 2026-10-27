# ShinyHunters Technique Response Playbook

## Target technique

**G1057 — ShinyHunters**


ShinyHunters is a cyber criminal collective that has been active since at least 2019 operating under the ShinyCorp persona. ShinyHunters has targeted multiple industries and geographic regions gathering legitimate credentials and personally identifiable information (PII) for resale or extortion of victims. ShinyHunters has been associated with the broader collective called The Community, also known as The Com whose members have also included Scattered Spider and LAPSUS$. Public reporting has mentioned a variety of names for operations ShinyHunters members have reportedly conducted with members of other groups, including “Scattered Lapsus Hunters,” “Scattered Lapsus Shiny Hunters,” and “SLSH.”.

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
- G1057: https://attack.mitre.org/groups/G1057
- Reviewed: 2026-10-27
