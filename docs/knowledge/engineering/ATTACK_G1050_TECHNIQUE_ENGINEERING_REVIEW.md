# Water Galura Technique Engineering Review

## Reference

- Technique: **G1050 — Water Galura**

Water Galura are the operators of the Qilin Ransomware-as-a-Service (RaaS) who handle payload generation, ransom negotiations, and the publication of stolen data for Qilin affilates recruited on Russian cybercrime forums. Water Galura have been active since at least 2022 and use a double extortion model where they demand payment for providing decryption keys and for refraining from publishing the stolen data to their leak site.

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
- G1050: https://attack.mitre.org/groups/G1050
- Reviewed: 2026-10-27
