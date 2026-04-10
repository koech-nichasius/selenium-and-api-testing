import pytest
import requests
from api_testing.api_data.api_test_data import api_test_data


@pytest.fixture(scope="class", autouse=True)
def session(request):
    """Create a shared requests session for the test class."""
    session = requests.Session()
    request.cls.session = session
    yield
    session.close()

@pytest.fixture(params=api_test_data, ids=lambda c: c.name)
def case(request):
    return request.param