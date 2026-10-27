# T1574.014 AppDomainManager Outcome Lesson

## Authoritative description

- Technique: **T1574.014 — AppDomainManager**
- Tactics: stealth, execution
- Platforms: Windows

Adversaries may execute their own malicious payloads by hijacking how the .NET `AppDomainManager` loads assemblies. The .NET framework uses the `AppDomainManager` class to create and manage one or more isolated runtime environments (called application domains) inside a process to host the execution of .NET applications. Assemblies (`.exe` or `.dll` binaries compiled to run as .NET code) may be loaded into an application domain as executable code. Known as "AppDomainManager injection," adversaries may execute arbitrary code by hijacking how .NET applications load assemblies. For example, malware may create a custom application domain inside a target process to load and execute an arbitrary assembly. Alternatively, configuration files (`.config`) or process environment variables that define .NET runtime settings may be tampered with to instruct otherwise benign .NET applications to load a malicious assembly (identified by name) into the target process.

## Reusable lesson

This technique should be treated as an explicit review question when it is relevant to the system or organisation, rather than assumed to be covered by a generic control statement or by tooling that reports a related signal.

## Apply the lesson

1. Define the real scope before judging coverage.
2. Inspect current technical, process, governance, or operational evidence.
3. Separate documented intent from verified behaviour.
4. Record partial coverage and unresolved gaps instead of converting them into a pass.
5. Revisit when the underlying scope, threat environment, technology, suppliers, or mission materially changes.

## Source

- MITRE ATT&CK: https://attack.mitre.org/
- T1574.014: https://attack.mitre.org/techniques/T1574/014
- Reviewed: 2026-10-27

## Boundary

This lesson is derived from the published technique description. It does not invent an incident, prescribe one implementation, or claim the technique has been addressed.
