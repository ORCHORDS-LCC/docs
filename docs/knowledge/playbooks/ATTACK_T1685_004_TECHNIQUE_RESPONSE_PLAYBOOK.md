# Disable or Modify Linux Audit System Log Technique Response Playbook

## Target technique

**T1685.004 — Disable or Modify Linux Audit System Log**

- Tactics: defense-impairment
- Platforms: Linux

Adversaries may disable or modify the Linux Audit system to hide malicious activity and avoid detection. Linux admins use the Linux Audit system to track security-relevant information on a system. The Linux Audit system operates at the kernel-level and maintains event logs on application and system activity such as process, network, file, and login events based on pre-configured rules. Often referred to as `auditd`, this is the name of the daemon used to write events to disk and is governed by the parameters set in the `audit.conf` configuration file. Two primary ways to configure the log generation rules are through the command line `auditctl` utility and the file `/etc/audit/audit.rules`, containing a sequence of `auditctl` commands loaded at boot time. With root privileges, adversaries may be able to ensure their activity is not logged through disabling the Audit system service, editing the configuration/rule files, or by hooking the Audit system library functions. Using the command line, adversaries can disable the Audit system service through killing processes associated with `auditd` daemon or use `systemctl` to stop the Audit service. Adversaries can also hook Audit system functions to disable logging or modify the rules contained in the `/etc/audit/audit.rules` or `audit.conf` files to ignore malicious activity.

## Preconditions

- the estate in scope is identified, with the systems the technique could apply to;
- an owner is accountable for detection and response;
- current telemetry and configuration can be inspected;
- the technique is applicable or requires an applicability decision.

## Procedure

1. Confirm the scope and owner.
2. Read the current technique description and the associated detection guidance.
3. Inventory the telemetry that would carry the technique's indicators.
4. Inspect whether the indicators are present in the environment.
5. Exercise the detection path and confirm it produces the expected signal.
6. Record gaps in detection coverage and assign remediation owners.
7. Record justified non-applicability or accepted detection gaps separately.
8. Set the next event-driven or periodic verification trigger.

## Failure handling

If the detection path does not produce the expected signal, treat the coverage as unverified, preserve the test evidence, and route the gap through the appropriate remediation or risk process.

## Completion evidence

Scope, owner, source version, telemetry inspected, tests performed, findings, exceptions, remediation links, reviewer, and next trigger.

## Source

- MITRE ATT&CK: https://attack.mitre.org/
- T1685.004: https://attack.mitre.org/techniques/T1685/004
- Reviewed: 2026-10-27
