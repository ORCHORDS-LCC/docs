# Reverse Engineer an Executable to Expose Assumed Hidden Functionality Attack Pattern Assurance Profile

## Reference

- Attack pattern: **190 — Reverse Engineer an Executable to Expose Assumed Hidden Functionality**
- Status: Draft

## Pattern description

An attacker analyzes a binary file or executable for the purpose of discovering the structure, function, and possibly source-code of the file by using a variety of analysis techniques to effectively determine how the software functions and operates. This type of analysis is also referred to as Reverse Code Engineering, as techniques exist for extracting source code from an executable. Several techniques are often employed for this purpose, both black box and white box. The use of computer bus analyzers and packet sniffers allows the binary to be studied at a level of interactions with its computing environment, such as a host OS, inter-process communication, and/or network communication. This type of analysis falls into the 'black box' category because it involves behavioral analysis of the software without reference to source code, object code, or protocol specifications.

## Assurance profile

1. Determine whether the attack pattern is in scope for the systems and data being protected, and record the reason.
2. Review the pattern's prerequisites: the access, position, or precondition it requires.
3. Identify the observable indicators the pattern would produce in logs, telemetry, or configuration.
4. Define the control that prevents the pattern and the control that would detect it.
5. Define the verification method and the evidence that would demonstrate either prevention or detection.
6. Record the residual risk where only detection, not prevention, can be achieved.

## Verification evidence

- a scope decision recording why the pattern is or is not applicable;
- the indicator list mapped to the telemetry that would carry it;
- the control mapping with the evidence that supports it;
- a test or exercise record for the detection path.

## Limitations

An attack-pattern entry describes a class of abuse. Applicability and exposure are properties of a system, established only by evidence.

## Source

- MITRE CAPEC catalog: https://capec.mitre.org/data/xml/capec_latest.xml
- 190: https://capec.mitre.org/data/definitions/190.html
- Reviewed: 2026-10-27
