# T1036.011 Overwrite Process Arguments Outcome Lesson

## Authoritative description

- Technique: **T1036.011 — Overwrite Process Arguments**
- Tactics: stealth
- Platforms: Linux

Adversaries may modify a process's in-memory arguments to change its name in order to appear as a legitimate or benign process. On Linux, the operating system stores command-line arguments in the process’s stack and passes them to the `main()` function as the `argv` array. The first element, `argv[0]`, typically contains the process name or path - by default, the command used to actually start the process (e.g., `cat /etc/passwd`). By default, the Linux `/proc` filesystem uses this value to represent the process name. The `/proc/<PID>/cmdline` file reflects the contents of this memory, and tools like `ps` use it to display process information. Since arguments are stored in user-space memory at launch, this modification can be performed without elevated privileges. During runtime, adversaries can erase the memory used by all command-line arguments for a process, overwriting each argument string with null bytes. This removes evidence of how the process was originally launched. They can then write a spoofed string into the memory region previously occupied by `argv[0]` to mimic a benign command, such as `cat resolv.conf`. The new command-line string is reflected in `/proc/<PID>/cmdline` and displayed by tools like `ps`.

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
- T1036.011: https://attack.mitre.org/techniques/T1036/011
- Reviewed: 2026-10-27

## Boundary

This lesson is derived from the published technique description. It does not invent an incident, prescribe one implementation, or claim the technique has been addressed.
