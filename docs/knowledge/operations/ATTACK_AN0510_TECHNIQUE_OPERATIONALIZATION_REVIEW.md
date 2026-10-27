# Analytic 0510 Technique Operationalization Review

## Reference

- Technique: **AN0510 — Analytic 0510**

Detection correlates file creation or modification of `.lnk` (shortcut) files in autostart locations with anomalous parent-child process lineage or unsigned binaries. Defenders should watch for LNK creation/modification events outside of known software installations, patch events, or OS updates. Flag shortcut targets pointing to suspicious locations or unknown binaries, particularly those written by script interpreters or spawned from phishing delivery chains.

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
- AN0510: https://attack.mitre.org/detectionstrategies/DET0180#AN0510
- Reviewed: 2026-10-27
