---
title: "GitHub Actions Workflow Hardening"
owner: "Engineering Operations"
status: "approved"
classification: "public"
last-reviewed: "2026-11-24"
review-cycle: "180 days"
next-review: "2027-05-23"
---

# GitHub Actions Workflow Hardening

## Purpose

This card records the baseline controls for workflows that run builds, tests, and deployments. It complements the more specific cache and OIDC cards rather than duplicating them.

## Token permissions

- Set `permissions` at the workflow or job level and grant only the scopes the job needs.
- Prefer read-only `contents` as the default; add write scopes only to jobs that require them.
- Treat reusable workflow calls as a permission boundary: a called workflow cannot raise the token beyond the caller's grant.
- For cloud access, prefer short-lived OIDC credentials over long-lived repository secrets.

## Secrets and untrusted input

- Anyone with write access to a repository can read that repository's secrets. Design workflows on that assumption.
- Automatic secret redaction is not guaranteed. Do not echo secrets, write them to logs, or place them in caches.
- Pass untrusted expressions through an intermediate environment variable before using them in a shell step. Do not interpolate issue titles, branch names, or pull-request bodies directly into `run:` scripts.
- Review `pull_request_target`, `issue_comment`, and `workflow_run` workflows separately. These triggers can place privileged contexts near contributor-controlled content.
- Do not check out and execute untrusted pull-request code in a job that holds deployment credentials.

## Action and runner boundary

- Pin third-party actions to a full-length commit SHA for security-sensitive jobs; review updates to the pinned SHA.
- Keep untrusted builds away from privileged runners. Split "build untrusted code" and "deploy with credentials" into separate jobs with separate permissions.
- Treat restored dependency caches as untrusted input. See [GitHub Actions Cache Trust Boundaries](../../operations/GITHUB_ACTIONS_CACHE_TRUST_BOUNDARIES.md).
- Record immutable workflow references in deployment evidence where reproducibility matters. See [GitHub Reusable Workflow OIDC Trust](../../operations/GITHUB_REUSABLE_WORKFLOW_OIDC_TRUST.md).

## Pre-merge review checklist

- The workflow declares explicit `permissions`.
- Every `run:` step that consumes an expression uses a safe input path.
- No secret is written to a cache, artifact, generated file, or log line.
- Third-party actions are pinned or the exception is recorded.
- Low-trust triggers do not execute contributor code with write credentials.
- OIDC trust conditions identify the expected repository, ref, and workflow.
- A failed permissions change is tested before rollout.

## Failure modes

- **Broad token scopes.** A compromised step inherits every scope granted to the job.
- **Direct expression interpolation.** Contributor-controlled text becomes shell syntax.
- **Mutable action references.** A tag or branch can move after review.
- **Cache poisoning.** A restored cache supplies executable files to a later privileged step.
- **Reusable workflow ambiguity.** Trust checks the caller but not the workflow that actually supplied the job definition.

## Sources

- GitHub Docs — Security hardening for GitHub Actions: https://docs.github.com/en/actions/security-for-github-actions/security-guides/security-hardening-for-github-actions
- GitHub Docs — Securely using `pull_request_target`: https://docs.github.com/en/actions/reference/security/securely-using-pull_request_target
- GitHub Docs — Dependency caching reference: https://docs.github.com/en/actions/reference/workflows-and-actions/dependency-caching

## Scope note

This card covers workflow design controls. Runner patching, organization-level policy enforcement, and provider-specific OIDC trust syntax are reviewed separately.
