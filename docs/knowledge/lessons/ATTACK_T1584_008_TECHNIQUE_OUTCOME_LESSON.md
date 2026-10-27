# T1584.008 Network Devices Outcome Lesson

## Authoritative description

- Technique: **T1584.008 — Network Devices**
- Tactics: resource-development
- Platforms: PRE

Adversaries may compromise third-party network devices that can be used during targeting. Network devices, such as small office/home office (SOHO) routers, may be compromised where the adversary's ultimate goal is not Initial Access to that environment, but rather to leverage these devices to support additional targeting. Once an adversary has control, compromised network devices can be used to launch additional operations, such as hosting payloads for Phishing campaigns (i.e., Link Target) or enabling the required access to execute Content Injection operations. Adversaries may also be able to harvest reusable credentials (i.e., Valid Accounts) from compromised network devices. Adversaries often target Internet-facing edge devices and related network appliances that specifically do not support robust host-based defenses. Compromised network devices may be used to support subsequent Command and Control activity, such as Hide Infrastructure through an established Proxy and/or Botnet network.

## Reusable lesson

This technique should be treated as an explicit review question when it is relevant to the system or organisation, rather than assumed to be covered by a generic control statement or by tooling that reports a related signal.

## Apply the lesson

1. Define the real scope before judging coverage.
2. Inspect current technical, process, governance, or operational evidence.
3. Separate documented intent from verified behaviour.
4. Record partial coverage and unresolved gaps instead of converting them into a pass.
5. Revisit when the underlying scope, threat environment, technology, suppliers, or mission materially changes.

## Source

- MITRE ATT&CK: https://attack.mitre.org/
- T1584.008: https://attack.mitre.org/techniques/T1584/008
- Reviewed: 2026-10-27

## Boundary

This lesson is derived from the published technique description. It does not invent an incident, prescribe one implementation, or claim the technique has been addressed.
