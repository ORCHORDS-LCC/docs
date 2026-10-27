# Taint Shared Content Mitigation Technique Platform Profile

## Reference

- Technique: **T1080 — Taint Shared Content Mitigation**
- Platforms named in the source: not stated

Protect shared folders by minimizing users who have write access. Use utilities that detect or mitigate common features used in exploitation, such as the Microsoft Enhanced Mitigation Experience Toolkit (EMET). Reduce potential lateral movement risk by using web-based document management and collaboration services that do not use network file and directory sharing. Identify potentially malicious software that may be used to taint content or may result from it and audit and/or block the unknown programs by using whitelisting tools, like AppLocker, or Software Restriction Policies where appropriate.

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
- T1080: https://attack.mitre.org/mitigations/T1080
- Reviewed: 2026-10-27
