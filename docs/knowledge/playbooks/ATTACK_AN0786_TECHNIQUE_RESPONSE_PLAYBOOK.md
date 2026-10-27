# Analytic 0786 Technique Response Playbook

## Target technique

**AN0786 — Analytic 0786**

- Platforms: Windows

Detection of suspicious token manipulation chains: use of token-related APIs (e.g., LogonUser, DuplicateTokenEx) or commands (runas) → spawning of a new process under a different security context (e.g., SYSTEM) → mismatched parent-child process lineage or anomalies in Event Tracing for Windows (ETW) token/PPID data → abnormal lateral or privilege escalation activity.

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
- AN0786: https://attack.mitre.org/detectionstrategies/DET0283#AN0786
- Reviewed: 2026-10-27
