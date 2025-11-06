#!/bin/bash
# 1. Start ZAP
echo "[+] Starting ZAP in daemon mode..."
docker run --rm -u zap -d -p 8080:8080 --name zap-scanner \
  ghcr.io/zaproxy/zaproxy:stable \
  zap.sh -daemon -host 0.0.0.0 -port 8080 \
  -config api.disablekey=true \
  -config api.addrs.addr.name=.* \
  -config api.addrs.addr.regex=true

sleep 15

# 2. Run Newman collection (functional API tests)
echo "[+] Running Postman collection via Newman..."
bash src/newman_run.sh

# 3. Run ZAP automated scan
echo "[+] Running OWASP ZAP active scan..."
python3 src/zap_scan.py --target https://reqres.in --reportdir deliverables/zap_reports

# 4. Stop ZAP
echo "[+] Stopping ZAP container..."
docker stop zap-scanner

echo "[+] Combined API test & security scan complete!"
