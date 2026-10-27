# Analytic 0680 Technique Response Playbook

## Target technique

**AN0680 — Analytic 0680**

- Platforms: SaaS

Unusual or excessive database/table exports from SaaS database platforms (e.g., Snowflake, Firebase, BigQuery, Airtable) by users or apps not in known analytics or dev groups. Defender observes access patterns outside baseline working hours or with new query templates, and correlates those with audit logs or file downloads.

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
- AN0680: https://attack.mitre.org/detectionstrategies/DET0242#AN0680
- Reviewed: 2026-10-27
