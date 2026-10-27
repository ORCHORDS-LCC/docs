# System Language Discovery Technique Response Playbook

## Target technique

**T1614.001 — System Language Discovery**

- Tactics: discovery
- Platforms: Linux, macOS, Windows

Adversaries may attempt to gather information about the system language of a victim in order to infer the geographical location of that host. This information may be used to shape follow-on behaviors, including whether the adversary infects the target and/or attempts specific actions. This decision may be employed by malware developers and operators to reduce their risk of attracting the attention of specific law enforcement agencies or prosecution/scrutiny from other entities. There are various sources of data an adversary could use to infer system language, such as system defaults and keyboard layouts. Specific checks will vary based on the target and/or adversary, but may involve behaviors such as Query Registry and calls to Native API functions. For example, on a Windows system adversaries may attempt to infer the language of a system by querying the registry key <code>HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Nls\Language</code> or parsing the outputs of Windows API functions <code>GetUserDefaultUILanguage</code>, <code>GetSystemDefaultUILanguage</code>, <code>GetKeyboardLayoutList</code> and <code>GetUserDefaultLangID</code>. On a macOS or Linux system, adversaries may query <code>locale</code> to retrieve the value of the <code>$LANG</code> environment variable.

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
- T1614.001: https://attack.mitre.org/techniques/T1614/001
- Reviewed: 2026-10-27
