# IP Addresses Technique Response Playbook

## Target technique

**T1590.005 — IP Addresses**

- Tactics: reconnaissance
- Platforms: PRE

Adversaries may gather the victim's IP addresses that can be used during targeting. Public IP addresses may be allocated to organizations by block, or a range of sequential addresses. Information about assigned IP addresses may include a variety of details, such as which IP addresses are in use. IP addresses may also enable an adversary to derive other details about a victim, such as organizational size, physical location(s), Internet service provider, and or where/how their publicly-facing infrastructure is hosted. Adversaries may gather this information in various ways, such as direct collection actions via Active Scanning or Phishing for Information. Information about assigned IP addresses may also be exposed to adversaries via online or other accessible data sets (ex: Search Open Technical Databases). Gathering this information may reveal opportunities for other forms of reconnaissance (ex: Active Scanning or Search Open Websites/Domains), establishing operational resources (ex: Acquire Infrastructure or Compromise Infrastructure), and/or initial access (ex: External Remote Services).

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
- T1590.005: https://attack.mitre.org/techniques/T1590/005
- Reviewed: 2026-10-27
