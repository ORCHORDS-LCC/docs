# Disable or Modify Cloud Firewall Technique Operationalization Review

## Reference

- Technique: **T1562.007 — Disable or Modify Cloud Firewall**

Adversaries may disable or modify a firewall within a cloud environment to bypass controls that limit access to cloud resources. Cloud firewalls are separate from system firewalls that are described in Disable or Modify System Firewall. Cloud environments typically utilize restrictive security groups and firewall rules that only allow network activity from trusted IP addresses via expected ports and protocols. An adversary with appropriate permissions may introduce new firewall rules or policies to allow access into a victim cloud environment and/or move laterally from the cloud control plane to the data plane. For example, an adversary may use a script or utility that creates new ingress rules in existing security groups (or creates new security groups entirely) to allow any TCP/IP connectivity to a cloud-hosted instance. They may also remove networking limitations to support traffic associated with malicious activity (such as cryptomining). Modifying or disabling a cloud firewall may enable adversary C2 communications, lateral movement, and/or data exfiltration that would otherwise not be allowed. It may also be used to open up resources for Brute Force or Endpoint Denial of Service.

## Operationalization review

1. Record the operational scope: which services, environments, and data the technique could affect.
2. Record the runbook that would be executed, and its owner.
3. Record the telemetry the runbook depends on, and whether it is retained long enough to investigate.
4. Record the detection that would surface the technique before or after it has an effect.
5. Record the recovery path, and the evidence that recovery has been rehearsed.
6. Record the residual operational risk where the runbook depends on a manual step.

## Review evidence

- the runbook and its owner;
- the telemetry retention and coverage record;
- the detection mapping;
- the exercise or rehearsal record.

## Limitations

An operationalization review describes the runbook and the evidence around it. It does not claim the technique has been prevented or detected in a live environment.

## Source

- MITRE ATT&CK: https://attack.mitre.org/
- T1562.007: https://attack.mitre.org/techniques/T1562/007
- Reviewed: 2026-10-27
