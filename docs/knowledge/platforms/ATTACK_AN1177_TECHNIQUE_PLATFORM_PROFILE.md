# Analytic 1177 Technique Platform Profile

## Reference

- Technique: **AN1177 — Analytic 1177**
- Platforms named in the source: Windows

Multi-stage Windows DACL manipulation behavioral chain: (1) Process creation of permission-modifying utilities (icacls.exe, takeown.exe, attrib.exe, cacls.exe) or PowerShell ACL cmdlets, (2) Command-line analysis revealing privilege escalation intent through suspicious parameters (/grant, /takeown, /T, Set-Acl), (3) DACL modification events (4670) correlating with process execution, (4) Subsequent file access attempts (4663) indicating successful permission bypass, (5) Potential follow-on persistence or lateral movement activities.

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
- AN1177: https://attack.mitre.org/detectionstrategies/DET0418#AN1177
- Reviewed: 2026-10-27
