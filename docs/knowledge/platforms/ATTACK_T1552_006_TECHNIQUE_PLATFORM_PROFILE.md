# Group Policy Preferences Technique Platform Profile

## Reference

- Technique: **T1552.006 — Group Policy Preferences**
- Platforms named in the source: Windows

Adversaries may attempt to find unsecured credentials in Group Policy Preferences (GPP). GPP are tools that allow administrators to create domain policies with embedded credentials. These policies allow administrators to set local accounts. These group policies are stored in SYSVOL on a domain controller. This means that any domain user can view the SYSVOL share and decrypt the password (using the AES key that has been made public). The following tools and scripts can be used to gather and decrypt the password file from Group Policy Preference XML files: * Metasploit’s post exploitation module: <code>post/windows/gather/credentials/gpp</code> * Get-GPPPassword * gpprefdecrypt.py On the SYSVOL share, adversaries may use the following command to enumerate potential GPP XML files: <code>dir /s * .xml</code>.

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
- T1552.006: https://attack.mitre.org/techniques/T1552/006
- Reviewed: 2026-10-27
