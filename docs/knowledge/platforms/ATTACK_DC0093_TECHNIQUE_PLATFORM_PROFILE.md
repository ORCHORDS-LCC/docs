# Certificate Registration Technique Platform Profile

## Reference

- Technique: **DC0093 — Certificate Registration**
- Platforms named in the source: not stated

Certificate Registration refers to the collection and analysis of information about digital certificates, including current, revoked, and expired certificates. Sources such as Certificate Transparency logs and other public resources provide visibility into certificates issued for specific domains or organizations. Monitoring certificate registrations can help identify potential misuse, such as unauthorized certificates or signs of adversary reconnaissance. Examples: - Certificate Transparency Logs: These logs record the issuance of SSL/TLS certificates by trusted Certificate Authorities (CAs). - Revoked Certificates: Information about certificates that have been invalidated before their expiration date. - Expired Certificates: Reports of expired certificates for a domain, which may indicate lax security practices or opportunities for adversaries to exploit expired credentials. - Domain Monitoring for Certificates: Maps SSL/TLS certificates to domains and subdomains, helping to identify any rogue certificates. - Public Certificate Directories: Services providing APIs to query issued certificates for analysis. This data component can be collected through the following measures: Use Certificate Transparency Monitors - Tools like crt.sh, CertStream, or APIs provided by certificate authorities (CAs) allow you to monitor issued certificates in real-time. - Example: Use CertStream to stream certificate issuance logs and filter for domains of interest. Analyze Certificate Revocation Sources - Monitor CRLs or query OCSP responders to detect revoked certificates. - Configure tools like OpenSSL or browsers to validate certificate revocation status automatically. Leverage Public Scanning Tools - Use tools such as SSL Labs, Censys, or Shodan to scan for certificate details related to your domain or network. Automate Certificate Monitoring - Set up automated scripts or services to parse Certificate Transparency logs for anomalies. - Example: Automate searches on crt.sh to identify certificates issued for typo-squatted domains. Integrate with Threat Intelligence - Enrich certificate data with threat intelligence feeds to detect connections to known adversary-controlled infrastructure. - Tools like VirusTotal can identify malicious certificates based on associated indicators.

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
- DC0093: https://attack.mitre.org/datacomponents/DC0093
- Reviewed: 2026-10-27
