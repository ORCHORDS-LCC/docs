# Certificate Registration Technique Response Playbook

## Target technique

**DC0093 — Certificate Registration**


Certificate Registration refers to the collection and analysis of information about digital certificates, including current, revoked, and expired certificates. Sources such as Certificate Transparency logs and other public resources provide visibility into certificates issued for specific domains or organizations. Monitoring certificate registrations can help identify potential misuse, such as unauthorized certificates or signs of adversary reconnaissance. Examples: - Certificate Transparency Logs: These logs record the issuance of SSL/TLS certificates by trusted Certificate Authorities (CAs). - Revoked Certificates: Information about certificates that have been invalidated before their expiration date. - Expired Certificates: Reports of expired certificates for a domain, which may indicate lax security practices or opportunities for adversaries to exploit expired credentials. - Domain Monitoring for Certificates: Maps SSL/TLS certificates to domains and subdomains, helping to identify any rogue certificates. - Public Certificate Directories: Services providing APIs to query issued certificates for analysis. This data component can be collected through the following measures: Use Certificate Transparency Monitors - Tools like crt.sh, CertStream, or APIs provided by certificate authorities (CAs) allow you to monitor issued certificates in real-time. - Example: Use CertStream to stream certificate issuance logs and filter for domains of interest. Analyze Certificate Revocation Sources - Monitor CRLs or query OCSP responders to detect revoked certificates. - Configure tools like OpenSSL or browsers to validate certificate revocation status automatically. Leverage Public Scanning Tools - Use tools such as SSL Labs, Censys, or Shodan to scan for certificate details related to your domain or network. Automate Certificate Monitoring - Set up automated scripts or services to parse Certificate Transparency logs for anomalies. - Example: Automate searches on crt.sh to identify certificates issued for typo-squatted domains. Integrate with Threat Intelligence - Enrich certificate data with threat intelligence feeds to detect connections to known adversary-controlled infrastructure. - Tools like VirusTotal can identify malicious certificates based on associated indicators.

## Preconditions

- the estate in scope is identified, with the systems the technique could apply to;
- an owner is accountable for detection and response;
- current telemetry and configuration can be inspected;
- the technique is applicable or requires an applicability decision.

## Procedure

1. Confirm the scope and owner.
2. Read the current technique description and the associated detection guidance.
3. Inventory the telemetry that would carry the technique's indicators.
4. Inspect whether the indicators are present in the environment.
5. Exercise the detection path and confirm it produces the expected signal.
6. Record gaps in detection coverage and assign remediation owners.
7. Record justified non-applicability or accepted detection gaps separately.
8. Set the next event-driven or periodic verification trigger.

## Failure handling

If the detection path does not produce the expected signal, treat the coverage as unverified, preserve the test evidence, and route the gap through the appropriate remediation or risk process.

## Completion evidence

Scope, owner, source version, telemetry inspected, tests performed, findings, exceptions, remediation links, reviewer, and next trigger.

## Source

- MITRE ATT&CK: https://attack.mitre.org/
- DC0093: https://attack.mitre.org/datacomponents/DC0093
- Reviewed: 2026-10-27
