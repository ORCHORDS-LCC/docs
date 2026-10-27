# Network Device Firewall Technique Platform Profile

## Reference

- Technique: **T1686.002 — Network Device Firewall**
- Platforms named in the source: Network Devices

Adversaries may disable network device-based firewall mechanisms entirely or add, delete, or modify particular rules in order to bypass controls limiting network usage. Adversaries may obtain access to devices such as routers, switches, or other perimeter/network devices and change access control lists (ACLs), security zones, or policy rules to permit otherwise blocked traffic. For example, adversaries may add new network firewall rules to allow access to all internal network subnets without restrictions. Allowing access to internal network subsets may enable unrestricted inbound/outbound connectivity or open paths for command and control and lateral movement. Adversaries may obtain access to network device management interfaces via Valid Accounts or by exploiting vulnerabilities. In some cases, threat actors may target firewalls and other network infrastructure that are exposed to the internet by leveraging weaknesses in public-facing applications (Exploit Public-Facing Application). Adversaries may also modify host networking configurations that indirectly manipulate system firewalls, such as adjusting interface bandwidth or network connection request thresholds.

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
- T1686.002: https://attack.mitre.org/techniques/T1686/002
- Reviewed: 2026-10-27
