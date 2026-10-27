# Analytic 2070 Technique Response Playbook

## Target technique

**AN2070 — Analytic 2070**

- Platforms: SaaS

An analyst observes an authenticated AI interaction initiate resource access, tool invocation, API operation, or privileged activity outside $AuthorizedAIWorkflow$ or $AICapabilityScope$, without an authorized workflow transition permitting the operation.

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
- AN2070: https://attack.mitre.org/detectionstrategies/DET0923#AN2070
- Reviewed: 2026-10-27
