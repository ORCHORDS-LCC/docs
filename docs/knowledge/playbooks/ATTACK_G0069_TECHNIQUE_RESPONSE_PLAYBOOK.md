# MuddyWater Technique Response Playbook

## Target technique

**G0069 — MuddyWater**


MuddyWater is a cyber espionage group assessed to be a subordinate element within Iran's Ministry of Intelligence and Security (MOIS). Since at least 2017, MuddyWater has targeted a range of government and private organizations across sectors, including telecommunications, local government, finance, defense, and oil and natural gas organizations, in the Middle East (specifically the UAE and Saudi Arabia), Asia, Africa, Europe, and North America. MuddyWater has reused domains dating back to October 2025, and has a preference for NameCheap and Hosterdaddy Private Limited (AS136557). In late 2025 and early 2026, MuddyWater used commercial satellite internet (i.e., Starlink) for command and control (C2) communication.

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
- G0069: https://attack.mitre.org/groups/G0069
- Reviewed: 2026-10-27
