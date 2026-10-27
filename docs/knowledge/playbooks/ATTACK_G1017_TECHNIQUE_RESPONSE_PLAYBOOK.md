# Volt Typhoon Technique Response Playbook

## Target technique

**G1017 — Volt Typhoon**


Volt Typhoon is a People's Republic of China (PRC) state-sponsored actor that has been active since at least 2021, primarily targeting critical infrastructure organizations in the US and its territories including Guam. Volt Typhoon's targeting and pattern of behavior have been assessed as pre-positioning to enable lateral movement to operational technology (OT) assets for potential destructive or disruptive attacks. Volt Typhoon has emphasized stealth in operations using web shells, living-off-the-land (LOTL) binaries, hands on keyboard activities, and stolen credentials.. The group has leveraged compromised SOHO routers to proxy command and control traffic and obscure its infrastructure, activity associated with the KV botnet.. Reporting indicates a separate initial access cluster, SYLVANITE, has been observed exploiting internet-facing edge devices and transferring access to Volt Typhoon, also tracked as VOLTZITE, for follow-on operations.

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
- G1017: https://attack.mitre.org/groups/G1017
- Reviewed: 2026-10-27
