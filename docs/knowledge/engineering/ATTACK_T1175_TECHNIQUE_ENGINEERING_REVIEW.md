# Distributed Component Object Model Mitigation Technique Engineering Review

## Reference

- Technique: **T1175 — Distributed Component Object Model Mitigation**

Modify Registry settings (directly or using Dcomcnfg.exe) in HKEY_LOCAL_MACHINE\SOFTWARE\Classes\AppID\{AppID_GUID} associated with the process-wide security of individual COM applications. Modify Registry settings (directly or using Dcomcnfg.exe) in HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Ole associated with system-wide security defaults for all COM applications that do no set their own process-wide security. Consider disabling DCOM through Dcomcnfg.exe. Enable Windows firewall, which prevents DCOM instantiation by default. Ensure all COM alerts and Protected View are enabled.

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
- T1175: https://attack.mitre.org/mitigations/T1175
- Reviewed: 2026-10-27
