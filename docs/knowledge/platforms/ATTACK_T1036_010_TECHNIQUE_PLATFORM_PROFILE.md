# Masquerade Account Name Technique Platform Profile

## Reference

- Technique: **T1036.010 — Masquerade Account Name**
- Platforms named in the source: Containers, IaaS, Identity Provider, Linux, macOS, Office Suite, SaaS, Windows

Adversaries may match or approximate the names of legitimate accounts to make newly created ones appear benign. This will typically occur during Create Account, although accounts may also be renamed at a later date. This may also coincide with Account Access Removal if the actor first deletes an account before re-creating one with the same name. Often, adversaries will attempt to masquerade as service accounts, such as those associated with legitimate software, data backups, or container cluster management. They may also give accounts generic, trustworthy names, such as “admin”, “help”, or “root.” Sometimes adversaries may model account names off of those already existing in the system, as a follow-on behavior to Account Discovery. Note that this is distinct from Impersonation, which describes impersonating specific trusted individuals or organizations, rather than user or service account names.

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
- T1036.010: https://attack.mitre.org/techniques/T1036/010
- Reviewed: 2026-10-27
