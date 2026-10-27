# Ninja Technique Response Playbook

## Target technique

**S1100 — Ninja**

- Platforms: Windows

Ninja is a malware developed in C++ that has been used by ToddyCat to penetrate networks and control remote systems since at least 2020. Ninja is possibly part of a post exploitation toolkit exclusively used by ToddyCat and allows multiple operators to work simultaneously on the same machine. Ninja has been used against government and military entities in Europe and Asia and observed in specific infection chains being deployed by Samurai.

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
- S1100: https://attack.mitre.org/software/S1100
- Reviewed: 2026-10-27
