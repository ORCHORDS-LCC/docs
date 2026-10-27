# Remote Direct Memory Access - Connection Manager (RDMA-CM) Private Data for RPC-over-RDMA Version 1 Engineering Implementation Review

## Reference

- Document: **RFC 8797 — Remote Direct Memory Access - Connection Manager (RDMA-CM) Private Data for RPC-over-RDMA Version 1**
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
- RFC 8797: https://www.rfc-editor.org/info/rfc8797
- Reviewed: 2026-10-27
