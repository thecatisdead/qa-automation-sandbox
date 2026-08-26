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
def test_user_sorting(page: Page, sort_option, logged_in, reverse):
    inventory_page = logged_in

    inventory_page.sort_by(sort_option)

    if sort_option in ["az", "za"]:
        actual = inventory_page.get_product_names()

    else:
        actual = inventory_page.get_product_prices()

    assert actual == sorted(actual, reverse=reverse)
