# Process Argument Spoofing Technique Response Playbook

## Target technique

**T1564.010 — Process Argument Spoofing**

- Tactics: stealth
- Platforms: Windows

Adversaries may attempt to hide process command-line arguments by overwriting process memory. Process command-line arguments are stored in the process environment block (PEB), a data structure used by Windows to store various information about/used by a process. The PEB includes the process command-line arguments that are referenced when executing the process. When a process is created, defensive tools/sensors that monitor process creations may retrieve the process arguments from the PEB. Adversaries may manipulate a process PEB to evade defenses. For example, Process Hollowing can be abused to spawn a process in a suspended state with benign arguments. After the process is spawned and the PEB is initialized (and process information is potentially logged by tools/sensors), adversaries may override the PEB to modify the command-line arguments (ex: using the Native API <code>WriteProcessMemory()</code> function) then resume process execution with malicious arguments. Adversaries may also execute a process with malicious command-line arguments then patch the memory with benign arguments that may bypass subsequent process memory analysis. This behavior may also be combined with other tricks (such as Parent PID Spoofing) to manipulate or further evade process-based detections.

## Preconditions

- the estate in scope is identified, with the systems the technique could apply to;
- an owner is accountable for detection and response;
- current telemetry and configuration can be inspected;
- the technique is applicable or requires an applicability decision.

## Procedure

1. Confirm the scope and owner.
2. Read the current technique description and the associated detection guidance.
3. Inventory the telemetry that would carry the technique's indicators.
4. Inspect whether the indicators are present in the environment.
5. Exercise the detection path and confirm it produces the expected signal.
6. Record gaps in detection coverage and assign remediation owners.
7. Record justified non-applicability or accepted detection gaps separately.
8. Set the next event-driven or periodic verification trigger.

## Failure handling

If the detection path does not produce the expected signal, treat the coverage as unverified, preserve the test evidence, and route the gap through the appropriate remediation or risk process.

## Completion evidence

Scope, owner, source version, telemetry inspected, tests performed, findings, exceptions, remediation links, reviewer, and next trigger.

## Source

- MITRE ATT&CK: https://attack.mitre.org/
- T1564.010: https://attack.mitre.org/techniques/T1564/010
- Reviewed: 2026-10-27
