# TCC Manipulation Technique Platform Profile

## Reference

- Technique: **T1548.006 — TCC Manipulation**
- Platforms named in the source: macOS

Adversaries can manipulate or abuse the Transparency, Consent, & Control (TCC) service or database to grant malicious executables elevated permissions. TCC is a Privacy & Security macOS control mechanism used to determine if the running process has permission to access the data or services protected by TCC, such as screen sharing, camera, microphone, or Full Disk Access (FDA). When an application requests to access data or a service protected by TCC, the TCC daemon (`tccd`) checks the TCC database, located at `/Library/Application Support/com.apple.TCC/TCC.db` (and `~/` equivalent), and an overwrites file (if connected to an MDM) for existing permissions. If permissions do not exist, then the user is prompted to grant permission. Once permissions are granted, the database stores the application's permissions and will not prompt the user again unless reset. For example, when a web browser requests permissions to the user's webcam, once granted the web browser may not explicitly prompt the user again. Adversaries may access restricted data or services protected by TCC through abusing applications previously granted permissions through Process Injection or executing a malicious binary using another application. For example, adversaries can use Finder, a macOS native app with FDA permissions, to execute a malicious AppleScript. When executing under the Finder App, the malicious AppleScript inherits access to all files on the system without requiring a user prompt. When System Integrity Protection (SIP) is disabled, TCC protections are also disabled. For a system without SIP enabled, adversaries can manipulate the TCC database to add permissions to their malicious executable through loading an adversary controlled TCC database using environment variables and Launchctl.

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
- T1548.006: https://attack.mitre.org/techniques/T1548/006
- Reviewed: 2026-10-27
