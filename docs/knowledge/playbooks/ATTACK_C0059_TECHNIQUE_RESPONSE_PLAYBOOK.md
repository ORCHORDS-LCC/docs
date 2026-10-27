# Salesforce Data Exfiltration Technique Response Playbook

## Target technique

**C0059 — Salesforce Data Exfiltration**


The Salesforce Data Exfiltration campaign began in October 2024 with financially-motivated threat actor UNC6040 using Spearphishing Voice (vishing) to compromise corporate Salesforce instances for large-scale data theft and extortion. Following the initial data theft, victim organizations received extortion demands from a separate threat actor, UNC6240, who claimed to be the “ShinyHunters” group. The observed infrastructure and TTPs used during the Salesforce Data Exfiltration campaign overlap with those used by threat groups with suspected ties to the broader collective known as "The Com.” These overlaps could plausibly be the result of associated actors operating within the same communities and are not necessarily an indication of a direct operational relationship.

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
- C0059: https://attack.mitre.org/campaigns/C0059
- Reviewed: 2026-10-27
