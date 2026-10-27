# Path Traversal: '/dir/../filename' Risk Classification Review

## Reference

- Weakness: **26 — Path Traversal: '/dir/../filename'**
- Abstraction: Variant
- Status: Draft

## Weakness description

The product uses external input to construct a pathname that should be within a restricted directory, but it does not properly neutralize "/dir/../filename" sequences that can resolve to a location that is outside of that directory.

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
- 26: https://cwe.mitre.org/data/definitions/26.html
- Reviewed: 2026-10-27
