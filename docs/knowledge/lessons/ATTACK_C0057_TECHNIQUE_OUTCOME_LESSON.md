# C0057 3CX Supply Chain Attack Outcome Lesson

## Authoritative description

- Technique: **C0057 — 3CX Supply Chain Attack**

The 3CX Supply Chain Attack was the first publicly reported case of one supply chain compromise triggering another, leading to a cascading, two-stage intrusion. The initial supply chain attack began when a 3CX employee downloaded and executed a trojanized, end-of-life version of the X_Trader trading software from Trading Technologies. This provided UNC4736, a threat cluster associated with AppleJeus, access to the 3CX environment. From there UNC4736 compromised the Windows and macOS build environments used to distribute the 3CX desktop application to their customers. While 3CX serves more than 600,000 customers and 12 million users, only a subset of systems were affected. Subsequent targeting focused on victims in the defense and cryptocurrency sectors, where attackers deployed secondary payloads such as Gopuram for credential theft and persistence. The campaign began in late 2022 and was disrupted after security vendors publicly reported the compromise in March 2023.

## Reusable lesson

This technique should be treated as an explicit review question when it is relevant to the system or organisation, rather than assumed to be covered by a generic control statement or by tooling that reports a related signal.

## Apply the lesson

1. Define the real scope before judging coverage.
2. Inspect current technical, process, governance, or operational evidence.
3. Separate documented intent from verified behaviour.
4. Record partial coverage and unresolved gaps instead of converting them into a pass.
5. Revisit when the underlying scope, threat environment, technology, suppliers, or mission materially changes.

## Source

- MITRE ATT&CK: https://attack.mitre.org/
- C0057: https://attack.mitre.org/campaigns/C0057
- Reviewed: 2026-10-27

## Boundary

This lesson is derived from the published technique description. It does not invent an incident, prescribe one implementation, or claim the technique has been addressed.
