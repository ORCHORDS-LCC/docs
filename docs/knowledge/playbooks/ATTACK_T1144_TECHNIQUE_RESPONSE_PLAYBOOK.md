# Gatekeeper Bypass Technique Response Playbook

## Target technique

**T1144 — Gatekeeper Bypass**

- Tactics: stealth
- Platforms: macOS

In macOS and OS X, when applications or programs are downloaded from the internet, there is a special attribute set on the file called com.apple.quarantine. This attribute is read by Apple's Gatekeeper defense program at execution time and provides a prompt to the user to allow or deny execution. Apps loaded onto the system from USB flash drive, optical disk, external hard drive, or even from a drive shared over the local network won’t set this flag. Additionally, other utilities or events like drive-by downloads don’t necessarily set it either. This completely bypasses the built-in Gatekeeper check. The presence of the quarantine flag can be checked by the xattr command xattr /path/to/MyApp.app for com.apple.quarantine. Similarly, given sudo access or elevated permission, this attribute can be removed with xattr as well, sudo xattr -r -d com.apple.quarantine /path/to/MyApp.app. In typical operation, a file will be downloaded from the internet and given a quarantine flag before being saved to disk. When the user tries to open the file or application, macOS’s gatekeeper will step in and check for the presence of this flag. If it exists, then macOS will then prompt the user to confirmation that they want to run the program and will even provide the URL where the application came from. However, this is all based on the file being downloaded from a quarantine-savvy application.

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
- T1144: https://attack.mitre.org/techniques/T1144
- Reviewed: 2026-10-27
