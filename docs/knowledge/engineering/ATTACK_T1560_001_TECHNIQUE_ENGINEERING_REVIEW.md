# Archive via Utility Technique Engineering Review

## Reference

- Technique: **T1560.001 — Archive via Utility**

Adversaries may use utilities to compress and/or encrypt collected data prior to exfiltration. Many utilities include functionalities to compress, encrypt, or otherwise package data into a format that is easier/more secure to transport. Adversaries may abuse various utilities to compress or encrypt data before exfiltration. Some third party utilities may be preinstalled, such as tar on Linux and macOS or zip on Windows systems. On Windows, diantz or makecab may be used to package collected files into a cabinet (.cab) file. diantz may also be used to download and compress files from remote locations (i.e. Remote Data Staging). xcopy on Windows can copy files and directories with a variety of options. Additionally, adversaries may use certutil to Base64 encode collected data before exfiltration. Adversaries may use also third party utilities, such as 7-Zip, WinRAR, and WinZip, to perform similar activities.

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
- T1560.001: https://attack.mitre.org/techniques/T1560/001
- Reviewed: 2026-10-27
