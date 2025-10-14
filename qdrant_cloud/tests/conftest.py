
import os

import mock
import pytest

from datadog_checks.dev import get_here
from tests.common import read_file

HERE = get_here()

CHECK = "qdrant_cloud"
ENDPOINT = "https://xyz-example.cloud-region.cloud-provider.cloud.qdrant.io:6333/sys_metrics"


@pytest.fixture(scope="session")
def dd_environment():
    instances = {"instances": [{"openmetrics_endpoint": ENDPOINT}]}

    yield instances


@pytest.fixture(scope="session")
def instance():
    return {"openmetrics_endpoint": ENDPOINT, "tags": ["instance"]}


@pytest.fixture(autouse=True, scope="function")
def mock_http_response():
    file_paths = {
        "metrics": os.path.join(HERE, "data", "metrics.txt"),
        "version": os.path.join(HERE, "data", "version.json"),
        "readyz": os.path.join(HERE, "data", "readyz.txt"),
        "livez": os.path.join(HERE, "data", "livez.txt"),
    }

    text_data = read_file(file_paths["metrics"])
    version_data = read_file(file_paths["version"], is_json=True)
    readyz_data = read_file(file_paths["readyz"])
    livez_data = read_file(file_paths["livez"])

    with mock.patch("requests.Session.request") as mock_request:
        def mock_session_request(method, url, *args, **kwargs):
            if url.endswith("/sys_metrics"):
                return mock.MagicMock(
                    status_code=200,
                    iter_lines=lambda **kwargs: text_data.split("\n"),
                    headers={"Content-Type": "text/plain"},
                )
            elif url.endswith("/readyz"):
                return mock.MagicMock(
                    status_code=200,
                    iter_lines=lambda **kwargs: readyz_data.split("\n"),
                    headers={"Content-Type": "text/plain"},
                )
            elif url.endswith("/livez"):
                return mock.MagicMock(
                    status_code=200,
                    iter_lines=lambda **kwargs: livez_data.split("\n"),
                    headers={"Content-Type": "text/plain"},
                )
            elif url.endswith("/"):
                return mock.MagicMock(
                    status_code=200,
                    json=lambda: version_data,
                    headers={"Content-Type": "application/json"},
                )
            else:
                # Return the actual requests.get for other URLs
                return mock.MagicMock(
                    status_code=400,
                    headers={"Content-Type": "text/plain"},
                )
        
        mock_request.side_effect = mock_session_request
        yield
