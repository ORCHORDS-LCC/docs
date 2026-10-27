# Ccache Files Technique Engineering Review

## Reference

- Technique: **T1558.005 — Ccache Files**

Adversaries may attempt to steal Kerberos tickets stored in credential cache files (or ccache). These files are used for short term storage of a user's active session credentials. The ccache file is created upon user authentication and allows for access to multiple services without the user having to re-enter credentials. The /etc/krb5.conf configuration file and the KRB5CCNAME environment variable are used to set the storage location for ccache entries. On Linux, credentials are typically stored in the `/tmp` directory with a naming format of `krb5cc_%UID%` or `krb5.ccache`. On macOS, ccache entries are stored by default in memory with an `API:{uuid}` naming scheme. Typically, users interact with ticket storage using kinit, which obtains a Ticket-Granting-Ticket (TGT) for the principal; klist, which lists obtained tickets currently held in the credentials cache; and other built-in binaries. Adversaries can collect tickets from ccache files stored on disk and authenticate as the current user without their password to perform Pass the Ticket attacks. Adversaries can also use these tickets to impersonate legitimate users with elevated privileges to perform Privilege Escalation. Tools like Kekeo can also be used by adversaries to convert ccache files to Windows format for further Lateral Movement. On macOS, adversaries may use open-source tools or the Kerberos framework to interact with ccache files and extract TGTs or Service Tickets via lower-level APIs.

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
- T1558.005: https://attack.mitre.org/techniques/T1558/005
- Reviewed: 2026-10-27
