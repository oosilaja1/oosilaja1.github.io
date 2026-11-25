# Access Control Matrix

Every permission below is enforced on the server and in the database, not only in the interface. All roles require a verified MFA session.

| Action | Client | Preparer | Admin |
| --- | :---: | :---: | :---: |
| Complete quick start and see own checklist | ✓ | — | — |
| Upload, review and confirm own documents | ✓ | — | — |
| Edit and submit own organizer | ✓ (until submitted) | — | — |
| Download own originals | ✓ (until submitted) | — | — |
| See client list | — | Assigned clients only | All clients |
| View a client's documents (60-second link) | — | Assigned clients only | ✓ |
| Request missing documents, add internal notes | — | Assigned clients only | ✓ |
| Update a client's status | — | Status field only, assigned clients | ✓ |
| Export to Excel / CSV | — | Assigned clients only | ✓ |
| Reset a client's MFA | — | — | ✓ (audited; staff targets refused) |
| Add staff and grant or revoke roles | — | — | ✓ (last admin protected) |
| Assign clients to preparers | — | — | ✓ |
| Delete originals, run purges, change settings and retention | — | — | ✓ |
| View the audit log | — | — | ✓ |

**Design principle:** a preparer gets nothing by default. Access comes only from an explicit, audited assignment by an admin (NIST AC-6; FTC Safeguards Rule 314.4(c)(1)).
