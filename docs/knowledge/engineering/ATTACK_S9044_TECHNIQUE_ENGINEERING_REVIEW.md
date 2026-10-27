# Kali365 Technique Engineering Review

## Reference

- Technique: **S9044 — Kali365**

Kali365 is a Phishing-as-a-Service (PHaaS) kit first observed in April 2026 that generates victim-targeted lures across multiple operating systems to induce users into copying and pasting actor-controlled commands for local execution. Kali365 incorporates on-demand device code generation and mirrors the copy-paste execution tradecraft associated with ClickFix. Operators have used Kali365 to harvest victims' OAuth tokens and session cookies through adversary-in-the-middle (AiTM) interception, enabling account takeover. Kali365 PHaaS was first observed in April 2026. Kali365 has also been affiliated with other branding to include Octopi365 and Freedom365.

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
- S9044: https://attack.mitre.org/software/S9044
- Reviewed: 2026-10-27
