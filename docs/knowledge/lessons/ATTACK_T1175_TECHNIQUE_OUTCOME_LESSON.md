# T1175 Distributed Component Object Model Mitigation Outcome Lesson

## Authoritative description

- Technique: **T1175 — Distributed Component Object Model Mitigation**

Modify Registry settings (directly or using Dcomcnfg.exe) in <code>HKEY_LOCAL_MACHINE\SOFTWARE\Classes\AppID\{AppID_GUID}</code> associated with the process-wide security of individual COM applications. Modify Registry settings (directly or using Dcomcnfg.exe) in <code>HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Ole</code> associated with system-wide security defaults for all COM applications that do no set their own process-wide security. Consider disabling DCOM through Dcomcnfg.exe. Enable Windows firewall, which prevents DCOM instantiation by default. Ensure all COM alerts and Protected View are enabled.

## Reusable lesson

This technique should be treated as an explicit review question when it is relevant to the system or organisation, rather than assumed to be covered by a generic control statement or by tooling that reports a related signal.

## Apply the lesson

1. Define the real scope before judging coverage.
2. Inspect current technical, process, governance, or operational evidence.
3. Separate documented intent from verified behaviour.
4. Record partial coverage and unresolved gaps instead of converting them into a pass.
5. Revisit when the underlying scope, threat environment, technology, suppliers, or mission materially changes.

## Source

- MITRE ATT&CK: https://attack.mitre.org/
- T1175: https://attack.mitre.org/mitigations/T1175
- Reviewed: 2026-10-27

## Boundary

This lesson is derived from the published technique description. It does not invent an incident, prescribe one implementation, or claim the technique has been addressed.
