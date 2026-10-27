# AppCert DLLs Technique Engineering Review

## Reference

- Technique: **T1546.009 — AppCert DLLs**

Adversaries may establish persistence and/or elevate privileges by executing malicious content triggered by AppCert DLLs loaded into processes. Dynamic-link libraries (DLLs) that are specified in the AppCertDLLs Registry key under HKEY_LOCAL_MACHINE\System\CurrentControlSet\Control\Session Manager\ are loaded into every process that calls the ubiquitously used application programming interface (API) functions CreateProcess, CreateProcessAsUser, CreateProcessWithLoginW, CreateProcessWithTokenW, or WinExec. Similar to Process Injection, this value can be abused to obtain elevated privileges by causing a malicious DLL to be loaded and run in the context of separate processes on the computer. Malicious AppCert DLLs may also provide persistence by continuously being triggered by API activity.

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
- T1546.009: https://attack.mitre.org/techniques/T1546/009
- Reviewed: 2026-10-27
