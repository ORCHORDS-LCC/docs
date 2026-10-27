# NTDS Technique Operationalization Review

## Reference

- Technique: **T1003.003 — NTDS**

Adversaries may attempt to access or create a copy of the Active Directory domain database in order to steal credential information, as well as obtain other information about domain members such as devices, users, and access rights. By default, the NTDS file (NTDS.dit) is located in <code>%SystemRoot%\NTDS\Ntds.dit</code> of a domain controller. In addition to looking for NTDS files on active Domain Controllers, adversaries may search for backups that contain the same or similar information. The following tools and techniques can be used to enumerate the NTDS file and the contents of the entire Active Directory hashes. * Volume Shadow Copy * secretsdump.py * Using the in-built Windows tool, ntdsutil.exe * Invoke-NinjaCopy.

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
- T1003.003: https://attack.mitre.org/techniques/T1003/003
- Reviewed: 2026-10-27
