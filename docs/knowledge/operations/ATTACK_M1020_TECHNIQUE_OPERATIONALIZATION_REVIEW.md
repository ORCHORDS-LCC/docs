# SSL/TLS Inspection Technique Operationalization Review

## Reference

- Technique: **M1020 — SSL/TLS Inspection**

SSL/TLS inspection involves decrypting encrypted network traffic to examine its content for signs of malicious activity. This capability is crucial for detecting threats that use encryption to evade detection, such as phishing, malware, or data exfiltration. After inspection, the traffic is re-encrypted and forwarded to its destination. This mitigation can be implemented through the following measures: Deploy SSL/TLS Inspection Appliances: - Implement SSL/TLS inspection solutions to decrypt and inspect encrypted traffic. - Ensure appliances are placed at critical network choke points for maximum coverage. Configure Decryption Policies: - Define rules to decrypt traffic for specific applications, ports, or domains. - Avoid decrypting sensitive or privacy-related traffic, such as financial or healthcare websites, to comply with regulations. Integrate Threat Intelligence: - Use threat intelligence feeds to correlate inspected traffic with known indicators of compromise (IOCs). Integrate with Security Tools: - Combine SSL/TLS inspection with SIEM and NDR tools to analyze decrypted traffic and generate alerts for suspicious activity. - Example Tools: Splunk, Darktrace Implement Certificate Management: - Use trusted internal or third-party certificates for traffic re-encryption after inspection. - Regularly update certificate authorities (CAs) to ensure secure re-encryption. Monitor and Tune: - Continuously monitor SSL/TLS inspection logs for anomalies and fine-tune policies to reduce false positives.

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
- M1020: https://attack.mitre.org/mitigations/M1020
- Reviewed: 2026-10-27
