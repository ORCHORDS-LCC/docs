# Analytic 0692 Technique Operationalization Review

## Reference

- Technique: **AN0692 — Analytic 0692**

IAAS (Cloud images/VMs): A new VM/instance is launched from a non-approved or newly-seen image (AMI/GCP Image/Azure Image). On first boot, cloud-init/user-data or embedded agents download code, spawn system utilities, or open outbound C2/mining traffic. The analytic correlates Instance/Image Creation → Instance Start → in-guest Process/Command Execution and/or anomalous network traffic.

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
- AN0692: https://attack.mitre.org/detectionstrategies/DET0248#AN0692
- Reviewed: 2026-10-27
