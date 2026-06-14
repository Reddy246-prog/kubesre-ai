import requests
import json

url = "http://localhost:9090/api/v1/query"

query = "kube_pod_container_status_restarts_total"

response = requests.get(
    url,
    params={"query": query}
)

data = response.json()

print(json.dumps(data, indent=2))