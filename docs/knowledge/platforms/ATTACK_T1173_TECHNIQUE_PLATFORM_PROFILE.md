# Dynamic Data Exchange Mitigation Technique Platform Profile

## Reference

- Technique: **T1173 — Dynamic Data Exchange Mitigation**
- Platforms named in the source: not stated

Registry keys specific to Microsoft Office feature control security can be set to disable automatic DDE/OLE execution. Microsoft also created, and enabled by default, Registry keys to completely disable DDE execution in Word and Excel. Ensure Protected View is enabled and consider disabling embedded files in Office programs, such as OneNote, not enrolled in Protected View. On Windows 10, enable Attack Surface Reduction (ASR) rules to prevent DDE attacks and spawning of child processes from Office programs.

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
- T1173: https://attack.mitre.org/mitigations/T1173
- Reviewed: 2026-10-27
