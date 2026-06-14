import requests

PROM_URL = "http://localhost:9090/api/v1/query"

def get_restart_counts():

    query = "kube_pod_container_status_restarts_total"

    response = requests.get(
        PROM_URL,
        params={"query": query}
    )

    data = response.json()

    restart_map = {}

    for item in data["data"]["result"]:

        pod_name = item["metric"].get("pod")

        restart_count = int(float(item["value"][1]))

        restart_map[pod_name] = restart_count

    return restart_map