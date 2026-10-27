# /etc/passwd and /etc/shadow Technique Operationalization Review

## Reference

- Technique: **T1003.008 — /etc/passwd and /etc/shadow**

Adversaries may attempt to dump the contents of /etc/passwd and /etc/shadow to enable offline password cracking. Most modern Linux operating systems use a combination of /etc/passwd and /etc/shadow to store user account information, including password hashes in /etc/shadow. By default, /etc/shadow is only readable by the root user. Linux stores user information such as user ID, group ID, home directory path, and login shell in /etc/passwd. A "user" on the system may belong to a person or a service. All password hashes are stored in /etc/shadow - including entries for users with no passwords and users with locked or disabled accounts. Adversaries may attempt to read or dump the /etc/passwd and /etc/shadow files on Linux systems via command line utilities such as the cat command. Additionally, the Linux utility unshadow can be used to combine the two files in a format suited for password cracking utilities such as John the Ripper - for example, via the command /usr/bin/unshadow /etc/passwd /etc/shadow > /tmp/crack.password.db. Since the user information stored in /etc/passwd are linked to the password hashes in /etc/shadow, an adversary would need to have access to both.

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
- T1003.008: https://attack.mitre.org/techniques/T1003/008
- Reviewed: 2026-10-27
