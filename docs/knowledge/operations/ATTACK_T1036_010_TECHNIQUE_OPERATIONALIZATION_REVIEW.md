# Masquerade Account Name Technique Operationalization Review

## Reference

- Technique: **T1036.010 — Masquerade Account Name**

Adversaries may match or approximate the names of legitimate accounts to make newly created ones appear benign. This will typically occur during Create Account, although accounts may also be renamed at a later date. This may also coincide with Account Access Removal if the actor first deletes an account before re-creating one with the same name. Often, adversaries will attempt to masquerade as service accounts, such as those associated with legitimate software, data backups, or container cluster management. They may also give accounts generic, trustworthy names, such as “admin”, “help”, or “root.” Sometimes adversaries may model account names off of those already existing in the system, as a follow-on behavior to Account Discovery. Note that this is distinct from Impersonation, which describes impersonating specific trusted individuals or organizations, rather than user or service account names.

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
- T1036.010: https://attack.mitre.org/techniques/T1036/010
- Reviewed: 2026-10-27
