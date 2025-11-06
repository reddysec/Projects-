\# API Security Testing Framework



\*\*Author:\*\* Yeddula Chakradhar Reddy



\## What



Focused API security testing framework that combines functional API validation (\*\*Postman → Newman\*\*) with automated vulnerability scanning (\*\*OWASP ZAP\*\*) in a reproducible, CI-friendly pipeline.



\*\*Purpose:\*\* Identify and validate API security weaknesses (based on OWASP API Security Top 10) in a safe, controlled environment.



\*\*Demo target:\*\* `https://reqres.in` (public test API)



---



\## Quick start (deploy \& run)



1\. Ensure Docker, Node/npm, and Python 3 are installed and running.



2\. Pull \& run OWASP ZAP in daemon mode:



&nbsp;  ```bash

&nbsp;  docker pull ghcr.io/zaproxy/zaproxy:stable

&nbsp;  docker run --rm -u zap -d -p 8080:8080 --name zap-scanner \\

&nbsp;    ghcr.io/zaproxy/zaproxy:stable \\

&nbsp;    zap.sh -daemon -host 0.0.0.0 -port 8080 \\

&nbsp;    -config api.disablekey=true \\

&nbsp;    -config api.addrs.addr.name=.\* \\

&nbsp;    -config api.addrs.addr.regex=true

&nbsp;  ```



3\. Create a Python virtual environment and install dependencies:



&nbsp;  ```bash

&nbsp;  python3 -m venv .venv

&nbsp;  source .venv/bin/activate

&nbsp;  pip install python-owasp-zap-v2.4 requests

&nbsp;  ```



4\. Install Newman (Postman CLI):



&nbsp;  ```bash

&nbsp;  sudo npm install -g newman

&nbsp;  ```



5\. Run the orchestrator to execute the full functional + security scan:



&nbsp;  ```bash

&nbsp;  ./src/orchestrate\_scan.sh

&nbsp;  ```



6\. Open the generated reports under `deliverables/` (e.g., `deliverables/newman\_reports/`, `deliverables/zap\_reports/`).



\*\*Note:\*\* This framework is intended only for authorized testing on permitted or demo targets. Do not scan production systems.



---



\## Tools used



\* \*\*OWASP ZAP\*\* (containerized) — spidering, passive and active scanning

\* \*\*Postman + Newman\*\* — functional API test execution

\* \*\*Python 3 + python-owasp-zap-v2.4\*\* — programmatic orchestration (`src/zap\_scan.py`)

\* \*\*Docker\*\* — reproducible runtime for ZAP

\* \*\*jq, git, Firefox/xdg-open\*\* — utilities for parsing and reviewing results



---



\## What I tested (high level)



\* \*\*Reconnaissance:\*\* Spider/crawl to discover API endpoints

\* \*\*Functional validation:\*\* Verified expected responses via Newman test collection

\* \*\*Passive analysis:\*\* Checked for missing headers and information leakage

\* \*\*Active scanning:\*\* Parameter fuzzing and injection detection (e.g., XSS, SQLi-like checks)

\* \*\*Orchestration:\*\* Full automated workflow producing structured JSON + HTML reports



---



\## Important findings (summary)



\* \*\*Missing security headers \& weak server configuration\*\* — flagged by ZAP passive scans

\* \*\*Verbose responses / information disclosure\*\* — excessive details in API responses

\* \*\*API misconfigurations\*\* — insecure behavior consistent with OWASP API Security Top 10 findings



> Note: All results are from the demo API (`https://reqres.in`) in a controlled test environment.



---



\## Test artifacts



\* `deliverables/newman\_reports/newman\_report.html` — functional test summary

\* `deliverables/newman\_reports/newman\_report.json` — structured test output

\* `deliverables/zap\_reports/zap\_report.html` — ZAP vulnerability report

\* `deliverables/zap\_reports/zap\_report.json` — machine-readable ZAP results



All artifacts are safe, reproducible, and demonstrate proof of concept in a controlled lab.



---



\## Safe-testing notes



\* All testing was performed \*\*non-destructively\*\* against the public demo API (`https://reqres.in`).

\* No production or unauthorized targets were scanned.

\* Only benign payloads were used to demonstrate proof-of-concept impact.



---



\## Next steps / enhancements



1\. Add authenticated scanning (ZAP contexts / token handling)

2\. Integrate into CI/CD pipelines (GitHub Actions / GitLab / Jenkins)

3\. Automate remediation checklist generation from `zap\_report.json`

4\. Add `.env` support and visual dashboards (Grafana / Allure)



---



\## Conclusion



The API Security Testing Framework successfully integrates \*\*functional\*\* (Postman/Newman) and \*\*security\*\* (OWASP ZAP) testing into one repeatable pipeline.

It highlights OWASP API-Security–relevant issues (missing headers, information leakage, misconfigurations) and demonstrates a scalable model for DevSecOps adoption.



---



\## References



\* OWASP ZAP documentation

\* OWASP API Security Top 10 (2023)

\* Postman \& Newman documentation

\* Python OWASP ZAP API (`python-owasp-zap-v2.4`)



