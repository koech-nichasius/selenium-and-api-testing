import os
import yaml
import pytest
from api.base_client import BaseClient
from api.users_api import UsersAPI

@pytest.fixture(scope="session")
def base_url():
    return "https://reqres.in"

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
    with open("api_testing/config/config.yaml") as f:
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


