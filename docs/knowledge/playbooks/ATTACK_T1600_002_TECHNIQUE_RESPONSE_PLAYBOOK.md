# Disable Crypto Hardware Technique Response Playbook

## Target technique

**T1600.002 — Disable Crypto Hardware**

- Tactics: defense-impairment
- Platforms: Network Devices

Adversaries disable a network device’s dedicated hardware encryption, which may enable them to leverage weaknesses in software encryption in order to reduce the effort involved in collecting, manipulating, and exfiltrating transmitted data. Many network devices such as routers, switches, and firewalls, perform encryption on network traffic to secure transmission across networks. Often, these devices are equipped with special, dedicated encryption hardware to greatly increase the speed of the encryption process as well as to prevent malicious tampering. When an adversary takes control of such a device, they may disable the dedicated hardware, for example, through use of Modify System Image, forcing the use of software to perform encryption on general processors. This is typically used in conjunction with attacks to weaken the strength of the cipher in software (e.g., Reduce Key Space).

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
- T1600.002: https://attack.mitre.org/techniques/T1600/002
- Reviewed: 2026-10-27
