# Windows Host Firewall Technique Engineering Review

## Reference

- Technique: **T1686.003 — Windows Host Firewall**

Adversaries may disable or modify the Windows host firewall to bypass controls limiting network usage. This can include disabling the Windows host firewall entirely, suppressing specific profiles (domain, private, public), or adding, deleting, and modifying firewall rules to allow or restrict traffic. Adversaries may perform these modifications through multiple mechanisms depending on the Windows operating system and access level. For example, adversaries may use command-line utilities (e.g., `netsh advfirewall` or PowerShell cmdlets like `Set-NetFirewallProfile`, `New-NetFirewallRule`), Windows Registry modifications (e.g., altering firewall states and rule configurations via registry keys), or the Windows Control Panel to modify firewall settings through the Windows Security interface. By disabling or modifying Windows firewall services, adversaries may enable access to remote services, open ports for command and control traffic, or configure rules for further actions.

## Engineering review

1. Identify the engineering boundary where the technique would apply: the component, the service, or the deployment.
2. Review the design decision that would prevent the technique, and record the alternative considered.
3. Review the implementation evidence for the preventive control.
4. Review the test coverage that would fail if the control regressed.
5. Review the observability: which signal would show the control is not operating.
6. Record the residual risk where prevention is not achievable, and the detection that compensates.

## Review evidence

- the design record for the preventive decision;
- the implementation or configuration evidence;
- the test record showing the control is exercised;
- the observability mapping.

## Limitations

An engineering review describes what the design and the implementation evidence show. It does not claim the technique has been addressed in production.

## Source

- MITRE ATT&CK: https://attack.mitre.org/
- T1686.003: https://attack.mitre.org/techniques/T1686/003
- Reviewed: 2026-10-27
