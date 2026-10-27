# Disable or Modify Cloud Firewall Technique Response Playbook

## Target technique

**T1562.007 — Disable or Modify Cloud Firewall**

- Tactics: stealth
- Platforms: IaaS

Adversaries may disable or modify a firewall within a cloud environment to bypass controls that limit access to cloud resources. Cloud firewalls are separate from system firewalls that are described in Disable or Modify System Firewall. Cloud environments typically utilize restrictive security groups and firewall rules that only allow network activity from trusted IP addresses via expected ports and protocols. An adversary with appropriate permissions may introduce new firewall rules or policies to allow access into a victim cloud environment and/or move laterally from the cloud control plane to the data plane. For example, an adversary may use a script or utility that creates new ingress rules in existing security groups (or creates new security groups entirely) to allow any TCP/IP connectivity to a cloud-hosted instance. They may also remove networking limitations to support traffic associated with malicious activity (such as cryptomining). Modifying or disabling a cloud firewall may enable adversary C2 communications, lateral movement, and/or data exfiltration that would otherwise not be allowed. It may also be used to open up resources for Brute Force or Endpoint Denial of Service.

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
- T1562.007: https://attack.mitre.org/techniques/T1562/007
- Reviewed: 2026-10-27
