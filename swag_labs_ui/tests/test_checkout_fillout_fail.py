import pytest
from playwright.sync_api import Page
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


@pytest.mark.parametrize(
    "first_name, last_name, postal_code, expected_error",
    [
        ("Johnny", "", "", "Error: Last Name is required"),
        ("", "Bravo", "", "Error: First Name is required"),
        ("", "Bravo", "3987", "Error: First Name is required"),
        ("Johnny", "", "3987", "Error: Last Name is required"),
        ("Johnny", "Bravo", "", "Error: Postal Code is required"),
        ("", "", "", "Error: First Name is required"),
    ],
)
def test_checkout_form_validations(
    page: Page, logged_in, first_name, last_name, postal_code, expected_error
):
    inventory_page = logged_in
    cart_page = CartPage(page)
    checkout_page = CheckoutPage(page)

    inventory_page.add_first_item_to_cart()
    inventory_page.go_to_cart()
    cart_page.checkout_button.click()

    checkout_page.fill_shipping_info(first_name, last_name, postal_code)

    checkout_page.verify_error_message(expected_error)
