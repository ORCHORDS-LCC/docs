# Masquerade Account Name Technique Engineering Review

## Reference

- Technique: **T1036.010 — Masquerade Account Name**

Adversaries may match or approximate the names of legitimate accounts to make newly created ones appear benign. This will typically occur during Create Account, although accounts may also be renamed at a later date. This may also coincide with Account Access Removal if the actor first deletes an account before re-creating one with the same name. Often, adversaries will attempt to masquerade as service accounts, such as those associated with legitimate software, data backups, or container cluster management. They may also give accounts generic, trustworthy names, such as “admin”, “help”, or “root.” Sometimes adversaries may model account names off of those already existing in the system, as a follow-on behavior to Account Discovery. Note that this is distinct from Impersonation, which describes impersonating specific trusted individuals or organizations, rather than user or service account names.

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
- T1036.010: https://attack.mitre.org/techniques/T1036/010
- Reviewed: 2026-10-27
