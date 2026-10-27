# Windows Credential Manager Technique Operationalization Review

## Reference

- Technique: **T1555.004 — Windows Credential Manager**

Adversaries may acquire credentials from the Windows Credential Manager. The Credential Manager stores credentials for signing into websites, applications, and/or devices that request authentication through NTLM or Kerberos in Credential Lockers (previously known as Windows Vaults). The Windows Credential Manager separates website credentials from application or network credentials in two lockers. As part of Credentials from Web Browsers, Internet Explorer and Microsoft Edge website credentials are managed by the Credential Manager and are stored in the Web Credentials locker. Application and network credentials are stored in the Windows Credentials locker. Credential Lockers store credentials in encrypted `.vcrd` files, located under `%Systemdrive%\Users\\[Username]\AppData\Local\Microsoft\\[Vault/Credentials]\`. The encryption key can be found in a file named Policy.vpol, typically located in the same folder as the credentials. Adversaries may list credentials managed by the Windows Credential Manager through several mechanisms. vaultcmd.exe is a native Windows executable that can be used to enumerate credentials stored in the Credential Locker through a command-line interface. Adversaries may also gather credentials by directly reading files located inside of the Credential Lockers. Windows APIs, such as CredEnumerateA, may also be absued to list credentials managed by the Credential Manager. Adversaries may also obtain credentials from credential backups. Credential backups and restorations may be performed by running rundll32.exe keymgr.dll KRShowKeyMgr then selecting the “Back up...” button on the “Stored User Names and Passwords” GUI. Password recovery tools may also obtain plain text passwords from the Credential Manager.

## Operationalization review

1. Record the operational scope: which services, environments, and data the technique could affect.
2. Record the runbook that would be executed, and its owner.
3. Record the telemetry the runbook depends on, and whether it is retained long enough to investigate.
4. Record the detection that would surface the technique before or after it has an effect.
5. Record the recovery path, and the evidence that recovery has been rehearsed.
6. Record the residual operational risk where the runbook depends on a manual step.

## Review evidence

- the runbook and its owner;
- the telemetry retention and coverage record;
- the detection mapping;
- the exercise or rehearsal record.

## Limitations

An operationalization review describes the runbook and the evidence around it. It does not claim the technique has been prevented or detected in a live environment.

## Source

- MITRE ATT&CK: https://attack.mitre.org/
- T1555.004: https://attack.mitre.org/techniques/T1555/004
- Reviewed: 2026-10-27
