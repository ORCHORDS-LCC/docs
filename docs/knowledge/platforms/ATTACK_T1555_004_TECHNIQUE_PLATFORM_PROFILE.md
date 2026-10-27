# Windows Credential Manager Technique Platform Profile

## Reference

- Technique: **T1555.004 — Windows Credential Manager**
- Platforms named in the source: Windows

Adversaries may acquire credentials from the Windows Credential Manager. The Credential Manager stores credentials for signing into websites, applications, and/or devices that request authentication through NTLM or Kerberos in Credential Lockers (previously known as Windows Vaults). The Windows Credential Manager separates website credentials from application or network credentials in two lockers. As part of Credentials from Web Browsers, Internet Explorer and Microsoft Edge website credentials are managed by the Credential Manager and are stored in the Web Credentials locker. Application and network credentials are stored in the Windows Credentials locker. Credential Lockers store credentials in encrypted `.vcrd` files, located under `%Systemdrive%\Users\\[Username]\AppData\Local\Microsoft\\[Vault/Credentials]\`. The encryption key can be found in a file named Policy.vpol, typically located in the same folder as the credentials. Adversaries may list credentials managed by the Windows Credential Manager through several mechanisms. vaultcmd.exe is a native Windows executable that can be used to enumerate credentials stored in the Credential Locker through a command-line interface. Adversaries may also gather credentials by directly reading files located inside of the Credential Lockers. Windows APIs, such as CredEnumerateA, may also be absued to list credentials managed by the Credential Manager. Adversaries may also obtain credentials from credential backups. Credential backups and restorations may be performed by running rundll32.exe keymgr.dll KRShowKeyMgr then selecting the “Back up...” button on the “Stored User Names and Passwords” GUI. Password recovery tools may also obtain plain text passwords from the Credential Manager.

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
- T1555.004: https://attack.mitre.org/techniques/T1555/004
- Reviewed: 2026-10-27
