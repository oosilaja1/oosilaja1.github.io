# Case Study: Building a Compliance-First Client Portal for a Tax-Preparation Firm

**Client:** boutique, fully virtual tax-preparation firm (name withheld)
**Timeline:** October–November 2026, ahead of the 2027 filing season
**My role:** product owner and security/GRC lead

## 1. The problem

The firm collected client documents the way many small practices do: email attachments, text-message photos and long back-and-forth threads asking for "one more form."

That created three risks:

- **Data exposure.** Tax documents carry Social Security numbers, income and bank details. They were sitting in personal inboxes and phones.
- **Compliance gaps.** Under the FTC Safeguards Rule (16 CFR Part 314), tax preparers are financial institutions. They must have access controls, MFA, encryption, logging and secure disposal. IRS Publication 4557 sets the same expectations, and IRC §7216 requires written consent before tax-return information is used for anything beyond preparing the return.
- **Wasted time.** Preparers chased missing forms one email at a time, and clients didn't know what to send.

## 2. The solution

A secure client portal with three experiences:

| Who | What they get |
| --- | --- |
| **Client** | A 2-minute quick start (14 yes/no questions) that builds a personal document checklist; upload by phone camera or drag-and-drop; AI reads each form and pre-fills the organizer; the client reviews, confirms and submits |
| **Preparer** | Only the clients assigned to them, with checklist progress, document review, missing-document requests, internal notes and Excel/CSV export |
| **Admin** | Staff and role management, client-to-preparer assignments, firm settings, retention, and the full audit log |

## 3. Compliance by design

I treated compliance as a design input, not a review at the end. Every control below came from a specific requirement and has a test behind it.

| Requirement | How the portal meets it |
| --- | --- |
| MFA for anyone accessing customer information (16 CFR 314.4(c)(5)) | Authenticator-app MFA is mandatory for every client, preparer and admin, and the database itself refuses reads without a verified second factor |
| Access limited to authorized users (314.4(c)(1)) | Separate Client, Preparer and Admin roles; preparers see only clients explicitly assigned to them; roles can't be changed from the browser |
| Consent before using tax-return information (IRC §7216) | Timestamped consent captured at sign-up, versioned, and disclosed in plain language, including that AI reads uploaded documents |
| Logging and monitoring of user activity (314.4(c)(8)) | Audit log for document views and downloads, role changes, assignments, submissions, resets and settings changes |
| Secure disposal (314.4(c)(6)) | Automated retention purge (default 3 years) with a per-file audit record; only admins can delete originals |
| Minimize sensitive data | Only the last four digits of an SSN are stored; free text is masked by database triggers; error messages are generic |
| Session protection (Pub 4557) | Automatic sign-out after 15 minutes of inactivity |

Full mapping: [compliance-crosswalk.md](compliance-crosswalk.md).

## 4. Design decisions that mattered

1. **Enforce at the database, not just the screen.** Hiding a button doesn't stop a determined user. Row-level security policies require a verified MFA session (AAL2) and a matching client or assignment before any row is returned.
2. **Never hand out permanent file links.** Original documents live in a private bucket. Authorized staff get a view or download link that expires in 60 seconds, and every link issued is logged.
3. **AI assists, people confirm.** Extraction highlights low-confidence fields and flags duplicates, and the client confirms every value before it reaches the organizer.
4. **Least privilege for staff.** The first version let any preparer see every client. I changed it to explicit assignment, added a separate Admin role, and made sure the last administrator can never be removed.
5. **Secure staff onboarding.** New staff are added through a pre-approved list held in a private schema the browser can't reach, so the first admin account could be set up without a backdoor.

## 5. Benefits

- **For clients:** one secure place to send everything, a checklist that tells them exactly what's needed, and no more emailing tax forms.
- **For preparers:** complete, pre-organized files; missing documents requested in one click; less time re-keying numbers.
- **For the firm:** controls that line up with the FTC Safeguards Rule and IRS Publication 4557, an audit trail for every sensitive action, and evidence ready for its Written Information Security Plan (WISP).
- **For growth:** a professional, branded experience that scales past what an inbox can handle, with no extra staff.

## 6. Lessons learned

1. **Security friction is a business decision.** Mandatory authenticator-app MFA is the strongest option, but it can scare off less technical clients. I kept it for launch and laid out the trade-off of email or text codes for the owner to decide, rather than quietly weakening the control.
2. **Least privilege usually arrives in version two.** "Every preparer sees every client" was easy to build and wrong for a firm that will grow. Plan assignments from day one.
3. **Protect the keys to the kingdom.** Role changes are serialized, audited, and blocked from removing the last admin. Without that guard, one mistake can lock a firm out of its own data.
4. **Logs can leak too.** Free-text fields and error telemetry can capture SSNs. Masking at the database and generic error messages closed that gap.
5. **Retention is an operation, not a setting.** A purge job needs scheduling, authentication, batching and per-file auditing, and it stays paused until the app is live.
6. **Technical controls don't equal compliance.** The portal supports the Safeguards Rule, but the firm still owns its WISP, Qualified Individual, risk assessment, staff training, vendor oversight and incident response. I documented that boundary so nobody mistakes the software for certification.
7. **Email is infrastructure.** Branded, deliverable notifications needed a dedicated sending subdomain, kept separate from the firm's main mail domain so its existing email wasn't touched.

## 7. Status

Core client, preparer and admin features are built and tested, including live tests for cross-client isolation and MFA enforcement. The remaining launch items are turning on the daily retention job and enabling client email notifications once the sending domain is verified.
