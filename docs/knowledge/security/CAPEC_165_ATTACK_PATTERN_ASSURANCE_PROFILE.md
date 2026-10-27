# File Manipulation Attack Pattern Assurance Profile

## Reference

- Attack pattern: **165 — File Manipulation**
- Status: Draft

## Pattern description

An attacker modifies file contents or attributes (such as extensions or names) of files in a manner to cause incorrect processing by an application. Attackers use this class of attacks to cause applications to enter unstable states, overwrite or expose sensitive information, and even execute arbitrary code with the application's privileges. This class of attacks differs from attacks on configuration information (even if file-based) in that file manipulation causes the file processing to result in non-standard behaviors, such as buffer overflows or use of the incorrect interpreter. Configuration attacks rely on the application interpreting files correctly in order to insert harmful configuration information. Likewise, resource location attacks rely on controlling an application's ability to locate files, whereas File Manipulation attacks do not require the application to look in a non-default location, although the two classes of attacks are often combined.

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
- 165: https://capec.mitre.org/data/definitions/165.html
- Reviewed: 2026-10-27
