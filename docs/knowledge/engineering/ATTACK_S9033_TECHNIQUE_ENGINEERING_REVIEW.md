# Fooder Technique Engineering Review

## Reference

- Technique: **S9033 — Fooder**

Fooder is a custom 64-bit C/C++ loader used by MuddyWater that can decrypt and reflectively load embedded payloads such as a go-socks5 proxy utility, the open-source HackBrowserData infostealer, or the MuddyViper backdoor. Fooder has frequently masqueraded as an entertainment executable, such as the Snake game (e.g., `Snake_Game.exe`).

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
- S9033: https://attack.mitre.org/software/S9033
- Reviewed: 2026-10-27
