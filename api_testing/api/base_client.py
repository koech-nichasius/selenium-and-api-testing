import requests
from typing import Any
from requests import Response


class BaseClient:
    """
    This class defines the Base HTTP client responsible for sending requests to an API.
    Implements configuration such as headers, timeout, and session handling.
    It also exposes common HTTP methods.
    """

    def __init__(self, base_url: str, headers: dict, timeout: int = 10) -> None:
        """Initialize the BaseClient."""
        self.session = requests.Session()
        self.base_url = base_url
        self.headers = headers
        self.timeout = timeout

    def _request(self, method: str, endpoint: str, **kwargs: Any) -> Response:
        """Send an HTTP request using the configured session."""
        url = f"{self.base_url}{endpoint}"
        response = self.session.request(
            method=method,
            url=url,
            headers=self.headers,
            timeout=self.timeout,
            **kwargs
        )
        return response

    def get(self, endpoint: str, **kwargs: Any) -> Response:
        """Send a GET request."""
        return self._request("GET", endpoint, **kwargs)

    def post(self, endpoint: str, **kwargs: Any) -> Response:
        """Send a POST request. Return requests.Response` object"""
        return self._request("POST", endpoint, **kwargs)

    def put(self, endpoint: str, **kwargs: Any) -> Response:
        """Send a PUT request. Return requests.Response` object"""
        return self._request("PUT", endpoint, **kwargs)

    def delete(self, endpoint: str, **kwargs: Any) -> Response:
        """Send a DELETE request. Return requests.Response` object"""
        return self._request("DELETE", endpoint, **kwargs)
