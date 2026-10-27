# IOControl Technique Engineering Review

## Reference

- Technique: **S9046 — IOControl**

IOControl is a malware that targeted Linux ARM-based IoT/OT devices including Hikvision IP cameras, D-Link firewalls and routers, Unitronics PLCs and HMIs, Orpak and Gasboy fuel management systems, and Baicells LTE controllers across the United States and Israel. The malware has been attributed to CyberAv3ngers which is suspected to be affiliated with the Iranian Government Islamic Revolutionary Guard Corps (IRGC).

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
- S9046: https://attack.mitre.org/software/S9046
- Reviewed: 2026-10-27
