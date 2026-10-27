# Analytic 2017 Technique Platform Profile

## Reference

- Technique: **AN2017 — Analytic 2017**
- Platforms named in the source: PRE

Once adversaries have provisioned compromised infrastructure (ex: a server for use in command and control), internet scans may help proactively discover compromised infrastructure. Consider looking for identifiable patterns such as services listening, certificates in use, SSL/TLS negotiation features, or other response artifacts associated with adversary C2 software. Consider monitoring for anomalous changes to domain registrant information and/or domain resolution information that may indicate the compromise of a domain. Efforts may need to be tailored to specific domains of interest as benign registration and resolution changes are a common occurrence on the internet. Monitor for queried domain name system (DNS) registry data that may compromise third-party infrastructure that can be used during targeting. Detection efforts may be focused on related stages of the adversary lifecycle, such as during Command and Control. Monitor for logged domain name system (DNS) data that may compromise third-party infrastructure that can be used during targeting. Detection efforts may be focused on related stages of the adversary lifecycle, such as during Command and Control. Monitor for contextual data about an Internet-facing resource gathered from a scan, such as running services or ports that may compromise third-party infrastructure that can be used during targeting. Detection efforts may be focused on related stages of the adversary lifecycle, such as during Command and Control.

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
- AN2017: https://attack.mitre.org/detectionstrategies/DET0885#AN2017
- Reviewed: 2026-10-27
