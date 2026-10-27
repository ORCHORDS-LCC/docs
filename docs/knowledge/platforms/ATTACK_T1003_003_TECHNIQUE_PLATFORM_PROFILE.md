# NTDS Technique Platform Profile

## Reference

- Technique: **T1003.003 — NTDS**
- Platforms named in the source: Windows

Adversaries may attempt to access or create a copy of the Active Directory domain database in order to steal credential information, as well as obtain other information about domain members such as devices, users, and access rights. By default, the NTDS file (NTDS.dit) is located in <code>%SystemRoot%\NTDS\Ntds.dit</code> of a domain controller. In addition to looking for NTDS files on active Domain Controllers, adversaries may search for backups that contain the same or similar information. The following tools and techniques can be used to enumerate the NTDS file and the contents of the entire Active Directory hashes. * Volume Shadow Copy * secretsdump.py * Using the in-built Windows tool, ntdsutil.exe * Invoke-NinjaCopy.

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
- T1003.003: https://attack.mitre.org/techniques/T1003/003
- Reviewed: 2026-10-27
