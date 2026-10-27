# Local Account Technique Platform Profile

## Reference

- Technique: **T1136.001 — Local Account**
- Platforms named in the source: Containers, ESXi, Linux, macOS, Network Devices, Windows

Adversaries may create a local account to maintain access to victim systems. Local accounts are those configured by an organization for use by users, remote support, services, or for administration on a single system or service. For example, with a sufficient level of access, the Windows <code>net user /add</code> command can be used to create a local account. In Linux, the `useradd` command can be used, while on macOS systems, the <code>dscl -create</code> command can be used. Local accounts may also be added to network devices, often via common Network Device CLI commands such as <code>username</code>, to ESXi servers via `esxcli system account add`, or to Kubernetes clusters using the `kubectl` utility. Adversaries may also create new local accounts on network firewall management consoles – for example, by exploiting a vulnerable firewall management system, threat actors may be able to establish super-admin accounts that could be used to modify firewall rules and gain further access to the network. Such accounts may be used to establish secondary credentialed access that do not require persistent remote access tools to be deployed on the system.

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
- T1136.001: https://attack.mitre.org/techniques/T1136/001
- Reviewed: 2026-10-27
