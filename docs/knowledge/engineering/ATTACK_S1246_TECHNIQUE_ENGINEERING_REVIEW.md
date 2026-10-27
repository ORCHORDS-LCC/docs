# BeaverTail Technique Engineering Review

## Reference

- Technique: **S1246 — BeaverTail**

BeaverTail is a malware that has both a JavaScript and C++ variant. Active since 2022, BeaverTail is capable of stealing logins from browsers and serves as a downloader for second stage payloads. BeaverTail has previously been leveraged by North Korea-affiliated actors identified as DeceptiveDevelopment or Contagious Interview. BeaverTail has been delivered to victims through code repository sites and has been embedded within malicious attachments.

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
- S1246: https://attack.mitre.org/software/S1246
- Reviewed: 2026-10-27
