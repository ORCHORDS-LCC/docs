# Analytic 0861 Technique Platform Profile

## Reference

- Technique: **AN0861 — Analytic 0861**
- Platforms named in the source: IaaS

Detection focuses on identifying unauthorized or anomalous changes to compute infrastructure components. Defender perspective: monitor for creation, deletion, or modification of instances, volumes, and snapshots outside of approved change management windows; correlate abnormal activity such as rapid snapshot creation followed by new instance mounts, or repeated infrastructure changes by rarely used accounts. Flagging activity linked to unusual geolocation, API client, or automation script is suspicious.

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
- AN0861: https://attack.mitre.org/detectionstrategies/DET0308#AN0861
- Reviewed: 2026-10-27
