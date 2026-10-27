# Brute Ratel C4 Technique Platform Profile

## Reference

- Technique: **S1063 — Brute Ratel C4**
- Platforms named in the source: Windows

Brute Ratel C4 is a commercial red-teaming and adversarial attack simulation tool that first appeared in December 2020. Brute Ratel C4 was specifically designed to avoid detection by endpoint detection and response (EDR) and antivirus (AV) capabilities, and deploys agents called badgers to enable arbitrary command execution for lateral movement, privilege escalation, and persistence. In September 2022, a cracked version of Brute Ratel C4 was leaked in the cybercriminal underground, leading to its use by threat actors.

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
- S1063: https://attack.mitre.org/software/S1063
- Reviewed: 2026-10-27
