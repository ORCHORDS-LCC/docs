# Odbcconf Technique Operationalization Review

## Reference

- Technique: **T1218.008 — Odbcconf**

Adversaries may abuse odbcconf.exe to proxy execution of malicious payloads. Odbcconf.exe is a Windows utility that allows you to configure Open Database Connectivity (ODBC) drivers and data source names. The Odbcconf.exe binary may be digitally signed by Microsoft. Adversaries may abuse odbcconf.exe to bypass application control solutions that do not account for its potential abuse. Similar to Regsvr32, odbcconf.exe has a REGSVR flag that can be misused to execute DLLs (ex: odbcconf.exe /S /A &lbrace;REGSVR "(a user home directory)file.dll"&rbrace;).

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
- T1218.008: https://attack.mitre.org/techniques/T1218/008
- Reviewed: 2026-10-27
