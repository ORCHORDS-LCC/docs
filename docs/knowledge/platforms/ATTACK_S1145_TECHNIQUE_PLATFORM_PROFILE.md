# Pikabot Technique Platform Profile

## Reference

- Technique: **S1145 — Pikabot**
- Platforms named in the source: Windows

Pikabot is a backdoor used for initial access and follow-on tool deployment active since early 2023. Pikabot is notable for extensive use of multiple encoding, encryption, and defense evasion mechanisms to evade defenses and avoid analysis. Pikabot has some overlaps with QakBot, but insufficient evidence exists to definitively link these two malware families. Pikabot is frequently used to deploy follow on tools such as Cobalt Strike or ransomware variants.

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
- S1145: https://attack.mitre.org/software/S1145
- Reviewed: 2026-10-27
