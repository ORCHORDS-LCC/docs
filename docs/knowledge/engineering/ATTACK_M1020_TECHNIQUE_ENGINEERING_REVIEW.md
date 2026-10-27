# SSL/TLS Inspection Technique Engineering Review

## Reference

- Technique: **M1020 — SSL/TLS Inspection**

SSL/TLS inspection involves decrypting encrypted network traffic to examine its content for signs of malicious activity. This capability is crucial for detecting threats that use encryption to evade detection, such as phishing, malware, or data exfiltration. After inspection, the traffic is re-encrypted and forwarded to its destination. This mitigation can be implemented through the following measures: Deploy SSL/TLS Inspection Appliances: - Implement SSL/TLS inspection solutions to decrypt and inspect encrypted traffic. - Ensure appliances are placed at critical network choke points for maximum coverage. Configure Decryption Policies: - Define rules to decrypt traffic for specific applications, ports, or domains. - Avoid decrypting sensitive or privacy-related traffic, such as financial or healthcare websites, to comply with regulations. Integrate Threat Intelligence: - Use threat intelligence feeds to correlate inspected traffic with known indicators of compromise (IOCs). Integrate with Security Tools: - Combine SSL/TLS inspection with SIEM and NDR tools to analyze decrypted traffic and generate alerts for suspicious activity. - Example Tools: Splunk, Darktrace Implement Certificate Management: - Use trusted internal or third-party certificates for traffic re-encryption after inspection. - Regularly update certificate authorities (CAs) to ensure secure re-encryption. Monitor and Tune: - Continuously monitor SSL/TLS inspection logs for anomalies and fine-tune policies to reduce false positives.

## Engineering review

1. Identify the engineering boundary where the technique would apply: the component, the service, or the deployment.
2. Review the design decision that would prevent the technique, and record the alternative considered.
3. Review the implementation evidence for the preventive control.
4. Review the test coverage that would fail if the control regressed.
5. Review the observability: which signal would show the control is not operating.
6. Record the residual risk where prevention is not achievable, and the detection that compensates.

## Review evidence

- the design record for the preventive decision;
- the implementation or configuration evidence;
- the test record showing the control is exercised;
- the observability mapping.

## Limitations

An engineering review describes what the design and the implementation evidence show. It does not claim the technique has been addressed in production.

## Source

- MITRE ATT&CK: https://attack.mitre.org/
- M1020: https://attack.mitre.org/mitigations/M1020
- Reviewed: 2026-10-27
