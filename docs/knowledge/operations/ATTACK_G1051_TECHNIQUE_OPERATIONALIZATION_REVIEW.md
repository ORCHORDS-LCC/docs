# Medusa Group Technique Operationalization Review

## Reference

- Technique: **G1051 — Medusa Group**

Medusa Group has been active since at least 2021 and was initially operated as a closed ransomware group before evolving into a Ransomware-as-a-Service (RaaS) operation. Some reporting indicates that certain attacks may still be conducted directly by the ransomware’s core developers. Public sources have also referred to the group as “Spearwing” or “Medusa Actors.” Medusa Group employs living-off-the-land techniques, frequently leveraging publicly available tools and common remote management software to conduct operations. The group engages in double extortion tactics, exfiltrating data prior to encryption and threatening to publish stolen information if ransom demands are not met. For initial access, Medusa Group has exploited publicly known vulnerabilities, conducted phishing campaigns, and used credentials or access purchased from Initial Access Brokers (IABs). The group is opportunistic and has targeted a wide range of sectors globally.

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
- G1051: https://attack.mitre.org/groups/G1051
- Reviewed: 2026-10-27
