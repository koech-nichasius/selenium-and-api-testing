import pytest
import requests
from dataclasses import asdict
from api_testing.api_data.api_test_data import api_test_data
from api_testing.common_functions.common_api_functions import end_point


@pytest.fixture(params=api_test_data, ids=lambda c: c.name)
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

