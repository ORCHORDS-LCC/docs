# Indirect Command Execution Mitigation Technique Response Playbook

## Target technique

**T1202 — Indirect Command Execution Mitigation**


Identify or block potentially malicious software that may contain abusive functionality by using whitelisting tools, like AppLocker, or Software Restriction Policies where appropriate. . These mechanisms can also be used to disable and/or limit user access to Windows utilities and file types/locations used to invoke malicious execution.

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
- T1202: https://attack.mitre.org/mitigations/T1202
- Reviewed: 2026-10-27
