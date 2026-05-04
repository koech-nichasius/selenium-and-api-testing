from api_testing.api_data.api_test_data import StatusCodes, UserTestData
from api_testing.utils.assertions import assert_status_code

class TestUsers:
    """"Test set for user related verifications."""
    def test_get_users(self, users_api):
        """Test retrieve a single page of users."""
        response = users_api.get_users(page=1)
        assert_status_code(response=response, expected=StatusCodes.OK)
        data = response.json()
        assert "data" in data
        assert len(data["data"]) > 0
    
    def test_get_single_user(self, users_api):
        """Test single user retrieval."""
        response = users_api.get_user(user_id=2)
        assert_status_code(response=response, expected=StatusCodes.OK)
        assert response.json()["data"]["id"] == 2
    
    def test_create_user(self, users_api):
        """Test valid user creation."""
        response = users_api.create_user(payload=UserTestData.valid_user_payload)
        assert_status_code(response=response,expected=StatusCodes.Created)
    
        body = response.json()
        assert body["name"].strip() == "Nichasius"
        assert "id" in body
    
    def test_delete_user(self, users_api):
        """Test User deletion."""
        response = users_api.delete_user(payload=UserTestData.valid_user_payload)
        assert_status_code(response=response,expected=StatusCodes.Deleted)
    
    def test_create_invalid_user(self, users_api):
        """Test Invalid request to create user."""
        response = users_api.create_user(payload=UserTestData.invalid_user_payload)
        assert_status_code(response=response, expected=StatusCodes.BadRequest)
        body = response.json()
        assert "error" in body
