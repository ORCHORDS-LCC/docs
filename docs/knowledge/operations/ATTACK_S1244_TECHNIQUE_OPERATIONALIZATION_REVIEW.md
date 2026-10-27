# Medusa Ransomware Technique Operationalization Review

## Reference

- Technique: **S1244 — Medusa Ransomware**

Medusa Ransomware has been utilized in attacks since at least 2021. Medusa Ransomware has been known to be utilized in conjunction with living off the land techniques and remote management software. Medusa Ransomware has been used in campaigns associated with “double extortion” ransomware activity, where data is exfiltrated from victim environments prior to encryption, with threats to publish files if a ransom is not paid. Medusa Ransomware software was initially a closed ransomware variant which later evolved to a Ransomware as a Service (RaaS). Medusa Ransomware has impacted victims from a diverse range of sectors within a multitude of countries, and it is assessed Medusa Ransomware is used in an opportunistic manner.

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
- S1244: https://attack.mitre.org/software/S1244
- Reviewed: 2026-10-27
