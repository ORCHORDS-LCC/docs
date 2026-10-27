# Analytic 2010 Technique Platform Profile

## Reference

- Technique: **AN2010 — Analytic 2010**
- Platforms named in the source: PRE

Monitor for suspicious email activity, such as numerous accounts receiving messages from a single unusual/unknown sender. Filtering based on DKIM+SPF or header analysis can help detect when the email sender is spoofed. Monitor for references to uncategorized or known-bad sites. URL inspection within email (including expanding shortened links and identifying obfuscated URLs) can also help detect links leading to known malicious sites. Furthermore, monitor browser logs for homographs in ASCII and in internationalized domain names abusing different character sets (e.g. Cyrillic vs Latin versions of trusted sites). Monitor network data for uncommon data flows. Processes utilizing the network that do not normally have network communication or have never been seen before are suspicious. Monitor and analyze traffic patterns and packet inspection associated to protocol(s), leveraging SSL/TLS inspection for encrypted traffic, that do not follow the expected protocol standards and traffic flows (e.g extraneous packets that do not belong to established flows, gratuitous or anomalous traffic patterns, anomalous syntax, or structure). Consider correlation with process monitoring and command line to detect anomalous processes execution and command line arguments associated to traffic patterns (e.g. monitor anomalies in use of files that do not normally initiate connections for respective protocol(s)). Furthermore, monitor network traffic for homographs via the use of internationalized domain names abusing different character sets (e.g. Cyrillic vs Latin versions of trusted sites). Also monitor and analyze traffic patterns and packet inspection for indicators of cloned websites. For example, if adversaries use HTTrack to clone websites, Mirrored from (victim URL) may be visible in the HTML section of packets.

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
- AN2010: https://attack.mitre.org/detectionstrategies/DET0878#AN2010
- Reviewed: 2026-10-27
