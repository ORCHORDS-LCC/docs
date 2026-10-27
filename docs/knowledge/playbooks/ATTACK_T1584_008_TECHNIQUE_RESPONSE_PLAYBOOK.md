# Network Devices Technique Response Playbook

## Target technique

**T1584.008 — Network Devices**

- Tactics: resource-development
- Platforms: PRE

Adversaries may compromise third-party network devices that can be used during targeting. Network devices, such as small office/home office (SOHO) routers, may be compromised where the adversary's ultimate goal is not Initial Access to that environment, but rather to leverage these devices to support additional targeting. Once an adversary has control, compromised network devices can be used to launch additional operations, such as hosting payloads for Phishing campaigns (i.e., Link Target) or enabling the required access to execute Content Injection operations. Adversaries may also be able to harvest reusable credentials (i.e., Valid Accounts) from compromised network devices. Adversaries often target Internet-facing edge devices and related network appliances that specifically do not support robust host-based defenses. Compromised network devices may be used to support subsequent Command and Control activity, such as Hide Infrastructure through an established Proxy and/or Botnet network.

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
- T1584.008: https://attack.mitre.org/techniques/T1584/008
- Reviewed: 2026-10-27
