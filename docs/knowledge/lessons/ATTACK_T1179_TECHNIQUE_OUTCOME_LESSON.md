# T1179 Hooking Outcome Lesson

## Authoritative description

- Technique: **T1179 — Hooking**
- Tactics: persistence, privilege-escalation, credential-access
- Platforms: Windows

Windows processes often leverage application programming interface (API) functions to perform tasks that require reusable system resources. Windows API functions are typically stored in dynamic-link libraries (DLLs) as exported functions. Hooking involves redirecting calls to these functions and can be implemented via: * **Hooks procedures**, which intercept and execute designated code in response to events such as messages, keystrokes, and mouse inputs. * **Import address table (IAT) hooking**, which use modifications to a process’s IAT, where pointers to imported API functions are stored. * **Inline hooking**, which overwrites the first bytes in an API function to redirect code flow. Similar to Process Injection, adversaries may use hooking to load and execute malicious code within the context of another process, masking the execution while also allowing access to the process's memory and possibly elevated privileges. Installing hooking mechanisms may also provide Persistence via continuous invocation when the functions are called through normal use. Malicious hooking mechanisms may also capture API calls that include parameters that reveal user authentication credentials for Credential Access. Hooking is commonly utilized by Rootkits to conceal files, processes, Registry keys, and other objects in order to hide malware and associated behaviors.

## Reusable lesson

This technique should be treated as an explicit review question when it is relevant to the system or organisation, rather than assumed to be covered by a generic control statement or by tooling that reports a related signal.

## Apply the lesson

1. Define the real scope before judging coverage.
2. Inspect current technical, process, governance, or operational evidence.
3. Separate documented intent from verified behaviour.
4. Record partial coverage and unresolved gaps instead of converting them into a pass.
5. Revisit when the underlying scope, threat environment, technology, suppliers, or mission materially changes.

## Source

- MITRE ATT&CK: https://attack.mitre.org/
- T1179: https://attack.mitre.org/techniques/T1179
- Reviewed: 2026-10-27

## Boundary

This lesson is derived from the published technique description. It does not invent an incident, prescribe one implementation, or claim the technique has been addressed.
