# Analytic 0466 Technique Platform Profile

## Reference

- Technique: **AN0466 — Analytic 0466**
- Platforms named in the source: Linux

Detects adversary behavior where the command-line arguments of a running process are overwritten in memory to spoof the process name, typically replacing it with a benign or misleading string. The detection correlates unexpected null byte sequences, discrepancies between `/proc/<pid>/cmdline` and process ancestry, and suspicious memory writes shortly after process start.

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
- AN0466: https://attack.mitre.org/detectionstrategies/DET0164#AN0466
- Reviewed: 2026-10-27
