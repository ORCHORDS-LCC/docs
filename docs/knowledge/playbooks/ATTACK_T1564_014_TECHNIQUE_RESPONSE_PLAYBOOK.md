# Extended Attributes Technique Response Playbook

## Target technique

**T1564.014 — Extended Attributes**

- Tactics: stealth
- Platforms: Linux, macOS

Adversaries may abuse extended attributes (xattrs) on macOS and Linux to hide their malicious data in order to evade detection. Extended attributes are key-value pairs of file and directory metadata used by both macOS and Linux. They are not visible through standard tools like `Finder`, `ls`, or `cat` and require utilities such as `xattr` (macOS) or `getfattr` (Linux) for inspection. Operating systems and applications use xattrs for tagging, integrity checks, and access control. On Linux, xattrs are organized into namespaces such as `user.` (user permissions), `trusted.` (root permissions), `security.`, and `system.`, each with specific permissions. On macOS, xattrs are flat strings without namespace prefixes, commonly prefixed with `com.apple.*` (e.g., `com.apple.quarantine`, `com.apple.metadata:_kMDItemUserTags`) and used by system features like Gatekeeper and Spotlight. An adversary may leverage xattrs by embedding a second-stage payload into the extended attribute of a legitimate file. On macOS, a payload can be embedded into a custom attribute using the `xattr` command. A separate loader can retrieve the attribute with `xattr -p`, decode the content, and execute it using a scripting interpreter. On Linux, an adversary may use `setfattr` to write a payload into the `user.` namespace of a legitimate file. A loader script can later extract the payload with `getfattr --only-values`, decode it, and execute it using bash or another interpreter. In both cases, because the primary file content remains unchanged, security tools and integrity checks that do not inspect extended attributes will observe the original file hash, allowing the malicious payload to evade detection.

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
- T1564.014: https://attack.mitre.org/techniques/T1564/014
- Reviewed: 2026-10-27
