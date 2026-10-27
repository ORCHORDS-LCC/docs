# Windows Credential Manager Technique Engineering Review

## Reference

- Technique: **T1555.004 — Windows Credential Manager**

Adversaries may acquire credentials from the Windows Credential Manager. The Credential Manager stores credentials for signing into websites, applications, and/or devices that request authentication through NTLM or Kerberos in Credential Lockers (previously known as Windows Vaults). The Windows Credential Manager separates website credentials from application or network credentials in two lockers. As part of Credentials from Web Browsers, Internet Explorer and Microsoft Edge website credentials are managed by the Credential Manager and are stored in the Web Credentials locker. Application and network credentials are stored in the Windows Credentials locker. Credential Lockers store credentials in encrypted `.vcrd` files, located under `%Systemdrive%\Users\\[Username]\AppData\Local\Microsoft\\[Vault/Credentials]\`. The encryption key can be found in a file named Policy.vpol, typically located in the same folder as the credentials. Adversaries may list credentials managed by the Windows Credential Manager through several mechanisms. vaultcmd.exe is a native Windows executable that can be used to enumerate credentials stored in the Credential Locker through a command-line interface. Adversaries may also gather credentials by directly reading files located inside of the Credential Lockers. Windows APIs, such as CredEnumerateA, may also be absued to list credentials managed by the Credential Manager. Adversaries may also obtain credentials from credential backups. Credential backups and restorations may be performed by running rundll32.exe keymgr.dll KRShowKeyMgr then selecting the “Back up...” button on the “Stored User Names and Passwords” GUI. Password recovery tools may also obtain plain text passwords from the Credential Manager.

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
- T1555.004: https://attack.mitre.org/techniques/T1555/004
- Reviewed: 2026-10-27
