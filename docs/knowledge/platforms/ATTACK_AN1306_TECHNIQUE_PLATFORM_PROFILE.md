# Analytic 1306 Technique Platform Profile

## Reference

- Technique: **AN1306 — Analytic 1306**
- Platforms named in the source: Linux

Linux environmental keying behavioral chain: (1) System information gathering through native commands (uname, hostname, id, whoami, ifconfig/ip) and file system enumeration, (2) Network configuration discovery (route tables, DNS settings, network interfaces), (3) Filesystem and mount point analysis for target-specific directories or devices, (4) Process and service enumeration to identify target-specific software, (5) Cryptographic library usage correlation with collected environmental data, (6) Payload execution following successful environmental validation.

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
- AN1306: https://attack.mitre.org/detectionstrategies/DET0474#AN1306
- Reviewed: 2026-10-27
