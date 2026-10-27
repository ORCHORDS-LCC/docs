# Raspberry Robin Technique Response Playbook

## Target technique

**S1130 — Raspberry Robin**

- Platforms: Windows

Raspberry Robin is initial access malware first identified in September 2021, and active through early 2024. The malware is notable for spreading via infected USB devices containing a malicious LNK object that, on execution, retrieves remote hosted payloads for installation. Raspberry Robin has been widely used against various industries and geographies, and as a precursor to information stealer, ransomware, and other payloads such as SocGholish, Cobalt Strike, IcedID, and Bumblebee. The DLL componenet in the Raspberry Robin infection chain is also referred to as "Roshtyak." The name "Raspberry Robin" is used to refer to both the malware as well as the threat actor associated with its use, although the Raspberry Robin operators are also tracked as <code>Storm-0856</code> by some vendors.

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
- S1130: https://attack.mitre.org/software/S1130
- Reviewed: 2026-10-27
