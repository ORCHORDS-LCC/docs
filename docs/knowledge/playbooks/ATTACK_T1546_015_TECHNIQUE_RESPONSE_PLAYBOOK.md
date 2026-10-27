# Component Object Model Hijacking Technique Response Playbook

## Target technique

**T1546.015 — Component Object Model Hijacking**

- Tactics: privilege-escalation, persistence
- Platforms: Windows

Adversaries may establish persistence by executing malicious content triggered by hijacked references to Component Object Model (COM) objects. COM is a system within Windows to enable interaction between software components through the operating system. References to various COM objects are stored in the Registry. Adversaries may use the COM system to insert malicious code that can be executed in place of legitimate software through hijacking the COM references and relationships as a means for persistence. Hijacking a COM object requires a change in the Registry to replace a reference to a legitimate system component which may cause that component to not work when executed. When that system component is executed through normal system operation the adversary's code will be executed instead. An adversary is likely to hijack objects that are used frequently enough to maintain a consistent level of persistence, but are unlikely to break noticeable functionality within the system as to avoid system instability that could lead to detection. One variation of COM hijacking involves abusing Type Libraries (TypeLibs), which provide metadata about COM objects, such as their interfaces and methods. Adversaries may modify Registry keys associated with TypeLibs to redirect legitimate COM object functionality to malicious scripts or payloads. Unlike traditional COM hijacking, which commonly uses local DLLs, this variation may leverage the "script:" moniker to execute remote scripts hosted on external servers. This approach enables stealthy execution of code while maintaining persistence, as the remote payload would be automatically downloaded whenever the hijacked COM object is accessed.

## Preconditions

- the estate in scope is identified, with the systems the technique could apply to;
- an owner is accountable for detection and response;
- current telemetry and configuration can be inspected;
- the technique is applicable or requires an applicability decision.

## Procedure

1. Confirm the scope and owner.
2. Read the current technique description and the associated detection guidance.
3. Inventory the telemetry that would carry the technique's indicators.
4. Inspect whether the indicators are present in the environment.
5. Exercise the detection path and confirm it produces the expected signal.
6. Record gaps in detection coverage and assign remediation owners.
7. Record justified non-applicability or accepted detection gaps separately.
8. Set the next event-driven or periodic verification trigger.

## Failure handling

If the detection path does not produce the expected signal, treat the coverage as unverified, preserve the test evidence, and route the gap through the appropriate remediation or risk process.

## Completion evidence

Scope, owner, source version, telemetry inspected, tests performed, findings, exceptions, remediation links, reviewer, and next trigger.

## Source

- MITRE ATT&CK: https://attack.mitre.org/
- T1546.015: https://attack.mitre.org/techniques/T1546/015
- Reviewed: 2026-10-27
