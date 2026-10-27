# SUGARDUMP Technique Platform Profile

## Reference

- Technique: **S1042 — SUGARDUMP**
- Platforms named in the source: Windows

SUGARDUMP is a proprietary browser credential harvesting tool that was used by UNC3890 during the C0010 campaign. The first known SUGARDUMP version was used since at least early 2021, a second SMTP C2 version was used from late 2021-early 2022, and a third HTTP C2 variant was used since at least April 2022.

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
- S1042: https://attack.mitre.org/software/S1042
- Reviewed: 2026-10-27
