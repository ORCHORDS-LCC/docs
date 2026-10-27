# Exposure of File Descriptor to Unintended Control Sphere ('File Descriptor Leak') Risk Classification Review

## Reference

- Weakness: **403 — Exposure of File Descriptor to Unintended Control Sphere ('File Descriptor Leak')**
- Abstraction: Base
- Status: Draft

## Weakness description

A process does not close sensitive file descriptors before invoking a child process, which allows the child to perform unauthorized I/O operations using those descriptors.

## Risk classification review

1. Record whether the weakness class is relevant to the systems and data in scope, and the reason.
2. Record the business impact if the weakness class were present and exploited, in terms of the affected capability.
3. Record the likelihood assessment and the evidence behind it.
4. Record the classification and the criteria it was measured against.
5. Record the treatment: remediate, mitigate, transfer, or accept, with the owner.
6. Record the review trigger for the classification.

## Classification record

- In scope: _to be completed_
- Impact: _to be completed_
- Likelihood: _to be completed_
- Classification: _to be completed_
- Treatment and owner: _to be completed_
- Review trigger: _to be completed_

## Limitations

A weakness entry describes a class of weakness. The classification is a judgement about a specific estate, recorded with its evidence.

## Source

- MITRE CWE catalog: https://cwe.mitre.org/data/xml/cwec_latest.xml.zip
- 403: https://cwe.mitre.org/data/definitions/403.html
- Reviewed: 2026-10-27
