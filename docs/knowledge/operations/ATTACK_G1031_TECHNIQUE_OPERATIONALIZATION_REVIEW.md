# Saint Bear Technique Operationalization Review

## Reference

- Technique: **G1031 — Saint Bear**

Saint Bear is a Russian-nexus threat actor active since early 2021, primarily targeting entities in Ukraine and Georgia. The group is notable for a specific remote access tool, Saint Bot, and information stealer, OutSteel in campaigns. Saint Bear typically relies on phishing or web staging of malicious documents and related file types for initial access, spoofing government or related entities. Saint Bear has previously been confused with Ember Bear operations, but analysis of behaviors, tools, and targeting indicates these are distinct clusters.

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
- G1031: https://attack.mitre.org/groups/G1031
- Reviewed: 2026-10-27
