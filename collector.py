from kubernetes import client, config
from rich import print

config.load_kube_config()

v1 = client.CoreV1Api()

pods = v1.list_pod_for_all_namespaces()

print("\n=== POD REPORT ===\n")

for pod in pods.items:
    print(
        f"[green]{pod.metadata.namespace}[/green] "
        f"{pod.metadata.name} "
        f"{pod.status.phase}"
    )