# Protocol or Service Impersonation Technique Operationalization Review

## Reference

- Technique: **T1001.003 — Protocol or Service Impersonation**

Adversaries may impersonate legitimate protocols or web service traffic to disguise command and control activity and thwart analysis efforts. By impersonating legitimate protocols or web services, adversaries can make their command and control traffic blend in with legitimate network traffic. Adversaries may impersonate a fake SSL/TLS handshake to make it look like subsequent traffic is SSL/TLS encrypted, potentially interfering with some security tooling, or to make the traffic look like it is related with a trusted entity. Adversaries may also leverage legitimate protocols to impersonate expected web traffic or trusted services. For example, adversaries may manipulate HTTP headers, URI endpoints, SSL certificates, and transmitted data to disguise C2 communications or mimic legitimate services such as Gmail, Google Drive, and Yahoo Messenger.

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
- T1001.003: https://attack.mitre.org/techniques/T1001/003
- Reviewed: 2026-10-27
