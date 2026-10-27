# T1027.016 Junk Code Insertion Outcome Lesson

## Authoritative description

- Technique: **T1027.016 — Junk Code Insertion**
- Tactics: stealth
- Platforms: Linux, macOS, Windows

Adversaries may use junk code / dead code to obfuscate a malware’s functionality. Junk code is code that either does not execute, or if it does execute, does not change the functionality of the code. Junk code makes analysis more difficult and time-consuming, as the analyst steps through non-functional code instead of analyzing the main code. It also may hinder detections that rely on static code analysis due to the use of benign functionality, especially when combined with Compression or Software Packing. No-Operation (NOP) instructions are an example of dead code commonly used in x86 assembly language. They are commonly used as the 0x90 opcode. When NOPs are added to malware, the disassembler may show the NOP instructions, leading to the analyst needing to step through them. The use of junk / dead code insertion is distinct from Binary Padding because the purpose is to obfuscate the functionality of the code, rather than simply to change the malware’s signature.

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
- T1027.016: https://attack.mitre.org/techniques/T1027/016
- Reviewed: 2026-10-27

## Boundary

This lesson is derived from the published technique description. It does not invent an incident, prescribe one implementation, or claim the technique has been addressed.
