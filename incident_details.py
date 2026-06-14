from kubernetes import client, config
import json
from datetime import datetime
from prometheus_metrics import get_restart_counts
from prometheus_memory import get_memory_usage

# Load Kubernetes config
config.load_kube_config()

# Create Kubernetes API client
v1 = client.CoreV1Api()

# Get restart counts from Prometheus
restart_map = get_restart_counts()
memory_map = get_memory_usage()

# Get all pods in default namespace
pods = v1.list_namespaced_pod("default")

# Store all incidents
incidents = []

for pod in pods.items:

    # Default status
    status = pod.status.phase

    # Get actual container state if available
    if pod.status.container_statuses:
        container = pod.status.container_statuses[0]

        if container.state.waiting:
            status = container.state.waiting.reason

    # Only collect failed/non-running pods
    if status != "Running":

        # Get logs
        try:
            logs = v1.read_namespaced_pod_log(
                pod.metadata.name,
                "default",
                tail_lines=20
            )

            if isinstance(logs, bytes):
                logs = logs.decode("utf-8")

        except Exception:
            logs = "No logs available"

        # Get events
        events = v1.list_namespaced_event("default")

        pod_events = []

        for event in events.items:
            if event.involved_object.name == pod.metadata.name:
                pod_events.append({
                    "reason": event.reason,
                    "message": event.message
                })

        # Create incident object
        incidents.append({
            "namespace": pod.metadata.namespace,
            "node": pod.spec.node_name,
            "pod": pod.metadata.name,
            "status": status,
            "collected_at": datetime.utcnow().isoformat(),
            "restart_count": restart_map.get(
                pod.metadata.name,
                0
            ),
            "memory_bytes": memory_map.get(
               pod.metadata.name,
               0
             ),

            "logs": logs,
            "events": pod_events
        })

# Save incidents to file
with open("incidents.json", "w") as f:
    json.dump(incidents, f, indent=2)

print(f"Found {len(incidents)} incidents")
print("incidents.json created successfully")