# SLOTHFULMEDIA Technique Platform Profile

## Reference

- Technique: **S0533 — SLOTHFULMEDIA**
- Platforms named in the source: Windows

SLOTHFULMEDIA is a remote access Trojan written in C++ that has been used by an unidentified "sophisticated cyber actor" since at least January 2017. It has been used to target government organizations, defense contractors, universities, and energy companies in Russia, India, Kazakhstan, Kyrgyzstan, Malaysia, Ukraine, and Eastern Europe. In October 2020, Kaspersky Labs assessed SLOTHFULMEDIA is part of an activity cluster it refers to as "IAmTheKing". ESET also noted code similarity between SLOTHFULMEDIA and droppers used by a group it refers to as "PowerPool".

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
- S0533: https://attack.mitre.org/software/S0533
- Reviewed: 2026-10-27
