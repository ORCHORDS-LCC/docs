# Analytic 1413 Technique Platform Profile

## Reference

- Technique: **AN1413 — Analytic 1413**
- Platforms named in the source: Windows

Detects non-browser processes that establish encrypted outbound connections (e.g., TLS/SSL) to unfamiliar or atypical destinations for the host/user, following a data staging or compression event.

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
- AN1413: https://attack.mitre.org/detectionstrategies/DET0512#AN1413
- Reviewed: 2026-10-27
