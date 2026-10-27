# Token Impersonation/Theft Technique Response Playbook

## Target technique

**T1134.001 — Token Impersonation/Theft**

- Tactics: stealth, privilege-escalation
- Platforms: Windows

Adversaries may duplicate then impersonate another user's existing token to escalate privileges and bypass access controls. For example, an adversary can duplicate an existing token using `DuplicateToken` or `DuplicateTokenEx`. The token can then be used with `ImpersonateLoggedOnUser` to allow the calling thread to impersonate a logged on user's security context, or with `SetThreadToken` to assign the impersonated token to a thread. An adversary may perform Token Impersonation/Theft when they have a specific, existing process they want to assign the duplicated token to. For example, this may be useful for when the target user has a non-network logon session on the system. When an adversary would instead use a duplicated token to create a new process rather than attaching to an existing process, they can additionally Create Process with Token using `CreateProcessWithTokenW` or `CreateProcessAsUserW`. Token Impersonation/Theft is also distinct from Make and Impersonate Token in that it refers to duplicating an existing token, rather than creating a new one.

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
- T1134.001: https://attack.mitre.org/techniques/T1134/001
- Reviewed: 2026-10-27
