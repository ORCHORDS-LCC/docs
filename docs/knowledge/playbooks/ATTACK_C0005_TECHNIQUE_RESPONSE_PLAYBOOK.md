# Operation Spalax Technique Response Playbook

## Target technique

**C0005 — Operation Spalax**


Operation Spalax was a campaign that primarily targeted Colombian government organizations and private companies, particularly those associated with the energy and metallurgical industries. The Operation Spalax threat actors distributed commodity malware and tools using generic phishing topics related to COVID-19, banking, and law enforcement action. Security researchers noted indicators of compromise and some infrastructure overlaps with other campaigns dating back to April 2018, including at least one separately attributed to APT-C-36, however identified enough differences to report this as separate, unattributed activity.

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
- C0005: https://attack.mitre.org/campaigns/C0005
- Reviewed: 2026-10-27
