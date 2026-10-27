# Supply Chain Compromise Mitigation Technique Platform Profile

## Reference

- Technique: **T1195 — Supply Chain Compromise Mitigation**
- Platforms named in the source: not stated

Apply supply chain risk management (SCRM) practices and procedures , such as supply chain analysis and appropriate risk management, throughout the life-cycle of a system. Leverage established software development lifecycle (SDLC) practices : * Uniquely Identify Supply Chain Elements, Processes, and Actors * Limit Access and Exposure within the Supply Chain * Establish and Maintain the Provenance of Elements, Processes, Tools, and Data * Share Information within Strict Limits * Perform SCRM Awareness and Training * Use Defensive Design for Systems, Elements, and Processes * Perform Continuous Integrator Review * Strengthen Delivery Mechanisms * Assure Sustainment Activities and Processes * Manage Disposal and Final Disposition Activities throughout the System or Element Life Cycle A patch management process should be implemented to check unused dependencies, unmaintained and/or previously vulnerable dependencies, unnecessary features, components, files, and documentation. Continuous monitoring of vulnerability sources and the use of automatic and manual code review tools should also be implemented as well.

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
- T1195: https://attack.mitre.org/mitigations/T1195
- Reviewed: 2026-10-27
