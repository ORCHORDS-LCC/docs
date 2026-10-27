# Install Root Certificate Mitigation Technique Engineering Review

## Reference

- Technique: **T1130 — Install Root Certificate Mitigation**

HTTP Public Key Pinning (HPKP) is one method to mitigate potential man-in-the-middle situations where and adversary uses a mis-issued or fraudulent certificate to intercept encrypted communications by enforcing use of an expected certificate. Windows Group Policy can be used to manage root certificates and the Flags value of HKLM\SOFTWARE\Policies\Microsoft\SystemCertificates\Root\ProtectedRoots can be set to 1 to prevent non-administrator users from making further root installations into their own HKCU certificate store.

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
- T1130: https://attack.mitre.org/mitigations/T1130
- Reviewed: 2026-10-27
