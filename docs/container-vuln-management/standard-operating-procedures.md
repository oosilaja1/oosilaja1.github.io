# Standard Operating Procedures (SOP Suite)

> Sanitized reference SOPs. Generic steps only — no employer-internal systems, data, or configurations.

These SOPs operationalize the [handbook](aqua-vulnerability-management-handbook.md). Each is intentionally short and executable.

---

## SOP-01 — Image Scanning & Coverage

**Trigger:** every CI/CD build; continuous registry rescans; weekly coverage reconciliation.

1. On build, the pipeline invokes the scanner against the image (all layers + base image).
2. If findings exceed the build gate (e.g., any unremediated P1, or > threshold criticals), **fail the build** and return findings to the developer.
3. Push passing images to the registry; registry continuously rescans for newly disclosed CVEs.
4. **Coverage reconciliation:** weekly, diff cluster inventory against scanned inventory. Any cluster/workload not under scanning is logged as a **coverage gap** and routed to SOP-06 for onboarding.

**Output:** scan results in the platform; coverage-gap list.

---

## SOP-02 — Triage & Risk-Based Prioritization

**Trigger:** new findings surfaced.

1. De-duplicate findings across image/registry/runtime for the same workload.
2. Enrich each finding: KEV / exploit availability, EPSS, CNAPP reachability & attack-path, workload business criticality.
3. Compute priority per the handbook §5 model. Elevate confirmed attack-path / toxic-combination findings above standalone CVEs.
4. Assign a priority tier (P1–P4) and the corresponding SLA.

**Output:** ranked remediation queue with tiers and SLA clocks started.

---

## SOP-03 — Remediation & Ownership Routing

**Trigger:** prioritized finding assigned.

1. Route the finding to the owning team per the RACI (cluster owner vs KaaS team).
2. Create a remediation ticket using `templates/remediation-ticket-template.md`.
3. Owner remediates (rebuild on patched base image, upgrade dependency, remove package, or apply mitigation).
4. **Verify:** rescan confirms closure. Do **not** close on owner assertion alone.
5. Record MTTR (confirmation → verified fix).

**Output:** verified-closed finding; MTTR data point.

---

## SOP-04 — Exceptions & Risk Acceptance

**Trigger:** finding cannot be remediated within SLA.

1. Owner submits a risk acceptance using `templates/risk-acceptance-template.md`.
2. Document compensating controls, residual risk, and a **hard expiry date**.
3. GRC reviews and signs off; record as a POA&M item where applicable.
4. Track to expiry — on expiry, the finding re-enters the active queue automatically.

**Output:** time-boxed, signed exception; POA&M entry.

---

## SOP-05 — Runtime Detection & Response

**Trigger:** runtime alert (drift, anomalous behavior, newly vulnerable running image).

1. Validate the alert against baseline; suppress known-good drift.
2. For confirmed issues, assess blast radius using CNAPP context.
3. For active exploitation, invoke incident response; otherwise route to SOP-03 as a P1.

**Output:** contained runtime issue or IR handoff.

---

## SOP-06 — Cluster Onboarding & EOL Upgrade

**Trigger:** coverage gap (SOP-01) or EOL/near-EOL cluster detected.

1. Onboard the cluster into scanning and admission control; establish a baseline scan.
2. For EOL versions, engage the owner with an SLA-tracked upgrade plan.
3. Track version-compliance % to the estate target (see companion tracker).

**Output:** cluster under continuous scanning; version-compliance updated.

---

## SOP-07 — Metrics & Executive Reporting

**Trigger:** reporting cadence (e.g., weekly ops, monthly leadership).

1. Refresh MTTR (P1/P2 trend), critical/high exposure, coverage %, version-compliance %, and open exceptions.
2. Present control-aligned so the same figures serve standups and audit/ATO.
3. Flag SLA breaches and aging exceptions for escalation.

**Output:** executive dashboard + ops report.
