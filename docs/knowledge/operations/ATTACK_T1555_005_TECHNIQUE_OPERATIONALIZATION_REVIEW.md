# Password Managers Technique Operationalization Review

## Reference

- Technique: **T1555.005 — Password Managers**

Adversaries may acquire user credentials from third-party password managers. Password managers are applications designed to store user credentials, normally in an encrypted database. Credentials are typically accessible after a user provides a master password that unlocks the database. After the database is unlocked, these credentials may be copied to memory. These databases can be stored as files on disk. Adversaries may acquire user credentials from password managers by extracting the master password and/or plain-text credentials from memory. Adversaries may extract credentials from memory via Exploitation for Credential Access. Adversaries may also try brute forcing via Password Guessing to obtain the master password of a password manager.

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
- T1555.005: https://attack.mitre.org/techniques/T1555/005
- Reviewed: 2026-10-27
