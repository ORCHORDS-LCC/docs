# Quad7 Activity Technique Engineering Review

## Reference

- Technique: **C0055 — Quad7 Activity**

Quad7 Activity, also known as CovertNetwork-1658 or the 7777 Botnet, is a network of compromised small office/home office (SOHO) routers. The botnet was initially composed primarily of TP-Link routers and was named Quad7 due to compromised devices exposing TCP port 7777 with the distinctive banner xlogin. Later activity showed a significant increase in compromised Asus routers and the addition of new ports and banners, including TCP port 63256 displaying alogin. Quad7 infrastructure functions as a collection of egress IPs that various China-affiliated threat actors have used to conduct password-spraying and brute-force operations. Microsoft has reported that Storm-0940 leveraged credentials obtained through Quad7 Activity to target organizations in North America and Europe, including government agencies, non-governmental organizations, think tanks, law firms, energy firms, IT providers, and defense industrial base entities.

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
- C0055: https://attack.mitre.org/campaigns/C0055
- Reviewed: 2026-10-27
