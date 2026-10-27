# Analytic 0999 Technique Platform Profile

## Reference

- Technique: **AN0999 — Analytic 0999**
- Platforms named in the source: macOS

MacOS permission and attribute manipulation behavioral chain: (1) Process execution of permission utilities (chmod, chown, chgrp) or macOS-specific tools (chflags) with suspicious parameters, (2) System Integrity Protection (SIP) bypass attempts through permission modifications, (3) File flags manipulation (uchg, schg, hidden) for evasion or persistence, (4) Extended attribute (xattr) modifications affecting security metadata, (5) Unified log correlation with file system events and subsequent access patterns, (6) Gatekeeper and code signing bypass through permission/attribute manipulation.

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
- AN0999: https://attack.mitre.org/detectionstrategies/DET0351#AN0999
- Reviewed: 2026-10-27
