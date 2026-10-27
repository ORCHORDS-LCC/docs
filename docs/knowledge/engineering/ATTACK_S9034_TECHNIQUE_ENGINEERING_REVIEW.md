# Tsundere Botnet Technique Engineering Review

## Reference

- Technique: **S9034 — Tsundere Botnet**

Tsundere Botnet is a botnet first reported in mid-2025 that is delivered via MSI installer or a PowerShell script. It leverages Node.js and JavaScript for payload delivery and execution, and uses smart contracts on the blockchain to host command and control (C2) addresses. Tsundere Botnet is attributed to a likely Russian-speaking threat actor. A variant named DinDoor has been linked to MuddyWater operations and uses the Deno runtime for execution rather than Node.js.

## Engineering review

1. Identify the engineering boundary where the technique would apply: the component, the service, or the deployment.
2. Review the design decision that would prevent the technique, and record the alternative considered.
3. Review the implementation evidence for the preventive control.
4. Review the test coverage that would fail if the control regressed.
5. Review the observability: which signal would show the control is not operating.
6. Record the residual risk where prevention is not achievable, and the detection that compensates.

## Review evidence

- the design record for the preventive decision;
- the implementation or configuration evidence;
- the test record showing the control is exercised;
- the observability mapping.

## Limitations

An engineering review describes what the design and the implementation evidence show. It does not claim the technique has been addressed in production.

## Source

- MITRE ATT&CK: https://attack.mitre.org/
- S9034: https://attack.mitre.org/software/S9034
- Reviewed: 2026-10-27
