# Supply Chain Compromise Mitigation Technique Operationalization Review

## Reference

- Technique: **T1195 — Supply Chain Compromise Mitigation**

Apply supply chain risk management (SCRM) practices and procedures , such as supply chain analysis and appropriate risk management, throughout the life-cycle of a system. Leverage established software development lifecycle (SDLC) practices : * Uniquely Identify Supply Chain Elements, Processes, and Actors * Limit Access and Exposure within the Supply Chain * Establish and Maintain the Provenance of Elements, Processes, Tools, and Data * Share Information within Strict Limits * Perform SCRM Awareness and Training * Use Defensive Design for Systems, Elements, and Processes * Perform Continuous Integrator Review * Strengthen Delivery Mechanisms * Assure Sustainment Activities and Processes * Manage Disposal and Final Disposition Activities throughout the System or Element Life Cycle A patch management process should be implemented to check unused dependencies, unmaintained and/or previously vulnerable dependencies, unnecessary features, components, files, and documentation. Continuous monitoring of vulnerability sources and the use of automatic and manual code review tools should also be implemented as well.

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
- T1195: https://attack.mitre.org/mitigations/T1195
- Reviewed: 2026-10-27
