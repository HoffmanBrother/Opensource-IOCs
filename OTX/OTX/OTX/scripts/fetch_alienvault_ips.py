from OTXv2 import OTXv2
import os
import csv

API_KEY = os.getenv("OTX_API_KEY")
otx = OTXv2(b6af396d80a486f2fe219a83682ecc54722edb0360b44ddb0b31c534fd42ec46)

pulses = otx.getall()
ips = []

for pulse in pulses:
    for indicator in pulse['indicators']:
        if indicator['type'] == 'IPv4':
            ips.append([
                "IpAddress",
                indicator['indicator'],
                "Alert",
                "Medium",
                pulse['name'][:50],
                pulse.get('description', '')[:100]
            ])

os.makedirs("OTX", exist_ok=True)

with open("OTX/alienvault_ipv4.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["IndicatorType", "IndicatorValue", "Action", "Severity", "Title", "Description"])
    writer.writerows(ips)
