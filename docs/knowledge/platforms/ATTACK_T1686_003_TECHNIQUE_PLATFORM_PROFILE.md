# Windows Host Firewall Technique Platform Profile

## Reference

- Technique: **T1686.003 — Windows Host Firewall**
- Platforms named in the source: Windows

Adversaries may disable or modify the Windows host firewall to bypass controls limiting network usage. This can include disabling the Windows host firewall entirely, suppressing specific profiles (domain, private, public), or adding, deleting, and modifying firewall rules to allow or restrict traffic. Adversaries may perform these modifications through multiple mechanisms depending on the Windows operating system and access level. For example, adversaries may use command-line utilities (e.g., `netsh advfirewall` or PowerShell cmdlets like `Set-NetFirewallProfile`, `New-NetFirewallRule`), Windows Registry modifications (e.g., altering firewall states and rule configurations via registry keys), or the Windows Control Panel to modify firewall settings through the Windows Security interface. By disabling or modifying Windows firewall services, adversaries may enable access to remote services, open ports for command and control traffic, or configure rules for further actions.

## Platform profile

1. Record the platforms in scope and the versions actually deployed.
2. Compare the deployed platform surface against the platforms the source names.
3. Record where the platform provides a native control for the technique, and where it does not.
4. Record the configuration evidence for the native control, where one exists.
5. Record the gap where the platform provides no native control, and the compensating detection.
6. Record the platform version, because platform behaviour changes between versions.

## Evidence

- the platform and version inventory for the scoped estate;
- the configuration export or screenshot for the native control;
- the detection evidence where the platform provides none.

## Limitations

A technique entry describes a class of abuse across platforms. The platform-specific exposure is a property of the deployment, established only by inventory and configuration evidence.

## Source

- MITRE ATT&CK: https://attack.mitre.org/
- T1686.003: https://attack.mitre.org/techniques/T1686/003
- Reviewed: 2026-10-27
