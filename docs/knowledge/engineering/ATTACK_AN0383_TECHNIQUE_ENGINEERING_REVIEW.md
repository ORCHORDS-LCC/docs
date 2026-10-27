# Analytic 0383 Technique Engineering Review

## Reference

- Technique: **AN0383 — Analytic 0383**

Detection of unauthorized modification of Active Directory SID-History attributes to escalate privileges. This chain involves: (1) privileged operations or API calls to DsAddSidHistory or related AD modification functions, (2) observed attribute changes in SID-History (Event ID 5136), (3) new logon sessions where the token includes unexpected or privileged SID-History values, and (4) follow-on resource access using elevated privileges derived from SID-History injection.

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
- AN0383: https://attack.mitre.org/detectionstrategies/DET0136#AN0383
- Reviewed: 2026-10-27
