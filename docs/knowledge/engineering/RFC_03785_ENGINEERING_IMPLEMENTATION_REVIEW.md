# Use of Interior Gateway Protocol (IGP) Metric as a second MPLS Traffic Engineering (TE) Metric. F. Le Faucheur, R. Uppili, A. Vedrenne, P. Merckx, T. Telkamp. Engineering Implementation Review

## Reference

- Document: **RFC 3785 — Use of Interior Gateway Protocol (IGP) Metric as a second MPLS Traffic Engineering (TE) Metric. F. Le Faucheur, R. Uppili, A. Vedrenne, P. Merckx, T. Telkamp.**
- Series status: BEST CURRENT PRACTICE
- Published: True

## Implementation review

1. Read the current source text and separate the wire format, the state machine, and the error handling.
2. Record the implementation surface: the parser, the serializer, the state transitions, and the timer behaviour.
3. Record the extension points the document defines, and the decision to implement or not implement each.
4. Record the interoperability cases where a peer behaves differently from the document.
5. Record the security considerations and the implementation control that addresses each.
6. Record the conformance test cases that would catch a regression.

## Review evidence

- the implementation or configuration evidence for the scoped component;
- the interoperability test record;
- the conformance test record.

## Limitations

An implementation review describes the design and its evidence. It does not assert interoperability with any particular peer.

## Source

- RFC Editor index: https://www.rfc-editor.org/rfc-index.txt
- RFC 3785: https://www.rfc-editor.org/info/rfc3785
- Reviewed: 2026-10-27
