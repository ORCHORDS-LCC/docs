# T1055.004 Asynchronous Procedure Call Outcome Lesson

## Authoritative description

- Technique: **T1055.004 — Asynchronous Procedure Call**
- Tactics: stealth, privilege-escalation
- Platforms: Windows

Adversaries may inject malicious code into processes via the asynchronous procedure call (APC) queue in order to evade process-based defenses as well as possibly elevate privileges. APC injection is a method of executing arbitrary code in the address space of a separate live process. APC injection is commonly performed by attaching malicious code to the APC Queue of a process's thread. Queued APC functions are executed when the thread enters an alterable state. A handle to an existing victim process is first created with native Windows API calls such as <code>OpenThread</code>. At this point <code>QueueUserAPC</code> can be used to invoke a function (such as <code>LoadLibrayA</code> pointing to a malicious DLL). A variation of APC injection, dubbed "Early Bird injection", involves creating a suspended process in which malicious code can be written and executed before the process' entry point (and potentially subsequent anti-malware hooks) via an APC. AtomBombing is another variation that utilizes APCs to invoke malicious code previously written to the global atom table. Running code in the context of another process may allow access to the process's memory, system/network resources, and possibly elevated privileges. Execution via APC injection may also evade detection from security products since the execution is masked under a legitimate process.

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
- T1055.004: https://attack.mitre.org/techniques/T1055/004
- Reviewed: 2026-10-27

## Boundary

This lesson is derived from the published technique description. It does not invent an incident, prescribe one implementation, or claim the technique has been addressed.
