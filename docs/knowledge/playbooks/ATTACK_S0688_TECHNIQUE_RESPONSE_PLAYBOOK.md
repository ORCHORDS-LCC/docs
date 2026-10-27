# Meteor Technique Response Playbook

## Target technique

**S0688 — Meteor**

- Platforms: Windows

Meteor is a wiper that was used against Iranian government organizations, including Iranian Railways, the Ministry of Roads, and Urban Development systems, in July 2021. Meteor is likely a newer version of similar wipers called Stardust and Comet that were reportedly used by a group called "Indra" since at least 2019 against private companies in Syria.

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
- S0688: https://attack.mitre.org/software/S0688
- Reviewed: 2026-10-27
