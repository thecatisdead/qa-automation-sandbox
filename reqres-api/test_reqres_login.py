import pytest
import requests
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("REQRES_API_KEY")


@pytest.mark.parametrize(
    "email, password, expected_status",
    [
        ("eve.holt@reqres.in", "cityslicka", 200),
        ("eve.holt@reqres.in", "", 400),
        ("missing_user@reqres.in", "password", 400),
    ],
)
def test_login_status_codes(email, password, expected_status):
    url = "https://reqres.in/api/login"
    payload = {"email": email, "password": password}
    headers = {"x-api-key": api_key}
    assert api_key, "REQRES_API_KEY is not set"

    response = requests.post(url, json=payload, headers=headers)

    assert response.status_code == expected_status

    if expected_status == 200:
        assert "token" in response.json()
