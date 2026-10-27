# T1055.008 Ptrace System Calls Outcome Lesson

## Authoritative description

- Technique: **T1055.008 — Ptrace System Calls**
- Tactics: stealth, privilege-escalation
- Platforms: Linux

Adversaries may inject malicious code into processes via ptrace (process trace) system calls in order to evade process-based defenses as well as possibly elevate privileges. Ptrace system call injection is a method of executing arbitrary code in the address space of a separate live process. Ptrace system call injection involves attaching to and modifying a running process. The ptrace system call enables a debugging process to observe and control another process (and each individual thread), including changing memory and register values. Ptrace system call injection is commonly performed by writing arbitrary code into a running process (ex: <code>malloc</code>) then invoking that memory with <code>PTRACE_SETREGS</code> to set the register containing the next instruction to execute. Ptrace system call injection can also be done with <code>PTRACE_POKETEXT</code>/<code>PTRACE_POKEDATA</code>, which copy data to a specific address in the target processes’ memory (ex: the current address of the next instruction). Ptrace system call injection may not be possible targeting processes that are non-child processes and/or have higher-privileges. Running code in the context of another process may allow access to the process's memory, system/network resources, and possibly elevated privileges. Execution via ptrace system call injection may also evade detection from security products since the execution is masked under a legitimate process.

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
- T1055.008: https://attack.mitre.org/techniques/T1055/008
- Reviewed: 2026-10-27

## Boundary

This lesson is derived from the published technique description. It does not invent an incident, prescribe one implementation, or claim the technique has been addressed.
