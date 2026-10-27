# Hooking Technique Engineering Review

## Reference

- Technique: **T1179 — Hooking**

Windows processes often leverage application programming interface (API) functions to perform tasks that require reusable system resources. Windows API functions are typically stored in dynamic-link libraries (DLLs) as exported functions. Hooking involves redirecting calls to these functions and can be implemented via: * **Hooks procedures**, which intercept and execute designated code in response to events such as messages, keystrokes, and mouse inputs. * **Import address table (IAT) hooking**, which use modifications to a process’s IAT, where pointers to imported API functions are stored. * **Inline hooking**, which overwrites the first bytes in an API function to redirect code flow. Similar to Process Injection, adversaries may use hooking to load and execute malicious code within the context of another process, masking the execution while also allowing access to the process's memory and possibly elevated privileges. Installing hooking mechanisms may also provide Persistence via continuous invocation when the functions are called through normal use. Malicious hooking mechanisms may also capture API calls that include parameters that reveal user authentication credentials for Credential Access. Hooking is commonly utilized by Rootkits to conceal files, processes, Registry keys, and other objects in order to hide malware and associated behaviors.

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
- T1179: https://attack.mitre.org/techniques/T1179
- Reviewed: 2026-10-27
