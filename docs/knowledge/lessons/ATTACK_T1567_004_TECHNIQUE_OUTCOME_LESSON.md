# T1567.004 Exfiltration Over Webhook Outcome Lesson

## Authoritative description

- Technique: **T1567.004 — Exfiltration Over Webhook**
- Tactics: exfiltration
- Platforms: ESXi, Linux, macOS, Office Suite, SaaS, Windows

Adversaries may exfiltrate data to a webhook endpoint rather than over their primary command and control channel. Webhooks are simple mechanisms for allowing a server to push data over HTTP/S to a client without the need for the client to continuously poll the server. Many public and commercial services, such as Discord, Slack, and `webhook.site`, support the creation of webhook endpoints that can be used by other services, such as Github, Jira, or Trello. When changes happen in the linked services (such as pushing a repository update or modifying a ticket), these services will automatically post the data to the webhook endpoint for use by the consuming application. Adversaries may link an adversary-owned environment to a victim-owned SaaS service to achieve repeated Automated Exfiltration of emails, chat messages, and other data. Alternatively, instead of linking the webhook endpoint to a service, an adversary can manually post staged data directly to the URL in order to exfiltrate it. Access to webhook endpoints is often over HTTPS, which gives the adversary an additional level of protection. Exfiltration leveraging webhooks can also blend in with normal network traffic if the webhook endpoint points to a commonly used SaaS application or collaboration service.

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
- T1567.004: https://attack.mitre.org/techniques/T1567/004
- Reviewed: 2026-10-27

## Boundary

This lesson is derived from the published technique description. It does not invent an incident, prescribe one implementation, or claim the technique has been addressed.
