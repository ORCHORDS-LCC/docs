# Turian Technique Response Playbook

## Target technique

**S0647 — Turian**

- Platforms: Windows, Linux

Turian is a backdoor that has been used by BackdoorDiplomacy to target Ministries of Foreign Affairs, telecommunication companies, and charities in Africa, Europe, the Middle East, and Asia. First reported in 2021, Turian is likely related to Quarian, an older backdoor that was last observed being used in 2013 against diplomatic targets in Syria and the United States.

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
- S0647: https://attack.mitre.org/software/S0647
- Reviewed: 2026-10-27
