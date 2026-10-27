# T1564.014 Extended Attributes Outcome Lesson

## Authoritative description

- Technique: **T1564.014 — Extended Attributes**
- Tactics: stealth
- Platforms: Linux, macOS

Adversaries may abuse extended attributes (xattrs) on macOS and Linux to hide their malicious data in order to evade detection. Extended attributes are key-value pairs of file and directory metadata used by both macOS and Linux. They are not visible through standard tools like `Finder`, `ls`, or `cat` and require utilities such as `xattr` (macOS) or `getfattr` (Linux) for inspection. Operating systems and applications use xattrs for tagging, integrity checks, and access control. On Linux, xattrs are organized into namespaces such as `user.` (user permissions), `trusted.` (root permissions), `security.`, and `system.`, each with specific permissions. On macOS, xattrs are flat strings without namespace prefixes, commonly prefixed with `com.apple.*` (e.g., `com.apple.quarantine`, `com.apple.metadata:_kMDItemUserTags`) and used by system features like Gatekeeper and Spotlight. An adversary may leverage xattrs by embedding a second-stage payload into the extended attribute of a legitimate file. On macOS, a payload can be embedded into a custom attribute using the `xattr` command. A separate loader can retrieve the attribute with `xattr -p`, decode the content, and execute it using a scripting interpreter. On Linux, an adversary may use `setfattr` to write a payload into the `user.` namespace of a legitimate file. A loader script can later extract the payload with `getfattr --only-values`, decode it, and execute it using bash or another interpreter. In both cases, because the primary file content remains unchanged, security tools and integrity checks that do not inspect extended attributes will observe the original file hash, allowing the malicious payload to evade detection.

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
- T1564.014: https://attack.mitre.org/techniques/T1564/014
- Reviewed: 2026-10-27

## Boundary

This lesson is derived from the published technique description. It does not invent an incident, prescribe one implementation, or claim the technique has been addressed.
