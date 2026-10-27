# GlassWorm Technique Engineering Review

## Reference

- Technique: **S9010 — GlassWorm**

GlassWorm is a worm that propagated through supply chain attacks by compromising repository credentials from victim environments and having malicious payloads added to those compromised accounts for distribution to victims across the various development ecosystems. GlassWorm has numerous variants, including Rust binaries, encrypted JavaScript and a variant leveraging invisible Unicode characters that made reverse engineering difficult. GlassWorm has employed a unique command and control (C2) methodology using Solana blockchain. GlassWorm was first reported in October 2025.

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
- S9010: https://attack.mitre.org/software/S9010
- Reviewed: 2026-10-27
