import requests

PROM_URL = "http://localhost:9090/api/v1/query"

def get_memory_usage():

    query = "container_memory_usage_bytes"

    response = requests.get(
        PROM_URL,
        params={"query": query}
    )

    data = response.json()

    memory_map = {}

    for item in data["data"]["result"]:

        pod_name = item["metric"].get("pod")

        memory_bytes = int(float(item["value"][1]))

        memory_map[pod_name] = memory_bytes

    return memory_map