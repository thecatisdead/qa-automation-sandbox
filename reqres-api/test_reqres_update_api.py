import pytest
import requests


@pytest.mark.parametrize(
    "name, job, expected_status",
    [
        ("James", "Qa Automation", 200),
    ],
)
def test_user_status_codes(name, job, expected_status):

    payload = {"name": name, "job": job}

    url = "https://reqres.in/api/users/2"

    headers = {"x-api-key": ""}

    response = requests.patch(url, json=payload, headers=headers)

    assert response.status_code == expected_status

    response_data = response.json()

    assert response_data["name"] == "James"
    assert response_data["job"] == "Qa Automation"
