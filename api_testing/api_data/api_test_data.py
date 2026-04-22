"""This module contains data definitions for testing API."""
from typing import Any
from dataclasses import dataclass

@dataclass(frozen=True)
class StatusCodes:
    """This class defines API Test data."""
    OK: int = 200
    Created: int = 201
    Accepted: int = 202
    Deleted: int = 204
    Bad_Request: int = 400


@dataclass(frozen=True)
class TestUser:
    """This class defines API Test data."""
    valid_payload = {
         "name": "Nichasius",
        "job": "QA Engineer"}
    invalid_payload = ""
