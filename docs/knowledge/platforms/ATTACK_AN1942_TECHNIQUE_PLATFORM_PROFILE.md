# Analytic 1942 Technique Platform Profile

## Reference

- Technique: **AN1942 — Analytic 1942**
- Platforms named in the source: PRE

Monitor for suspicious network traffic that could be indicative of adversary reconnaissance, such as rapid successions of requests indicative of web crawling and/or large quantities of requests originating from a single source (especially if the source is known to be associated with an adversary). Analyzing web metadata may also reveal artifacts that can be attributed to potentially malicious activity, such as referer or user-agent string HTTP/S fields.

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
- AN1942: https://attack.mitre.org/detectionstrategies/DET0810#AN1942
- Reviewed: 2026-10-27
