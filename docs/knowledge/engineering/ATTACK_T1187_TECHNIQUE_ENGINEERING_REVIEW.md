# Forced Authentication Technique Engineering Review

## Reference

- Technique: **T1187 — Forced Authentication**

Adversaries may gather credential material by invoking or forcing a user to automatically provide authentication information through a mechanism in which they can intercept. The Server Message Block (SMB) protocol is commonly used in Windows networks for authentication and communication between systems for access to resources and file sharing. When a Windows system attempts to connect to an SMB resource it will automatically attempt to authenticate and send credential information for the current user to the remote system. This behavior is typical in enterprise environments so that users do not need to enter credentials to access network resources. Web Distributed Authoring and Versioning (WebDAV) is also typically used by Windows systems as a backup protocol when SMB is blocked or fails. WebDAV is an extension of HTTP and will typically operate over TCP ports 80 and 443. Adversaries may take advantage of this behavior to gain access to user account hashes through forced SMB/WebDAV authentication. An adversary can send an attachment to a user through spearphishing that contains a resource link to an external server controlled by the adversary (i.e. Template Injection), or place a specially crafted file on navigation path for privileged accounts (e.g. .SCF file placed on desktop) or on a publicly accessible share to be accessed by victim(s). When the user's system accesses the untrusted resource, it will attempt authentication and send information, including the user's hashed credentials, over SMB to the adversary-controlled server. With access to the credential hash, an adversary can perform off-line Brute Force cracking to gain access to plaintext credentials. There are several different ways this can occur. Some specifics from in-the-wild use include: * A spearphishing attachment containing a document with a resource that is automatically loaded when the document is opened (i.e. Template Injection). The document can include, for example, a request similar to file[:]//[remote address]/Normal.dotm to trigger the SMB request. * A modified .LNK or .SCF file with the icon filename pointing to an external reference such as \\[remote address]\pic.png that will force the system to load the resource when the icon is rendered to repeatedly gather credentials. Alternatively, by leveraging the EfsRpcOpenFileRaw function, an adversary can send SMB requests to a remote system's MS-EFSRPC interface and force the victim computer to initiate an authentication procedure and share its authentication details. The Encrypting File System Remote Protocol (EFSRPC) is a protocol used in Windows networks for maintenance and management operations on encrypted data that is stored remotely to be accessed over a network. Utilization of EfsRpcOpenFileRaw function in EFSRPC is used to open an encrypted object on the server for backup or restore. Adversaries can collect this data and abuse it as part of a NTLM relay attack to gain access to remote systems on the same internal network.

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
- T1187: https://attack.mitre.org/techniques/T1187
- Reviewed: 2026-10-27
