# User Execution Mitigation Technique Platform Profile

## Reference

- Technique: **T1204 — User Execution Mitigation**
- Platforms named in the source: not stated

Use user training as a way to bring awareness to common phishing and spearphishing techniques and how to raise suspicion for potentially malicious events. Application whitelisting may be able to prevent the running of executables masquerading as other files. If a link is being visited by a user, block unknown or unused files in transit by default that should not be downloaded or by policy from suspicious sites as a best practice to prevent some vectors, such as .scr, .exe, .lnk, .pif, .cpl, etc. Some download scanning devices can open and analyze compressed and encrypted formats, such as zip and RAR that may be used to conceal malicious files in Obfuscated Files or Information. If a link is being visited by a user, network intrusion prevention systems and systems designed to scan and remove malicious downloads can be used to block activity. Solutions can be signature and behavior based, but adversaries may construct files in a way to avoid these systems.

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
- T1204: https://attack.mitre.org/mitigations/T1204
- Reviewed: 2026-10-27
