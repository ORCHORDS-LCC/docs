# T1205.002 Socket Filters Outcome Lesson

## Authoritative description

- Technique: **T1205.002 — Socket Filters**
- Tactics: stealth, persistence, command-and-control
- Platforms: Linux, macOS, Windows

Adversaries may attach filters to a network socket to monitor then activate backdoors used for persistence or command and control. With elevated permissions, adversaries can use features such as the `libpcap` library to open sockets and install filters to allow or disallow certain types of data to come through the socket. The filter may apply to all traffic passing through the specified network interface (or every interface if not specified). When the network interface receives a packet matching the filter criteria, additional actions can be triggered on the host, such as activation of a reverse shell. To establish a connection, an adversary sends a crafted packet to the targeted host that matches the installed filter criteria. Adversaries have used these socket filters to trigger the installation of implants, conduct ping backs, and to invoke command shells. Communication with these socket filters may also be used in conjunction with Protocol Tunneling. Filters can be installed on any Unix-like platform with `libpcap` installed or on Windows hosts using `Winpcap`. Adversaries may use either `libpcap` with `pcap_setfilter` or the standard library function `setsockopt` with `SO_ATTACH_FILTER` options. Since the socket connection is not active until the packet is received, this behavior may be difficult to detect due to the lack of activity on a host, low CPU overhead, and limited visibility into raw socket usage.

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
- T1205.002: https://attack.mitre.org/techniques/T1205/002
- Reviewed: 2026-10-27

## Boundary

This lesson is derived from the published technique description. It does not invent an incident, prescribe one implementation, or claim the technique has been addressed.
