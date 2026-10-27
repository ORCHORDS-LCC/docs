# Relocate Malware Technique Platform Profile

## Reference

- Technique: **T1070.010 — Relocate Malware**
- Platforms named in the source: Linux, macOS, Network Devices, Windows

Once a payload is delivered, adversaries may reproduce copies of the same malware on the victim system to remove evidence of their presence and/or avoid defenses. Copying malware payloads to new locations may also be combined with File Deletion to cleanup older artifacts. Relocating malware may be a part of many actions intended to evade defenses. For example, adversaries may copy and rename payloads to better blend into the local environment (i.e., Match Legitimate Resource Name or Location). Payloads may also be repositioned to target File/Path Exclusions as well as specific locations associated with establishing Persistence. Relocating malicious payloads may also hinder defensive analysis, especially to separate these payloads from earlier events (such as User Execution and Phishing) that may have generated alerts or otherwise drawn attention from defenders. Moving payloads into target directories does not alter the Creation timestamp, thereby evading detection logic reliant on modifications to this artifact (i.e., Timestomp).

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
- T1070.010: https://attack.mitre.org/techniques/T1070/010
- Reviewed: 2026-10-27
