# T1601.002 Downgrade System Image Outcome Lesson

## Authoritative description

- Technique: **T1601.002 — Downgrade System Image**
- Tactics: defense-impairment
- Platforms: Network Devices

Adversaries may install an older version of the operating system of a network device to weaken security. Older operating system versions on network devices often have weaker encryption ciphers and, in general, fewer/less updated defensive features. On embedded devices, downgrading the version typically only requires replacing the operating system file in storage. With most embedded devices, this can be achieved by downloading a copy of the desired version of the operating system file and reconfiguring the device to boot from that file on next system restart. The adversary could then restart the device to implement the change immediately or they could wait until the next time the system restarts. Downgrading the system image to an older versions may allow an adversary to evade defenses by enabling behaviors such as Weaken Encryption. Downgrading of a system image can be done on its own, or it can be used in conjunction with Patch System Image.

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
- T1601.002: https://attack.mitre.org/techniques/T1601/002
- Reviewed: 2026-10-27

## Boundary

This lesson is derived from the published technique description. It does not invent an incident, prescribe one implementation, or claim the technique has been addressed.
