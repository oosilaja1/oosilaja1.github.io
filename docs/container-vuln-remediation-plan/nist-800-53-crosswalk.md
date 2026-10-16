# NIST 800-53 (Rev. 5) Crosswalk — Container Vulnerability Management

> Sanitized reference crosswalk. Maps container VM program activities to NIST SP 800-53 controls for audit/ATO evidence.

| Program activity | Control | Control name | Evidence produced |
| --- | --- | --- | --- |
| Image/registry/CI-CD/runtime scanning | **RA-5** | Vulnerability Monitoring & Scanning | Scan schedules, coverage %, scan reports |
| Risk-based prioritization | **RA-5(2)**, **RA-3** | Update frequency / Risk Assessment | Prioritization methodology, exploitability enrichment |
| Flaw remediation & MTTR | **SI-2** | Flaw Remediation | Remediation tickets, verified-close rescans, MTTR metrics |
| Automated remediation tracking | **SI-2(2)** | Automated Flaw Remediation Status | Dashboards, SLA tracking |
| Baseline configuration | **CM-2** | Baseline Configuration | Approved base images, admission policy |
| Configuration settings | **CM-6** | Configuration Settings | Hardening/benchmarks, policy-as-code |
| System component inventory | **CM-8** | System Component Inventory | Cluster/workload inventory, coverage reconciliation |
| Least functionality | **CM-7** | Least Functionality | Removed packages, minimal base images |
| Developer testing (shift-left) | **SA-11** | Developer Testing & Evaluation | CI/CD scan gates, build-fail evidence |
| Development process | **SA-15** | Development Process, Standards & Tools | Pipeline security controls |
| Malicious code / runtime | **SI-3** | Malicious Code Protection | Runtime protection config & alerts |
| Software/firmware integrity | **SI-7** | Software, Firmware & Information Integrity | Image signing, admission control, drift detection |
| Continuous monitoring | **CA-7** | Continuous Monitoring | ConMon cadence, continuous rescans |
| POA&M | **CA-5** | Plan of Action & Milestones | POA&M entries from open/accepted findings |
| Risk acceptance governance | **PM-4** | POA&M Process | Exception records, GRC sign-off |
| Boundary/exposure context | **SC-7** | Boundary Protection | Attack-path/exposure analysis inputs |
