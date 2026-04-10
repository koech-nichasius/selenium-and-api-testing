
from api_testing.Api_data.objects_data import base_url


def request_object(id:int)-> str:
    return f"{base_url}objects/{id}"

