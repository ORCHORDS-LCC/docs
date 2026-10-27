# Domain Account Technique Operationalization Review

## Reference

- Technique: **T1087.002 — Domain Account**

Adversaries may attempt to get a listing of domain accounts. This information can help adversaries determine which domain accounts exist to aid in follow-on behavior such as targeting specific accounts which possess particular privileges. Commands such as net user /domain and net group /domain of the Net utility, dscacheutil -q group on macOS, and ldapsearch on Linux can list domain users and groups. PowerShell cmdlets including Get-ADUser and Get-ADGroupMember may enumerate members of Active Directory groups.

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
- T1087.002: https://attack.mitre.org/techniques/T1087/002
- Reviewed: 2026-10-27
