import json
from openai import OpenAI

client = OpenAI(
    api_key="YOUR_API_KEY",
    base_url="https://openrouter.ai/api/v1"
)

with open("incidents.json", "r") as f:
    incidents = json.load(f)

for incident in incidents:

    prompt = f"""
Analyze this Kubernetes incident.

Pod: {incident['pod']}
Namespace: {incident['namespace']}
Status: {incident['status']}

Restart Count:
{incident['restart_count']}

Memory Usage (Bytes):
{incident['memory_bytes']}

Logs:
{incident['logs']}

Events:
{incident['events']}

Provide:

1. Root Cause
2. Severity (P1/P2/P3)
3. Evidence
4. Recommended Fix
5. Business Impact
"""

    response = client.chat.completions.create(
        model="openai/gpt-4o-mini",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    print("\n" + "=" * 60)
    print(f"Pod: {incident['pod']}")
    print(response.choices[0].message.content)