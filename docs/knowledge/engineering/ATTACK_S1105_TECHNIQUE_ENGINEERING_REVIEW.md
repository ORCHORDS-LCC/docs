# COATHANGER Technique Engineering Review

## Reference

- Technique: **S1105 — COATHANGER**

COATHANGER is a remote access tool (RAT) targeting FortiGate networking appliances. First used in 2023 in targeted intrusions against military and government entities in the Netherlands along with other victims, COATHANGER was disclosed in early 2024, with a high confidence assessment linking this malware to a state-sponsored entity in the People's Republic of China. COATHANGER is delivered after gaining access to a FortiGate device, with in-the-wild observations linked to exploitation of CVE-2022-42475. The name COATHANGER is based on a unique string in the malware used to encrypt configuration files on disk: “She took his coat and hung it up”.

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
- S1105: https://attack.mitre.org/software/S1105
- Reviewed: 2026-10-27
