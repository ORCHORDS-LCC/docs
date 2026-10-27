# Unintended Proxy or Intermediary ('Confused Deputy') Risk Classification Review

## Reference

- Weakness: **441 — Unintended Proxy or Intermediary ('Confused Deputy')**
- Abstraction: Class
- Status: Draft

## Weakness description

The product receives a request, message, or directive from an upstream component, but the product does not sufficiently preserve the original source of the request before forwarding the request to an external actor that is outside of the product's control sphere. This causes the product to appear to be the source of the request, leading it to act as a proxy or other intermediary between the upstream component and the external actor.

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
- 441: https://cwe.mitre.org/data/definitions/441.html
- Reviewed: 2026-10-27
