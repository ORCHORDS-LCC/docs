# Improperly Preserved Integrity of Hardware Configuration State During a Power Save/Restore Operation Security Assurance Profile

## Reference

- Weakness: **1304 — Improperly Preserved Integrity of Hardware Configuration State During a Power Save/Restore Operation**
- Abstraction: Base
- Status: Draft

## Weakness description

The product performs a power save/restore operation, but it does not ensure that the integrity of the configuration state is maintained and/or verified between the beginning and ending of the operation.

## Assurance profile

1. Confirm whether the weakness is present in the systems in scope, and record the method used to determine that.
2. Review the weakness's related weaknesses to understand the chain it participates in.
3. Determine which code, configuration, or design element could introduce the weakness.
4. Define the verification method: static analysis, dynamic testing, code review, or configuration inspection.
5. Record the evidence that would show the weakness is absent or remediated.
6. Track the weakness's status and re-check when the catalog is revised.

## Verification evidence

- a scope statement naming the systems examined;
- the verification method and its date;
- findings linked to the specific weakness identifier;
- a remediation or mitigation record for each finding;
- a residual-risk acceptance where remediation is deferred.

## Limitations

A weakness entry describes a class of weakness. Its presence in a system is a property of that system, established only by verification evidence.

## Source

- MITRE CWE catalog: https://cwe.mitre.org/data/xml/cwec_latest.xml.zip
- 1304: https://cwe.mitre.org/data/definitions/1304.html
- Reviewed: 2026-10-27
