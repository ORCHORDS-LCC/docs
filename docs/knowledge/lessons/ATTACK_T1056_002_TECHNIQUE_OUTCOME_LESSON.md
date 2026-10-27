# T1056.002 GUI Input Capture Outcome Lesson

## Authoritative description

- Technique: **T1056.002 — GUI Input Capture**
- Tactics: collection, credential-access
- Platforms: Linux, macOS, Windows

Adversaries may mimic common operating system GUI components to prompt users for credentials with a seemingly legitimate prompt. When programs are executed that need additional privileges than are present in the current user context, it is common for the operating system to prompt the user for proper credentials to authorize the elevated privileges for the task (ex: Bypass User Account Control). Adversaries may mimic this functionality to prompt users for credentials with a seemingly legitimate prompt for a number of reasons that mimic normal usage, such as a fake installer requiring additional access or a fake malware removal suite. This type of prompt can be used to collect credentials via various languages such as AppleScript and PowerShell. On Linux systems adversaries may launch dialog boxes prompting users for credentials from malicious shell scripts or the command line (i.e. Unix Shell). Adversaries may also mimic common software authentication requests, such as those from browsers or email clients. This may also be paired with user activity monitoring (i.e., Browser Information Discovery and/or Application Window Discovery) to spoof prompts when users are naturally accessing sensitive sites/data.

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
- T1056.002: https://attack.mitre.org/techniques/T1056/002
- Reviewed: 2026-10-27

## Boundary

This lesson is derived from the published technique description. It does not invent an incident, prescribe one implementation, or claim the technique has been addressed.
