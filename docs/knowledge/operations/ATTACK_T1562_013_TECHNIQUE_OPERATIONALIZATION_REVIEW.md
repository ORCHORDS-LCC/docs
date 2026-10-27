# Disable or Modify Network Device Firewall Technique Operationalization Review

## Reference

- Technique: **T1562.013 — Disable or Modify Network Device Firewall**

Adversaries may disable network device-based firewall mechanisms entirely or add, delete, or modify particular rules in order to bypass controls limiting network usage. Modifying or disabling a network firewall may enable adversary C2 communications, lateral movement, and/or data exfiltration that would otherwise not be allowed. For example, adversaries may add new network firewall rules to allow access to all internal network subnets without restrictions. Adversaries may gain access to the firewall management console via Valid Accounts or by exploiting a vulnerability. In some cases, threat actors may target firewalls that have been exposed to the internet Exploit Public-Facing Application.

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
- T1562.013: https://attack.mitre.org/techniques/T1562/013
- Reviewed: 2026-10-27
