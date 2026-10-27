# IDE Tunneling Technique Operationalization Review

## Reference

- Technique: **T1219.001 — IDE Tunneling**

Adversaries may abuse Integrated Development Environment (IDE) software with remote development features to establish an interactive command and control channel on target systems within a network. IDE tunneling combines SSH, port forwarding, file sharing, and debugging into a single secure connection, letting developers work on remote systems as if they were local. Unlike SSH and port forwarding, IDE tunneling encapsulates an entire session and may use proprietary tunneling protocols alongside SSH, allowing adversaries to blend in with legitimate development workflows. Some IDEs, like Visual Studio Code, also provide CLI tools (e.g., `code tunnel`) that adversaries may use to programmatically establish tunnels and generate web-accessible URLs for remote access. These tunnels can be authenticated through accounts such as GitHub, enabling the adversary to control the compromised system via a legitimate developer portal. Additionally, adversaries may use IDE tunneling for persistence. Some IDEs, such as Visual Studio Code and JetBrains, support automatic reconnection. Adversaries may configure the IDE to auto-launch at startup, re-establishing the tunnel upon execution. Compromised developer machines may also be exploited as jump hosts to move further into the network. IDE tunneling tools may be built-in or installed as IDE Extensions.

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
- T1219.001: https://attack.mitre.org/techniques/T1219/001
- Reviewed: 2026-10-27
