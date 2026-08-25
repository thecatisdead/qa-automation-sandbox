from playwright.sync_api import Page
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.checkout_page import CheckoutPage
from pages.cart_page import CartPage


def test_user_can_login_and_add_item_to_cart(page: Page, logged_in):
    inventory_page = logged_in
    cart_page = CartPage(page)
    checkout_page = CheckoutPage(page)

    inventory_page.verify_on_inventory_page()
    inventory_page.add_first_item_to_cart()
    inventory_page.go_to_cart()

    cart_page.checkout_button.click()

    checkout_page.fill_shipping_info("Johnny", "Bravo", "3987")
    checkout_page.complete_checkout()

    checkout_page.verify_order_success()
