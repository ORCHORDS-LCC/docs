# Disable or Modify Linux Audit System Log Technique Platform Profile

## Reference

- Technique: **T1685.004 — Disable or Modify Linux Audit System Log**
- Platforms named in the source: Linux

Adversaries may disable or modify the Linux Audit system to hide malicious activity and avoid detection. Linux admins use the Linux Audit system to track security-relevant information on a system. The Linux Audit system operates at the kernel-level and maintains event logs on application and system activity such as process, network, file, and login events based on pre-configured rules. Often referred to as `auditd`, this is the name of the daemon used to write events to disk and is governed by the parameters set in the `audit.conf` configuration file. Two primary ways to configure the log generation rules are through the command line `auditctl` utility and the file `/etc/audit/audit.rules`, containing a sequence of `auditctl` commands loaded at boot time. With root privileges, adversaries may be able to ensure their activity is not logged through disabling the Audit system service, editing the configuration/rule files, or by hooking the Audit system library functions. Using the command line, adversaries can disable the Audit system service through killing processes associated with `auditd` daemon or use `systemctl` to stop the Audit service. Adversaries can also hook Audit system functions to disable logging or modify the rules contained in the `/etc/audit/audit.rules` or `audit.conf` files to ignore malicious activity.

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
- T1685.004: https://attack.mitre.org/techniques/T1685/004
- Reviewed: 2026-10-27
