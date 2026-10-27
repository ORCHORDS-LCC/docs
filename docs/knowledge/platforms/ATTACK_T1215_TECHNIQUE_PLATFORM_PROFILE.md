# Kernel Modules and Extensions Mitigation Technique Platform Profile

## Reference

- Technique: **T1215 — Kernel Modules and Extensions Mitigation**
- Platforms named in the source: not stated

Common tools for detecting Linux rootkits include: rkhunter , chrootkit , although rootkits may be designed to evade certain detection tools. LKMs and Kernel extensions require root level permissions to be installed. Limit access to the root account and prevent users from loading kernel modules and extensions through proper privilege separation and limiting Privilege Escalation opportunities. Application whitelisting and software restriction tools, such as SELinux, can also aide in restricting kernel module loading.

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
- T1215: https://attack.mitre.org/mitigations/T1215
- Reviewed: 2026-10-27
