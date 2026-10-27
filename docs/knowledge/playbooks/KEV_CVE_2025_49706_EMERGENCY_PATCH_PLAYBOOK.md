# Microsoft SharePoint Improper Authentication Vulnerability Emergency Patch Playbook

## Reference

- Vulnerability: **CVE-2025-49706**
- Vendor project: Microsoft
- Product: SharePoint
- Date added: 2025-07-22
- Remediation due: 2025-07-23

## Required action

Disconnect public-facing versions of SharePoint Server that have reached their end-of-life (EOL) or end-of-service (EOS) to include SharePoint Server 2013 and earlier versions. For supported versions, please follow the mitigations according to CISA (URL listed below in Notes) and vendor instructions (URL listed below in Notes). Adhere to the applicable BOD 22-01 guidance for cloud services or discontinue use of the product if mitigations are not available.

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
- CVE-2025-49706: https://nvd.nist.gov/vuln/detail/CVE-2025-49706
- Reviewed: 2026-10-27
