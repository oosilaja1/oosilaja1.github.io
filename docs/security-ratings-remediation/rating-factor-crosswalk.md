# Crosswalk — RiskRecon Domain → Qualys WAS Check → Controls

How each kind of RiskRecon finding was validated and verified, and which controls the work provides evidence for. RiskRecon domain names are paraphrased; check the current RiskRecon methodology for exact naming.

| RiskRecon domain (paraphrased) | Typical finding | Validation & verification | NIST 800-53 Rev. 5 | ISO 27001:2022 |
|---|---|---|---|---|
| Web encryption | TLS 1.0/1.1, weak ciphers, expired / invalid certificate, no HTTPS redirect, no HSTS | **Qualys WAS**: SSL/TLS checks, certificate chain, redirect & HSTS headers | SC-8, SC-13, SC-17, SC-23 | 8.24 |
| Web application security | Missing security headers, insecure cookies, XSS / injection | **Qualys WAS**: header & cookie checks, OWASP vulnerability tests | SI-10, SA-11, RA-5 | 8.26, 8.28, 8.29 |
| Software patching | Outdated or end-of-life web server, CMS, framework | **Qualys WAS**: version / banner detection, plus owner confirmation of the upgrade | SI-2, SA-22, RA-5 | 8.8 |
| Network filtering | RDP, SSH, database, or admin ports exposed | Port scan from an external vantage point | CM-7, SC-7 | 8.20, 8.22 |
| Email security | Missing or weak SPF, DMARC not enforced | DNS / MX record lookup | SC-20, SI-8 | 8.20 |
| Asset attribution | Asset not owned, or owned but orphaned | Inventory reconciliation; dispute or decommission | CM-8, PM-5 | 5.9 |

## How to use it

- **Pick the right check:** web findings go through Qualys WAS. Network and email findings use the check listed.
- **Evidence:** the validation scan, the verification rescan, and the RiskRecon retest result together form the audit trail for RA-5 / SI-2 / CA-7.
- **Third-party risk:** use the same mapping to answer customer security questionnaires consistently.
