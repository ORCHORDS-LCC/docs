# Defacement Mitigation Technique Platform Profile

## Reference

- Technique: **T1491 — Defacement Mitigation**
- Platforms named in the source: not stated

Implementing best practices for websites such as defending against Exploit Public-Facing Application . Consider implementing IT disaster recovery plans that contain procedures for taking regular data backups that can be used to restore organizational data. (Ready.gov IT DRP) Ensure backups are stored off system and is protected from common methods adversaries may use to gain access and destroy the backups to prevent recovery.

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
- T1491: https://attack.mitre.org/mitigations/T1491
- Reviewed: 2026-10-27
