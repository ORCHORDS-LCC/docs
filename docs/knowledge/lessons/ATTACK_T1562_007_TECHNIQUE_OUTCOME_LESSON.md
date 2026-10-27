# T1562.007 Disable or Modify Cloud Firewall Outcome Lesson

## Authoritative description

- Technique: **T1562.007 — Disable or Modify Cloud Firewall**
- Tactics: stealth
- Platforms: IaaS

Adversaries may disable or modify a firewall within a cloud environment to bypass controls that limit access to cloud resources. Cloud firewalls are separate from system firewalls that are described in Disable or Modify System Firewall. Cloud environments typically utilize restrictive security groups and firewall rules that only allow network activity from trusted IP addresses via expected ports and protocols. An adversary with appropriate permissions may introduce new firewall rules or policies to allow access into a victim cloud environment and/or move laterally from the cloud control plane to the data plane. For example, an adversary may use a script or utility that creates new ingress rules in existing security groups (or creates new security groups entirely) to allow any TCP/IP connectivity to a cloud-hosted instance. They may also remove networking limitations to support traffic associated with malicious activity (such as cryptomining). Modifying or disabling a cloud firewall may enable adversary C2 communications, lateral movement, and/or data exfiltration that would otherwise not be allowed. It may also be used to open up resources for Brute Force or Endpoint Denial of Service.

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
- T1562.007: https://attack.mitre.org/techniques/T1562/007
- Reviewed: 2026-10-27

## Boundary

This lesson is derived from the published technique description. It does not invent an incident, prescribe one implementation, or claim the technique has been addressed.
