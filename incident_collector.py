from kubernetes import client, config
import json

config.load_kube_config()
v1 = client.CoreV1Api()

pods = v1.list_namespaced_pod("default")

incidents = []

for pod in pods.items:

    status = pod.status.phase

    if pod.status.container_statuses:
        container = pod.status.container_statuses[0]

        if container.state.waiting:
            status = container.state.waiting.reason

    incidents.append({
        "pod": pod.metadata.name,
        "status": status
    })

print(json.dumps(incidents, indent=2))