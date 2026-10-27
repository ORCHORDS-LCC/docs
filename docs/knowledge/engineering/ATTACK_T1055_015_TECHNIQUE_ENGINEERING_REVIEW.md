# ListPlanting Technique Engineering Review

## Reference

- Technique: **T1055.015 — ListPlanting**

Adversaries may abuse list-view controls to inject malicious code into hijacked processes in order to evade process-based defenses as well as possibly elevate privileges. ListPlanting is a method of executing arbitrary code in the address space of a separate live process. Code executed via ListPlanting may also evade detection from security products since the execution is masked under a legitimate process. List-view controls are user interface windows used to display collections of items. Information about an application's list-view settings are stored within the process' memory in a SysListView32 control. ListPlanting (a form of message-passing "shatter attack") may be performed by copying code into the virtual address space of a process that uses a list-view control then using that code as a custom callback for sorting the listed items. Adversaries must first copy code into the target process’ memory space, which can be performed various ways including by directly obtaining a handle to the SysListView32 child of the victim process window (via Windows API calls such as FindWindow and/or EnumWindows) or other Process Injection methods. Some variations of ListPlanting may allocate memory in the target process but then use window messages to copy the payload, to avoid the use of the highly monitored WriteProcessMemory function. For example, an adversary can use the PostMessage and/or SendMessage API functions to send LVM_SETITEMPOSITION and LVM_GETITEMPOSITION messages, effectively copying a payload 2 bytes at a time to the allocated memory. Finally, the payload is triggered by sending the LVM_SORTITEMS message to the SysListView32 child of the process window, with the payload within the newly allocated buffer passed and executed as the ListView_SortItems callback.

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
- T1055.015: https://attack.mitre.org/techniques/T1055/015
- Reviewed: 2026-10-27
