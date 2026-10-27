# T1480.002 Mutual Exclusion Outcome Lesson

## Authoritative description

- Technique: **T1480.002 — Mutual Exclusion**
- Tactics: stealth
- Platforms: Linux, macOS, Windows

Adversaries may constrain execution or actions based on the presence of a mutex associated with malware. A mutex is a locking mechanism used to synchronize access to a resource. Only one thread or process can acquire a mutex at a given time. While local mutexes only exist within a given process, allowing multiple threads to synchronize access to a resource, system mutexes can be used to synchronize the activities of multiple processes. By creating a unique system mutex associated with a particular malware, adversaries can verify whether or not a system has already been compromised. In Linux environments, malware may instead attempt to acquire a lock on a mutex file. If the malware is able to acquire the lock, it continues to execute; if it fails, it exits to avoid creating a second instance of itself. Mutex names may be hard-coded or dynamically generated using a predictable algorithm.

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
- T1480.002: https://attack.mitre.org/techniques/T1480/002
- Reviewed: 2026-10-27

## Boundary

This lesson is derived from the published technique description. It does not invent an incident, prescribe one implementation, or claim the technique has been addressed.
