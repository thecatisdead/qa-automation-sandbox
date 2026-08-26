from playwright.sync_api import Page
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


def test_user_can_continue_shopping_from_cart(page: Page, logged_in):
    inventory_page = logged_in
    inventory_page = InventoryPage(page)
    cart_page = CartPage(page)

    inventory_page.verify_on_inventory_page()
    inventory_page.add_first_item_to_cart()
    inventory_page.go_to_cart()

    cart_page.continue_shopping_button.click()

    inventory_page.verify_on_inventory_page()

    inventory_page.add_second_item_to_cart()
    inventory_page.go_to_cart()


def test_user_view_products_add_to_cart(page: Page, logged_in):
    inventory_page = logged_in

    inventory_page.view_item_description()
    inventory_page.add_item_from_description()

    inventory_page.back_to_inventory()
    inventory_page.go_to_cart()


def test_user_cancel_checkout_remove_item(page: Page, logged_in):
    inventory_page = logged_in
    cart_page = CartPage(page)
    checkout_page = CheckoutPage(page)

    inventory_page.verify_on_inventory_page()
    inventory_page.add_first_item_to_cart()
    inventory_page.go_to_cart()
    cart_page.checkout_button.click()
    checkout_page.fill_shipping_info("Johnny", "Bravo", "3987")

    checkout_page.cancel_checkout_button.click()
    inventory_page.go_to_cart()

    cart_page.remove_first_item_to_cart()
