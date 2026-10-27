# Brute Ratel C4 Technique Engineering Review

## Reference

- Technique: **S1063 — Brute Ratel C4**

Brute Ratel C4 is a commercial red-teaming and adversarial attack simulation tool that first appeared in December 2020. Brute Ratel C4 was specifically designed to avoid detection by endpoint detection and response (EDR) and antivirus (AV) capabilities, and deploys agents called badgers to enable arbitrary command execution for lateral movement, privilege escalation, and persistence. In September 2022, a cracked version of Brute Ratel C4 was leaked in the cybercriminal underground, leading to its use by threat actors.

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
- S1063: https://attack.mitre.org/software/S1063
- Reviewed: 2026-10-27
