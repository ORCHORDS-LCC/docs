# Raspberry Robin Technique Operationalization Review

## Reference

- Technique: **S1130 — Raspberry Robin**

Raspberry Robin is initial access malware first identified in September 2021, and active through early 2024. The malware is notable for spreading via infected USB devices containing a malicious LNK object that, on execution, retrieves remote hosted payloads for installation. Raspberry Robin has been widely used against various industries and geographies, and as a precursor to information stealer, ransomware, and other payloads such as SocGholish, Cobalt Strike, IcedID, and Bumblebee. The DLL componenet in the Raspberry Robin infection chain is also referred to as "Roshtyak." The name "Raspberry Robin" is used to refer to both the malware as well as the threat actor associated with its use, although the Raspberry Robin operators are also tracked as <code>Storm-0856</code> by some vendors.

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
- S1130: https://attack.mitre.org/software/S1130
- Reviewed: 2026-10-27
