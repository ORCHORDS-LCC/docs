# Certificate Registration Technique Engineering Review

## Reference

- Technique: **DC0093 — Certificate Registration**

Certificate Registration refers to the collection and analysis of information about digital certificates, including current, revoked, and expired certificates. Sources such as Certificate Transparency logs and other public resources provide visibility into certificates issued for specific domains or organizations. Monitoring certificate registrations can help identify potential misuse, such as unauthorized certificates or signs of adversary reconnaissance. Examples: - Certificate Transparency Logs: These logs record the issuance of SSL/TLS certificates by trusted Certificate Authorities (CAs). - Revoked Certificates: Information about certificates that have been invalidated before their expiration date. - Expired Certificates: Reports of expired certificates for a domain, which may indicate lax security practices or opportunities for adversaries to exploit expired credentials. - Domain Monitoring for Certificates: Maps SSL/TLS certificates to domains and subdomains, helping to identify any rogue certificates. - Public Certificate Directories: Services providing APIs to query issued certificates for analysis. This data component can be collected through the following measures: Use Certificate Transparency Monitors - Tools like crt.sh, CertStream, or APIs provided by certificate authorities (CAs) allow you to monitor issued certificates in real-time. - Example: Use CertStream to stream certificate issuance logs and filter for domains of interest. Analyze Certificate Revocation Sources - Monitor CRLs or query OCSP responders to detect revoked certificates. - Configure tools like OpenSSL or browsers to validate certificate revocation status automatically. Leverage Public Scanning Tools - Use tools such as SSL Labs, Censys, or Shodan to scan for certificate details related to your domain or network. Automate Certificate Monitoring - Set up automated scripts or services to parse Certificate Transparency logs for anomalies. - Example: Automate searches on crt.sh to identify certificates issued for typo-squatted domains. Integrate with Threat Intelligence - Enrich certificate data with threat intelligence feeds to detect connections to known adversary-controlled infrastructure. - Tools like VirusTotal can identify malicious certificates based on associated indicators.

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
- DC0093: https://attack.mitre.org/datacomponents/DC0093
- Reviewed: 2026-10-27
