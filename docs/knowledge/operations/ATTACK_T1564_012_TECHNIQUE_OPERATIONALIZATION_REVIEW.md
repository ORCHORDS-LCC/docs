# File/Path Exclusions Technique Operationalization Review

## Reference

- Technique: **T1564.012 — File/Path Exclusions**

Adversaries may attempt to hide their file-based artifacts by writing them to specific folders or file names excluded from antivirus (AV) scanning and other defensive capabilities. AV and other file-based scanners often include exclusions to optimize performance as well as ease installation and legitimate use of applications. These exclusions may be contextual (e.g., scans are only initiated in response to specific triggering events/alerts), but are also often hardcoded strings referencing specific folders and/or files assumed to be trusted and legitimate. Adversaries may abuse these exclusions to hide their file-based artifacts. For example, rather than tampering with tool settings to add a new exclusion (i.e., Disable or Modify Tools), adversaries may drop their file-based payloads in default or otherwise well-known exclusions. Adversaries may also use Security Software Discovery and other Discovery/Reconnaissance activities to both discover and verify existing exclusions in a victim environment.

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
- T1564.012: https://attack.mitre.org/techniques/T1564/012
- Reviewed: 2026-10-27
