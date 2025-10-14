import json


def read_file(file_path, is_json=False):
    with open(file_path, "r") as f:
        return json.load(f) if is_json else f.read()


OM_METRICS = [
    # Qdrant Operator Cluster Metrics
    "qdrant_cloud.qdrant.operator.cluster.phase",
    "qdrant_cloud.qdrant.operator.cluster.pod.up.to.date",
    "qdrant_cloud.qdrant.operator.cluster.status.nodes",
    "qdrant_cloud.qdrant.operator.cluster.status.nodes.ready",
    "qdrant_cloud.qdrant.operator.cluster.info.total",
    
    # Qdrant Node Metrics
    "qdrant_cloud.qdrant.node.rssanon.bytes",
    
    # Container Metrics
    "qdrant_cloud.container.file.descriptors",
    "qdrant_cloud.container.network.receive.bytes.count",
    "qdrant_cloud.container.network.receive.packets.dropped.count",
    "qdrant_cloud.container.network.receive.packets.count",
    "qdrant_cloud.container.network.transmit.bytes.count",
    "qdrant_cloud.container.network.transmit.packets.dropped.count",
    "qdrant_cloud.container.network.transmit.packets.count",
    "qdrant_cloud.container.cpu.cfs.periods.count",
    "qdrant_cloud.container.cpu.cfs.throttled.periods.count",
    "qdrant_cloud.container.cpu.usage.seconds.count",
    "qdrant_cloud.container.fs.reads.bytes.count",
    "qdrant_cloud.container.fs.reads.count",
    "qdrant_cloud.container.fs.writes.bytes.count",
    "qdrant_cloud.container.fs.writes.count",
    "qdrant_cloud.container.memory.cache",
    "qdrant_cloud.container.memory.mapped.file",
    "qdrant_cloud.container.memory.rss",
    "qdrant_cloud.container.memory.working.set.bytes",
    
    # Kubernetes Metrics
    "qdrant_cloud.kube.pod.container.info",
    "qdrant_cloud.kube.pod.container.resource.limits",
    "qdrant_cloud.kube.pod.container.resource.requests",
    "qdrant_cloud.kube.pod.container.status.restarts.count",
    "qdrant_cloud.kube.pod.info",
    "qdrant_cloud.kube.pod.status.phase",
    "qdrant_cloud.kube.pod.status.ready",
    "qdrant_cloud.kube.pod.status.ready.time",
]
