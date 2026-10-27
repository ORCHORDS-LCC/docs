# ListPlanting Technique Platform Profile

## Reference

- Technique: **T1055.015 — ListPlanting**
- Platforms named in the source: Windows

Adversaries may abuse list-view controls to inject malicious code into hijacked processes in order to evade process-based defenses as well as possibly elevate privileges. ListPlanting is a method of executing arbitrary code in the address space of a separate live process. Code executed via ListPlanting may also evade detection from security products since the execution is masked under a legitimate process. List-view controls are user interface windows used to display collections of items. Information about an application's list-view settings are stored within the process' memory in a <code>SysListView32</code> control. ListPlanting (a form of message-passing "shatter attack") may be performed by copying code into the virtual address space of a process that uses a list-view control then using that code as a custom callback for sorting the listed items. Adversaries must first copy code into the target process’ memory space, which can be performed various ways including by directly obtaining a handle to the <code>SysListView32</code> child of the victim process window (via Windows API calls such as <code>FindWindow</code> and/or <code>EnumWindows</code>) or other Process Injection methods. Some variations of ListPlanting may allocate memory in the target process but then use window messages to copy the payload, to avoid the use of the highly monitored <code>WriteProcessMemory</code> function. For example, an adversary can use the <code>PostMessage</code> and/or <code>SendMessage</code> API functions to send <code>LVM_SETITEMPOSITION</code> and <code>LVM_GETITEMPOSITION</code> messages, effectively copying a payload 2 bytes at a time to the allocated memory. Finally, the payload is triggered by sending the <code>LVM_SORTITEMS</code> message to the <code>SysListView32</code> child of the process window, with the payload within the newly allocated buffer passed and executed as the <code>ListView_SortItems</code> callback.

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
- T1055.015: https://attack.mitre.org/techniques/T1055/015
- Reviewed: 2026-10-27
