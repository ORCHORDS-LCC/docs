# Analytic 1351 Technique Platform Profile

## Reference

- Technique: **AN1351 — Analytic 1351**
- Platforms named in the source: Windows

A process explicitly forges its parent using EXTENDED_STARTUPINFO + PROC_THREAD_ATTRIBUTE_PARENT_PROCESS (UpdateProcThreadAttribute → CreateProcess[A/W]/CreateProcessAsUserW) or other Native API paths, resulting in **mismatched/implausible lineage** across ETW EventHeader ProcessId, Security 4688 Creator Process ID/Name, and sysmon ParentProcessGuid. Often paired with privilege escalation when the chosen parent runs as SYSTEM.

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
- AN1351: https://attack.mitre.org/detectionstrategies/DET0489#AN1351
- Reviewed: 2026-10-27
