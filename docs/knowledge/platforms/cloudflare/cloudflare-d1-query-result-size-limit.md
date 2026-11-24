---
title: "Cloudflare D1 Query Result Size Limit"
owner: "Platform Engineering"
status: "approved"
classification: "public"
last-reviewed: "2026-11-24"
review-cycle: "180 days"
next-review: "2027-05-23"
---

# Cloudflare D1 Query Result Size Limit

## Purpose

Cloudflare began enforcing a 50 MB maximum serialized query result size for D1 on 2026-11-04. This card records the operational consequence and the safe response. It does not restate every D1 platform limit.

## Scope

This guidance applies to:

- Worker and API queries whose serialized result can exceed 50 MB.
- Read paths that previously relied on `SELECT *` or unpaginated result sets.
- Integrations that treated an oversized result as a warning rather than a hard failure.

REST API import and export operations are not subject to this query-result limit. Keep using the documented export API for bulk data movement.

## Failure signature

Cloudflare documents this error for queries above the limit:

```txt
D1 query result exceeded the maximum response size limit of 50 MB
```

Treat the error as a workload-shape problem, not a transient database fault. Retrying the same statement without changing the result shape will not help.

## Safe response

1. Identify the exact statement and measure the serialized result, not only the row count.
2. Replace `SELECT *` with the columns the caller actually uses.
3. Paginate with `LIMIT` and `OFFSET`, or use a stable keyset cursor where ordering and cursor integrity are already defined.
4. Aggregate, sample, or summarize before returning rows to the Worker.
5. Move full-dataset exports to the documented D1 REST API export path.
6. Add a regression test with production-like row widths so a future schema change cannot silently cross the limit.
7. Alert on the specific error string so reviewers can distinguish it from D1 overload and query-duration errors.

## Review checklist

- No unbounded user-facing query returns the full contents of a table.
- Large-result paths have an explicit pagination or export contract.
- Callers handle a failed oversized query without retry storms.
- Evidence includes the statement, result size, and the mitigation chosen.
- The implementation is rechecked against the primary D1 limits page before release.

## Failure modes

- **Confusing export and query limits.** The REST API export exemption does not make a normal Worker query exempt.
- **Measuring rows instead of bytes.** Wide rows can exceed the serialized limit with a modest row count.
- **Adding retries.** The result shape remains too large; retries add load without fixing the cause.
- **Truncating silently.** Dropping rows without telling the caller changes the meaning of the response.

## Sources

- Cloudflare changelog — D1 will enforce a maximum query result size of 50 MB: https://developers.cloudflare.com/changelog/post/2026-10-30-query-result-size-limit/
- Cloudflare Docs — D1 limits: https://developers.cloudflare.com/d1/platform/limits/
- Cloudflare Docs — D1 error list: https://developers.cloudflare.com/d1/observability/debug-d1/#error-list

## Scope note

Cloudflare can change platform limits. Before relying on a numeric limit in an implementation decision, verify it against the primary documentation linked above.
