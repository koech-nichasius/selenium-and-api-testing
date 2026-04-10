"""This module contains data definitions for testing API."""
from typing import Any
from dataclasses import dataclass

@dataclass(frozen=True)
class ApiTestData:
    """This class defines API Test data."""
    id: str
    name: str
    data: None | str | dict[str, Any]
    base_url = "https://api.restful-api.dev/"

objects_data = [
    ApiTestData('1', 'Google Pixel 6 Pro', {
            "color": "Cloudy White",
            "capacity": "128 GB"
        }),
    ApiTestData('2', 'Apple iPhone 12 Mini, 256GB, Blue', None),
    ApiTestData('3', 'Apple iPhone 12 Pro Max', {
            "color": "Cloudy White",
            "capacity GB": 512
        }),
    ApiTestData('4', 'Apple iPhone 11, 64GB', {
            "price": 389.99,
            "color": "Purple"
        }),
    ApiTestData('5', 'Samsung Galaxy Z Fold2', {'color': 'Brown', 'price': 689.99}),
    ApiTestData('6', 'Apple AirPods', {
            "generation": "3rd",
            "price": 120
        }),
]