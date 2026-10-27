# Analytic 1956 Technique Platform Profile

## Reference

- Technique: **AN1956 — Analytic 1956**
- Platforms named in the source: PRE

If infrastructure or patterns in malware have been previously identified, internet scanning may uncover when an adversary has staged malware to make it accessible for targeting. Much of this activity will take place outside the visibility of the target organization, making detection of this behavior difficult. Detection efforts may be focused on post-compromise phases of the adversary lifecycle, such as User Execution or Ingress Tool Transfer .

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
- AN1956: https://attack.mitre.org/detectionstrategies/DET0824#AN1956
- Reviewed: 2026-10-27
