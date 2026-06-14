import requests
import json

PROM_URL = "http://localhost:9090/api/v1/query"

query = "container_memory_usage_bytes"

response = requests.get(
    PROM_URL,
    params={"query": query}
)

print(json.dumps(response.json(), indent=2))