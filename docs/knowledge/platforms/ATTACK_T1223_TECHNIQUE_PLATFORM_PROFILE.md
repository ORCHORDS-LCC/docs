# Compiled HTML File Mitigation Technique Platform Profile

## Reference

- Technique: **T1223 — Compiled HTML File Mitigation**
- Platforms named in the source: not stated

Consider blocking download/transfer and execution of potentially uncommon file types known to be used in adversary campaigns, such as CHM files. Also consider using application whitelisting to prevent execution of hh.exe if it is not required for a given system or network to prevent potential misuse by adversaries.

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
- T1223: https://attack.mitre.org/mitigations/T1223
- Reviewed: 2026-10-27
