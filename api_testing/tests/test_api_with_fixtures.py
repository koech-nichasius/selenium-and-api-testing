import pytest
import requests
from dataclasses import asdict
from api_testing.Api_data.objects_data import objects_data
from api_testing.common_functions.common_functions import end_point


@pytest.fixture(params=objects_data, ids=lambda c: c.name)
def case(request):
    return request.param

@pytest.fixture
def session():
    return requests.Session()

@pytest.fixture
def response(case, session):
    return session.get(end_point(case.id))

@pytest.fixture
def expected(case):
    return asdict(case)


def test_get_object_status_code(response, case):
    assert response.status_code == 200, (
        f"Unexpected status code for case '{case.name}'"
    )


def test_get_object_response_body(response, expected, case):
    assert response.headers.get("Content-Type", "").startswith("application/json")

    assert response.json() == expected, (
        f"Response body mismatch for case '{case.name}'"
    )

