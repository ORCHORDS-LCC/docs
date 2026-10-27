# Group Policy Preferences Technique Response Playbook

## Target technique

**T1552.006 — Group Policy Preferences**

- Tactics: credential-access
- Platforms: Windows

Adversaries may attempt to find unsecured credentials in Group Policy Preferences (GPP). GPP are tools that allow administrators to create domain policies with embedded credentials. These policies allow administrators to set local accounts. These group policies are stored in SYSVOL on a domain controller. This means that any domain user can view the SYSVOL share and decrypt the password (using the AES key that has been made public). The following tools and scripts can be used to gather and decrypt the password file from Group Policy Preference XML files: * Metasploit’s post exploitation module: <code>post/windows/gather/credentials/gpp</code> * Get-GPPPassword * gpprefdecrypt.py On the SYSVOL share, adversaries may use the following command to enumerate potential GPP XML files: <code>dir /s * .xml</code>.

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
- T1552.006: https://attack.mitre.org/techniques/T1552/006
- Reviewed: 2026-10-27
