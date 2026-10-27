# Mini Shai-Hulud Technique Engineering Review

## Reference

- Technique: **S9043 — Mini Shai-Hulud**

Mini Shai-Hulud is a credential stealer and self-replicating supply chain worm, derived from Shai-Hulud, that has been used by TeamPCP to target Continuous Integration and Continuous Delivery/Deployment (CI/CD) workflows since at least 2026. Mini Shai-Hulud can compromise credentials across multiple cloud, container, and AI configuration file paths and can use stolen npm and GitHub OIDC tokens to spread to other packages maintained by the compromised user. Mini Shai-Hulud also has a targeted wiper component and has used multiple C2 and data exfiltration mechanisms.

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
- S9043: https://attack.mitre.org/software/S9043
- Reviewed: 2026-10-27
