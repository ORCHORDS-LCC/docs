# FLORAHOX Activity Technique Response Playbook

## Target technique

**C0053 — FLORAHOX Activity**


FLORAHOX Activity is conducted using a hybrid operational relay box (ORB) network, which combines two types of infrastructure: compromised devices and leased Virtual Private Servers (VPS). The compromised devices include end-of-life routers and IoT devices, while VPS space is commercially leased and managed by ORB network administrators. This hybrid ORB network allows adversaries to proxy and obscure malicious traffic, making the source of the traffic more difficult to trace. The FLORAHOX ORB network has been leveraged by multiple cyber threat actors, including China-nexus actors like ZIRCONIUM. These adversaries conduct espionage campaigns through FLORAHOX Activity, relying on the ORB network's ability to funnel traffic through Tor nodes, provisioned VPS servers, and compromised routers to obfuscate malicious traffic.

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
- C0053: https://attack.mitre.org/campaigns/C0053
- Reviewed: 2026-10-27
