import pytest
import requests

from api_testing.Api_data.objects_data import objects_data


@pytest.fixture(scope="class", autouse=True)
def session(request):
    """Create a shared requests session for the test class."""
    session = requests.Session()
    request.cls.session = session
    yield session
    session.close()

@pytest.fixture(params=objects_data, ids=lambda c: c.name)
def case(request):
    return request.param