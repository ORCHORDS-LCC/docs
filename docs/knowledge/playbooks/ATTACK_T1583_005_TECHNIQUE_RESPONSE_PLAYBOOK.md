# Botnet Technique Response Playbook

## Target technique

**T1583.005 — Botnet**

- Tactics: resource-development
- Platforms: PRE

Adversaries may buy, lease, or rent a network of compromised systems that can be used during targeting. A botnet is a network of compromised systems that can be instructed to perform coordinated tasks. Adversaries may purchase a subscription to use an existing botnet from a booter/stresser service. Internet-facing edge devices and related network appliances that are end-of-life (EOL) and unsupported by their manufacturers are commonly acquired for botnet activities. Adversaries may lease operational relay box (ORB) networks – consisting of virtual private servers (VPS), small office/home office (SOHO) routers, or Internet of Things (IoT) devices – to serve as a botnet. With a botnet at their disposal, adversaries may perform follow-on activity such as large-scale Phishing or Distributed Denial of Service (DDoS). Acquired botnets may also be used to support Command and Control activity, such as Hide Infrastructure through an established Proxy network.

## Preconditions

- the estate in scope is identified, with the systems the technique could apply to;
- an owner is accountable for detection and response;
- current telemetry and configuration can be inspected;
- the technique is applicable or requires an applicability decision.

## Procedure

1. Confirm the scope and owner.
2. Read the current technique description and the associated detection guidance.
3. Inventory the telemetry that would carry the technique's indicators.
4. Inspect whether the indicators are present in the environment.
5. Exercise the detection path and confirm it produces the expected signal.
6. Record gaps in detection coverage and assign remediation owners.
7. Record justified non-applicability or accepted detection gaps separately.
8. Set the next event-driven or periodic verification trigger.

## Failure handling

If the detection path does not produce the expected signal, treat the coverage as unverified, preserve the test evidence, and route the gap through the appropriate remediation or risk process.

## Completion evidence

Scope, owner, source version, telemetry inspected, tests performed, findings, exceptions, remediation links, reviewer, and next trigger.

## Source

- MITRE ATT&CK: https://attack.mitre.org/
- T1583.005: https://attack.mitre.org/techniques/T1583/005
- Reviewed: 2026-10-27
