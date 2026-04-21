from typing import Any, Dict


class UsersAPI:
    """This class implements API wrapper for user-related endpoints.
    All operations related to users are encapsulated and HTTP communication delegated
    to the provided API client.
    """

    def __init__(self, client):
        """Initialize the UsersAPI."""
        self.client = client

    def get_users(self, page: int = 1) -> Dict[str, Any]:
        """Retrieve a paginated list of users.
        Return response payload or status information from the get action"""
        return self.client.get("/users", params={"page": page})

    def get_user(self, user_id: int) -> Dict[str, Any]:
        """Retrieve a single user by ID.
        Return response payload or status information from the get action"""
        return self.client.get(f"/users/{user_id}")

    def create_user(self, payload: Dict[str, Any]) -> Dict[str, Any]:
        """Create a new user.
        Return response payload or status information from the post action"""
        return self.client.post("/users", json=payload)

    def delete_user(self, payload: Dict[str, Any]) -> Dict[str, Any]:
        """Delete a user.
        Return response payload or status information from the delete action"""
        return self.client.delete("/users", json=payload)