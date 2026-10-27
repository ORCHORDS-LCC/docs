# Analytic 0456 Technique Platform Profile

## Reference

- Technique: **AN0456 — Analytic 0456**
- Platforms named in the source: Linux

Chain: (1) interactive/non-interactive `chage -l`, `grep`/`cat` of PAM config (e.g., `/etc/pam.d/common-password`, `/etc/security/pwquality.conf`); (2) optional reads of `/etc/login.defs`; (3) same user performs account enumeration or password change attempts shortly after. Use auditd `execve` and file read events plus shell history collection.

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
- AN0456: https://attack.mitre.org/detectionstrategies/DET0161#AN0456
- Reviewed: 2026-10-27
