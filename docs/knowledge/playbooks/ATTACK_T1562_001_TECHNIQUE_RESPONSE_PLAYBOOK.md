# Disable or Modify Tools Technique Response Playbook

## Target technique

**T1562.001 — Disable or Modify Tools**

- Tactics: stealth
- Platforms: Containers, IaaS, Linux, macOS, Network Devices, Windows

Adversaries may modify and/or disable security tools to avoid possible detection of their malware/tools and activities. This may take many forms, such as killing security software processes or services, modifying / deleting Registry keys or configuration files so that tools do not operate properly, or other methods to interfere with security tools scanning or reporting information. Adversaries may also disable updates to prevent the latest security patches from reaching tools on victim systems. Adversaries may trigger a denial-of-service attack via legitimate system processes. It has been previously observed that the Windows Time Travel Debugging (TTD) monitor driver can be used to initiate a debugging session for a security tool (e.g., an EDR) and render the tool non-functional. By hooking the debugger into the EDR process, all child processes from the EDR will be automatically suspended. The attacker can terminate any EDR helper processes (unprotected by Windows Protected Process Light) by abusing the Process Explorer driver. In combination this will halt any attempt to restart services and cause the tool to crash. Adversaries may also tamper with artifacts deployed and utilized by security tools. Security tools may make dynamic changes to system components in order to maintain visibility into specific events. For example, security products may load their own modules and/or modify those loaded by processes to facilitate data collection. Similar to Indicator Blocking, adversaries may unhook or otherwise modify these features added by tools (especially those that exist in userland or are otherwise potentially accessible to adversaries) to avoid detection. For example, adversaries may abuse the Windows process mitigation policy to block certain endpoint detection and response (EDR) products from loading their user-mode code via DLLs. By spawning a process with the PROCESS_CREATION_MITIGATION_POLICY_BLOCK_NON_MICROSOFT_BINARIES_ALWAYS_ON attribute using API calls like UpdateProcThreadAttribute, adversaries may evade detection by endpoint security solutions that rely on DLLs that are not signed by Microsoft. Alternatively, they may add new directories to an EDR tool’s exclusion list, enabling them to hide malicious files via File/Path Exclusions. Adversaries may also focus on specific applications such as Sysmon. For example, the “Start” and “Enable” values in <code>HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\WMI\Autologger\EventLog-Microsoft-Windows-Sysmon-Operational</code> may be modified to tamper with and potentially disable Sysmon logging. On network devices, adversaries may attempt to skip digital signature verification checks by altering startup configuration files and effectively disabling firmware verification that typically occurs at boot. In cloud environments, tools disabled by adversaries may include cloud monitoring agents that report back to services such as AWS CloudWatch or Google Cloud Monitor. Furthermore, although defensive tools may have anti-tampering mechanisms, adversaries may abuse tools such as legitimate rootkit removal kits to impair and/or disable these tools. For example, adversaries have used tools such as GMER to find and shut down hidden processes and antivirus software on infected systems. Additionally, adversaries may exploit legitimate drivers from anti-virus software to gain access to kernel space (i.e. Exploitation for Privilege Escalation), which may lead to bypassing anti-tampering features.

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
- T1562.001: https://attack.mitre.org/techniques/T1562/001
- Reviewed: 2026-10-27
