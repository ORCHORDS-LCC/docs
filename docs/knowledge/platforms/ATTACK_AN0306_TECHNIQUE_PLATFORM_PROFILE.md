# Analytic 0306 Technique Platform Profile

## Reference

- Technique: **AN0306 — Analytic 0306**
- Platforms named in the source: macOS

Monitor for unexpected modifications of plist files in persistence or configuration directories (e.g., ~/Library/LaunchAgents, ~/Library/Preferences, /Library/LaunchDaemons). Detect when modifications are followed by execution of new or unexpected binaries. Track use of utilities such as defaults, plutil, or text editors making changes to Info.plist files. Correlate file modifications with subsequent process launches or service starts that reference the altered plist.

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
- AN0306: https://attack.mitre.org/detectionstrategies/DET0109#AN0306
- Reviewed: 2026-10-27
