# APT38 Technique Response Playbook

## Target technique

**G0082 — APT38**


APT38 is a North Korean state-sponsored threat group that specializes in financial cyber operations; it has been attributed to the Reconnaissance General Bureau. Active since at least 2014, APT38 has targeted banks, financial institutions, casinos, cryptocurrency exchanges, SWIFT system endpoints, and ATMs in at least 38 countries worldwide. Significant operations include the 2016 Bank of Bangladesh heist, Bancomext and Banco de Chile , along with software supply chain compromises and destructive malware attacks. North Korean group definitions are known to have significant overlap, and some security researchers report all North Korean state-sponsored cyber activity under the name Lazarus Group instead of tracking clusters or subgroups.

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
- G0082: https://attack.mitre.org/groups/G0082
- Reviewed: 2026-10-27
