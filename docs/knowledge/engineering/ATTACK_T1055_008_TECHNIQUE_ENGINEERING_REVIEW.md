# Ptrace System Calls Technique Engineering Review

## Reference

- Technique: **T1055.008 — Ptrace System Calls**

Adversaries may inject malicious code into processes via ptrace (process trace) system calls in order to evade process-based defenses as well as possibly elevate privileges. Ptrace system call injection is a method of executing arbitrary code in the address space of a separate live process. Ptrace system call injection involves attaching to and modifying a running process. The ptrace system call enables a debugging process to observe and control another process (and each individual thread), including changing memory and register values. Ptrace system call injection is commonly performed by writing arbitrary code into a running process (ex: malloc) then invoking that memory with PTRACE_SETREGS to set the register containing the next instruction to execute. Ptrace system call injection can also be done with PTRACE_POKETEXT/PTRACE_POKEDATA, which copy data to a specific address in the target processes’ memory (ex: the current address of the next instruction). Ptrace system call injection may not be possible targeting processes that are non-child processes and/or have higher-privileges. Running code in the context of another process may allow access to the process's memory, system/network resources, and possibly elevated privileges. Execution via ptrace system call injection may also evade detection from security products since the execution is masked under a legitimate process.

## Engineering review

1. Identify the engineering boundary where the technique would apply: the component, the service, or the deployment.
2. Review the design decision that would prevent the technique, and record the alternative considered.
3. Review the implementation evidence for the preventive control.
4. Review the test coverage that would fail if the control regressed.
5. Review the observability: which signal would show the control is not operating.
6. Record the residual risk where prevention is not achievable, and the detection that compensates.

## Review evidence

- the design record for the preventive decision;
- the implementation or configuration evidence;
- the test record showing the control is exercised;
- the observability mapping.

## Limitations

An engineering review describes what the design and the implementation evidence show. It does not claim the technique has been addressed in production.

## Source

- MITRE ATT&CK: https://attack.mitre.org/
- T1055.008: https://attack.mitre.org/techniques/T1055/008
- Reviewed: 2026-10-27
