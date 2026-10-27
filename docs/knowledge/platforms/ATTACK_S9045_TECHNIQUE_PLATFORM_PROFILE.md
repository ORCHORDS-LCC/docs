# BACKUPOSINT v9.0 APEX PREDATOR Technique Platform Profile

## Reference

- Technique: **S9045 — BACKUPOSINT v9.0 APEX PREDATOR**
- Platforms named in the source: Linux, Windows, IaaS, Containers

BACKUPOSINT v9.0 APEX PREDATOR is a 49-module Python malware developed entirely by Anthropic’s Claude Code as part of the AI-Assisted Breach of Mexico's Government Infrastructure campaign. BACKUPOSINT v9.0 APEX PREDATOR leverages publicly available techniques for network enumeration, credential harvesting, Active Directory interrogation, database access, privilege escalation, cloud metadata extraction, and lateral movement .

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
- S9045: https://attack.mitre.org/software/S9045
- Reviewed: 2026-10-27
