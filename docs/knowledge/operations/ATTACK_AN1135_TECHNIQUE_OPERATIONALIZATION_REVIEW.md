# Analytic 1135 Technique Operationalization Review

## Reference

- Technique: **AN1135 — Analytic 1135**

Abuse of extended attributes (xattrs) to embed hidden payloads into legitimate files. Defender perspective: detect anomalous use of setfattr or getfattr commands, or direct syscalls (setxattr, getxattr) where attributes are unusually large or contain encoded data. Behavior chain includes: (1) execution of setfattr with suspicious namespaces (user., trusted.), (2) file metadata modification inconsistent with file size/hash, and (3) subsequent process execution reading attributes followed by decoding activity.

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
- AN1135: https://attack.mitre.org/detectionstrategies/DET0406#AN1135
- Reviewed: 2026-10-27
