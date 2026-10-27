# Analytic 1307 Technique Platform Profile

## Reference

- Technique: **AN1307 — Analytic 1307**
- Platforms named in the source: macOS

MacOS environmental keying behavioral chain: (1) System information discovery through native utilities (system_profiler, sw_vers, hostname, dscl) and Security framework queries, (2) Hardware and software enumeration including serial numbers, installed applications, and system versions, (3) Network configuration assessment (networksetup, scutil) and wireless network discovery, (4) Keychain and security context validation, (5) Unified Logs correlation with cryptographic framework usage (CommonCrypto, Security.framework), (6) Application bundle execution following environmental validation.

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
- AN1307: https://attack.mitre.org/detectionstrategies/DET0474#AN1307
- Reviewed: 2026-10-27
