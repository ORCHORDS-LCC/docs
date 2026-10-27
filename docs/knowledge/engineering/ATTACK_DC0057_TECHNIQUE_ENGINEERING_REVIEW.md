# Snapshot Creation Technique Engineering Review

## Reference

- Technique: **DC0057 — Snapshot Creation**

The process of taking a point-in-time copy of a cloud storage volume (files, settings, configurations, etc.), virtual machine (VM), or database that can be created and deployed in cloud environments.

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
- DC0057: https://attack.mitre.org/datacomponents/DC0057
- Reviewed: 2026-10-27
