def assert_status_code(response, expected):
    assert response.status_code == expected, (
        f"Expected {expected}, got {response.status_code}")


def assert_json_has_keys(response, keys):
    body = response.json()
    for key in keys:
        assert key in body, f"Missing key: {key}"