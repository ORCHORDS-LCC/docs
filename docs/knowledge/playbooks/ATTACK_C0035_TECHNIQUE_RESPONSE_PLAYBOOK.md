# KV Botnet Activity Technique Response Playbook

## Target technique

**C0035 — KV Botnet Activity**


KV Botnet Activity consisted of exploitation of primarily “end-of-life” small office-home office (SOHO) equipment from manufacturers such as Cisco, NETGEAR, and DrayTek. KV Botnet Activity was used by Volt Typhoon to obfuscate connectivity to victims in multiple critical infrastructure segments, including energy and telecommunication companies and entities based on the US territory of Guam. While the KV Botnet is the most prominent element of this campaign, it overlaps with another botnet cluster referred to as the JDY cluster. This botnet was disrupted by US law enforcement entities in early 2024 after periods of activity from October 2022 through January 2024.

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
- C0035: https://attack.mitre.org/campaigns/C0035
- Reviewed: 2026-10-27
