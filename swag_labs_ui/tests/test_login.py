import pytest
from playwright.sync_api import Page
from pages.login_page import LoginPage

USERS_TO_TEST = [
    "standard_user",
    "problem_user",
    "performance_glitch_user",
    "error_user",
    "visual_user",
]


@pytest.mark.parametrize("username", USERS_TO_TEST)
def test_different_users_can_login(username, page: Page):
    login_page = LoginPage(page)

    login_page.navigate()
    login_page.login(username, "secret_sauce")

    login_page.verify_login_successful()
