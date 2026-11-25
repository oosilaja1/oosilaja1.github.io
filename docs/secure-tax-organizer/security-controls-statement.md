# Security Features Statement (Sample)

**System:** Secure Tax Organizer client portal
**Prepared for:** firm owner and Qualified Individual (firm name withheld)
**Classification:** Internal. This sample has the client's identifying details removed.

This statement describes the technical safeguards built into the portal and how each one was verified. It supports the firm's Written Information Security Plan (WISP). It is **not** a certification of compliance.

## 1. Authentication

| Control | Implementation | Verified by |
| --- | --- | --- |
| Mandatory MFA | Authenticator-app (TOTP) MFA is required for every client, preparer and admin before any portal data is shown | Live test: an account without MFA (AAL1) is denied at the page and at the database |
| Database-level MFA check | Restrictive row-level security policies require an AAL2 session, a currently verified TOTP factor, and a fresh challenge after any password reset | Live test: a refreshed reset token without a new challenge is refused |
| MFA secret handling | Enrollment secrets exist only briefly in the enrollment screen and the identity service; they are never written to app tables or logs | Code and log review |
| Session timeout | Users are signed out after 15 minutes of inactivity | Manual test |

## 2. Authorization and least privilege

| Control | Implementation | Verified by |
| --- | --- | --- |
| Role separation | Client, Preparer and Admin roles; roles and assignments are read-only from the browser | Live test: role change from the client side is rejected |
| Assignment-based access | A preparer can read only clients explicitly assigned by an admin | Live test: cross-client isolation |
| Privileged changes | Admin-only server functions require an MFA-verified session and call transactional procedures; changes are serialized with an advisory lock | Regression test |
| Last-admin protection | The final administrator role cannot be revoked | Isolated regression check |
| Staff onboarding | New staff roles come from a pre-approved list in a private schema the browser can't read or change | Database review |

## 3. Document protection

| Control | Implementation |
| --- | --- |
| Private storage | Tax documents are stored in a private bucket; browser-side listing, reading, signing and deleting are denied |
| Short-lived access | Authorized server functions issue view/download links that expire in **60 seconds**, and every issue is audited |
| Post-submission lock | After submitting, clients keep document metadata but can no longer download originals |
| Deletion rights | Only admins can delete originals, run purges or change settings; direct row deletion is revoked |

## 4. Data minimization and privacy

- Only the **last four digits** of an SSN are stored from extracted documents.
- Free text and JSON saved by users is **masked by database triggers** before storage.
- User-facing errors are **generic**; error telemetry excludes raw exception payloads.
- **IRC §7216 consent** is captured at sign-up with a timestamp and version, and discloses that automated software, including AI, reads uploaded documents solely to fill in the organizer.

## 5. Logging and monitoring

The audit log records document views and downloads, submissions, role grants and revocations, client assignments, MFA resets, settings changes and retention purges, with the actor, target, time and details.

## 6. Retention and disposal

- Default retention is **3 years** (editable by admins from 1 to 100 years, with validation and audit).
- A daily authenticated job purges expired originals in batches of up to 100, with a per-file audit record.
- The job is created but **paused until launch**, by design.

## 7. Testing

Automated live tests create isolated accounts, perform real TOTP enrollment, verify cross-client isolation and AAL1 denial, test reset-token refresh denial, purge expired test documents and clean up all fixtures. Platform security scans pass.

## 8. Known items and boundary

- **Platform warning:** the database linter flags a managed extension in the public schema. It is non-relocatable and was deliberately left in place, because reinstalling it would risk the scheduler.
- **Link expiry window:** an issued 60-second link stays valid until it expires, even if the client submits or resets in that window.
- **Firm responsibilities:** these technical controls do not by themselves satisfy 16 CFR Part 314 or IRS Publication 4557. The firm remains responsible for its WISP, designated Qualified Individual, risk assessment, identity-verification and recovery procedures, workforce training, service-provider oversight, and incident response and reporting.
