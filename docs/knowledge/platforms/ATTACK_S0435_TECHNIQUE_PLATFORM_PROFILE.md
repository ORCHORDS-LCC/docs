# PLEAD Technique Platform Profile

## Reference

- Technique: **S0435 — PLEAD**
- Platforms named in the source: Windows

PLEAD is a remote access tool (RAT) and downloader used by BlackTech in targeted attacks in East Asia including Taiwan, Japan, and Hong Kong. PLEAD has also been referred to as TSCookie, though more recent reporting indicates likely separation between the two. PLEAD was observed in use as early as March 2017.

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
- S0435: https://attack.mitre.org/software/S0435
- Reviewed: 2026-10-27
