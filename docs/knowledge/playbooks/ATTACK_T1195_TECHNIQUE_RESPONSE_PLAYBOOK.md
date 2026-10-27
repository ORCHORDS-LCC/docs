# Supply Chain Compromise Mitigation Technique Response Playbook

## Target technique

**T1195 — Supply Chain Compromise Mitigation**


Apply supply chain risk management (SCRM) practices and procedures , such as supply chain analysis and appropriate risk management, throughout the life-cycle of a system. Leverage established software development lifecycle (SDLC) practices : * Uniquely Identify Supply Chain Elements, Processes, and Actors * Limit Access and Exposure within the Supply Chain * Establish and Maintain the Provenance of Elements, Processes, Tools, and Data * Share Information within Strict Limits * Perform SCRM Awareness and Training * Use Defensive Design for Systems, Elements, and Processes * Perform Continuous Integrator Review * Strengthen Delivery Mechanisms * Assure Sustainment Activities and Processes * Manage Disposal and Final Disposition Activities throughout the System or Element Life Cycle A patch management process should be implemented to check unused dependencies, unmaintained and/or previously vulnerable dependencies, unnecessary features, components, files, and documentation. Continuous monitoring of vulnerability sources and the use of automatic and manual code review tools should also be implemented as well.

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
- T1195: https://attack.mitre.org/mitigations/T1195
- Reviewed: 2026-10-27
