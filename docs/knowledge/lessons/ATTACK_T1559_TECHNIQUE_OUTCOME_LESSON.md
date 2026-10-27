# T1559 Inter-Process Communication Outcome Lesson

## Authoritative description

- Technique: **T1559 — Inter-Process Communication**
- Tactics: execution
- Platforms: Linux, macOS, Windows

Adversaries may abuse inter-process communication (IPC) mechanisms for local code or command execution. IPC is typically used by processes to share data, communicate with each other, or synchronize execution. IPC is also commonly used to avoid situations such as deadlocks, which occurs when processes are stuck in a cyclic waiting pattern. Adversaries may abuse IPC to execute arbitrary code or commands. IPC mechanisms may differ depending on OS, but typically exists in a form accessible through programming languages/libraries or native interfaces such as Windows Dynamic Data Exchange or Component Object Model. Linux environments support several different IPC mechanisms, two of which being sockets and pipes. Higher level execution mediums, such as those of Command and Scripting Interpreters, may also leverage underlying IPC mechanisms. Adversaries may also use Remote Services such as Distributed Component Object Model to facilitate remote IPC execution.

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
- T1559: https://attack.mitre.org/techniques/T1559
- Reviewed: 2026-10-27

## Boundary

This lesson is derived from the published technique description. It does not invent an incident, prescribe one implementation, or claim the technique has been addressed.
