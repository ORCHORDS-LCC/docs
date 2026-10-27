# Exfiltration to Text Storage Sites Technique Operationalization Review

## Reference

- Technique: **T1567.003 — Exfiltration to Text Storage Sites**

Adversaries may exfiltrate data to text storage sites instead of their primary command and control channel. Text storage sites, such as <code>pastebin[.]com</code>, are commonly used by developers to share code and other information. Text storage sites are often used to host malicious code for C2 communication (e.g., Stage Capabilities), but adversaries may also use these sites to exfiltrate collected data. Furthermore, paid features and encryption options may allow adversaries to conceal and store data more securely. **Note:** This is distinct from Exfiltration to Code Repository, which highlight access to code repositories via APIs.

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
- T1567.003: https://attack.mitre.org/techniques/T1567/003
- Reviewed: 2026-10-27
