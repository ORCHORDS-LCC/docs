# Component Object Model Hijacking Technique Engineering Review

## Reference

- Technique: **T1546.015 — Component Object Model Hijacking**

Adversaries may establish persistence by executing malicious content triggered by hijacked references to Component Object Model (COM) objects. COM is a system within Windows to enable interaction between software components through the operating system. References to various COM objects are stored in the Registry. Adversaries may use the COM system to insert malicious code that can be executed in place of legitimate software through hijacking the COM references and relationships as a means for persistence. Hijacking a COM object requires a change in the Registry to replace a reference to a legitimate system component which may cause that component to not work when executed. When that system component is executed through normal system operation the adversary's code will be executed instead. An adversary is likely to hijack objects that are used frequently enough to maintain a consistent level of persistence, but are unlikely to break noticeable functionality within the system as to avoid system instability that could lead to detection. One variation of COM hijacking involves abusing Type Libraries (TypeLibs), which provide metadata about COM objects, such as their interfaces and methods. Adversaries may modify Registry keys associated with TypeLibs to redirect legitimate COM object functionality to malicious scripts or payloads. Unlike traditional COM hijacking, which commonly uses local DLLs, this variation may leverage the "script:" moniker to execute remote scripts hosted on external servers. This approach enables stealthy execution of code while maintaining persistence, as the remote payload would be automatically downloaded whenever the hijacked COM object is accessed.

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
- T1546.015: https://attack.mitre.org/techniques/T1546/015
- Reviewed: 2026-10-27
