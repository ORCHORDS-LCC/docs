# C0055 Quad7 Activity Outcome Lesson

## Authoritative description

- Technique: **C0055 — Quad7 Activity**

Quad7 Activity, also known as CovertNetwork-1658 or the 7777 Botnet, is a network of compromised small office/home office (SOHO) routers. The botnet was initially composed primarily of TP-Link routers and was named Quad7 due to compromised devices exposing TCP port 7777 with the distinctive banner <code>xlogin</code>. Later activity showed a significant increase in compromised Asus routers and the addition of new ports and banners, including TCP port 63256 displaying <code>alogin</code>. Quad7 infrastructure functions as a collection of egress IPs that various China-affiliated threat actors have used to conduct password-spraying and brute-force operations. Microsoft has reported that Storm-0940 leveraged credentials obtained through Quad7 Activity to target organizations in North America and Europe, including government agencies, non-governmental organizations, think tanks, law firms, energy firms, IT providers, and defense industrial base entities.

## Reusable lesson

This technique should be treated as an explicit review question when it is relevant to the system or organisation, rather than assumed to be covered by a generic control statement or by tooling that reports a related signal.

## Apply the lesson

1. Define the real scope before judging coverage.
2. Inspect current technical, process, governance, or operational evidence.
3. Separate documented intent from verified behaviour.
4. Record partial coverage and unresolved gaps instead of converting them into a pass.
5. Revisit when the underlying scope, threat environment, technology, suppliers, or mission materially changes.

## Source

- MITRE ATT&CK: https://attack.mitre.org/
- C0055: https://attack.mitre.org/campaigns/C0055
- Reviewed: 2026-10-27

## Boundary

This lesson is derived from the published technique description. It does not invent an incident, prescribe one implementation, or claim the technique has been addressed.
