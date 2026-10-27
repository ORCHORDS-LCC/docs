# 3CX Supply Chain Attack Technique Operationalization Review

## Reference

- Technique: **C0057 — 3CX Supply Chain Attack**

The 3CX Supply Chain Attack was the first publicly reported case of one supply chain compromise triggering another, leading to a cascading, two-stage intrusion. The initial supply chain attack began when a 3CX employee downloaded and executed a trojanized, end-of-life version of the X_Trader trading software from Trading Technologies. This provided UNC4736, a threat cluster associated with AppleJeus, access to the 3CX environment. From there UNC4736 compromised the Windows and macOS build environments used to distribute the 3CX desktop application to their customers. While 3CX serves more than 600,000 customers and 12 million users, only a subset of systems were affected. Subsequent targeting focused on victims in the defense and cryptocurrency sectors, where attackers deployed secondary payloads such as Gopuram for credential theft and persistence. The campaign began in late 2022 and was disrupted after security vendors publicly reported the compromise in March 2023.

## Operationalization review

1. Record the operational scope: which services, environments, and data the technique could affect.
2. Record the runbook that would be executed, and its owner.
3. Record the telemetry the runbook depends on, and whether it is retained long enough to investigate.
4. Record the detection that would surface the technique before or after it has an effect.
5. Record the recovery path, and the evidence that recovery has been rehearsed.
6. Record the residual operational risk where the runbook depends on a manual step.

## Review evidence

- the runbook and its owner;
- the telemetry retention and coverage record;
- the detection mapping;
- the exercise or rehearsal record.

## Limitations

An operationalization review describes the runbook and the evidence around it. It does not claim the technique has been prevented or detected in a live environment.

## Source

- MITRE ATT&CK: https://attack.mitre.org/
- C0057: https://attack.mitre.org/campaigns/C0057
- Reviewed: 2026-10-27
