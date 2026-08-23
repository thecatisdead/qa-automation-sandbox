import pytest
import requests
import os

from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("REQRES_API_KEY")


@pytest.mark.parametrize(
    "user_id, expected_status",
    [
        (2, 200),
        (999, 404),
    ],
)
def test_user_status_codes(user_id, expected_status):
    url = f"https://reqres.in/api/users/{user_id}"

    headers = {"x-api-key": api_key}
    assert api_key, "REQRES_API_KEY is not set"

    response = requests.get(url, headers=headers)

    assert response.status_code == expected_status

    if expected_status == 200:
        assert "data" in response.json()
