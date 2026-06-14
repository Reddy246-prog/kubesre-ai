import json

with open("incidents.json", "r") as f:
    incidents = json.load(f)

for incident in incidents:

    status = incident["status"]

    if status == "ImagePullBackOff":
        root_cause = "Container image could not be pulled"
        severity = "P2"
        fix = "Verify image name, tag and registry access"

    elif status == "CrashLoopBackOff":
        root_cause = "Application is repeatedly crashing"
        severity = "P1"
        fix = "Inspect application logs and startup configuration"

    else:
        root_cause = "Unknown"
        severity = "Unknown"
        fix = "Investigate manually"

    print("\n" + "=" * 50)

    print(f"Pod: {incident['pod']}")
    print(f"Status: {status}")
    print(f"Root Cause: {root_cause}")
    print(f"Severity: {severity}")
    print(f"Fix: {fix}")