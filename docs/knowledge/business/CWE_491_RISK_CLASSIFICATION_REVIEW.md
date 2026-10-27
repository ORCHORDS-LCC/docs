# Public cloneable() Method Without Final ('Object Hijack') Risk Classification Review

## Reference

- Weakness: **491 — Public cloneable() Method Without Final ('Object Hijack')**
- Abstraction: Variant
- Status: Draft

## Weakness description

A class has a cloneable() method that is not declared final, which allows an object to be created without calling the constructor. This can cause the object to be in an unexpected state.

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
- 491: https://cwe.mitre.org/data/definitions/491.html
- Reviewed: 2026-10-27
