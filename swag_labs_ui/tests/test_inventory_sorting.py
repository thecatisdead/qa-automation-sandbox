import pytest
from playwright.sync_api import Page
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage


@pytest.mark.parametrize(
    "sort_option, reverse",
    [
        ("az", False),
        ("za", True),
        ("lohi", False),
        ("hilo", True),
    ],
)
def test_user_sorting(page: Page, sort_option, reverse):
    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)

    login_page.navigate()
    login_page.login("standard_user", "secret_sauce")

    inventory_page.sort_by(sort_option)

    if sort_option in ["az", "za"]:
        actual = inventory_page.get_product_names()

    else:
        actual = inventory_page.get_product_prices()

    assert actual == sorted(actual, reverse=reverse)
