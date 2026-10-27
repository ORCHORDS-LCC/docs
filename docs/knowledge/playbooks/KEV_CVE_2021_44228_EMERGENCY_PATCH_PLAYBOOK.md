# Apache Log4j2 Remote Code Execution Vulnerability Emergency Patch Playbook

## Reference

- Vulnerability: **CVE-2021-44228**
- Vendor project: Apache
- Product: Log4j2
- Date added: 2021-12-10
- Remediation due: 2021-12-24

## Required action

For all affected software assets for which updates exist, the only acceptable remediation actions are: 1) Apply updates; OR 2) remove affected assets from agency networks. Temporary mitigations using one of the measures provided at https://www.cisa.gov/uscert/ed-22-02-apache-log4j-recommended-mitigation-measures are only acceptable until updates are available.

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
- CVE-2021-44228: https://nvd.nist.gov/vuln/detail/CVE-2021-44228
- Reviewed: 2026-10-27
