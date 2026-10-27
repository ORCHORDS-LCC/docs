# Kali365 Technique Operationalization Review

## Reference

- Technique: **S9044 — Kali365**

Kali365 is a Phishing-as-a-Service (PHaaS) kit first observed in April 2026 that generates victim-targeted lures across multiple operating systems to induce users into copying and pasting actor-controlled commands for local execution. Kali365 incorporates on-demand device code generation and mirrors the copy-paste execution tradecraft associated with ClickFix. Operators have used Kali365 to harvest victims' OAuth tokens and session cookies through adversary-in-the-middle (AiTM) interception, enabling account takeover. Kali365 PHaaS was first observed in April 2026. Kali365 has also been affiliated with other branding to include Octopi365 and Freedom365.

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
- S9044: https://attack.mitre.org/software/S9044
- Reviewed: 2026-10-27
