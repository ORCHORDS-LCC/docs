# Quad7 Activity Technique Operationalization Review

## Reference

- Technique: **C0055 — Quad7 Activity**

Quad7 Activity, also known as CovertNetwork-1658 or the 7777 Botnet, is a network of compromised small office/home office (SOHO) routers. The botnet was initially composed primarily of TP-Link routers and was named Quad7 due to compromised devices exposing TCP port 7777 with the distinctive banner <code>xlogin</code>. Later activity showed a significant increase in compromised Asus routers and the addition of new ports and banners, including TCP port 63256 displaying <code>alogin</code>. Quad7 infrastructure functions as a collection of egress IPs that various China-affiliated threat actors have used to conduct password-spraying and brute-force operations. Microsoft has reported that Storm-0940 leveraged credentials obtained through Quad7 Activity to target organizations in North America and Europe, including government agencies, non-governmental organizations, think tanks, law firms, energy firms, IT providers, and defense industrial base entities.

## Operationalization review

1. Record the operational scope: which services, environments, and data the technique could affect.
2. Record the runbook that would be executed, and its owner.
3. Record the telemetry the runbook depends on, and whether it is retained long enough to investigate.
4. Record the detection that would surface the technique before or after it has an effect.
5. Record the recovery path, and the evidence that recovery has been rehearsed.
6. Record the residual operational risk where the runbook depends on a manual step.

## Review evidence

- the runbook and its owner;
- the telemetry retention and coverage record;
- the detection mapping;
- the exercise or rehearsal record.

## Limitations

An operationalization review describes the runbook and the evidence around it. It does not claim the technique has been prevented or detected in a live environment.

## Source

- MITRE ATT&CK: https://attack.mitre.org/
- C0055: https://attack.mitre.org/campaigns/C0055
- Reviewed: 2026-10-27
