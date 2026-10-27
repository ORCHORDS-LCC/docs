# PHPsert Technique Response Playbook

## Target technique

**S9028 — PHPsert**

- Platforms: Network Devices

PHPsert is a webshell used to execute PHP code that has been in use since at least 2023 against targets in Japan, Singapore, Peru, Taiwan, Iran, Republic of Korea, and the Philippines. PHPsert is not typically deployed as a standalone but integrated into web content such as text editors and content management systems.

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
- S9028: https://attack.mitre.org/software/S9028
- Reviewed: 2026-10-27
