# Security Account Manager Technique Platform Profile

## Reference

- Technique: **T1003.002 — Security Account Manager**
- Platforms named in the source: Windows

Adversaries may attempt to extract credential material from the Security Account Manager (SAM) database either through in-memory techniques or through the Windows Registry where the SAM database is stored. The SAM is a database file that contains local accounts for the host, typically those found with the net user command. Enumerating the SAM database requires SYSTEM level access. A number of tools can be used to retrieve the SAM file through in-memory techniques: * pwdumpx.exe * gsecdump * Mimikatz * secretsdump.py Alternatively, the SAM can be extracted from the Registry with Reg: * reg save HKLM\sam sam * reg save HKLM\system system Creddump7 can then be used to process the SAM database locally to retrieve hashes. Notes: * RID 500 account is the local, built-in administrator. * RID 501 is the guest account. * User accounts start with a RID of 1,000+.

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
- T1003.002: https://attack.mitre.org/techniques/T1003/002
- Reviewed: 2026-10-27
