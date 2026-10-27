# Local Account Technique Response Playbook

## Target technique

**T1087.001 — Local Account**

- Tactics: discovery
- Platforms: ESXi, Linux, macOS, Windows

Adversaries may attempt to get a listing of local system accounts. This information can help adversaries determine which local accounts exist on a system to aid in follow-on behavior. Commands such as net user and net localgroup of the Net utility and id and groups on macOS and Linux can list local users and groups. On Linux, local users can also be enumerated through the use of the /etc/passwd file. On macOS, the dscl . list /Users command can be used to enumerate local accounts. On ESXi servers, the `esxcli system account list` command can list local user accounts.

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
- T1087.001: https://attack.mitre.org/techniques/T1087/001
- Reviewed: 2026-10-27
