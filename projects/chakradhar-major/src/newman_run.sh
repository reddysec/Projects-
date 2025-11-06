#!/bin/bash
COLLECTION="src/postman_collection.json"
REPORT_DIR="deliverables/newman_reports"

mkdir -p "$REPORT_DIR"

echo "[+] Running Postman collection via Newman..."
newman run "$COLLECTION" --reporters cli,html,json \
  --reporter-html-export "$REPORT_DIR/newman_report.html" \
  --reporter-json-export "$REPORT_DIR/newman_report.json"

echo "[+] Newman run complete. Reports saved in $REPORT_DIR"
