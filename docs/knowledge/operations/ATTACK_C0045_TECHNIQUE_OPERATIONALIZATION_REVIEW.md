# ShadowRay Technique Operationalization Review

## Reference

- Technique: **C0045 — ShadowRay**

ShadowRay was a campaign that began in late 2023 targeting the education, cryptocurrency, biopharma, and other sectors through a vulnerability (CVE-2023-48022) in the Ray AI framework named ShadowRay. According to security researchers ShadowRay was the first known instance of AI workloads being activley exploited in the wild through vulnerabilities in AI infrastructure. CVE-2023-48022, which allows access to compute resources and sensitive data for exposed instances, remains unpatched and has been disputed by the vendor as they maintain that Ray is not intended for use outside of a strictly controlled network environment.

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
- C0045: https://attack.mitre.org/campaigns/C0045
- Reviewed: 2026-10-27
