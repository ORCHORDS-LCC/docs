# Cryptographic Operations are run Before Supporting Units are Ready Security Assurance Profile

## Reference

- Weakness: **1279 — Cryptographic Operations are run Before Supporting Units are Ready**
- Abstraction: Base
- Status: Incomplete

## Weakness description

Performing cryptographic operations without ensuring that the supporting inputs are ready to supply valid data may compromise the cryptographic result.

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
- 1279: https://cwe.mitre.org/data/definitions/1279.html
- Reviewed: 2026-10-27
