DEFAULT_METRICS = {
    # Qdrant Operator Cluster Metrics
    "qdrant_operator_cluster_phase": {"name": "qdrant.operator.cluster.phase", "type": "gauge"},
    "qdrant_operator_cluster_pod_up_to_date": {"name": "qdrant.operator.cluster.pod.up.to.date", "type": "gauge"},
    "qdrant_operator_cluster_status_nodes": {"name": "qdrant.operator.cluster.status.nodes", "type": "gauge"},
    "qdrant_operator_cluster_status_nodes_ready": {"name": "qdrant.operator.cluster.status.nodes.ready", "type": "gauge"},
    "qdrant_operator_cluster_info_total": {"name": "qdrant.operator.cluster.info.total", "type": "gauge"},
    
    # Qdrant Node Metrics
    "qdrant_node_rssanon_bytes": {"name": "qdrant.node.rssanon.bytes", "type": "gauge"},
    
    # Container Metrics
    "container_file_descriptors": {"name": "container.file.descriptors", "type": "gauge"},
    "container_network_receive_bytes_total": {"name": "container.network.receive.bytes", "type": "counter"},
    "container_network_receive_packets_dropped_total": {"name": "container.network.receive.packets.dropped", "type": "counter"},
    "container_network_receive_packets_total": {"name": "container.network.receive.packets", "type": "counter"},
    "container_network_transmit_bytes_total": {"name": "container.network.transmit.bytes", "type": "counter"},
    "container_network_transmit_packets_dropped_total": {"name": "container.network.transmit.packets.dropped", "type": "counter"},
    "container_network_transmit_packets_total": {"name": "container.network.transmit.packets", "type": "counter"},
    "container_cpu_cfs_periods_total": {"name": "container.cpu.cfs.periods", "type": "counter"},
    "container_cpu_cfs_throttled_periods_total": {"name": "container.cpu.cfs.throttled.periods", "type": "counter"},
    "container_cpu_usage_seconds_total": {"name": "container.cpu.usage.seconds", "type": "counter"},
    "container_fs_reads_bytes_total": {"name": "container.fs.reads.bytes", "type": "counter"},
    "container_fs_reads_total": {"name": "container.fs.reads", "type": "counter"},
    "container_fs_writes_bytes_total": {"name": "container.fs.writes.bytes", "type": "counter"},
    "container_fs_writes_total": {"name": "container.fs.writes", "type": "counter"},
    "container_memory_cache": {"name": "container.memory.cache", "type": "gauge"},
    "container_memory_mapped_file": {"name": "container.memory.mapped.file", "type": "gauge"},
    "container_memory_rss": {"name": "container.memory.rss", "type": "gauge"},
    "container_memory_working_set_bytes": {"name": "container.memory.working.set.bytes", "type": "gauge"},
    
    # Kubernetes Metrics
    "kube_pod_container_info": {"name": "kube.pod.container.info", "type": "gauge"},
    "kube_pod_container_resource_limits": {"name": "kube.pod.container.resource.limits", "type": "gauge"},
    "kube_pod_container_resource_requests": {"name": "kube.pod.container.resource.requests", "type": "gauge"},
    "kube_pod_container_status_restarts_total": {"name": "kube.pod.container.status.restarts", "type": "counter"},
    "kube_pod_info": {"name": "kube.pod.info", "type": "gauge"},
    "kube_pod_status_phase": {"name": "kube.pod.status.phase", "type": "gauge"},
    "kube_pod_status_ready": {"name": "kube.pod.status.ready", "type": "gauge"},
    "kube_pod_status_ready_time": {"name": "kube.pod.status.ready.time", "type": "gauge"},
}
