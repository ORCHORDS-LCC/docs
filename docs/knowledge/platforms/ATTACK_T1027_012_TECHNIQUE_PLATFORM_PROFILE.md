# LNK Icon Smuggling Technique Platform Profile

## Reference

- Technique: **T1027.012 — LNK Icon Smuggling**
- Platforms named in the source: Windows

Adversaries may smuggle commands to download malicious payloads past content filters by hiding them within otherwise seemingly benign windows shortcut files. Windows shortcut files (.LNK) include many metadata fields, including an icon location field (also known as the `IconEnvironmentDataBlock`) designed to specify the path to an icon file that is to be displayed for the LNK file within a host directory. Adversaries may abuse this LNK metadata to download malicious payloads. For example, adversaries have been observed using LNK files as phishing payloads to deliver malware. Once invoked (e.g., Malicious File), payloads referenced via external URLs within the LNK icon location field may be downloaded. These files may also then be invoked by Command and Scripting Interpreter/System Binary Proxy Execution arguments within the target path field of the LNK. LNK Icon Smuggling may also be utilized post compromise, such as malicious scripts executing an LNK on an infected host to download additional malicious payloads.

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
- T1027.012: https://attack.mitre.org/techniques/T1027/012
- Reviewed: 2026-10-27
