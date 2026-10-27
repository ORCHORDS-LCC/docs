# Spoof Security Alerting Technique Platform Profile

## Reference

- Technique: **T1562.011 — Spoof Security Alerting**
- Platforms named in the source: Windows, macOS, Linux

Adversaries may spoof security alerting from tools, presenting false evidence to impair defenders’ awareness of malicious activity. Messages produced by defensive tools contain information about potential security events as well as the functioning status of security software and the system. Security reporting messages are important for monitoring the normal operation of a system and identifying important events that can signal a security incident. Rather than or in addition to Indicator Blocking, an adversary can spoof positive affirmations that security tools are continuing to function even after legitimate security tools have been disabled (e.g., Disable or Modify Tools). An adversary can also present a “healthy” system status even after infection. This can be abused to enable further malicious activity by delaying defender responses. For example, adversaries may show a fake Windows Security GUI and tray icon with a “healthy” system status after Windows Defender and other system tools have been disabled.

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
- T1562.011: https://attack.mitre.org/techniques/T1562/011
- Reviewed: 2026-10-27
