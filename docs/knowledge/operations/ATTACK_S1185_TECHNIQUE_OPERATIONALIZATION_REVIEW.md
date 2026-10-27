# LightSpy Technique Operationalization Review

## Reference

- Technique: **S1185 — LightSpy**

First observed in 2018, LightSpy is a modular malware family that initially targeted iOS devices in Southern Asia before expanding to Android and macOS platforms. It consists of a downloader, a main executable that manages network communications, and functionality-specific modules, typically implemented as `.dylib` files (iOS, macOS) or `.apk` files (Android). LightSpy can collect VoIP call recordings, SMS messages, and credential stores, which are then exfiltrated to a command and control (C2) server.

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
- S1185: https://attack.mitre.org/software/S1185
- Reviewed: 2026-10-27
