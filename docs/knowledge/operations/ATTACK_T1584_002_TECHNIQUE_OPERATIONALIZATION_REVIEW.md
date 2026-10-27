# DNS Server Technique Operationalization Review

## Reference

- Technique: **T1584.002 — DNS Server**

Adversaries may compromise third-party DNS servers that can be used during targeting. During post-compromise activity, adversaries may utilize DNS traffic for various tasks, including for Command and Control (ex: Application Layer Protocol). Instead of setting up their own DNS servers, adversaries may compromise third-party DNS servers in support of operations. By compromising DNS servers, adversaries can alter DNS records. Such control can allow for redirection of an organization's traffic, facilitating Collection and Credential Access efforts for the adversary. Additionally, adversaries may leverage such control in conjunction with Digital Certificates to redirect traffic to adversary-controlled infrastructure, mimicking normal trusted network communications. Alternatively, they may be able to prove ownership of a domain to a SaaS service in order to assert control of the service or create a new administrative Cloud Account. Adversaries may also be able to silently create subdomains pointed at malicious servers without tipping off the actual owner of the DNS server.

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
- T1584.002: https://attack.mitre.org/techniques/T1584/002
- Reviewed: 2026-10-27
