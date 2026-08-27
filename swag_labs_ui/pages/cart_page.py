from playwright.sync_api import Page, expect


class CartPage:
    def __init__(self, page: Page):
        self.page = page
        self.continue_shopping_button = page.locator("[data-test='continue-shopping']")
        self.checkout_button = page.locator("[data-test='checkout']")

        self.first_item_remove_button = page.locator(
            "[data-test='remove-sauce-labs-backpack']"
        )
        self.backpack_item = page.locator("[data-test='inventory-item']").filter(
            has_text="Sauce Labs Backpack"
        )

    def continue_shopping(self):
        self.continue_shopping_button.click()

    def checkout(self):
        self.checkout_button.click()

    def remove_item_from_cart(self):
        self.first_item_remove_button.click()

    def verify_backpack_in_cart(self):
        expect(self.backpack_item).to_be_visible()
