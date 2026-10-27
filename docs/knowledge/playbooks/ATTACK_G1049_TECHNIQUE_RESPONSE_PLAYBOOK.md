# AppleJeus Technique Response Playbook

## Target technique

**G1049 — AppleJeus**


AppleJeus is a North Korean state-sponsored threat group attributed to the Reconnaissance General Bureau. Associated with the broader Lazarus Group umbrella of actors, AppleJeus has been active since at least 2018 and is closely aligned in resources with TEMP.hermit, another DPRK-affiliated group under the same umbrella. The group’s primary mission is to generate and launder revenue to provide financial support to the government. AppleJeus primarily targets the cryptocurrency industry and is most notably responsible for the 3CX Supply Chain Attack. The group traditionally deploys malicious cryptocurrency software in combination with Phishing. From these compromised environments, it selectively deploys additional backdoors to enable extended operations against high-value financial targets.

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
- G1049: https://attack.mitre.org/groups/G1049
- Reviewed: 2026-10-27
