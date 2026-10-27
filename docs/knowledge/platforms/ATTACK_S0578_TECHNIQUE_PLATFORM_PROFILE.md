# SUPERNOVA Technique Platform Profile

## Reference

- Technique: **S0578 — SUPERNOVA**
- Platforms named in the source: Windows

SUPERNOVA is an in-memory web shell written in .NET C#. It was discovered in November 2020 during the investigation of APT29's SolarWinds cyber operation but determined to be unrelated. Subsequent analysis suggests SUPERNOVA may have been used by the China-based threat group SPIRAL.

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
- S0578: https://attack.mitre.org/software/S0578
- Reviewed: 2026-10-27
