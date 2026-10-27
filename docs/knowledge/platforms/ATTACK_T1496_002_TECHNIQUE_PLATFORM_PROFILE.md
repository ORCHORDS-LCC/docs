# Bandwidth Hijacking Technique Platform Profile

## Reference

- Technique: **T1496.002 — Bandwidth Hijacking**
- Platforms named in the source: Linux, Windows, macOS, IaaS, Containers

Adversaries may leverage the network bandwidth resources of co-opted systems to complete resource-intensive tasks, which may impact system and/or hosted service availability. Adversaries may also use malware that leverages a system's network bandwidth as part of a botnet in order to facilitate Network Denial of Service campaigns and/or to seed malicious torrents. Alternatively, they may engage in proxyjacking by selling use of the victims' network bandwidth and IP address to proxyware services. Finally, they may engage in internet-wide scanning in order to identify additional targets for compromise. In addition to incurring potential financial costs or availability disruptions, this technique may cause reputational damage if a victim’s bandwidth is used for illegal activities.

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
- T1496.002: https://attack.mitre.org/techniques/T1496/002
- Reviewed: 2026-10-27
