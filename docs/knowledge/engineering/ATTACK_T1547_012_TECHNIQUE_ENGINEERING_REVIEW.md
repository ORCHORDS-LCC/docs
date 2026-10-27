# Print Processors Technique Engineering Review

## Reference

- Technique: **T1547.012 — Print Processors**

Adversaries may abuse print processors to run malicious DLLs during system boot for persistence and/or privilege escalation. Print processors are DLLs that are loaded by the print spooler service, `spoolsv.exe`, during boot. Adversaries may abuse the print spooler service by adding print processors that load malicious DLLs at startup. A print processor can be installed through the AddPrintProcessor API call with an account that has SeLoadDriverPrivilege enabled. Alternatively, a print processor can be registered to the print spooler service by adding the HKLM\SYSTEM\\[CurrentControlSet or ControlSet001]\Control\Print\Environments\\[Windows architecture: e.g., Windows x64]\Print Processors\\[user defined]\Driver Registry key that points to the DLL. For the malicious print processor to be correctly installed, the payload must be located in the dedicated system print-processor directory, that can be found with the GetPrintProcessorDirectory API call, or referenced via a relative path from this directory. After the print processors are installed, the print spooler service, which starts during boot, must be restarted in order for them to run. The print spooler service runs under SYSTEM level permissions, therefore print processors installed by an adversary may run under elevated privileges.

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
- T1547.012: https://attack.mitre.org/techniques/T1547/012
- Reviewed: 2026-10-27
