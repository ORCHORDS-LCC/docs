# Office Template Macros Technique Engineering Review

## Reference

- Technique: **T1137.001 — Office Template Macros**

Adversaries may abuse Microsoft Office templates to obtain persistence on a compromised system. Microsoft Office contains templates that are part of common Office applications and are used to customize styles. The base templates within the application are used each time an application starts. Office Visual Basic for Applications (VBA) macros can be inserted into the base template and used to execute code when the respective Office application starts in order to obtain persistence. Examples for both Word and Excel have been discovered and published. By default, Word has a Normal.dotm template created that can be modified to include a malicious macro. Excel does not have a template file created by default, but one can be added that will automatically be loaded. Shared templates may also be stored and pulled from remote locations. Word Normal.dotm location: (a user home directory)AppData\Roaming\Microsoft\Templates\Normal.dotm Excel Personal.xlsb location: (a user home directory)AppData\Roaming\Microsoft\Excel\XLSTART\PERSONAL.XLSB Adversaries may also change the location of the base template to point to their own by hijacking the application's search order, e.g. Word 2016 will first look for Normal.dotm under C:\Program Files (x86)\Microsoft Office\root\Office16\, or by modifying the GlobalDotName registry key. By modifying the GlobalDotName registry key an adversary can specify an arbitrary location, file name, and file extension to use for the template that will be loaded on application startup. To abuse GlobalDotName, adversaries may first need to register the template as a trusted document or place it in a trusted location. An adversary may need to enable macros to execute unrestricted depending on the system or enterprise security policy on use of macros.

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
- T1137.001: https://attack.mitre.org/techniques/T1137/001
- Reviewed: 2026-10-27
