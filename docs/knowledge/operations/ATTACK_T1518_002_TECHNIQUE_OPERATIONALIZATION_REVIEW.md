# Backup Software Discovery Technique Operationalization Review

## Reference

- Technique: **T1518.002 — Backup Software Discovery**

Adversaries may attempt to get a listing of backup software or configurations that are installed on a system. Adversaries may use this information to shape follow-on behaviors, such as Data Destruction, Inhibit System Recovery, or Data Encrypted for Impact. Commands that can be used to obtain security software information are netsh, `reg query` with Reg, `dir` with cmd, and Tasklist, but other indicators of discovery behavior may be more specific to the type of software or security system the adversary is looking for, such as Veeam, Acronis, Dropbox, or Paragon.

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
- T1518.002: https://attack.mitre.org/techniques/T1518/002
- Reviewed: 2026-10-27
