from kubernetes import client, config

# Load kubeconfig
config.load_kube_config()

# Create API client
v1 = client.CoreV1Api()

# Get events from default namespace
events = v1.list_namespaced_event("default")

print("\n=== EVENTS ===\n")

for event in events.items:
    print(f"Reason: {event.reason}")
    print(f"Message: {event.message}")
    print("-" * 50)