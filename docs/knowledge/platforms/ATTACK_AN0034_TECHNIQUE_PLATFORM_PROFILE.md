# Analytic 0034 Technique Platform Profile

## Reference

- Technique: **AN0034 — Analytic 0034**
- Platforms named in the source: Windows

Discrepancies between VBA source code and p-code inside Office documents. Defender perspective: anomalies in file metadata streams, execution of Office processes loading macros without source code consistency, and script execution with no corresponding source metadata.

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
- AN0034: https://attack.mitre.org/detectionstrategies/DET0012#AN0034
- Reviewed: 2026-10-27
