# Exfiltration Over Webhook Technique Platform Profile

## Reference

- Technique: **T1567.004 — Exfiltration Over Webhook**
- Platforms named in the source: ESXi, Linux, macOS, Office Suite, SaaS, Windows

Adversaries may exfiltrate data to a webhook endpoint rather than over their primary command and control channel. Webhooks are simple mechanisms for allowing a server to push data over HTTP/S to a client without the need for the client to continuously poll the server. Many public and commercial services, such as Discord, Slack, and `webhook.site`, support the creation of webhook endpoints that can be used by other services, such as Github, Jira, or Trello. When changes happen in the linked services (such as pushing a repository update or modifying a ticket), these services will automatically post the data to the webhook endpoint for use by the consuming application. Adversaries may link an adversary-owned environment to a victim-owned SaaS service to achieve repeated Automated Exfiltration of emails, chat messages, and other data. Alternatively, instead of linking the webhook endpoint to a service, an adversary can manually post staged data directly to the URL in order to exfiltrate it. Access to webhook endpoints is often over HTTPS, which gives the adversary an additional level of protection. Exfiltration leveraging webhooks can also blend in with normal network traffic if the webhook endpoint points to a commonly used SaaS application or collaboration service.

## Platform profile

1. Record the platforms in scope and the versions actually deployed.
2. Compare the deployed platform surface against the platforms the source names.
3. Record where the platform provides a native control for the technique, and where it does not.
4. Record the configuration evidence for the native control, where one exists.
5. Record the gap where the platform provides no native control, and the compensating detection.
6. Record the platform version, because platform behaviour changes between versions.

## Evidence

- the platform and version inventory for the scoped estate;
- the configuration export or screenshot for the native control;
- the detection evidence where the platform provides none.

## Limitations

A technique entry describes a class of abuse across platforms. The platform-specific exposure is a property of the deployment, established only by inventory and configuration evidence.

## Source

- MITRE ATT&CK: https://attack.mitre.org/
- T1567.004: https://attack.mitre.org/techniques/T1567/004
- Reviewed: 2026-10-27
