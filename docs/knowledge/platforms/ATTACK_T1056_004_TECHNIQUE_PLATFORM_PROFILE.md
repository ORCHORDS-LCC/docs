# Credential API Hooking Technique Platform Profile

## Reference

- Technique: **T1056.004 — Credential API Hooking**
- Platforms named in the source: Windows, Linux, macOS

Adversaries may hook into Windows application programming interface (API) functions and Linux system functions to collect user credentials. Malicious hooking mechanisms may capture API or function calls that include parameters that reveal user authentication credentials. Unlike Keylogging, this technique focuses specifically on API functions that include parameters that reveal user credentials. In Windows, hooking involves redirecting calls to these functions and can be implemented via: * **Hooks procedures**, which intercept and execute designated code in response to events such as messages, keystrokes, and mouse inputs. * **Import address table (IAT) hooking**, which use modifications to a process’s IAT, where pointers to imported API functions are stored. * **Inline hooking**, which overwrites the first bytes in an API function to redirect code flow. In Linux and macOS, adversaries may hook into system functions via the `LD_PRELOAD` (Linux) or `DYLD_INSERT_LIBRARIES` (macOS) environment variables, which enables loading shared libraries into a program’s address space. For example, an adversary may capture credentials by hooking into the `libc read` function leveraged by SSH or SCP.

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
- T1056.004: https://attack.mitre.org/techniques/T1056/004
- Reviewed: 2026-10-27
