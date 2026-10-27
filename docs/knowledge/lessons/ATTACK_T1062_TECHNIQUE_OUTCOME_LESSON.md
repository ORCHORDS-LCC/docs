# T1062 Hypervisor Outcome Lesson

## Authoritative description

- Technique: **T1062 — Hypervisor**
- Tactics: persistence
- Platforms: Windows

**This technique has been deprecated and should no longer be used.** A type-1 hypervisor is a software layer that sits between the guest operating systems and system's hardware. It presents a virtual running environment to an operating system. An example of a common hypervisor is Xen. A type-1 hypervisor operates at a level below the operating system and could be designed with Rootkit functionality to hide its existence from the guest operating system. A malicious hypervisor of this nature could be used to persist on systems through interruption.

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
- T1062: https://attack.mitre.org/techniques/T1062
- Reviewed: 2026-10-27

## Boundary

This lesson is derived from the published technique description. It does not invent an incident, prescribe one implementation, or claim the technique has been addressed.
