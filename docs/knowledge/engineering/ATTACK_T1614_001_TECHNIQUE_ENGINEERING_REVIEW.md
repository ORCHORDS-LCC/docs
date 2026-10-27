# System Language Discovery Technique Engineering Review

## Reference

- Technique: **T1614.001 — System Language Discovery**

Adversaries may attempt to gather information about the system language of a victim in order to infer the geographical location of that host. This information may be used to shape follow-on behaviors, including whether the adversary infects the target and/or attempts specific actions. This decision may be employed by malware developers and operators to reduce their risk of attracting the attention of specific law enforcement agencies or prosecution/scrutiny from other entities. There are various sources of data an adversary could use to infer system language, such as system defaults and keyboard layouts. Specific checks will vary based on the target and/or adversary, but may involve behaviors such as Query Registry and calls to Native API functions. For example, on a Windows system adversaries may attempt to infer the language of a system by querying the registry key HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Nls\Language or parsing the outputs of Windows API functions GetUserDefaultUILanguage, GetSystemDefaultUILanguage, GetKeyboardLayoutList and GetUserDefaultLangID. On a macOS or Linux system, adversaries may query locale to retrieve the value of the $LANG environment variable.

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
- T1614.001: https://attack.mitre.org/techniques/T1614/001
- Reviewed: 2026-10-27
