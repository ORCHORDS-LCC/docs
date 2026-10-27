# Analytic 0063 Technique Platform Profile

## Reference

- Technique: **AN0063 — Analytic 0063**
- Platforms named in the source: macOS

Use of launchctl to stop services or kill critical background processes (e.g., securityd, com.apple.*), typically followed by command-line tools like rm or diskutil. Behavioral chain: Terminal or remote shell + launchctl bootout/disable + process termination + follow-on modification.

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
- AN0063: https://attack.mitre.org/detectionstrategies/DET0021#AN0063
- Reviewed: 2026-10-27
