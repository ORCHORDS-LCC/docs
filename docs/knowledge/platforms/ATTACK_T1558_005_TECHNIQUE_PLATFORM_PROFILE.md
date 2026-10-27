# Ccache Files Technique Platform Profile

## Reference

- Technique: **T1558.005 — Ccache Files**
- Platforms named in the source: Linux, macOS

Adversaries may attempt to steal Kerberos tickets stored in credential cache files (or ccache). These files are used for short term storage of a user's active session credentials. The ccache file is created upon user authentication and allows for access to multiple services without the user having to re-enter credentials. The <code>/etc/krb5.conf</code> configuration file and the <code>KRB5CCNAME</code> environment variable are used to set the storage location for ccache entries. On Linux, credentials are typically stored in the `/tmp` directory with a naming format of `krb5cc_%UID%` or `krb5.ccache`. On macOS, ccache entries are stored by default in memory with an `API:{uuid}` naming scheme. Typically, users interact with ticket storage using <code>kinit</code>, which obtains a Ticket-Granting-Ticket (TGT) for the principal; <code>klist</code>, which lists obtained tickets currently held in the credentials cache; and other built-in binaries. Adversaries can collect tickets from ccache files stored on disk and authenticate as the current user without their password to perform Pass the Ticket attacks. Adversaries can also use these tickets to impersonate legitimate users with elevated privileges to perform Privilege Escalation. Tools like Kekeo can also be used by adversaries to convert ccache files to Windows format for further Lateral Movement. On macOS, adversaries may use open-source tools or the Kerberos framework to interact with ccache files and extract TGTs or Service Tickets via lower-level APIs.

## Platform profile

1. Record the platforms in scope and the versions actually deployed.
2. Compare the deployed platform surface against the platforms the source names.
3. Record where the platform provides a native control for the technique, and where it does not.
4. Record the configuration evidence for the native control, where one exists.
5. Record the gap where the platform provides no native control, and the compensating detection.
6. Record the platform version, because platform behaviour changes between versions.

## Evidence

- the platform and version inventory for the scoped estate;
- the configuration export or screenshot for the native control;
- the detection evidence where the platform provides none.

## Limitations

A technique entry describes a class of abuse across platforms. The platform-specific exposure is a property of the deployment, established only by inventory and configuration evidence.

## Source

- MITRE ATT&CK: https://attack.mitre.org/
- T1558.005: https://attack.mitre.org/techniques/T1558/005
- Reviewed: 2026-10-27
