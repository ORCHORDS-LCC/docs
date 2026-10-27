# Analytic 1307 Technique Operationalization Review

## Reference

- Technique: **AN1307 — Analytic 1307**

MacOS environmental keying behavioral chain: (1) System information discovery through native utilities (system_profiler, sw_vers, hostname, dscl) and Security framework queries, (2) Hardware and software enumeration including serial numbers, installed applications, and system versions, (3) Network configuration assessment (networksetup, scutil) and wireless network discovery, (4) Keychain and security context validation, (5) Unified Logs correlation with cryptographic framework usage (CommonCrypto, Security.framework), (6) Application bundle execution following environmental validation.

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
- AN1307: https://attack.mitre.org/detectionstrategies/DET0474#AN1307
- Reviewed: 2026-10-27
