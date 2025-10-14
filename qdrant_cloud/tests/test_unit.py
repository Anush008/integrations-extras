
import pytest

from datadog_checks.qdrant_cloud import QdrantCloudCheck


def test_empty_instance(dd_run_check):
    with pytest.raises(
        Exception,
        match="InstanceConfig`:\nopenmetrics_endpoint\n  Field required",
    ):
        check = QdrantCloudCheck("qdrant_cloud", {}, [{}])
        dd_run_check(check)


def test_invalid_instance(dd_run_check):
    with pytest.raises(
        Exception,
        match="InstanceConfig`:\nopenmetrics_endpoint\n  Field required",
    ):
        check = QdrantCloudCheck("qdrant_cloud", {}, [{"invalid": "config"}])
        dd_run_check(check)
