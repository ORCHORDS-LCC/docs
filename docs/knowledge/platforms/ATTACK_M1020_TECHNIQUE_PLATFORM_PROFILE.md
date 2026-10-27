# SSL/TLS Inspection Technique Platform Profile

## Reference

- Technique: **M1020 — SSL/TLS Inspection**
- Platforms named in the source: not stated

SSL/TLS inspection involves decrypting encrypted network traffic to examine its content for signs of malicious activity. This capability is crucial for detecting threats that use encryption to evade detection, such as phishing, malware, or data exfiltration. After inspection, the traffic is re-encrypted and forwarded to its destination. This mitigation can be implemented through the following measures: Deploy SSL/TLS Inspection Appliances: - Implement SSL/TLS inspection solutions to decrypt and inspect encrypted traffic. - Ensure appliances are placed at critical network choke points for maximum coverage. Configure Decryption Policies: - Define rules to decrypt traffic for specific applications, ports, or domains. - Avoid decrypting sensitive or privacy-related traffic, such as financial or healthcare websites, to comply with regulations. Integrate Threat Intelligence: - Use threat intelligence feeds to correlate inspected traffic with known indicators of compromise (IOCs). Integrate with Security Tools: - Combine SSL/TLS inspection with SIEM and NDR tools to analyze decrypted traffic and generate alerts for suspicious activity. - Example Tools: Splunk, Darktrace Implement Certificate Management: - Use trusted internal or third-party certificates for traffic re-encryption after inspection. - Regularly update certificate authorities (CAs) to ensure secure re-encryption. Monitor and Tune: - Continuously monitor SSL/TLS inspection logs for anomalies and fine-tune policies to reduce false positives.

## Platform profile

1. Record the platforms in scope and the versions actually deployed.
2. Compare the deployed platform surface against the platforms the source names.
3. Record where the platform provides a native control for the technique, and where it does not.
4. Record the configuration evidence for the native control, where one exists.
5. Record the gap where the platform provides no native control, and the compensating detection.
6. Record the platform version, because platform behaviour changes between versions.

## Evidence

- the platform and version inventory for the scoped estate;
- the configuration export or screenshot for the native control;
- the detection evidence where the platform provides none.

## Limitations

A technique entry describes a class of abuse across platforms. The platform-specific exposure is a property of the deployment, established only by inventory and configuration evidence.

## Source

- MITRE ATT&CK: https://attack.mitre.org/
- M1020: https://attack.mitre.org/mitigations/M1020
- Reviewed: 2026-10-27
