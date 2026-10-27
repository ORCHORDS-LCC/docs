# Disable or Modify Network Device Firewall Technique Platform Profile

## Reference

- Technique: **T1562.013 — Disable or Modify Network Device Firewall**
- Platforms named in the source: Network Devices

Adversaries may disable network device-based firewall mechanisms entirely or add, delete, or modify particular rules in order to bypass controls limiting network usage. Modifying or disabling a network firewall may enable adversary C2 communications, lateral movement, and/or data exfiltration that would otherwise not be allowed. For example, adversaries may add new network firewall rules to allow access to all internal network subnets without restrictions. Adversaries may gain access to the firewall management console via Valid Accounts or by exploiting a vulnerability. In some cases, threat actors may target firewalls that have been exposed to the internet Exploit Public-Facing Application.

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
- T1562.013: https://attack.mitre.org/techniques/T1562/013
- Reviewed: 2026-10-27
