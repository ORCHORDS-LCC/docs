# T1003.007 Proc Filesystem Outcome Lesson

## Authoritative description

- Technique: **T1003.007 — Proc Filesystem**
- Tactics: credential-access
- Platforms: Linux

Adversaries may gather credentials from the proc filesystem or `/proc`. The proc filesystem is a pseudo-filesystem used as an interface to kernel data structures for Linux based systems managing virtual memory. For each process, the `/proc/<PID>/maps` file shows how memory is mapped within the process’s virtual address space. And `/proc/<PID>/mem`, exposed for debugging purposes, provides access to the process’s virtual address space. When executing with root privileges, adversaries can search these memory locations for all processes on a system that contain patterns indicative of credentials. Adversaries may use regex patterns, such as <code>grep -E "^[0-9a-f-]* r" /proc/"$pid"/maps | cut -d' ' -f 1</code>, to look for fixed strings in memory structures or cached hashes. When running without privileged access, processes can still view their own virtual memory locations. Some services or programs may save credentials in clear text inside the process’s memory. If running as or with the permissions of a web browser, a process can search the `/maps` & `/mem` locations for common website credential patterns (that can also be used to find adjacent memory within the same structure) in which hashes or cleartext credentials may be located.

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
- T1003.007: https://attack.mitre.org/techniques/T1003/007
- Reviewed: 2026-10-27

## Boundary

This lesson is derived from the published technique description. It does not invent an incident, prescribe one implementation, or claim the technique has been addressed.
