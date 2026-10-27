# Disable or Modify Tools Technique Operationalization Review

## Reference

- Technique: **T1685 — Disable or Modify Tools**

Adversaries may disable, degrade, or tamper with security tools or applications (e.g., endpoint detection and response (EDR) tools, intrusion detection systems (IDS), antivirus, logging agents, sensors, etc.) to impair or reduce visibility of defensive capabilities. This may include stopping specific services, killing processes, modifying or deleting tool configuration files and Registry keys, or preventing tools from updating. This may also include impairing defenses more broadly by disrupting preventative, detection, and response mechanisms across host, network, and cloud environments. In addition to directly targeting tools, adversaries may block or manipulate indicators and telemetry used for detection. This includes maliciously disabling or redirecting sensors such as Event Tracing for Windows (ETW), modifying event log configurations (e.g., redirecting Security logs), or interfering with logging pipelines and forwarding mechanisms (e.g., SIEM ingestion). More advanced techniques include leveraging legitimate drivers or debugging mechanisms to render tools non-functional, bypassing anti-tampering protections, and targeting specific defenses such as Sysmon or cloud monitoring agents. Adversaries may also disrupt broader defensive operations, including update mechanisms, logging infrastructure (e.g., syslog), or event aggregation, further degrading an organization’s ability to detect and respond to malicious activity.

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
- T1685: https://attack.mitre.org/techniques/T1685
- Reviewed: 2026-10-27
