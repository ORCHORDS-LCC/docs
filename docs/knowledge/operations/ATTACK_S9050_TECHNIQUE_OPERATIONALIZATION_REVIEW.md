# Vidar Technique Operationalization Review

## Reference

- Technique: **S9050 — Vidar**

Vidar is a Windows infostealer that was first advertised in November 2018. Written in C++, Vidar collects PII, cryptocurrency wallets, documents and other data within the compromised machine. Version 2 of Vidar was published in October 2025, and has been used in numerous operations since its release. Vidar has been observed alongside other malware strains, including STOP/Djvu ransomware, Mina.exe (an XMRIG miner), and Clip1.exe (a Laplas Clipper sample).

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
- S9050: https://attack.mitre.org/software/S9050
- Reviewed: 2026-10-27
