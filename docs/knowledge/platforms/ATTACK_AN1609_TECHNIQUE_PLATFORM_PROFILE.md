# Analytic 1609 Technique Platform Profile

## Reference

- Technique: **AN1609 — Analytic 1609**
- Platforms named in the source: macOS

Unexpected creation or modification of files with `com.apple.ResourceFork` extended attributes containing unusually large or non-standard data. Defender perspective: detection of resource forks in contexts where they are uncommon, especially when paired with process execution or network activity.

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
- AN1609: https://attack.mitre.org/detectionstrategies/DET0584#AN1609
- Reviewed: 2026-10-27
