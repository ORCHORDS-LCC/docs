# Analytic 1433 Technique Operationalization Review

## Reference

- Technique: **AN1433 — Analytic 1433**

Detection focuses on unauthorized manipulation of .NET AppDomainManager behavior. Defenders may observe suspicious creation of new AppDomains within trusted processes, anomalous loading of assemblies via non-standard configuration files, or registry/environment variable changes redirecting AppDomainManager to malicious assemblies. Correlated events include config file tampering, new process creation of .NET host processes (e.g., w3wp.exe, powershell.exe) with modified runtime parameters, and module loads of unusual or unsigned .NET DLLs.

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
- AN1433: https://attack.mitre.org/detectionstrategies/DET0517#AN1433
- Reviewed: 2026-10-27
