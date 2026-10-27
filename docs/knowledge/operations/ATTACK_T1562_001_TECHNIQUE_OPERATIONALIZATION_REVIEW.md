# Disable or Modify Tools Technique Operationalization Review

## Reference

- Technique: **T1562.001 — Disable or Modify Tools**

Adversaries may modify and/or disable security tools to avoid possible detection of their malware/tools and activities. This may take many forms, such as killing security software processes or services, modifying / deleting Registry keys or configuration files so that tools do not operate properly, or other methods to interfere with security tools scanning or reporting information. Adversaries may also disable updates to prevent the latest security patches from reaching tools on victim systems. Adversaries may trigger a denial-of-service attack via legitimate system processes. It has been previously observed that the Windows Time Travel Debugging (TTD) monitor driver can be used to initiate a debugging session for a security tool (e.g., an EDR) and render the tool non-functional. By hooking the debugger into the EDR process, all child processes from the EDR will be automatically suspended. The attacker can terminate any EDR helper processes (unprotected by Windows Protected Process Light) by abusing the Process Explorer driver. In combination this will halt any attempt to restart services and cause the tool to crash. Adversaries may also tamper with artifacts deployed and utilized by security tools. Security tools may make dynamic changes to system components in order to maintain visibility into specific events. For example, security products may load their own modules and/or modify those loaded by processes to facilitate data collection. Similar to Indicator Blocking, adversaries may unhook or otherwise modify these features added by tools (especially those that exist in userland or are otherwise potentially accessible to adversaries) to avoid detection. For example, adversaries may abuse the Windows process mitigation policy to block certain endpoint detection and response (EDR) products from loading their user-mode code via DLLs. By spawning a process with the PROCESS_CREATION_MITIGATION_POLICY_BLOCK_NON_MICROSOFT_BINARIES_ALWAYS_ON attribute using API calls like UpdateProcThreadAttribute, adversaries may evade detection by endpoint security solutions that rely on DLLs that are not signed by Microsoft. Alternatively, they may add new directories to an EDR tool’s exclusion list, enabling them to hide malicious files via File/Path Exclusions. Adversaries may also focus on specific applications such as Sysmon. For example, the “Start” and “Enable” values in <code>HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\WMI\Autologger\EventLog-Microsoft-Windows-Sysmon-Operational</code> may be modified to tamper with and potentially disable Sysmon logging. On network devices, adversaries may attempt to skip digital signature verification checks by altering startup configuration files and effectively disabling firmware verification that typically occurs at boot. In cloud environments, tools disabled by adversaries may include cloud monitoring agents that report back to services such as AWS CloudWatch or Google Cloud Monitor. Furthermore, although defensive tools may have anti-tampering mechanisms, adversaries may abuse tools such as legitimate rootkit removal kits to impair and/or disable these tools. For example, adversaries have used tools such as GMER to find and shut down hidden processes and antivirus software on infected systems. Additionally, adversaries may exploit legitimate drivers from anti-virus software to gain access to kernel space (i.e. Exploitation for Privilege Escalation), which may lead to bypassing anti-tampering features.

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
- T1562.001: https://attack.mitre.org/techniques/T1562/001
- Reviewed: 2026-10-27
