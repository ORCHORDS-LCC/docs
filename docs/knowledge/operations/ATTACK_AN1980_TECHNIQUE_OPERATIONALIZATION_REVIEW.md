# Analytic 1980 Technique Operationalization Review

## Reference

- Technique: **AN1980 — Analytic 1980**

Consider use of services that may aid in the tracking of newly issued certificates and/or certificates in use on sites across the Internet. In some cases it may be possible to pivot on known pieces of certificate information to uncover other adversary infrastructure. Some server-side components of adversary tools may have default values set for SSL/TLS certificates. Monitor for logged network traffic in response to a scan showing both protocol header and body values that may buy and/or steal SSL/TLS certificates that can be used during targeting. Detection efforts may be focused on related behaviors, such as Web Protocols, Asymmetric Cryptography, and/or Install Root Certificate.

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
- AN1980: https://attack.mitre.org/detectionstrategies/DET0848#AN1980
- Reviewed: 2026-10-27
