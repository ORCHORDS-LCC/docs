# VOID MANTICORE Technique Response Playbook

## Target technique

**G1055 — VOID MANTICORE**


VOID MANTICORE is a threat group assessed to operate on behalf of Iran’s Ministry of Intelligence and Security (MOIS). Active since at least mid-2022, VOID MANTICORE has targeted government entities, critical infrastructure, and private sector organizations across Albania, Israel, and the United States. VOID MANTICORE conducts destructive cyber operations, combining wiper attacks with hack-and-leak campaigns. The group has operated under multiple public-facing personas, including HomeLand Justice in operations against Albania, Karma and Karma Below in campaigns targeting Israeli organizations, and Handala Hack, its current primary persona, which has claimed activity against Israeli and U.S. entities, including a March 2026 attack against Stryker Corporation. VOID MANTICORE has been observed collaborating with Scarred Manticore, which has been linked to initial access operations preceding VOID MANTICORE’s activity.

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
- G1055: https://attack.mitre.org/groups/G1055
- Reviewed: 2026-10-27
