# Web2 Attack/Vulnerability Database

**Canonical data lives in [`vulnerability-database.json`](vulnerability-database.json)
— 190 entries, 16 categories.** This file is just the index/README; don't edit vulnerability
content here, edit the JSON (keeps one source of truth instead of two drifting copies).

## Schema (per entry)
`id, name, category, cwe, description, severity_range, detection_method, example_payload, remediation, real_world_reference`

## Querying it

```bash
# list categories with counts
python3 query_vulns.py --list-categories

# filter by category
python3 query_vulns.py --category "Injection (Core)"

# filter by CWE
python3 query_vulns.py --cwe CWE-89

# filter by severity (substring match)
python3 query_vulns.py --severity Critical

# free-text search across name + description
python3 query_vulns.py --search "header"

# single entry by id
python3 query_vulns.py --id 39

# or raw jq against the JSON directly
jq '.vulnerabilities[] | select(.category=="Cloud / Infrastructure")' vulnerability-database.json
```

## Categories (16)
Injection (Core) · Cross-Site Scripting (XSS) · Access Control / Authorization ·
Authentication & Session Management · Business Logic · CSRF & UI Redressing ·
CORS & Cross-Origin · HTTP Protocol-Level · Deserialization · File Upload ·
API & Modern Architecture · Cloud / Infrastructure · Cryptographic ·
Client-Side / Browser · AI / LLM · Network & Miscellaneous

## Sources
- PortSwigger Web Security Academy — https://portswigger.net/web-security/all-topics
- PortSwigger Research, Top 10 Web Hacking Techniques of 2025 — https://portswigger.net/research/top-10-web-hacking-techniques-of-2025
- OWASP Web Security Testing Guide (WSTG) — https://owasp.org/www-project-web-security-testing-guide/
- OWASP API Security Top 10 — https://owasp.org/API-Security/
- OWASP Top 10 for LLM Applications (2025) — https://genai.owasp.org/resource/owasp-top-10-for-llm-applications-2025/
- OWASP Top 10 for Agentic Applications (ASI01–ASI10) — OWASP GenAI Security Project, published Dec 2025
- CWE (Common Weakness Enumeration) — https://cwe.mitre.org/
- 0xKayala/A-to-Z-Vulnerabilities — https://github.com/0xKayala/A-to-Z-Vulnerabilities
- NVD/CVE records cited inline per entry (e.g. CVE-2024-45409, CVE-2025-54136)
- This toolkit's own `hunt-*` skill knowledge bases (built from disclosed public bug bounty reports)

## Maintenance
Living document, not a hard ceiling — append new entries to the JSON's
`vulnerabilities` array as new bug classes/variants are learned during engagements.
Keep `total_entries` and the `--list-categories` count in sync after edits (the query
script recalculates categories live, but `total_entries` in the JSON header is manual).

**2026-07-28 update (batch 1):** +20 entries (161–180), covering 2024–2026 research: browser-powered
desync / pause-based desync / parser differentials (HTTP Protocol-Level); SAML XSW and
WebAuthn/passkey downgrade (Auth); CSWSH-via-WS-GraphQL (CORS); SVG filter pixel-stealing
and CSP nonce/bfcache bypass (Client-Side); dependency confusion and GitHub Actions
mutable-tag compromise (Cloud/Infra); OWASP LLM Top 10 2025 gaps — sensitive info
disclosure, data/model poisoning, RAG/vector poisoning — plus MCP tool poisoning, ASCII
smuggling, and four OWASP Agentic (ASI01–04) entries (AI/LLM); single-packet race
condition technique (Business Logic).

**2026-07-28 update (batch 2):** +10 entries (181–190): Kubernetes admission-webhook
config-injection RCE / IngressNightmare (Cloud/Infra); the three still-missing OWASP API
Security Top 10 2023 categories — BOPLA, improper inventory management (shadow/zombie
APIs), unrestricted sensitive business flows, unsafe consumption of third-party APIs
(API & Modern Architecture); HTTP/2 CONTINUATION Flood and Rapid Reset DoS (HTTP
Protocol-Level); OAuth device-code phishing, the MFA-bypassing technique behind the
Storm-2372/EvilTokens campaigns (Auth); malicious Service Worker registration for
persistent post-XSS compromise, and Trusted Types policy bypass (Client-Side / XSS).

Scope note: this DB stays Web2/API/Cloud/AI-LLM focused by design — Android/iOS-specific
classes (e.g. intent redirection, deep-link hijacking) are intentionally left to the
dedicated `apk-redteam-pipeline` skill rather than duplicated here. Say the word if you
want mobile folded into this DB too.
