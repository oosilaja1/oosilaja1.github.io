# RACI Matrix — Container Vulnerability Management

> Sanitized ownership model. Roles are generic. **R** = Responsible, **A** = Accountable, **C** = Consulted, **I** = Informed.

This matrix codifies the **KaaS (Kubernetes-as-a-Service) / Platform Team vs. Cluster Owner** split that is the single biggest driver of remediation accountability. Ambiguity here — not scanner accuracy — is what stalls most container programs.

## Roles

- **KaaS / Platform Team** — operates the cluster platform, admission control, and Kubernetes upgrades.
- **Cluster / Service Owner** — owns the workloads and images running in their namespace(s).
- **Container Security (this program)** — operates scanning, triage, prioritization, SLAs, and reporting.
- **GRC / Audit** — owns controls, ATO, POA&M, risk acceptance sign-off.
- **AppSec** — owns application-layer (SAST/DAST) findings.

## Matrix

| Activity | Container Security | KaaS / Platform | Cluster / Service Owner | GRC / Audit | AppSec |
| --- | --- | --- | --- | --- | --- |
| Operate scanners (image/registry/CI/CD/runtime) | **A/R** | C | I | I | I |
| Maintain admission-control policy | C | **A/R** | I | I | — |
| Coverage reconciliation (find shadow clusters) | **A/R** | C | I | I | — |
| Triage & risk-based prioritization | **A/R** | C | C | C | C |
| Remediate image / workload findings | C | C | **A/R** | I | C |
| Rebuild on patched base image | C | C | **A/R** | I | — |
| Kubernetes version / EOL upgrade | C | **A/R** | R | I | — |
| Verify remediation (rescan to close) | **A/R** | I | C | I | — |
| SLA tracking & escalation | **A/R** | C | R | I | — |
| Risk acceptance / exception approval | C | I | R | **A/R** | — |
| POA&M entry & control-mapped evidence | R | I | I | **A/R** | I |
| Executive & audit reporting | **A/R** | C | I | C | I |
| App-layer (SAST/DAST) findings | I | — | C | I | **A/R** |

## Principle

**One Accountable per row.** If more than one party believes they are accountable for remediation, none are — which is exactly the gap this matrix closes. Container Security is accountable for the *process* (find, prioritize, track, verify, report); owners are accountable for the *fix*.
