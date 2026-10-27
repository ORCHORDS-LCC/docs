# Additional Local or Domain Groups Technique Platform Profile

## Reference

- Technique: **T1098.007 — Additional Local or Domain Groups**
- Platforms named in the source: Windows, macOS, Linux

An adversary may add additional local or domain groups to an adversary-controlled account to maintain persistent access to a system or domain. On Windows, accounts may use the `net localgroup` and `net group` commands to add existing users to local and domain groups. On Linux, adversaries may use the `usermod` command for the same purpose. For example, accounts may be added to the local administrators group on Windows devices to maintain elevated privileges. They may also be added to the Remote Desktop Users group, which allows them to leverage Remote Desktop Protocol to log into the endpoints in the future. Adversaries may also add accounts to VPN user groups to gain future persistence on the network. On Linux, accounts may be added to the sudoers group, allowing them to persistently leverage Sudo and Sudo Caching for elevated privileges. In Windows environments, machine accounts may also be added to domain groups. This allows the local SYSTEM account to gain privileges on the domain.

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
- T1098.007: https://attack.mitre.org/techniques/T1098/007
- Reviewed: 2026-10-27
