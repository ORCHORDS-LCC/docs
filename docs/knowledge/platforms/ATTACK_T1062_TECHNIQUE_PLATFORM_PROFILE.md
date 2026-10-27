# Hypervisor Technique Platform Profile

## Reference

- Technique: **T1062 — Hypervisor**
- Platforms named in the source: Windows

**This technique has been deprecated and should no longer be used.** A type-1 hypervisor is a software layer that sits between the guest operating systems and system's hardware. It presents a virtual running environment to an operating system. An example of a common hypervisor is Xen. A type-1 hypervisor operates at a level below the operating system and could be designed with Rootkit functionality to hide its existence from the guest operating system. A malicious hypervisor of this nature could be used to persist on systems through interruption.

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
- T1062: https://attack.mitre.org/techniques/T1062
- Reviewed: 2026-10-27
