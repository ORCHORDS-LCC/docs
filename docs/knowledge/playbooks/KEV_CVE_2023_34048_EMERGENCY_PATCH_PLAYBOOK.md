# VMware vCenter Server Out-of-Bounds Write Vulnerability Emergency Patch Playbook

## Reference

- Vulnerability: **CVE-2023-34048**
- Vendor project: VMware
- Product: vCenter Server
- Date added: 2024-01-22
- Remediation due: 2024-02-12

## Required action

Apply mitigations per vendor instructions or discontinue use of the product if mitigations are unavailable.

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
- CVE-2023-34048: https://nvd.nist.gov/vuln/detail/CVE-2023-34048
- Reviewed: 2026-10-27
