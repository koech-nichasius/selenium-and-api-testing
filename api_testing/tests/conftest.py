import os
from pathlib import Path

import yaml
import pytest

from api_testing.api.base_client import BaseClient
from api_testing.api.products_api import ProductsAPI
from api_testing.api.users_api import UsersAPI

@pytest.fixture(scope="session")
def reqres_headers():
    api_key = os.getenv("REQRES_API_KEY")
    assert api_key, "REQRES_API_KEY env variable is not set"

    return {
        "x-api-key": api_key,
        "Content-Type": "application/json",
        "User-Agent": "pytest-api-tests/1.0"
    }

@pytest.fixture(scope="session")
def config():
    config_path = Path(__file__).parent.parent / "config/config.yaml"
    with config_path.open(encoding="utf-8") as f:
        return yaml.safe_load(f)

@pytest.fixture(scope="session")
def api_client(config, reqres_headers):
    return BaseClient(
        base_url=config["base_url"],
        timeout=config["timeout"],
        headers = reqres_headers)


@pytest.fixture
def users_api(api_client):
    """Client here is a BaseClient object."""
    return UsersAPI(api_client)

@pytest.fixture
def products_api(api_client):
    """Client here is a BaseClient object."""
    return ProductsAPI(api_client)