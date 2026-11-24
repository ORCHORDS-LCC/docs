---
title: "Secrets Exposure Detection and Response"
owner: "Security Engineering"
status: "approved"
classification: "public"
last-reviewed: "2026-11-25"
review-cycle: "180 days"
next-review: "2027-05-24"
---

# Secrets Exposure Detection and Response

## Purpose

A committed secret is a credential-exposure incident, not only a code-quality finding. This card defines the minimum detection, containment, and recovery controls for secrets in source, history, CI/CD, and logs.

## Detection layers

| Layer | Control | Evidence |
| --- | --- | --- |
| Developer workstation | Pre-commit secret scanning with maintained baseline/allowlist for verified false positives. | Hook config, scan output, baseline review record. |
| Pull request / push | Repository secret scanning and push protection where supported. Bypasses require documented justification and review. | Alert, bypass reason, reviewer identity. |
| Repository history | Periodic full-history scans, including new branches and imported repositories. | Scan report, finding disposition. |
| CI/CD and logs | Mask secrets, avoid echoing environment values, and scan build logs/artifacts for credential patterns. | Workflow config, log-redaction check. |

## Response sequence

1. **Classify the exposure.** Identify credential type, owner system, privilege, scope, and where it appeared: working tree, commit, pull request, issue, artifact, or log.
2. **Revoke or rotate first.** Treat the secret as compromised once it leaves a trusted secret store. Do not wait for history rewrite completion.
3. **Assess blast radius.** Review provider audit logs, recent API use, resource changes, and downstream systems that accepted the credential.
4. **Remove from active paths.** Delete from code, config, CI variables, artifacts, caches, and container images as applicable.
5. **Remediate history when needed.** Use history-rewrite tools only after rotation and team coordination. A history rewrite does not revoke the credential and does not remove clones, forks, mirrors, or archives.
6. **Close with evidence.** Record revocation time, replacement location, scan result after remediation, and any customer or regulatory notification decision.

## Design controls

- Store secrets in a secret manager or platform-provided secret store; do not place them in source, prompts, hidden context, or container layers.
- Prefer short-lived, scoped credentials (OIDC/workload identity, ephemeral tokens) over static long-lived keys.
- Give CI/CD identities least privilege and separate build credentials from deploy credentials.
- Treat secret-scanning bypasses as exceptions: document reason, expiry, and compensating control.
- Keep detection patterns current; custom patterns should be tested for false positives before enforcement.

## Failure modes

- **History-only cleanup.** Removing a key from HEAD leaves it valid and discoverable.
- **Bypass without review.** Push-protection bypass becomes an untracked exception path.
- **Secret copied into logs.** Incident responders rotate repo secrets but miss CI logs, artifacts, or crash reports.
- **Over-broad token replacement.** New secret has same excessive scope, preserving impact for the next exposure.

## Sources

- OWASP Cheat Sheet Series — Secrets Management: https://cheatsheetseries.owasp.org/cheatsheets/Secrets_Management_Cheat_Sheet.html
- GitHub Docs — About secret scanning: https://docs.github.com/en/code-security/secret-scanning/introduction/about-secret-scanning
- GitHub Docs — About push protection: https://docs.github.com/en/code-security/secret-scanning/introduction/about-push-protection
- GitHub Docs — Working with push protection: https://docs.github.com/en/code-security/secret-scanning/working-with-secret-scanning-and-push-protection/working-with-push-protection-in-the-github-ui

## Scope note

Provider-specific revocation steps, legal notification requirements, and customer communications are handled by the owning service's incident process. This card defines the engineering baseline.
