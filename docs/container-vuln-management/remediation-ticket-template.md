# Remediation Ticket Template

> Copy per finding. Fields marked *(auto)* are populated from scanner/CNAPP data.

| Field | Value |
| --- | --- |
| Ticket ID | `CVM-____` |
| Finding ID *(auto)* | |
| CVE(s) *(auto)* | |
| Affected image / workload *(auto)* | |
| Cluster / namespace *(auto)* | |
| Severity (CVSS) *(auto)* | |
| Exploitability (KEV / EPSS / public exploit) | |
| Reachability / attack path (CNAPP) | |
| Business criticality of owning service | |
| **Priority tier (P1–P4)** | |
| **SLA due date** | |
| Owning team (per RACI) | |
| Assigned owner | |

## Remediation

- **Fix type:** ☐ Rebuild on patched base image ☐ Upgrade dependency ☐ Remove package ☐ Config/mitigation ☐ Risk acceptance (→ SOP-04)
- **Action taken:**
- **Verification:** ☐ Rescan confirms closure — date: ______
- **MTTR (confirmation → verified fix):** ______ days

## Notes
- Do not close on owner assertion; closure requires a clean rescan.
