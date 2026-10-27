# Expanding Control over the Operating System from the Database Attack Pattern Assurance Profile

## Reference

- Attack pattern: **470 — Expanding Control over the Operating System from the Database**
- Status: Draft

## Pattern description

An attacker is able to leverage access gained to the database to read / write data to the file system, compromise the operating system, create a tunnel for accessing the host machine, and use this access to potentially attack other machines on the same network as the database machine. Traditionally SQL injections attacks are viewed as a way to gain unauthorized read access to the data stored in the database, modify the data in the database, delete the data, etc. However, almost every data base management system (DBMS) system includes facilities that if compromised allow an attacker complete access to the file system, operating system, and full access to the host running the database. The attacker can then use this privileged access to launch subsequent attacks. These facilities include dropping into a command shell, creating user defined functions that can call system level libraries present on the host machine, stored procedures, etc.

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
- 470: https://capec.mitre.org/data/definitions/470.html
- Reviewed: 2026-10-27
