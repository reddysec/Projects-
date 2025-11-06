#!/usr/bin/env python3
import os, time, argparse
from zapv2 import ZAPv2

def wait_for_passive(zap):
    while int(zap.pscan.records_to_scan) > 0:
        print("Passive records remaining:", zap.pscan.records_to_scan)
        time.sleep(1)

def main():
    p = argparse.ArgumentParser()
    p.add_argument('--target', required=True, help='Target base URL')
    p.add_argument('--zap-api-key', default='', help='ZAP API key (if set)')
    p.add_argument('--zap-proxy', default='http://127.0.0.1:8080', help='ZAP proxy base')
    p.add_argument('--reportdir', default='deliverables/zap_reports', help='Output dir')
    args = p.parse_args()

    outdir = os.path.abspath(args.reportdir)
    os.makedirs(outdir, exist_ok=True)

    zap = ZAPv2(apikey=args.zap_api_key, proxies={'http': args.zap_proxy, 'https': args.zap_proxy})
    target = args.target.rstrip('/')

    print("Opening target:", target)
    zap.urlopen(target)
    time.sleep(2)

    print("Starting spider...")
    sid = zap.spider.scan(target)
    while int(zap.spider.status(sid)) < 100:
        print("Spider %:", zap.spider.status(sid))
        time.sleep(2)

    print("Waiting for passive scan to finish...")
    wait_for_passive(zap)

    print("Starting active scan...")
    aid = zap.ascan.scan(target)
    while int(zap.ascan.status(aid)) < 100:
        print("Active scan %:", zap.ascan.status(aid))
        time.sleep(5)

    print("Generating reports...")
    html = zap.core.htmlreport()
    js   = zap.core.jsonreport()

    with open(os.path.join(outdir,'zap_report.html'),'w',encoding='utf-8') as f:
        f.write(html)
    with open(os.path.join(outdir,'zap_report.json'),'w',encoding='utf-8') as f:
        f.write(js)

    print("Reports saved to:", outdir)

if __name__ == '__main__':
    main()
