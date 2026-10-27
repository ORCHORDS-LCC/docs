# Network Device Firewall Technique Operationalization Review

## Reference

- Technique: **T1686.002 — Network Device Firewall**

Adversaries may disable network device-based firewall mechanisms entirely or add, delete, or modify particular rules in order to bypass controls limiting network usage. Adversaries may obtain access to devices such as routers, switches, or other perimeter/network devices and change access control lists (ACLs), security zones, or policy rules to permit otherwise blocked traffic. For example, adversaries may add new network firewall rules to allow access to all internal network subnets without restrictions. Allowing access to internal network subsets may enable unrestricted inbound/outbound connectivity or open paths for command and control and lateral movement. Adversaries may obtain access to network device management interfaces via Valid Accounts or by exploiting vulnerabilities. In some cases, threat actors may target firewalls and other network infrastructure that are exposed to the internet by leveraging weaknesses in public-facing applications (Exploit Public-Facing Application). Adversaries may also modify host networking configurations that indirectly manipulate system firewalls, such as adjusting interface bandwidth or network connection request thresholds.

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
- T1686.002: https://attack.mitre.org/techniques/T1686/002
- Reviewed: 2026-10-27
