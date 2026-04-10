from dataclasses import asdict
from api_testing.common_functions.common_functions import end_point

class TestApi:

    def get_object(self, case):
        """Helper method to fetch an object by case."""
        return self.session.get(end_point(case.id))

    def test_get_object_status_code(self, case):
        response = self.get_object(case)
        assert response.status_code == 200, (
            f"Unexpected status code for case '{case.name}'"
        )

    def test_get_object_response_body(self, case):
        response = self.get_object(case)
        assert response.headers["Content-Type"].startswith(
            "application/json"
        )
        assert response.json() == asdict(case), (
            f"Response body mismatch for case '{case.name}'"
        )