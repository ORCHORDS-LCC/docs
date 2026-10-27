# Malicious Library Technique Response Playbook

## Target technique

**T1204.005 — Malicious Library**

- Tactics: execution
- Platforms: Linux, macOS, Windows

Adversaries may rely on a user installing a malicious library to facilitate execution. Threat actors may Upload Malware to package managers such as NPM and PyPi, as well as to public code repositories such as GitHub. User may install libraries without realizing they are malicious, thus bypassing techniques that specifically achieve Initial Access. This can lead to the execution of malicious code, such as code that establishes persistence, steals data, or mines cryptocurrency. In some cases, threat actors may compromise and backdoor existing popular libraries (i.e., Compromise Software Dependencies and Development Tools). Alternatively, they may create entirely new packages and leverage behaviors such as typosquatting to encourage users to install them.

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
- T1204.005: https://attack.mitre.org/techniques/T1204/005
- Reviewed: 2026-10-27
