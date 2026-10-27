# SystemBC Technique Operationalization Review

## Reference

- Technique: **S9001 — SystemBC**

SystemBC is a malware family offered as a malware-as-a-service (MaaS) that is used to establish command and control and facilitate follow-on activity, including ransomware deployment.SystemBC executes a variety of tasks including setting up SOCKS5 proxies, maintaining persistence, ingesting malicious files, and handing C2 communication. SystemBC was first detected in 2018, and has been used by Wizard Spider since at least 2020, and by FIN7 since at least 2022.

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
- S9001: https://attack.mitre.org/software/S9001
- Reviewed: 2026-10-27
