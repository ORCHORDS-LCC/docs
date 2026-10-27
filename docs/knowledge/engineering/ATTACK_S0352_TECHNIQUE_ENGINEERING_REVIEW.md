# OSX_OCEANLOTUS.D Technique Engineering Review

## Reference

- Technique: **S0352 — OSX_OCEANLOTUS.D**

OSX_OCEANLOTUS.D is a macOS backdoor used by APT32. First discovered in 2015, APT32 has continued to make improvements using a plugin architecture to extend capabilities, specifically using `.dylib` files. OSX_OCEANLOTUS.D can also determine it's permission level and execute according to access type (`root` or `user`).

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
- S0352: https://attack.mitre.org/software/S0352
- Reviewed: 2026-10-27
