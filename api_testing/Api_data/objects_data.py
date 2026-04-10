from typing import Any
from dataclasses import dataclass

base_url="https://api.restful-api.dev/"

@dataclass(frozen=True)
class ApiResponse:
    """{'id': '2', 'name': 'Apple iPhone 12 Mini, 256GB, Blue', 'data': None}"""
    id: str
    name: str
    data: None | str | dict[str, Any]

objects_data = [
    ApiResponse('1', 'Google Pixel 6 Pro',  {
            "color": "Cloudy White",
            "capacity": "128 GB"
        }),
    ApiResponse('2', 'Apple iPhone 12 Mini, 256GB, Blue', None),
    ApiResponse('3', 'Apple iPhone 12 Pro Max', {
            "color": "Cloudy White",
            "capacity GB": 512
        }),
    ApiResponse('4', 'Apple iPhone 11, 64GB', {
            "price": 389.99,
            "color": "Purple"
        }),
    ApiResponse('5', 'Samsung Galaxy Z Fold2', {'color': 'Brown', 'price': 689.99}),
    ApiResponse('6', 'Apple AirPods', {
            "generation": "3rd",
            "price": 120
        }),
]