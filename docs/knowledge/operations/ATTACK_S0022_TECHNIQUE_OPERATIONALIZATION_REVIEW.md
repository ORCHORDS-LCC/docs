# Uroburos Technique Operationalization Review

## Reference

- Technique: **S0022 — Uroburos**

Uroburos is a sophisticated cyber espionage tool written in C that has been used by units within Russia's Federal Security Service (FSB) associated with the Turla toolset to collect intelligence on sensitive targets worldwide. Uroburos has several variants and has undergone nearly constant upgrade since its initial development in 2003 to keep it viable after public disclosures. Uroburos is typically deployed to external-facing nodes on a targeted network and has the ability to leverage additional tools and TTPs to further exploit an internal network. Uroburos has interoperable implants for Windows, Linux, and macOS, employs a high level of stealth in communications and architecture, and can easily incorporate new or replacement components.

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
- S0022: https://attack.mitre.org/software/S0022
- Reviewed: 2026-10-27
