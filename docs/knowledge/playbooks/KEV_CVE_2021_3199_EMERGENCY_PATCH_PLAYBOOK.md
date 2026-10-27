# ONLYOFFICE Docs Server Path Traversal Vulnerability Emergency Patch Playbook

## Reference

- Vulnerability: **CVE-2021-3199**
- Vendor project: ONLYOFFICE
- Product: Docs
- Date added: 2026-10-08
- Remediation due: 2026-10-11

## Required action

Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines.

## Preconditions

- the affected product is confirmed present in scope;
- an owner is accountable for the affected estate;
- a change path and verification path exist for the remediation;
- the urgency is understood relative to the stated due date.

## Procedure

1. Confirm the affected version range against the deployment inventory.
2. Prioritise the estate by exposure and business impact.
3. Apply the required action, or an approved compensating control where immediate patching is not possible.
4. Verify the remediation, and record the verification evidence.
5. Escalate where the due date will be missed, with the compensating control and the review date.
6. Confirm the recurring check that would catch a reintroduction of the affected version.

## Failure handling

If the affected version persists after the due date, treat it as an accepted exception with a named owner, a compensating control, and a fixed review date, and route it through the risk process.

## Completion evidence

Scope, owner, inventory evidence, change record, verification result, exception and compensating control where applicable, reviewer, and next check date.

## Source

- CISA Known Exploited Vulnerabilities catalog: https://www.cisa.gov/known-exploited-vulnerabilities-catalog
- CVE-2021-3199: https://nvd.nist.gov/vuln/detail/CVE-2021-3199
- Reviewed: 2026-10-27
