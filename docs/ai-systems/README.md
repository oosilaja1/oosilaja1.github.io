# AI Systems — Overview

AI systems built for vulnerability management and AI governance.

| System | What it does | Status |
|---|---|---|
| **ExploitLens** | Merges scanner exports (AquaSec, Kubescape, Qualys, Tenable, Trivy, Wiz), enriches CVEs with NVD, CISA KEV and EPSS, and returns an exploitability verdict, priority, SLA and remediation | Live |
| **AI Readiness Advisor** | Microsoft Copilot Studio agent that scores Microsoft 365 Copilot readiness and maps gaps to NIST 800-53 and the NIST AI RMF | Prototype |
| **VM AI Prompt Library** | Seven guarded prompt templates that reframe one finding for each audience | Complete |

**Links**

- Interactive page with screenshots and live demos: [AI Systems](../../ai-systems.html)
- ExploitLens (live app): https://exploitlens.myprovenacademy.com
- Full write-up: [CASE-STUDY.md](CASE-STUDY.md)

**Design principles:** grounded in named sources · explainable verdicts · human-in-the-loop · least privilege · audit trail.
