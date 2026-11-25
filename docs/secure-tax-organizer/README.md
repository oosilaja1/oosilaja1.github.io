# Secure Tax Organizer: Client Portal for a Tax-Preparation Firm

A secure, compliance-first client portal I designed and delivered for a boutique tax-preparation firm (client name withheld). Clients answer a short questionnaire, get a personal document checklist, upload their tax forms from a phone or laptop, and send a completed organizer to their preparer. Staff work inside a role-based back office with a full audit trail.

> **Redaction note:** The firm's name, logo and staff identities are removed from all screenshots and documents. Every person and record shown is synthetic test data.

## What's in this package

| Document | What it covers |
| --- | --- |
| [CASE-STUDY.md](CASE-STUDY.md) | The problem, the solution, how compliance shaped the design, benefits and lessons learned |
| [security-controls-statement.md](security-controls-statement.md) | Sample security features statement given to the firm, covering each control and how it was verified |
| [compliance-crosswalk.md](compliance-crosswalk.md) | Controls mapped to the FTC Safeguards Rule, IRS Publication 4557, IRC §7216, NIST SP 800-53 Rev. 5 and ISO/IEC 27001:2022 |
| [access-control-matrix.md](access-control-matrix.md) | What a Client, Preparer and Admin can and cannot do |
| [client-security-guide.md](client-security-guide.md) | Sample plain-language security guide for the firm's clients |

## At a glance

- **Users:** clients, preparers and administrators, each with separate permissions
- **Data protected:** W-2s, 1099s, 1098s, 1095-As and other forms containing Federal Tax Information and PII
- **Key controls:** mandatory authenticator-app MFA, least-privilege client assignment, IRC §7216 consent, private document storage with 60-second audited links, 15-minute idle sign-out, data masking, automated retention and purge, and an append-only audit log
- **Stack:** React front end, managed PostgreSQL with row-level security, private object storage and server-side functions, built with an AI-assisted full-stack platform
- **My role:** product owner and security/GRC lead. I set the requirements, threat-modeled the data flows, defined the control set and acceptance tests, and reviewed every release against it.

Interactive walkthrough: [tax-organizer.html](../../tax-organizer.html)
