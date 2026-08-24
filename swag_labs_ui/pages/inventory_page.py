from playwright.sync_api import Page, expect


class InventoryPage:
    def __init__(self, page: Page):
        self.page = page
        self.title_heading = page.locator("[data-test='title']")
        self.first_item_add_button = page.locator(
            "[data-test='add-to-cart-sauce-labs-backpack']"
        )
        self.cart_badge = page.locator("[data-test='shopping-cart-badge']")

    def verify_on_inventory_page(self):
        expect(self.page).to_have_url("https://www.saucedemo.com/inventory.html")
        expect(self.title_heading).to_have_text("Products")

    def add_first_item_to_cart(self):
        self.first_item_add_button.click()

    def verify_cart_count(self, expected_count: str):
        expect(self.cart_badge).to_have_text(expected_count)

    def go_to_cart(self):
        self.page.locator(".shopping_cart_link").click()
