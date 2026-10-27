# Change Default File Association Technique Response Playbook

## Target technique

**T1042 — Change Default File Association**

- Tactics: persistence
- Platforms: Windows

When a file is opened, the default program used to open the file (also called the file association or handler) is checked. File association selections are stored in the Windows Registry and can be edited by users, administrators, or programs that have Registry access or by administrators using the built-in assoc utility. Applications can modify the file association for a given file extension to call an arbitrary program when a file with the given extension is opened. System file associations are listed under HKEY_CLASSES_ROOT\.[extension], for example HKEY_CLASSES_ROOT\.txt. The entries point to a handler for that extension located at HKEY_CLASSES_ROOT\[handler]. The various commands are then listed as subkeys underneath the shell key at HKEY_CLASSES_ROOT\[handler]\shell\[action]\command. For example: * HKEY_CLASSES_ROOT\txtfile\shell\open\command * HKEY_CLASSES_ROOT\txtfile\shell\print\command * HKEY_CLASSES_ROOT\txtfile\shell\printto\command The values of the keys listed are commands that are executed when the handler opens the file extension. Adversaries can modify these values to continually execute arbitrary commands.

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
- T1042: https://attack.mitre.org/techniques/T1042
- Reviewed: 2026-10-27
