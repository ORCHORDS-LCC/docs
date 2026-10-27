# Analytic 0065 Technique Operationalization Review

## Reference

- Technique: **AN0065 — Analytic 0065**

Adversary stages a lure that references a remote resource (e.g., LNK/SCF/Office template). When the user opens/renders the file or a shell enumerates icons, the host automatically attempts SMB or WebDAV authentication to the attacker host. The chain is: (1) lure file is created or modified in a user-exposed location → (2) user or system accesses the lure → (3) host makes outbound NTLM (SMB 139/445 or WebDAV over 80/443) to an untrusted destination → (4) repeated attempts from multiple users/hosts or from privileged workstations.

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
- AN0065: https://attack.mitre.org/detectionstrategies/DET0022#AN0065
- Reviewed: 2026-10-27
