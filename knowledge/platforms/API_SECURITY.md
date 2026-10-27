# API Security

## Overview

API security protects application programming interfaces from attacks, unauthorized access, and abuse. This covers REST, GraphQL, gRPC, and WebSocket APIs across their lifecycle.

## Threat Landscape

### 1. Common API Vulnerabilities
- **Broken Object Level Authorization (BOLA)**: Accessing other users' data via ID manipulation
- **Broken Object Property Level Authorization (BOPLA)**: Accessing unauthorized fields/properties
- **Excessive Data Exposure**: Returning sensitive data not needed by the client
- **Lack of Resources & Rate Limiting**: Enabling denial-of-service attacks

### 2. Authentication & Authorization Risks
- **Broken Authentication**: Weak or missing authentication mechanisms
- **Improper Entity Handling**: Processing malicious input that changes object properties
- **Server Side Request Forgery (SSRF)**: Forcing the server to make unintended requests
- **Security Misconfiguration**: Default credentials, verbose error messages, missing headers

### 3. Data Exposure Risks
- **Mass Assignment**: Accepting arbitrary input parameters that modify unintended properties
- **Insecure Deserialization**: Executing malicious code through deserialized data
- **Business Logic Flaws**: Exploiting workflow gaps (e.g., skipping payment step)

## Security Controls

### 1. Authentication & Authorization
- Use OAuth 2.0 / OIDC for API authentication
- Implement API keys with scoped permissions
- Enforce role-based access control (RBAC) at the API level
- Validate JWT tokens with proper signature verification

### 2. Input Validation
- Schema validation for all request bodies (JSON Schema, OpenAPI)
- Type checking and length limits on all parameters
- Sanitize inputs to prevent injection attacks (SQL, NoSQL, XSS)
- Validate file uploads for type, size, and content

### 3. Rate Limiting & Throttling
- Implement per-user and per-IP rate limits
- Use token bucket or sliding window algorithms
- Return appropriate HTTP status codes (429 Too Many Requests)
- Implement exponential backoff for clients

### 4. Monitoring & Logging
- Log all API requests with user context and response codes
- Monitor for anomalous patterns (unusual endpoints, high error rates)
- Set up alerts for potential attacks (brute force, scraping)
- Maintain audit trails for compliance requirements

## API Security Checklist

| Control | Description |
|---------|-------------|
| Authentication | Enforce authentication on all endpoints |
| Authorization | Validate user permissions for each resource access |
| Input Validation | Validate all inputs against defined schemas |
| Rate Limiting | Implement per-user and per-IP rate limits |
| Error Handling | Return generic error messages, no stack traces |
| HTTPS | Enforce TLS 1.2+ for all API communications |
| CORS | Configure strict Cross-Origin Resource Sharing policies |
| API Versioning | Maintain version control for backward compatibility |

## Standards and Frameworks

- **OWASP API Security Top 10**: Most critical API security risks
- **OpenAPI Specification**: API documentation and validation
- **OAuth 2.0 / OIDC**: Industry-standard authentication protocols
- **NIST SP 800-181**: CCIR - API Security Guidelines

## References

- OWASP API Security Top 10 (2023)
- NIST Special Publication 800-181 - Cybersecurity Supply Chain Risk Management
- RFC 6749 - The OAuth 2.0 Authorization Framework
