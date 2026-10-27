# C0021 Technique Response Playbook

## Target technique

**C0021 — C0021**


C0021 was a spearphishing campaign conducted in November 2018 that targeted public sector institutions, non-governmental organizations (NGOs), educational institutions, and private-sector corporations in the oil and gas, chemical, and hospitality industries. The majority of targets were located in the US, particularly in and around Washington D.C., with other targets located in Europe, Hong Kong, India, and Canada. C0021's technical artifacts, tactics, techniques, and procedures (TTPs), and targeting overlap with previous suspected APT29 activity.

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
- C0021: https://attack.mitre.org/campaigns/C0021
- Reviewed: 2026-10-27
