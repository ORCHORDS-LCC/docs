# Analytic 1983 Technique Platform Profile

## Reference

- Technique: **AN1983 — Analytic 1983**
- Platforms named in the source: PRE

Monitor and analyze traffic patterns and packet inspection associated to protocol(s) that do not follow the expected protocol standards and traffic flows (e.g extraneous packets that do not belong to established flows, gratuitous or anomalous traffic patterns, anomalous syntax, or structure). Consider correlation with process monitoring and command line to detect anomalous processes execution and command line arguments associated to traffic patterns (e.g. monitor anomalies in use of files that do not normally initiate connections for respective protocol(s)). Consider monitoring social media activity related to your organization. Suspicious activity may include personas claiming to work for your organization or recently created/modified accounts making numerous connection requests to accounts affiliated with your organization. Detection efforts may be focused on related stages of the adversary lifecycle, such as during Initial Access (ex: Spearphishing via Service).

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
- AN1983: https://attack.mitre.org/detectionstrategies/DET0851#AN1983
- Reviewed: 2026-10-27
