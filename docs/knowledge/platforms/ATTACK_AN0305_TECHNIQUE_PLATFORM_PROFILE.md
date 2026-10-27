# Analytic 0305 Technique Platform Profile

## Reference

- Technique: **AN0305 — Analytic 0305**
- Platforms named in the source: ESXi

ESXi daemons (e.g., hostd, vpxa) are wrapped or impersonated to send large outbound traffic using gzip/Base64 encoding over SSH or HTTP. These actions follow suspicious logins or shell access.

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
- AN0305: https://attack.mitre.org/detectionstrategies/DET0108#AN0305
- Reviewed: 2026-10-27
