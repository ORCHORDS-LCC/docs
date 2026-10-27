# Analytic 0797 Technique Platform Profile

## Reference

- Technique: **AN0797 — Analytic 0797**
- Platforms named in the source: Windows

Cause→effect chain: (1) A client app (browser, Office, PDF/Flash/reader) experiences a crash/abnormal exit or loads from an unusual location, then (2) drops or modifies a file in user-writable paths, and/or (3) spawns an unexpected child (e.g., powershell/cmd/mshta/rundll32/wscript/installer), and (4) establishes outbound C2-like connections shortly after. Correlate application logs, file writes, process lineage, and network egress within a short window.

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
- AN0797: https://attack.mitre.org/detectionstrategies/DET0287#AN0797
- Reviewed: 2026-10-27
