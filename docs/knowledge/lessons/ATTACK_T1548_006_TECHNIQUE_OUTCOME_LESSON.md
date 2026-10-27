# T1548.006 TCC Manipulation Outcome Lesson

## Authoritative description

- Technique: **T1548.006 — TCC Manipulation**
- Tactics: privilege-escalation
- Platforms: macOS

Adversaries can manipulate or abuse the Transparency, Consent, & Control (TCC) service or database to grant malicious executables elevated permissions. TCC is a Privacy & Security macOS control mechanism used to determine if the running process has permission to access the data or services protected by TCC, such as screen sharing, camera, microphone, or Full Disk Access (FDA). When an application requests to access data or a service protected by TCC, the TCC daemon (`tccd`) checks the TCC database, located at `/Library/Application Support/com.apple.TCC/TCC.db` (and `~/` equivalent), and an overwrites file (if connected to an MDM) for existing permissions. If permissions do not exist, then the user is prompted to grant permission. Once permissions are granted, the database stores the application's permissions and will not prompt the user again unless reset. For example, when a web browser requests permissions to the user's webcam, once granted the web browser may not explicitly prompt the user again. Adversaries may access restricted data or services protected by TCC through abusing applications previously granted permissions through Process Injection or executing a malicious binary using another application. For example, adversaries can use Finder, a macOS native app with FDA permissions, to execute a malicious AppleScript. When executing under the Finder App, the malicious AppleScript inherits access to all files on the system without requiring a user prompt. When System Integrity Protection (SIP) is disabled, TCC protections are also disabled. For a system without SIP enabled, adversaries can manipulate the TCC database to add permissions to their malicious executable through loading an adversary controlled TCC database using environment variables and Launchctl.

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
- T1548.006: https://attack.mitre.org/techniques/T1548/006
- Reviewed: 2026-10-27

## Boundary

This lesson is derived from the published technique description. It does not invent an incident, prescribe one implementation, or claim the technique has been addressed.
