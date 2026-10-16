# FedRAMP Notes — Container Vulnerability Management

> Sanitized reference notes. FedRAMP builds on the NIST 800-53 baseline; these notes highlight the container-specific expectations relevant to an authorization.

## Baseline

FedRAMP inherits the NIST 800-53 control set (see [`nist-800-53-crosswalk.md`](nist-800-53-crosswalk.md)). The controls most scrutinized for container workloads are **RA-5**, **SI-2**, **CM-2/6/7/8**, **SA-11**, **SI-7**, and **CA-7**.

## Container-specific expectations

| Area | FedRAMP expectation | How the program meets it |
| --- | --- | --- |
| **Scan frequency (RA-5)** | Operating-system, web, and database scanning at defined frequencies (commonly monthly), plus scanning on significant change. | Continuous registry rescans + build-time scans exceed the minimum; coverage % is evidenced. |
| **Remediation timelines (RA-5 / SI-2)** | High within 30 days, Moderate within 90 days, Low within 180 days (standard FedRAMP timeframes). | SLA tiers are set at or inside these bounds; MTTR is tracked and reported. |
| **Vulnerability deviation requests** | Deviations (false positive, operational requirement, risk adjustment) must be formally requested and approved. | Handled through the time-boxed risk-acceptance / exception process and POA&M. |
| **POA&M (CA-5)** | Open findings past SLA tracked on the POA&M with milestones. | §14 POA&M integration; exceptions auto-reopen on expiry. |
| **Inventory (CM-8)** | Complete, current inventory of system components. | Coverage reconciliation detects shadow clusters; inventory kept current. |
| **Container image provenance (SI-7)** | Integrity of deployed images. | Image signing + admission control block unsigned/unscanned images. |

## Continuous monitoring

FedRAMP ConMon expects monthly evidence packages. The program's metrics (MTTR, exposure trend, coverage %, version-compliance %) are structured to drop directly into a monthly ConMon submission.

> These notes are illustrative and generic; confirm current FedRAMP timeframes and requirements against the authoritative FedRAMP documentation for any real authorization.
