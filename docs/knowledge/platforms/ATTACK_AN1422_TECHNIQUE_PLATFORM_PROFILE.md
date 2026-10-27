# Analytic 1422 Technique Platform Profile

## Reference

- Technique: **AN1422 — Analytic 1422**
- Platforms named in the source: Containers

Detects container breakout behavior via exploitation (e.g., DirtyPipe, CVE-2022-0847), followed by host OS interaction or escalated capability assignment.

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
- AN1422: https://attack.mitre.org/detectionstrategies/DET0514#AN1422
- Reviewed: 2026-10-27
