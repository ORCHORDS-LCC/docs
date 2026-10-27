# Group Policy Preferences Technique Operationalization Review

## Reference

- Technique: **T1552.006 — Group Policy Preferences**

Adversaries may attempt to find unsecured credentials in Group Policy Preferences (GPP). GPP are tools that allow administrators to create domain policies with embedded credentials. These policies allow administrators to set local accounts. These group policies are stored in SYSVOL on a domain controller. This means that any domain user can view the SYSVOL share and decrypt the password (using the AES key that has been made public). The following tools and scripts can be used to gather and decrypt the password file from Group Policy Preference XML files: * Metasploit’s post exploitation module: post/windows/gather/credentials/gpp * Get-GPPPassword * gpprefdecrypt.py On the SYSVOL share, adversaries may use the following command to enumerate potential GPP XML files: dir /s * .xml.

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
- T1552.006: https://attack.mitre.org/techniques/T1552/006
- Reviewed: 2026-10-27
