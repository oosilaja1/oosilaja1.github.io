# Compliance Crosswalk

How each portal control lines up with the rules a U.S. tax-preparation firm must follow, and with NIST SP 800-53 Rev. 5 and ISO/IEC 27001:2022 Annex A.

**Scope note:** this maps the **technical controls in the software**. Administrative safeguards, such as the WISP, the Qualified Individual, training and incident response, remain the firm's responsibility (see the last table).

## Technical controls

| Portal control | FTC Safeguards Rule (16 CFR 314.4) | IRS Pub 4557 / Pub 5708 (WISP) | NIST SP 800-53 Rev. 5 | ISO/IEC 27001:2022 Annex A |
| --- | --- | --- | --- | --- |
| Mandatory authenticator-app MFA for all users, enforced in the database | (c)(5) Multi-factor authentication | Use MFA on all systems holding taxpayer data | IA-2(1), IA-2(2), IA-5 | 8.5 Secure authentication |
| Client / Preparer / Admin roles; roles read-only from the browser | (c)(1) Access controls | Limit access to authorized staff | AC-2, AC-3 | 5.15 Access control, 5.18 Access rights |
| Preparers see only assigned clients | (c)(1) Least privilege | Need-to-know access | AC-6, AC-5 | 8.2 Privileged access rights, 8.3 Information access restriction |
| Last-admin protection, serialized role changes | (c)(1) | — | AC-2(1), AC-6(5) | 8.2 |
| Pre-approved staff list in a private schema | (c)(1) | Control who is granted access | AC-2 | 5.16 Identity management |
| IRC §7216 consent captured at sign-up (timestamped, versioned) | — | IRC §7216 and Treas. Reg. §301.7216-3 consent | PT-4 Consent, PT-5 Privacy notice | 5.34 Privacy and protection of PII |
| Private document storage; 60-second audited links | (c)(1), (c)(3) | Protect data in storage and transit | AC-3, SC-8, SC-28 (platform) | 8.3, 8.24 Use of cryptography |
| Clients lose original-file access after submission | (c)(1) | — | AC-3 | 8.3 |
| SSN last-4 only; masking of saved free text | (c)(1) data minimization | Minimize collection and storage of SSNs | SI-12, SC-28 | 8.11 Data masking |
| Generic errors; telemetry without raw payloads | — | — | SI-11 Error handling | 8.15 Logging |
| 15-minute idle sign-out | (c)(1) | Lock or sign out idle sessions | AC-11, AC-12 | 8.5 |
| Audit log of document access, roles, assignments, resets, settings, purges | (c)(8) Monitor and log activity | Keep activity logs | AU-2, AU-3, AU-12 | 8.15 Logging, 8.16 Monitoring |
| Retention default 3 years; automated purge with per-file audit | (c)(6) Secure disposal | Dispose of data securely when no longer needed | SI-12, MP-6 | 8.10 Information deletion |
| Live isolation and MFA tests; security scans | (d)(2) Regular testing | Test safeguards | CA-2, CA-8, RA-5 | 8.29 Security testing |
| AI extraction with human confirmation and low-confidence flags | — | — | SI-10 Input validation; NIST AI RMF "Manage" | 8.28 Secure coding |

> Retention note: the Safeguards Rule requires disposal no later than two years after information was last used for the customer, **unless** retention is needed for business operations or a legal requirement. The 3-year default reflects tax-record retention needs and is configurable by the firm.

## Firm responsibilities outside the software

| Requirement | Reference | Owner |
| --- | --- | --- |
| Written Information Security Plan | 16 CFR 314.4; IRS Pub 5708 | Firm |
| Designated Qualified Individual | 314.4(a) | Firm |
| Written risk assessment | 314.4(b) | Firm |
| Staff security awareness training | 314.4(e) | Firm (supported by the staff guide) |
| Service-provider oversight | 314.4(f) | Firm |
| Incident response plan and FTC notification for events affecting 500+ consumers | 314.4(h), 314.4(j) | Firm |
| Annual written report to leadership | 314.4(i) | Firm |
