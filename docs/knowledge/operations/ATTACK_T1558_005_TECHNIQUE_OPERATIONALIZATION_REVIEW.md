# Ccache Files Technique Operationalization Review

## Reference

- Technique: **T1558.005 — Ccache Files**

Adversaries may attempt to steal Kerberos tickets stored in credential cache files (or ccache). These files are used for short term storage of a user's active session credentials. The ccache file is created upon user authentication and allows for access to multiple services without the user having to re-enter credentials. The <code>/etc/krb5.conf</code> configuration file and the <code>KRB5CCNAME</code> environment variable are used to set the storage location for ccache entries. On Linux, credentials are typically stored in the `/tmp` directory with a naming format of `krb5cc_%UID%` or `krb5.ccache`. On macOS, ccache entries are stored by default in memory with an `API:{uuid}` naming scheme. Typically, users interact with ticket storage using <code>kinit</code>, which obtains a Ticket-Granting-Ticket (TGT) for the principal; <code>klist</code>, which lists obtained tickets currently held in the credentials cache; and other built-in binaries. Adversaries can collect tickets from ccache files stored on disk and authenticate as the current user without their password to perform Pass the Ticket attacks. Adversaries can also use these tickets to impersonate legitimate users with elevated privileges to perform Privilege Escalation. Tools like Kekeo can also be used by adversaries to convert ccache files to Windows format for further Lateral Movement. On macOS, adversaries may use open-source tools or the Kerberos framework to interact with ccache files and extract TGTs or Service Tickets via lower-level APIs.

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
- T1558.005: https://attack.mitre.org/techniques/T1558/005
- Reviewed: 2026-10-27
