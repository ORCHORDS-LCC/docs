# Analytic 0481 Technique Operationalization Review

## Reference

- Technique: **AN0481 — Analytic 0481**

Defenders should monitor for suspicious enumeration of cloud infrastructure components via APIs or CLI tools. Observable behaviors include repeated listing or description operations for compute instances, snapshots, storage buckets, and volumes. From a defender’s perspective, risky activity is often identified by new or untrusted identities making discovery calls (e.g., DescribeInstances, ListBuckets, az vm list, gcloud compute instances list), enumeration from unusual geolocations or IPs, or rapid multi-service discovery in sequence. Correlating discovery API usage with later snapshot creation or instance modification provides further context of adversary behavior.

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
- AN0481: https://attack.mitre.org/detectionstrategies/DET0169#AN0481
- Reviewed: 2026-10-27
