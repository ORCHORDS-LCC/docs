# BOLDMOVE Technique Platform Profile

## Reference

- Technique: **S1184 — BOLDMOVE**
- Platforms named in the source: Linux, Network Devices

BOLDMOVE is a type of backdoor malware written in C linked to People’s Republic of China operations from 2022 through 2023. BOLDMOVE includes both Windows and Linux variants, with some Linux variants specifically designed for FortiGate Firewall devices. BOLDMOVE is linked to zero-day exploitation of CVE-2022-42475 in FortiOSS SSL-VPNs. The record for BOLDMOVE only covers known Linux variants.

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
- S1184: https://attack.mitre.org/software/S1184
- Reviewed: 2026-10-27
