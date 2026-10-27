# Extended Attributes Technique Operationalization Review

## Reference

- Technique: **T1564.014 — Extended Attributes**

Adversaries may abuse extended attributes (xattrs) on macOS and Linux to hide their malicious data in order to evade detection. Extended attributes are key-value pairs of file and directory metadata used by both macOS and Linux. They are not visible through standard tools like `Finder`, `ls`, or `cat` and require utilities such as `xattr` (macOS) or `getfattr` (Linux) for inspection. Operating systems and applications use xattrs for tagging, integrity checks, and access control. On Linux, xattrs are organized into namespaces such as `user.` (user permissions), `trusted.` (root permissions), `security.`, and `system.`, each with specific permissions. On macOS, xattrs are flat strings without namespace prefixes, commonly prefixed with `com.apple.*` (e.g., `com.apple.quarantine`, `com.apple.metadata:_kMDItemUserTags`) and used by system features like Gatekeeper and Spotlight. An adversary may leverage xattrs by embedding a second-stage payload into the extended attribute of a legitimate file. On macOS, a payload can be embedded into a custom attribute using the `xattr` command. A separate loader can retrieve the attribute with `xattr -p`, decode the content, and execute it using a scripting interpreter. On Linux, an adversary may use `setfattr` to write a payload into the `user.` namespace of a legitimate file. A loader script can later extract the payload with `getfattr --only-values`, decode it, and execute it using bash or another interpreter. In both cases, because the primary file content remains unchanged, security tools and integrity checks that do not inspect extended attributes will observe the original file hash, allowing the malicious payload to evade detection.

## Operationalization review

1. Record the operational scope: which services, environments, and data the technique could affect.
2. Record the runbook that would be executed, and its owner.
3. Record the telemetry the runbook depends on, and whether it is retained long enough to investigate.
4. Record the detection that would surface the technique before or after it has an effect.
5. Record the recovery path, and the evidence that recovery has been rehearsed.
6. Record the residual operational risk where the runbook depends on a manual step.

## Review evidence

- the runbook and its owner;
- the telemetry retention and coverage record;
- the detection mapping;
- the exercise or rehearsal record.

## Limitations

An operationalization review describes the runbook and the evidence around it. It does not claim the technique has been prevented or detected in a live environment.

## Source

- MITRE ATT&CK: https://attack.mitre.org/
- T1564.014: https://attack.mitre.org/techniques/T1564/014
- Reviewed: 2026-10-27
