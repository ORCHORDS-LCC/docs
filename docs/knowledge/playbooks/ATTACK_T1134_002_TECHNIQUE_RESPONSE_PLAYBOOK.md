# Create Process with Token Technique Response Playbook

## Target technique

**T1134.002 — Create Process with Token**

- Tactics: stealth, privilege-escalation
- Platforms: Windows

Adversaries may create a new process with an existing token to escalate privileges and bypass access controls. Processes can be created with the token and resulting security context of another user using features such as <code>CreateProcessWithTokenW</code> and <code>runas</code>. Creating processes with a token not associated with the current user may require the credentials of the target user, specific privileges to impersonate that user, or access to the token to be used. For example, the token could be duplicated via Token Impersonation/Theft or created via Make and Impersonate Token before being used to create a process. While this technique is distinct from Token Impersonation/Theft, the techniques can be used in conjunction where a token is duplicated and then used to create a new process.

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
- T1134.002: https://attack.mitre.org/techniques/T1134/002
- Reviewed: 2026-10-27
