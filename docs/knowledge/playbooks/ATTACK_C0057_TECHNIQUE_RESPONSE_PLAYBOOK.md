# 3CX Supply Chain Attack Technique Response Playbook

## Target technique

**C0057 — 3CX Supply Chain Attack**


The 3CX Supply Chain Attack was the first publicly reported case of one supply chain compromise triggering another, leading to a cascading, two-stage intrusion. The initial supply chain attack began when a 3CX employee downloaded and executed a trojanized, end-of-life version of the X_Trader trading software from Trading Technologies. This provided UNC4736, a threat cluster associated with AppleJeus, access to the 3CX environment. From there UNC4736 compromised the Windows and macOS build environments used to distribute the 3CX desktop application to their customers. While 3CX serves more than 600,000 customers and 12 million users, only a subset of systems were affected. Subsequent targeting focused on victims in the defense and cryptocurrency sectors, where attackers deployed secondary payloads such as Gopuram for credential theft and persistence. The campaign began in late 2022 and was disrupted after security vendors publicly reported the compromise in March 2023.

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
- C0057: https://attack.mitre.org/campaigns/C0057
- Reviewed: 2026-10-27
