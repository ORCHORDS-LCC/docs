# Simple Two-Way Active Measurement Protocol (STAMP) Extensions for Segment Routing Networks. R. Gandhi, Ed., C. Filsfils, M. Chen, B. Janssens, R. Foote. Engineering Implementation Review

## Reference

- Document: **RFC 9503 — Simple Two-Way Active Measurement Protocol (STAMP) Extensions for Segment Routing Networks. R. Gandhi, Ed., C. Filsfils, M. Chen, B. Janssens, R. Foote.**
- Series status: PROPOSED STANDARD
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
- RFC 9503: https://www.rfc-editor.org/info/rfc9503
- Reviewed: 2026-10-27
