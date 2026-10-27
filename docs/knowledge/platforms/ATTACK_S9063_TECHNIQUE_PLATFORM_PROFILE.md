# DEEPROOT Technique Platform Profile

## Reference

- Technique: **S9063 — DEEPROOT**
- Platforms named in the source: Linux

DEEPROOT is a Linux backdoor written in Golang. DEEPROOT is able to execute commands via a shell, enumerate systems, delete or download files, and exfiltrate data. DEEPROOT was first observed in 2025. DEEPROOT has been affiliated with the cyber espionage threat group NIMBUS MANTICORE.

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
- S9063: https://attack.mitre.org/software/S9063
- Reviewed: 2026-10-27
