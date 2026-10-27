# LNK Icon Smuggling Technique Engineering Review

## Reference

- Technique: **T1027.012 — LNK Icon Smuggling**

Adversaries may smuggle commands to download malicious payloads past content filters by hiding them within otherwise seemingly benign windows shortcut files. Windows shortcut files (.LNK) include many metadata fields, including an icon location field (also known as the `IconEnvironmentDataBlock`) designed to specify the path to an icon file that is to be displayed for the LNK file within a host directory. Adversaries may abuse this LNK metadata to download malicious payloads. For example, adversaries have been observed using LNK files as phishing payloads to deliver malware. Once invoked (e.g., Malicious File), payloads referenced via external URLs within the LNK icon location field may be downloaded. These files may also then be invoked by Command and Scripting Interpreter/System Binary Proxy Execution arguments within the target path field of the LNK. LNK Icon Smuggling may also be utilized post compromise, such as malicious scripts executing an LNK on an infected host to download additional malicious payloads.

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
- T1027.012: https://attack.mitre.org/techniques/T1027/012
- Reviewed: 2026-10-27
