# Bandwidth Hijacking Technique Engineering Review

## Reference

- Technique: **T1496.002 — Bandwidth Hijacking**

Adversaries may leverage the network bandwidth resources of co-opted systems to complete resource-intensive tasks, which may impact system and/or hosted service availability. Adversaries may also use malware that leverages a system's network bandwidth as part of a botnet in order to facilitate Network Denial of Service campaigns and/or to seed malicious torrents. Alternatively, they may engage in proxyjacking by selling use of the victims' network bandwidth and IP address to proxyware services. Finally, they may engage in internet-wide scanning in order to identify additional targets for compromise. In addition to incurring potential financial costs or availability disruptions, this technique may cause reputational damage if a victim’s bandwidth is used for illegal activities.

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
- T1496.002: https://attack.mitre.org/techniques/T1496/002
- Reviewed: 2026-10-27
