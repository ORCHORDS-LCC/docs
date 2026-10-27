# Process Argument Spoofing Technique Platform Profile

## Reference

- Technique: **T1564.010 — Process Argument Spoofing**
- Platforms named in the source: Windows

Adversaries may attempt to hide process command-line arguments by overwriting process memory. Process command-line arguments are stored in the process environment block (PEB), a data structure used by Windows to store various information about/used by a process. The PEB includes the process command-line arguments that are referenced when executing the process. When a process is created, defensive tools/sensors that monitor process creations may retrieve the process arguments from the PEB. Adversaries may manipulate a process PEB to evade defenses. For example, Process Hollowing can be abused to spawn a process in a suspended state with benign arguments. After the process is spawned and the PEB is initialized (and process information is potentially logged by tools/sensors), adversaries may override the PEB to modify the command-line arguments (ex: using the Native API <code>WriteProcessMemory()</code> function) then resume process execution with malicious arguments. Adversaries may also execute a process with malicious command-line arguments then patch the memory with benign arguments that may bypass subsequent process memory analysis. This behavior may also be combined with other tricks (such as Parent PID Spoofing) to manipulate or further evade process-based detections.

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
- T1564.010: https://attack.mitre.org/techniques/T1564/010
- Reviewed: 2026-10-27
