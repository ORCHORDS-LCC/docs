# Analytic 1029 Technique Engineering Review

## Reference

- Technique: **AN1029 — Analytic 1029**

Detection of AppCert DLL abuse involves correlating registry modifications to the AppCertDLLs key with subsequent unexpected DLL load behavior during process creation events. Specifically, defenders can observe abnormal DLLs being loaded into standard Windows processes after changes to the 'AppCertDLLs' registry value. Monitoring CreateProcess-family API executions with injected DLLs and linking those DLLs back to recent registry edits is key to identifying misuse. This is often accompanied by elevated privileges and potential lateral movement or discovery behavior.

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
- AN1029: https://attack.mitre.org/detectionstrategies/DET0362#AN1029
- Reviewed: 2026-10-27
