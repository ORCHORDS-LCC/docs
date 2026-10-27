# Search Threat Vendor Data Technique Response Playbook

## Target technique

**T1681 — Search Threat Vendor Data**

- Tactics: reconnaissance
- Platforms: PRE

Threat actors may seek information/indicators from closed or open threat intelligence sources gathered about their own campaigns, as well as those conducted by other adversaries that may align with their target industries, capabilities/objectives, or other operational concerns. These reports may include descriptions of behavior, detailed breakdowns of attacks, atomic indicators such as malware hashes or IP addresses, timelines of a group’s activity, and more. Adversaries may change their behavior when planning their future operations. Adversaries have been observed replacing atomic indicators mentioned in blog posts in under a week. Adversaries have also been seen searching for their own domain names in threat vendor data and then taking them down, likely to avoid seizure or further investigation. This technique is distinct from Threat Intel Vendors in that it describes threat actors performing reconnaissance on their own activity, not in search of victim information.

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
- T1681: https://attack.mitre.org/techniques/T1681
- Reviewed: 2026-10-27
