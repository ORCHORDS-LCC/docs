# VIRTUALPITA Technique Operationalization Review

## Reference

- Technique: **S1217 — VIRTUALPITA**

VIRTUALPITA is a passive backdoor with ESXi and Linux vCenter variants capable of command execution, file transfer, and starting and stopping processes. VIRTUALPITA has been in use since at least 2022 including by UNC3886 who leveraged malicious vSphere Installation Bundles (VIBs) for install on ESXi hypervisors.

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
- S1217: https://attack.mitre.org/software/S1217
- Reviewed: 2026-10-27
