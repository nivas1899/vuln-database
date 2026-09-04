# Web2 Attack / Vulnerability Database

A structured, queryable reference of **190 web, API, cloud and LLM vulnerability classes**
across **16 categories** — each with a CWE, a severity range, a concrete detection method,
an example payload, a remediation, and a real-world reference.

Built as a personal study and recon aid for web/API penetration testing and bug bounty work:
one source of truth instead of scattered notes, filterable from the command line.

## Layout

| File | Purpose |
|---|---|
| [`vulnerability-database.json`](vulnerability-database.json) | Canonical data — 190 entries. Edit here. |
| [`query_vulns.py`](query_vulns.py) | Zero-dependency CLI to filter and read the database. |
| [`vulnerability-database.md`](vulnerability-database.md) | Human-readable index and schema notes. |

## Schema (per entry)

```
id · name · category · cwe · description · severity_range
detection_method · example_payload · remediation · real_world_reference
```

## Querying

```bash
python3 query_vulns.py --list-categories          # categories with counts
python3 query_vulns.py --category "Injection (Core)"
python3 query_vulns.py --cwe CWE-89
python3 query_vulns.py --severity Critical         # substring match
python3 query_vulns.py --search "header"           # name + description
python3 query_vulns.py --id 39                     # single entry

# or straight jq against the JSON
jq '.vulnerabilities[] | select(.category=="Cloud / Infrastructure")' vulnerability-database.json
```

## Coverage

| Count | Category |
|---:|---|
| 42 | Injection (Core) |
| 24 | Authentication & Session Management |
| 15 | AI / LLM |
| 13 | HTTP Protocol-Level |
| 12 | Access Control / Authorization |
| 12 | API & Modern Architecture |
| 11 | Cross-Site Scripting (XSS) |
| 11 | Cloud / Infrastructure |
| 9 | Business Logic |
| 8 | Client-Side / Browser |
| 6 | CSRF & UI Redressing |
| 6 | File Upload |
| 6 | Network & Miscellaneous |
| 5 | CORS & Cross-Origin |
| 5 | Deserialization |
| 5 | Cryptographic |

## Scope and intent

This is a **defensive and educational reference** — detection cues and fixes for known
vulnerability classes, of the kind found in OWASP material and public disclosure writeups.
Payloads are illustrative and belong only on systems you are authorized to test.
