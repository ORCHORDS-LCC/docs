# Disable or Modify Network Device Firewall Technique Response Playbook

## Target technique

**T1562.013 — Disable or Modify Network Device Firewall**

- Tactics: stealth
- Platforms: Network Devices

Adversaries may disable network device-based firewall mechanisms entirely or add, delete, or modify particular rules in order to bypass controls limiting network usage. Modifying or disabling a network firewall may enable adversary C2 communications, lateral movement, and/or data exfiltration that would otherwise not be allowed. For example, adversaries may add new network firewall rules to allow access to all internal network subnets without restrictions. Adversaries may gain access to the firewall management console via Valid Accounts or by exploiting a vulnerability. In some cases, threat actors may target firewalls that have been exposed to the internet Exploit Public-Facing Application.

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
- T1562.013: https://attack.mitre.org/techniques/T1562/013
- Reviewed: 2026-10-27
