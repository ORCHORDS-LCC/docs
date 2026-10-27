# Windows Host Firewall Technique Operationalization Review

## Reference

- Technique: **T1686.003 — Windows Host Firewall**

Adversaries may disable or modify the Windows host firewall to bypass controls limiting network usage. This can include disabling the Windows host firewall entirely, suppressing specific profiles (domain, private, public), or adding, deleting, and modifying firewall rules to allow or restrict traffic. Adversaries may perform these modifications through multiple mechanisms depending on the Windows operating system and access level. For example, adversaries may use command-line utilities (e.g., `netsh advfirewall` or PowerShell cmdlets like `Set-NetFirewallProfile`, `New-NetFirewallRule`), Windows Registry modifications (e.g., altering firewall states and rule configurations via registry keys), or the Windows Control Panel to modify firewall settings through the Windows Security interface. By disabling or modifying Windows firewall services, adversaries may enable access to remote services, open ports for command and control traffic, or configure rules for further actions.

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
- T1686.003: https://attack.mitre.org/techniques/T1686/003
- Reviewed: 2026-10-27
