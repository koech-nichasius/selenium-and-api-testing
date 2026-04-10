"""This module contains common functions for API Testing."""
from api_testing.api_data.api_test_data import ApiTestData

def end_point(id:int)-> str:
    """Return resource from endpoint."""
    return f"{ApiTestData.base_url}objects/{id}"

