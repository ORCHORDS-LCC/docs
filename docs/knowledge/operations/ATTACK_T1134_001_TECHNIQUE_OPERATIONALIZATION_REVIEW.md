# Token Impersonation/Theft Technique Operationalization Review

## Reference

- Technique: **T1134.001 — Token Impersonation/Theft**

Adversaries may duplicate then impersonate another user's existing token to escalate privileges and bypass access controls. For example, an adversary can duplicate an existing token using `DuplicateToken` or `DuplicateTokenEx`. The token can then be used with `ImpersonateLoggedOnUser` to allow the calling thread to impersonate a logged on user's security context, or with `SetThreadToken` to assign the impersonated token to a thread. An adversary may perform Token Impersonation/Theft when they have a specific, existing process they want to assign the duplicated token to. For example, this may be useful for when the target user has a non-network logon session on the system. When an adversary would instead use a duplicated token to create a new process rather than attaching to an existing process, they can additionally Create Process with Token using `CreateProcessWithTokenW` or `CreateProcessAsUserW`. Token Impersonation/Theft is also distinct from Make and Impersonate Token in that it refers to duplicating an existing token, rather than creating a new one.

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
- T1134.001: https://attack.mitre.org/techniques/T1134/001
- Reviewed: 2026-10-27
