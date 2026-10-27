# FIN7 Technique Response Playbook

## Target technique

**G0046 — FIN7**


FIN7 is a financially-motivated threat group that has been active since 2013. FIN7 has targeted the retail, restaurant, hospitality, software, consulting, financial services, medical equipment, cloud services, media, food and beverage, transportation, pharmaceutical, and utilities industries in the United States. A portion of FIN7 was operated out of a front company called Combi Security and often used point-of-sale malware for targeting efforts. Since 2020, FIN7 shifted operations to big game hunting (BGH), including use of REvil ransomware and their own Ransomware-as-a-Service (RaaS), Darkside. FIN7 may be linked to the Carbanak Group, but multiple threat groups have been observed using Carbanak, leading these groups to be tracked separately.

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
- G0046: https://attack.mitre.org/groups/G0046
- Reviewed: 2026-10-27
