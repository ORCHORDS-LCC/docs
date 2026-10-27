# macOS.OSAMiner Technique Platform Profile

## Reference

- Technique: **S1048 — macOS.OSAMiner**
- Platforms named in the source: macOS

MacOS.OSAMiner is a Monero mining trojan that was first observed in 2018; security researchers assessed macOS.OSAMiner may have been circulating since at least 2015. macOS.OSAMiner is known for embedding one run-only AppleScript into another, which helped the malware evade full analysis for five years due to a lack of Apple event (AEVT) analysis tools.

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
- S1048: https://attack.mitre.org/software/S1048
- Reviewed: 2026-10-27
