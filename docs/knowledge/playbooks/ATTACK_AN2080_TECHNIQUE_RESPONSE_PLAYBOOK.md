# Analytic 2080 Technique Response Playbook

## Target technique

**AN2080 — Analytic 2080**

- Platforms: Linux

An analyst observes an AI-associated process access data outside $AuthorizedAIDataScope$, followed within $EndpointExfilWindow$ by transfer-capable execution and an outbound connection from the same lineage to a destination outside $AuthorizedAIEndpoints$.

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
- AN2080: https://attack.mitre.org/detectionstrategies/DET0927#AN2080
- Reviewed: 2026-10-27
