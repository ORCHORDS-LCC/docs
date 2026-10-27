# LunarLoader Technique Platform Profile

## Reference

- Technique: **S1143 — LunarLoader**
- Platforms named in the source: Windows

LunarLoader is the loader component for the LunarWeb and LunarMail backdoors that has been used by Turla since at least 2020 including against a European ministry of foreign affairs (MFA). LunarLoader has been observed as a standalone and as a part of trojanized open-source software such as AdmPwd.

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
- S1143: https://attack.mitre.org/software/S1143
- Reviewed: 2026-10-27
