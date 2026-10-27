# Token Impersonation/Theft Technique Platform Profile

## Reference

- Technique: **T1134.001 — Token Impersonation/Theft**
- Platforms named in the source: Windows

Adversaries may duplicate then impersonate another user's existing token to escalate privileges and bypass access controls. For example, an adversary can duplicate an existing token using `DuplicateToken` or `DuplicateTokenEx`. The token can then be used with `ImpersonateLoggedOnUser` to allow the calling thread to impersonate a logged on user's security context, or with `SetThreadToken` to assign the impersonated token to a thread. An adversary may perform Token Impersonation/Theft when they have a specific, existing process they want to assign the duplicated token to. For example, this may be useful for when the target user has a non-network logon session on the system. When an adversary would instead use a duplicated token to create a new process rather than attaching to an existing process, they can additionally Create Process with Token using `CreateProcessWithTokenW` or `CreateProcessAsUserW`. Token Impersonation/Theft is also distinct from Make and Impersonate Token in that it refers to duplicating an existing token, rather than creating a new one.

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
- T1134.001: https://attack.mitre.org/techniques/T1134/001
- Reviewed: 2026-10-27
