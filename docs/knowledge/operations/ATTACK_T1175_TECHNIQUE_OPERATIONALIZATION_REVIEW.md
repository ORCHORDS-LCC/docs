# Distributed Component Object Model Mitigation Technique Operationalization Review

## Reference

- Technique: **T1175 — Distributed Component Object Model Mitigation**

Modify Registry settings (directly or using Dcomcnfg.exe) in <code>HKEY_LOCAL_MACHINE\SOFTWARE\Classes\AppID\{AppID_GUID}</code> associated with the process-wide security of individual COM applications. Modify Registry settings (directly or using Dcomcnfg.exe) in <code>HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Ole</code> associated with system-wide security defaults for all COM applications that do no set their own process-wide security. Consider disabling DCOM through Dcomcnfg.exe. Enable Windows firewall, which prevents DCOM instantiation by default. Ensure all COM alerts and Protected View are enabled.

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
- T1175: https://attack.mitre.org/mitigations/T1175
- Reviewed: 2026-10-27
