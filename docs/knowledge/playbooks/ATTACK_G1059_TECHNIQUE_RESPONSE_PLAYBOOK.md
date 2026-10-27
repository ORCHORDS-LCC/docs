# NIMBUS MANTICORE Technique Response Playbook

## Target technique

**G1059 — NIMBUS MANTICORE**


NIMBUS MANTICORE is a State Sponsored cyber espionage group associated with the Iranian Regime specifically the Iranian Revolutionary Guard Corps (IRGC). NIMBUS MANTICORE has employed social engineering attacks to include HR related themes and has leveraged custom malware against its victims. NIMBUS MANTICORE has sought sensitive information in victims’ environments to include network/IT documentation, intellectual property and emails. NIMBUS MANTICORE has also leveraged compromised organizations as pivot points to access other organizations of interest. NIMBUS MANTICORE has been active since 2021 and has targeted critical infrastructure organizations to include aviation, aerospace, telecommunications and defense and information technology related organizations within the United States, Australia, Midde East and Europe.

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
- G1059: https://attack.mitre.org/groups/G1059
- Reviewed: 2026-10-27
