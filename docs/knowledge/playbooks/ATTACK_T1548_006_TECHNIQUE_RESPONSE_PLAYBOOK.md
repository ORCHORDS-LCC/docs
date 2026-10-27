# TCC Manipulation Technique Response Playbook

## Target technique

**T1548.006 — TCC Manipulation**

- Tactics: privilege-escalation
- Platforms: macOS

Adversaries can manipulate or abuse the Transparency, Consent, & Control (TCC) service or database to grant malicious executables elevated permissions. TCC is a Privacy & Security macOS control mechanism used to determine if the running process has permission to access the data or services protected by TCC, such as screen sharing, camera, microphone, or Full Disk Access (FDA). When an application requests to access data or a service protected by TCC, the TCC daemon (`tccd`) checks the TCC database, located at `/Library/Application Support/com.apple.TCC/TCC.db` (and `~/` equivalent), and an overwrites file (if connected to an MDM) for existing permissions. If permissions do not exist, then the user is prompted to grant permission. Once permissions are granted, the database stores the application's permissions and will not prompt the user again unless reset. For example, when a web browser requests permissions to the user's webcam, once granted the web browser may not explicitly prompt the user again. Adversaries may access restricted data or services protected by TCC through abusing applications previously granted permissions through Process Injection or executing a malicious binary using another application. For example, adversaries can use Finder, a macOS native app with FDA permissions, to execute a malicious AppleScript. When executing under the Finder App, the malicious AppleScript inherits access to all files on the system without requiring a user prompt. When System Integrity Protection (SIP) is disabled, TCC protections are also disabled. For a system without SIP enabled, adversaries can manipulate the TCC database to add permissions to their malicious executable through loading an adversary controlled TCC database using environment variables and Launchctl.

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
- T1548.006: https://attack.mitre.org/techniques/T1548/006
- Reviewed: 2026-10-27
