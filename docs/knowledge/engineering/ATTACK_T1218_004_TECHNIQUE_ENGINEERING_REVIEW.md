# InstallUtil Technique Engineering Review

## Reference

- Technique: **T1218.004 — InstallUtil**

Adversaries may use InstallUtil to proxy execution of code through a trusted Windows utility. InstallUtil is a command-line utility that allows for installation and uninstallation of resources by executing specific installer components specified in .NET binaries. The InstallUtil binary may also be digitally signed by Microsoft and located in the .NET directories on a Windows system: C:\Windows\Microsoft.NET\Framework\v<version>\InstallUtil.exe and C:\Windows\Microsoft.NET\Framework64\v<version>\InstallUtil.exe. InstallUtil may also be used to bypass application control through use of attributes within the binary that execute the class decorated with the attribute [System.ComponentModel.RunInstaller(true)].

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
- T1218.004: https://attack.mitre.org/techniques/T1218/004
- Reviewed: 2026-10-27
