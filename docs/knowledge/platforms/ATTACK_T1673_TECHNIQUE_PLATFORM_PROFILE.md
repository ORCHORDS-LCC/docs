# Virtual Machine Discovery Technique Platform Profile

## Reference

- Technique: **T1673 — Virtual Machine Discovery**
- Platforms named in the source: ESXi, Linux, macOS, Windows

An adversary may attempt to enumerate running virtual machines (VMs) after gaining access to a host or hypervisor. For example, adversaries may enumerate a list of VMs on an ESXi hypervisor using a Hypervisor CLI such as `esxcli` or `vim-cmd` (e.g. `esxcli vm process list or vim-cmd vmsvc/getallvms`). Adversaries may also directly leverage a graphical user interface, such as VMware vCenter, in order to view virtual machines on a host. Adversaries may use the information from Virtual Machine Discovery during discovery to shape follow-on behaviors. Subsequently discovered VMs may be leveraged for follow-on activities such as Service Stop or Data Encrypted for Impact.

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
- T1673: https://attack.mitre.org/techniques/T1673
- Reviewed: 2026-10-27
