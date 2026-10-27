# AN2010 Analytic 2010 Outcome Lesson

## Authoritative description

- Technique: **AN2010 — Analytic 2010**
- Platforms: PRE

Monitor for suspicious email activity, such as numerous accounts receiving messages from a single unusual/unknown sender. Filtering based on DKIM+SPF or header analysis can help detect when the email sender is spoofed. Monitor for references to uncategorized or known-bad sites. URL inspection within email (including expanding shortened links and identifying obfuscated URLs) can also help detect links leading to known malicious sites. Furthermore, monitor browser logs for homographs in ASCII and in internationalized domain names abusing different character sets (e.g. Cyrillic vs Latin versions of trusted sites). Monitor network data for uncommon data flows. Processes utilizing the network that do not normally have network communication or have never been seen before are suspicious. Monitor and analyze traffic patterns and packet inspection associated to protocol(s), leveraging SSL/TLS inspection for encrypted traffic, that do not follow the expected protocol standards and traffic flows (e.g extraneous packets that do not belong to established flows, gratuitous or anomalous traffic patterns, anomalous syntax, or structure). Consider correlation with process monitoring and command line to detect anomalous processes execution and command line arguments associated to traffic patterns (e.g. monitor anomalies in use of files that do not normally initiate connections for respective protocol(s)). Furthermore, monitor network traffic for homographs via the use of internationalized domain names abusing different character sets (e.g. Cyrillic vs Latin versions of trusted sites). Also monitor and analyze traffic patterns and packet inspection for indicators of cloned websites. For example, if adversaries use HTTrack to clone websites, <code> Mirrored from (victim URL)</code> may be visible in the HTML section of packets.

## Reusable lesson

This technique should be treated as an explicit review question when it is relevant to the system or organisation, rather than assumed to be covered by a generic control statement or by tooling that reports a related signal.

## Apply the lesson

1. Define the real scope before judging coverage.
2. Inspect current technical, process, governance, or operational evidence.
3. Separate documented intent from verified behaviour.
4. Record partial coverage and unresolved gaps instead of converting them into a pass.
5. Revisit when the underlying scope, threat environment, technology, suppliers, or mission materially changes.

## Source

- MITRE ATT&CK: https://attack.mitre.org/
- AN2010: https://attack.mitre.org/detectionstrategies/DET0878#AN2010
- Reviewed: 2026-10-27

## Boundary

This lesson is derived from the published technique description. It does not invent an incident, prescribe one implementation, or claim the technique has been addressed.
