"""This module contains data definitions for testing API."""
from dataclasses import dataclass

@dataclass(frozen=True)
class StatusCodes:
    """This class defines API Test data."""
    OK: int = 200
    Created: int = 201
    Accepted: int = 202
    Deleted: int = 204
    BadRequest: int = 400
    Unauthorized: int = 401
    Forbidden: int = 403
    NotFound: int = 404
    InternalServerError: int = 500
    NotImplemented: int = 501
    BadGateway: int = 502

@dataclass(frozen=True)
class UserTestData:
    """This class defines API Test data for Users."""
    valid_user_payload = {
         "name": "Nichasius",
        "job": "QA Engineer"}
    invalid_user_payload = ""

@dataclass(frozen=True)
class ProductTestData:
    """This class defines API Test data for Products."""
    valid_product_payload = {
         "name": "Blue Ribbon",
        "color": "Red"}
    invalid_product_payload = ""

"""
{
  "page": 1,
  "per_page": 6,
  "total": 12,
  "total_pages": 2,
  "data": [
    {
      "id": 1,
      "name": "cerulean",
      "year": 2000,
      "color": "#98B2D1",
      "pantone_value": "15-4020"
    },
    {
      "id": 2,
      "name": "fuchsia rose",
      "year": 2001,
      "color": "#C74375",
      "pantone_value": "17-2031"
    },
    {
      "id": 3,
      "name": "true red",
      "year": 2002,
      "color": "#BF1932",
      "pantone_value": "19-1664"
    },
    {
      "id": 4,
      "name": "aqua sky",
      "year": 2003,
      "color": "#7BC4C4",
      "pantone_value": "14-4811"
    },
    {
      "id": 5,
      "name": "tigerlily",
      "year": 2004,
      "color": "#E2583E",
      "pantone_value": "17-1456"
    },
    {
      "id": 6,
      "name": "blue turquoise",
      "year": 2005,
      "color": "#53B0AE",
      "pantone_value": "15-5217"
    }
  ],
  "support": {
    "url": "https://benhowdle.im/first-cto-playbook?utm_source=reqres&utm_medium=json&utm_campaign=referral",
    "text": "Become a better CTO. A playbook of painful stories and practical advice from a two-time startup CTO."
  }
}
"""