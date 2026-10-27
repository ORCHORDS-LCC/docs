# Cron Technique Platform Profile

## Reference

- Technique: **T1053.003 — Cron**
- Platforms named in the source: Linux, macOS, ESXi

Adversaries may abuse the <code>cron</code> utility to perform task scheduling for initial or recurring execution of malicious code. The <code>cron</code> utility is a time-based job scheduler for Unix-like operating systems. The <code> crontab</code> file contains the schedule of cron entries to be run and the specified times for execution. Any <code>crontab</code> files are stored in operating system-specific file paths. An adversary may use <code>cron</code> in Linux or Unix environments to execute programs at system startup or on a scheduled basis for Persistence. In ESXi environments, cron jobs must be created directly via the crontab file (e.g., `/var/spool/cron/crontabs/root`).

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
- T1053.003: https://attack.mitre.org/techniques/T1053/003
- Reviewed: 2026-10-27
