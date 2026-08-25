import pytest
from playwright.sync_api import Page
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage


@pytest.fixture
def logged_in(page: Page):
    login_page = LoginPage(page)

    login_page.navigate()
    login_page.login("standard_user", "secret_sauce")
    inventory_page = InventoryPage(page)

    return inventory_page
