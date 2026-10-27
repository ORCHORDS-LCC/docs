# Services Registry Permissions Weakness Technique Response Playbook

## Target technique

**T1574.011 — Services Registry Permissions Weakness**

- Tactics: stealth, execution
- Platforms: Windows

Adversaries may execute their own malicious payloads by hijacking the Registry entries used by services. Flaws in the permissions for Registry keys related to services can allow adversaries to redirect the originally specified executable to one they control, launching their own code when a service starts. Windows stores local service configuration information in the Registry under <code>HKLM\SYSTEM\CurrentControlSet\Services</code>. The information stored under a service's Registry keys can be manipulated to modify a service's execution parameters through tools such as the service controller, sc.exe, PowerShell, or Reg. Access to Registry keys is controlled through access control lists and user permissions. If the permissions for users and groups are not properly set and allow access to the Registry keys for a service, adversaries may change the service's binPath/ImagePath to point to a different executable under their control. When the service starts or is restarted, the adversary-controlled program will execute, allowing the adversary to establish persistence and/or privilege escalation to the account context the service is set to execute under (local/domain account, SYSTEM, LocalService, or NetworkService). Adversaries may also alter other Registry keys in the service’s Registry tree. For example, the <code>FailureCommand</code> key may be changed so that the service is executed in an elevated context anytime the service fails or is intentionally corrupted. The <code>Performance</code> key contains the name of a driver service's performance DLL and the names of several exported functions in the DLL. If the <code>Performance</code> key is not already present and if an adversary-controlled user has the <code>Create Subkey</code> permission, adversaries may create the <code>Performance</code> key in the service’s Registry tree to point to a malicious DLL. Adversaries may also add the <code>Parameters</code> key, which can reference malicious drivers file paths. This technique has been identified to be a method of abuse by configuring DLL file paths within the <code>Parameters</code> key of a given services registry configuration. By placing and configuring the <code>Parameters</code> key to reference a malicious DLL, adversaries can ensure that their code is loaded persistently whenever the associated service or library is invoked. For example, the registry path <code>HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\WinSock2\Parameters</code> contains the <code>AutodiaDLL</code> value, which specifies the DLL to be loaded for autodial funcitionality. An adversary could set the <code>AutodiaDLL</code> to point to a hijacked or malicious DLL: <code>"AutodialDLL"="c:\temp\foo.dll"</code> This ensures persistence, as it causes the DLL (in this case, foo.dll) to be loaded each time the Winsock 2 library is invoked.

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
- T1574.011: https://attack.mitre.org/techniques/T1574/011
- Reviewed: 2026-10-27
