# Analytic 0647 Technique Engineering Review

## Reference

- Technique: **AN0647 — Analytic 0647**

Defenders may observe adversary attempts to collect or export full device configurations by detecting unusual SNMP queries, Smart Install (SMI) activity, or CLI/API commands that request running or startup configuration dumps. Correlated behaviors include high-volume read requests for sensitive OIDs, repeated use of 'show running-config' or equivalent commands from untrusted IPs, or unexpected TFTP/SCP/FTP transfers containing configuration files. These behaviors often appear in sequence: anomalous authentication or privilege escalation, followed by bulk configuration retrieval and outbound transfer.

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
- AN0647: https://attack.mitre.org/detectionstrategies/DET0233#AN0647
- Reviewed: 2026-10-27
