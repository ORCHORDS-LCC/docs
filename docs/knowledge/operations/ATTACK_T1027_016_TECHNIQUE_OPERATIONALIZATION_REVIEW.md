# Junk Code Insertion Technique Operationalization Review

## Reference

- Technique: **T1027.016 — Junk Code Insertion**

Adversaries may use junk code / dead code to obfuscate a malware’s functionality. Junk code is code that either does not execute, or if it does execute, does not change the functionality of the code. Junk code makes analysis more difficult and time-consuming, as the analyst steps through non-functional code instead of analyzing the main code. It also may hinder detections that rely on static code analysis due to the use of benign functionality, especially when combined with Compression or Software Packing. No-Operation (NOP) instructions are an example of dead code commonly used in x86 assembly language. They are commonly used as the 0x90 opcode. When NOPs are added to malware, the disassembler may show the NOP instructions, leading to the analyst needing to step through them. The use of junk / dead code insertion is distinct from Binary Padding because the purpose is to obfuscate the functionality of the code, rather than simply to change the malware’s signature.

## Operationalization review

1. Record the operational scope: which services, environments, and data the technique could affect.
2. Record the runbook that would be executed, and its owner.
3. Record the telemetry the runbook depends on, and whether it is retained long enough to investigate.
4. Record the detection that would surface the technique before or after it has an effect.
5. Record the recovery path, and the evidence that recovery has been rehearsed.
6. Record the residual operational risk where the runbook depends on a manual step.

## Review evidence

- the runbook and its owner;
- the telemetry retention and coverage record;
- the detection mapping;
- the exercise or rehearsal record.

## Limitations

An operationalization review describes the runbook and the evidence around it. It does not claim the technique has been prevented or detected in a live environment.

## Source

- MITRE ATT&CK: https://attack.mitre.org/
- T1027.016: https://attack.mitre.org/techniques/T1027/016
- Reviewed: 2026-10-27
