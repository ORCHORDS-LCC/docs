# Create files with the same name as files protected with a higher classification Attack Pattern Assurance Profile

## Reference

- Attack pattern: **177 — Create files with the same name as files protected with a higher classification**
- Status: Draft

## Pattern description

An attacker exploits file location algorithms in an operating system or application by creating a file with the same name as a protected or privileged file. The attacker could manipulate the system if the attacker-created file is trusted by the operating system or an application component that attempts to load the original file. Applications often load or include external files, such as libraries or configuration files. These files should be protected against malicious manipulation. However, if the application only uses the name of the file when locating it, an attacker may be able to create a file with the same name and place it in a directory that the application will search before the directory with the legitimate file is searched. Because the attackers' file is discovered first, it would be used by the target application. This attack can be extremely destructive if the referenced file is executable and/or is granted special privileges based solely on having a particular name.

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
- 177: https://capec.mitre.org/data/definitions/177.html
- Reviewed: 2026-10-27
