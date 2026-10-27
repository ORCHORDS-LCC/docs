# Network Provider DLL Technique Operationalization Review

## Reference

- Technique: **T1556.008 — Network Provider DLL**

Adversaries may register malicious network provider dynamic link libraries (DLLs) to capture cleartext user credentials during the authentication process. Network provider DLLs allow Windows to interface with specific network protocols and can also support add-on credential management functions. During the logon process, Winlogon (the interactive logon module) sends credentials to the local `mpnotify.exe` process via RPC. The `mpnotify.exe` process then shares the credentials in cleartext with registered credential managers when notifying that a logon event is happening. Adversaries can configure a malicious network provider DLL to receive credentials from `mpnotify.exe`. Once installed as a credential manager (via the Registry), a malicious DLL can receive and save credentials each time a user logs onto a Windows workstation or domain via the `NPLogonNotify()` function. Adversaries may target planting malicious network provider DLLs on systems known to have increased logon activity and/or administrator logon activity, such as servers and domain controllers.

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
- T1556.008: https://attack.mitre.org/techniques/T1556/008
- Reviewed: 2026-10-27
