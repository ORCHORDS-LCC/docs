# Security Account Manager Technique Response Playbook

## Target technique

**T1003.002 — Security Account Manager**

- Tactics: credential-access
- Platforms: Windows

Adversaries may attempt to extract credential material from the Security Account Manager (SAM) database either through in-memory techniques or through the Windows Registry where the SAM database is stored. The SAM is a database file that contains local accounts for the host, typically those found with the <code>net user</code> command. Enumerating the SAM database requires SYSTEM level access. A number of tools can be used to retrieve the SAM file through in-memory techniques: * pwdumpx.exe * gsecdump * Mimikatz * secretsdump.py Alternatively, the SAM can be extracted from the Registry with Reg: * <code>reg save HKLM\sam sam</code> * <code>reg save HKLM\system system</code> Creddump7 can then be used to process the SAM database locally to retrieve hashes. Notes: * RID 500 account is the local, built-in administrator. * RID 501 is the guest account. * User accounts start with a RID of 1,000+.

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
- T1003.002: https://attack.mitre.org/techniques/T1003/002
- Reviewed: 2026-10-27
