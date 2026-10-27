# Versa Director Zero Day Exploitation Technique Operationalization Review

## Reference

- Technique: **C0039 — Versa Director Zero Day Exploitation**

Versa Director Zero Day Exploitation was conducted by Volt Typhoon from early June through August 2024 as zero-day exploitation of Versa Director servers controlling software-defined wide area network (SD-WAN) applications. Since tracked as CVE-2024-39717, exploitation focused on credential capture from compromised Versa Director servers at managed service providers (MSPs) and internet service providers (ISPs) to enable follow-on access to service provider clients. Versa Director Zero Day Exploitation was followed by the delivery of the VersaMem web shell for both credential theft and follow-on code execution.

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
- C0039: https://attack.mitre.org/campaigns/C0039
- Reviewed: 2026-10-27
