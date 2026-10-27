# Services Registry Permissions Weakness Technique Engineering Review

## Reference

- Technique: **T1574.011 — Services Registry Permissions Weakness**

Adversaries may execute their own malicious payloads by hijacking the Registry entries used by services. Flaws in the permissions for Registry keys related to services can allow adversaries to redirect the originally specified executable to one they control, launching their own code when a service starts. Windows stores local service configuration information in the Registry under HKLM\SYSTEM\CurrentControlSet\Services. The information stored under a service's Registry keys can be manipulated to modify a service's execution parameters through tools such as the service controller, sc.exe, PowerShell, or Reg. Access to Registry keys is controlled through access control lists and user permissions. If the permissions for users and groups are not properly set and allow access to the Registry keys for a service, adversaries may change the service's binPath/ImagePath to point to a different executable under their control. When the service starts or is restarted, the adversary-controlled program will execute, allowing the adversary to establish persistence and/or privilege escalation to the account context the service is set to execute under (local/domain account, SYSTEM, LocalService, or NetworkService). Adversaries may also alter other Registry keys in the service’s Registry tree. For example, the FailureCommand key may be changed so that the service is executed in an elevated context anytime the service fails or is intentionally corrupted. The Performance key contains the name of a driver service's performance DLL and the names of several exported functions in the DLL. If the Performance key is not already present and if an adversary-controlled user has the Create Subkey permission, adversaries may create the Performance key in the service’s Registry tree to point to a malicious DLL. Adversaries may also add the Parameters key, which can reference malicious drivers file paths. This technique has been identified to be a method of abuse by configuring DLL file paths within the Parameters key of a given services registry configuration. By placing and configuring the Parameters key to reference a malicious DLL, adversaries can ensure that their code is loaded persistently whenever the associated service or library is invoked. For example, the registry path HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\WinSock2\Parameters contains the AutodiaDLL value, which specifies the DLL to be loaded for autodial funcitionality. An adversary could set the AutodiaDLL to point to a hijacked or malicious DLL: "AutodialDLL"="c:\temp\foo.dll" This ensures persistence, as it causes the DLL (in this case, foo.dll) to be loaded each time the Winsock 2 library is invoked.

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
- T1574.011: https://attack.mitre.org/techniques/T1574/011
- Reviewed: 2026-10-27
