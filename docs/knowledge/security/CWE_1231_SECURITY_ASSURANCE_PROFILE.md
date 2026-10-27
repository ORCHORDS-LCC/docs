# Improper Prevention of Lock Bit Modification Security Assurance Profile

## Reference

- Weakness: **1231 — Improper Prevention of Lock Bit Modification**
- Abstraction: Base
- Status: Stable

## Weakness description

The product uses a trusted lock bit for restricting access to registers, address regions, or other resources, but the product does not prevent the value of the lock bit from being modified after it has been set.

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
- 1231: https://cwe.mitre.org/data/definitions/1231.html
- Reviewed: 2026-10-27
