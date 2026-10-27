# Security Account Manager Technique Engineering Review

## Reference

- Technique: **T1003.002 — Security Account Manager**

Adversaries may attempt to extract credential material from the Security Account Manager (SAM) database either through in-memory techniques or through the Windows Registry where the SAM database is stored. The SAM is a database file that contains local accounts for the host, typically those found with the net user command. Enumerating the SAM database requires SYSTEM level access. A number of tools can be used to retrieve the SAM file through in-memory techniques: * pwdumpx.exe * gsecdump * Mimikatz * secretsdump.py Alternatively, the SAM can be extracted from the Registry with Reg: * reg save HKLM\sam sam * reg save HKLM\system system Creddump7 can then be used to process the SAM database locally to retrieve hashes. Notes: * RID 500 account is the local, built-in administrator. * RID 501 is the guest account. * User accounts start with a RID of 1,000+.

## Engineering review

1. Identify the engineering boundary where the technique would apply: the component, the service, or the deployment.
2. Review the design decision that would prevent the technique, and record the alternative considered.
3. Review the implementation evidence for the preventive control.
4. Review the test coverage that would fail if the control regressed.
5. Review the observability: which signal would show the control is not operating.
6. Record the residual risk where prevention is not achievable, and the detection that compensates.

## Review evidence

- the design record for the preventive decision;
- the implementation or configuration evidence;
- the test record showing the control is exercised;
- the observability mapping.

## Limitations

An engineering review describes what the design and the implementation evidence show. It does not claim the technique has been addressed in production.

## Source

- MITRE ATT&CK: https://attack.mitre.org/
- T1003.002: https://attack.mitre.org/techniques/T1003/002
- Reviewed: 2026-10-27
